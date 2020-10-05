from django.shortcuts import render, redirect
from . models import Restaurant, Dish, Cuisine, Discount, Ambience, Verification, Order, Assigned_agent
from django.contrib import messages
from django.db.models import Q


def res_login(request):
    try:
        if request.method == "POST":
            email1 = request.POST.get('email')
            password = request.POST.get('password')
            restaurant = Restaurant.objects.get(email=email1)
            check_auth = restaurant.email == email1 and restaurant.password == password
            request.session['res_id'] = restaurant.id
            if (check_auth):
                return redirect('res_dashboard')
            else:
                messages.error(request, 'Password incorrect.')
                return redirect('res_login')
        else:
            return render(request, 'backend/res_login.html')
    except Restaurant.DoesNotExist:
        restaurant = None
        return render(request, 'backend/res_login.html')


def res_register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        contactnumber = request.POST.get('contactnumber')
        restaurant = Restaurant(
            name=name, email=email, password=password, status="notverified", address=address, mobile_number=contactnumber, pincode=pincode)
        restaurant.save()
        print("restaurant object:", restaurant)
        return redirect('res_login')
    else:
        return render(request, 'backend/res_register.html')


def res_dashboard(request):
    res_id = request.session['res_id']
    total_dish = Dish.objects.filter(restaurant_id=res_id).count()

    ongoing_order_list = Order.objects.filter(~Q(status='delivered'))
    delivered_order_list = Order.objects.filter(status="delivered")
    ongoing_list = []
    delivered_list = []

    for i in ongoing_order_list:
        if i.dish_id.restaurant_id.id == res_id:
            ongoing_list.append(i)
    total_ongoing_orders = len(ongoing_list)

    for i in delivered_order_list:
        if i.dish_id.restaurant_id.id == res_id:
            delivered_list.append(i)
    total_delivered_orders = len(delivered_list)

    return render(request, 'backend/res_dashboard.html', {'total_delivered_orders': total_delivered_orders, 'total_ongoing_orders': total_ongoing_orders, 'total_dish': total_dish})


def res_addDish(request):
    if request.method == "POST":
        dishname = request.POST.get('dishname')
        dishprice = request.POST.get('dishprice')
        dishdescription = request.POST.get('dishdescription')
        customization = request.POST.get('customization')
        dishimage = request.FILES['dishimage']
        cuisine = request.POST.get('cuisine')
        cuisine_id = Cuisine.objects.get(id=cuisine)
        res_id = request.session['res_id']
        restaurant = Restaurant.objects.get(id=res_id)

        dish = Dish(
            dish_name=dishname, price=dishprice, dish_description=dishdescription, customization=customization, dish_photo=dishimage, cuisine_id=cuisine_id, restaurant_id=restaurant)
        dish.save()
        return redirect('res_viewDish')
    else:
        cuisine_list = Cuisine.objects.all()
        return render(request, 'backend/res_addDish.html', {"cuisine_list": cuisine_list})


def res_viewDish(request):
    dish_list = Dish.objects.all()
    return render(request, 'backend/res_viewDish.html', {"dish_list": dish_list})


def res_editDish(request, id):
    dish = Dish.objects.get(id=id)
    cuisine_list = Cuisine.objects.all()
    return render(request, 'backend/res_editDish.html', {"dish_list": dish, "cuisine_list": cuisine_list})


def res_updateDish(request, id):
    if request.method == "POST":
        dish = Dish.objects.get(id=id)

        dishname = request.POST.get('dishname')
        dishprice = request.POST.get('dishprice')
        dishdescription = request.POST.get('dishdescription')
        customization = request.POST.get('customization')
        dishimage = request.FILES.get('dishimage', False)
        if(dishimage == False):
            dish.dish_photo = dish.dish_photo
        else:
            dish.dish_photo = dishimage
        cuisine = request.POST.get('cuisine')
        cuisine_id = Cuisine.objects.get(id=cuisine)
        dish.dish_name = dishname
        dish.price = dishprice
        dish.dish_description = dishdescription
        dish.customization = customization
        dish.cuisine_id = cuisine_id
        dish.save()

        return redirect('res_viewDish')


def res_deleteDish(request, id):
    dish = Dish.objects.get(id=id)
    dish.delete()
    return redirect('res_viewDish')


def res_editProfile(request):

    cuisine_list = Cuisine.objects.all()
    restaurant_list = Restaurant.objects.get(id=request.session['res_id'])
    cuisine_res_list = restaurant_list.cuisine_name
    print("cuisine::::::::", cuisine_res_list)
    return render(request, 'backend/res_editProfile.html', {"restaurant_list": restaurant_list, "cuisine_list": cuisine_list, 'cuisine_res_list': cuisine_res_list})


def res_updateProfile(request):
    restaurant = Restaurant.objects.get(id=request.session['res_id'])
    name = request.POST.get('name')
    address = request.POST.get('address')
    pincode = request.POST.get('pincode')
    mobile_number = request.POST.get('mobile_number')
    cuisine_name = request.POST.getlist('cuisine')
    print(":::::::::::::", cuisine_name)
    description = request.POST.get('description')
    pricefortwo = request.POST.get('pricefortwo')
    logo = request.FILES.get('logo', False)

    if(logo == False):
        restaurant.logo = restaurant.logo
    else:
        restaurant.logo = logo
    restaurant.name = name
    restaurant.address = address
    restaurant.pincode = pincode
    restaurant.mobile_number = mobile_number
    restaurant.cuisine_name = cuisine_name
    restaurant.description = description
    restaurant.price_for_two = pricefortwo
    restaurant.save()
    return redirect('res_dashboard')


