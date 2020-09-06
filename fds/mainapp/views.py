from django.shortcuts import render, redirect
from . models import Restaurant, Dish, Cuisine
from django.contrib import messages


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
            name=name, email=email, password=password, address=address, mobile_number=contactnumber, pincode=pincode)
        restaurant.save()
        print("restaurant object:", restaurant)
        return redirect('res_login')
    else:
        return render(request, 'backend/res_register.html')


def res_dashboard(request):
    return render(request, 'backend/res_dashboard.html')


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
    return render(request, 'backend/res_editProfile.html', {"restaurant_list": restaurant_list, "cuisine_list": cuisine_list})


def res_updateProfile(request):
    restaurant = Restaurant.objects.get(id=request.session['res_id'])
    name = request.POST.get('name')
    address = request.POST.get('address')
    pincode = request.POST.get('pincode')
    mobile_number = request.POST.get('mobile_number')
    cuisine_name = request.POST.get('cuisine')
    description = request.POST.get('description')
    pricefortwo = request.POST.get('pricefortwo')
    logo = request.FILES['logo']
    restaurant.name = name
    restaurant.address = address
    restaurant.pincode = pincode
    restaurant.mobile_number = mobile_number
    restaurant.cuisine_name = cuisine_name
    restaurant.description = description
    restaurant.price_for_two = pricefortwo
    restaurant.logo = logo
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