def res_changePassword(request):
    return render(request, 'backend/res_changePassword.html')


def res_updatePassword(request):
    restaurant = Restaurant.objects.get(id=request.session['res_id'])
    oldpassword = request.POST.get('oldpassword')
    newpassword = request.POST.get('newpassword')
    if(restaurant.password == oldpassword):
        restaurant.password = newpassword
        restaurant.save()
        return redirect('res_dashboard')
    else:
        messages.error(request, 'Old Password Did Not Match.')
        return redirect('res_changePassword')


# def res_addDiscount(request):
#     if request.method == "POST":
#         discount_value = request.POST.get('discount')
#         discountlimit = request.POST.get('discountlimit')
#         discountdescription = request.POST.get('discountdescription')
#         res_id = request.session['res_id']
#         restaurant = Restaurant.objects.get(id=res_id)
#         discount = Discount(discount_value=discount_value, discount_description=discountdescription,
#                             discount_limit=discountlimit, restaurant_id=restaurant)
#         discount.save()
#         return redirect('res_viewDiscount')
#     else:
#         return render(request, 'backend/res_addDiscount.html')

def res_editDiscount(request, id):
    discount = Discount.objects.get(id=id)
    return render(request, 'backend/res_editDiscount.html', {'discount': discount})


def res_updateDiscount(request, id):
    if request.method == "POST":

        discount_value = request.POST.get('discount')
        discountlimit = request.POST.get('discountlimit')
        discountdescription = request.POST.get('discountdescription')
        res_id = request.session['res_id']
        restaurant = Restaurant.objects.get(id=res_id)
        discount = Discount.objects.get(id=id)
        discount.discount_value = discount_value
        discount.discount_limit = discountlimit
        discount.discount_description = discountdescription
        discount.restaurant_id = res_id
        discount.save()

        return redirect('res_viewDiscount')


def res_viewDiscount(request):
    discount_list = Discount.objects.all()
    return render(request, 'backend/res_viewDiscount.html', {"discount_list": discount_list})


# def res_deleteDiscount(request, id):
#     discount = Discount.objects.get(id=id)
#     discount.delete()
#     return redirect('res_viewDiscount')


def res_addAmbience(request):
    if request.method == "POST":
        ambience_photos = request.FILES['ambiencephotos']
        res_id = request.session['res_id']
        restaurant = Restaurant.objects.get(id=res_id)
        ambience = Ambience(photos=ambience_photos, restaurant_id=restaurant)
        ambience.save()
        return redirect('res_viewAmbience')
    else:
        return render(request, 'backend/res_addAmbience.html')


def res_viewAmbience(request):
    ambience_list = Ambience.objects.all()
    return render(request, 'backend/res_viewAmbience.html', {"ambience_list": ambience_list})


def res_deleteAmbience(request, id):
    ambience = Ambience.objects.get(id=id)
    ambience.delete()
    return redirect('res_viewAmbience')


def res_verification(request):
    if request.method == "POST":
        shop_fssai_license = request.FILES['shopfssailicense']
        pancard = request.FILES['pancard']
        gst = request.POST.get('gst')
        res_id = request.session['res_id']
        restaurant = Restaurant.objects.get(id=res_id)
        restaurant.status = "pending"
        restaurant.save()
        verification = Verification(shop_fssai_license=shop_fssai_license,
                                    pan_card=pancard, gst_number=gst, res_id=restaurant)
        verification.save()
        return redirect('res_verification')
    else:
        res_id = request.session['res_id']
        restaurant = Restaurant.objects.get(id=res_id)
        verification_list = Verification.objects.filter(res_id=restaurant)
        return render(request, 'backend/res_verification.html', {'verification_list1': verification_list})


def res_viewNewOrder(request):
    res_id = request.session['res_id']
    order_list = Order.objects.filter(status="assigned")
    neworder_list = []
    for i in order_list:
        if i.dish_id.restaurant_id.id == res_id:
            neworder_list.append(i)
    return render(request, 'backend/res_viewNewOrder.html', {"neworder_list": neworder_list})


def res_viewAssignedAgent(request):
    res_id = request.session['res_id']
    agent_list = Assigned_agent.objects.all()

    newagent_list = []
    for i in agent_list:
        if i.order_id.dish_id.restaurant_id.id == res_id:
            newagent_list.append(i)
    return render(request, 'backend/res_viewAssignedAgent.html', {"agent_list": newagent_list})


def res_viewDeliveredOrder(request):
    res_id = request.session['res_id']
    order_list = Order.objects.filter(status="delivered")

    deliveredorder_list = []
    for i in order_list:
        if i.dish_id.restaurant_id.id == res_id:
            deliveredorder_list.append(i)
    return render(request, 'backend/res_viewDeliveredOrder.html', {"deliveredorder_list": deliveredorder_list})
