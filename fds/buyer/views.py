from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Feedback
from mainapp.models import Reg_user, Restaurant, Delivery_agent, Order, Cuisine, Report, Dish, Ambience, Verification, Discount, Cart, Assigned_agent
from django.core.mail import send_mail
import datetime
from django.http import HttpResponse
from . Paytm import checksum
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q


def buyer_login(request):
    try:
        if request.method == "POST":
            email = request.POST.get('email')
            password = request.POST.get('password')
            reg_user = Reg_user.objects.get(email=email)
            check_auth = reg_user.email == email and reg_user.password == password
            request.session['buyer_id'] = reg_user.id
            if (check_auth):
                return redirect('buyer_dashboard')
            else:
                messages.error(request, 'Password incorrect.',
                               extra_tags="loginerror")
                return redirect('buyer_dashboard')
        else:
            return render(request, 'buyer/buyer_dashboard.html')
    except Reg_user.DoesNotExist:
        reg_user = None
        return render(request, 'buyer/buyer_dashboard.html')


def buyer_register(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        mobile_no = request.POST.get('mobile_no')
        buyer = Reg_user(
            fname=fname, lname=lname, email=email, password=password, address=address, mobile_no=mobile_no, pincode=pincode, dob=dob)
        buyer.save()
        print("restaurant object:", buyer)
        return redirect('buyer_dashboard')
    else:
        return render(request, 'buyer/buyer_dashboard.html')


def buyer_dashboard(request):
    if "buyer_id" in request.session:
        buyer_id = request.session['buyer_id']
    else:
        buyer_id = False
    restaurant_list = Restaurant.objects.all()
    cuisine_list = Cuisine.objects.all()
    return render(request, "buyer/buyer_dashboard.html", {'buyer_id': buyer_id, "cuisine_list": cuisine_list, 'restaurant_list': restaurant_list})


def buyer_viewDishByCuisine(request, id):
    if "buyer_id" in request.session:
        buyer_id = request.session['buyer_id']
    else:
        buyer_id = False
    restaurant_list = Restaurant.objects.all()
    cuisine_list = Cuisine.objects.all()
    cuisine_by_id = Cuisine.objects.get(id=id)
    dish_list = Dish.objects.filter(cuisine_id=id)
    cuisine_name = ""
    cuisine_name = cuisine_by_id.cuisine_name
    return render(request, "buyer/buyer_viewDishByCuisine.html", {'buyer_id': buyer_id, "dish_list": dish_list, 'cuisine_list': cuisine_list, "cuisine_name": cuisine_name, 'restaurant_list': restaurant_list})


def buyer_viewDishByRestaurant(request, id):
    if "buyer_id" in request.session:
        buyer_id = request.session['buyer_id']
    else:
        buyer_id = False
    dishlist_by_restautrant_id = Dish.objects.filter(restaurant_id=id)
    restaurant_by_id = Restaurant.objects.get(id=id)
    restaurant_name = restaurant_by_id.name
    cuisine_list = Cuisine.objects.all()
    restaurant_list = Restaurant.objects.all()
    return render(request, "buyer/buyer_viewDishByRestaurant.html", {'buyer_id': buyer_id, "dishlist_by_restautrant_id": dishlist_by_restautrant_id, 'cuisine_list': cuisine_list, "restaurant_name": restaurant_name, 'restaurant_list': restaurant_list})


def buyer_viewDish(request):
    if "buyer_id" in request.session:
        buyer_id = request.session['buyer_id']
    else:
        buyer_id = False
    dish_list = Dish.objects.all()
    cuisine_list = Cuisine.objects.all()
    restaurant_list = Restaurant.objects.all()
    return render(request, "buyer/buyer_viewDish.html", {'buyer_id': buyer_id, "dish_list": dish_list, 'cuisine_list': cuisine_list, 'restaurant_list': restaurant_list})


def buyer_viewDiscount(request):
    if "buyer_id" in request.session:
        buyer_id = request.session['buyer_id']
    else:
        buyer_id = False
    discount_list = Discount.objects.all()
    cuisine_list = Cuisine.objects.all()
    restaurant_list = Restaurant.objects.all()
    return render(request, "buyer/buyer_viewDiscount.html", {'buyer_id': buyer_id, "discount_list": discount_list, 'cuisine_list': cuisine_list, 'restaurant_list': restaurant_list})


def buyer_addToCart(request):
    if request.method == "POST":
        if "buyer_id" in request.session:
            buyer_id = request.session['buyer_id']
        else:
            buyer_id = False
        dish_id = request.POST.get('dish_id')
        quantity = request.POST.get('quantity')
        dish_by_id = Dish.objects.get(id=dish_id)
        restaurant_id_by_dish_id = dish_by_id.restaurant_id.id

        cart_list = Cart.objects.filter(reg_user_id=buyer_id)

        print("::::::::::::::::::::cart list :", cart_list)
        restaurant_id_by_cart_id = 0
        for i in cart_list:
            restaurant_id_by_cart_id = i.dish_id.restaurant_id.id

        print("restaurant_id_by_cart_id:::::::", restaurant_id_by_cart_id)
        if (restaurant_id_by_dish_id is restaurant_id_by_cart_id) or (restaurant_id_by_cart_id == 0):
            price = dish_by_id.price
            total_amount = (float(price)*float(quantity))

            discount = Discount.objects.get(
                restaurant_id=restaurant_id_by_dish_id)
            discount_id = discount.id
            buyer = Reg_user.objects.get(id=buyer_id)

            cart = Cart(total_amount=total_amount, status="added", quantity=quantity,
                        discount_id=discount, dish_id=dish_by_id, reg_user_id=buyer)
            cart.save()
            return redirect('buyer_viewCart')
        else:
            messages.add_message(
                request, messages.INFO, 'Sorry! You cannot add to cart from multiple restaurants.', extra_tags='addtocart')
            return redirect('buyer_viewDishByRestaurant', id=restaurant_id_by_dish_id)


def buyer_viewCart(request):
    if "buyer_id" in request.session:
        buyer_id = request.session['buyer_id']
    else:
        buyer_id = False
    discount_list = Discount.objects.all()
    cuisine_list = Cuisine.objects.all()
    restaurant_list = Restaurant.objects.all()
    cart_list = Cart.objects.filter(reg_user_id=buyer_id)
    return render(request, "buyer/buyer_viewCart.html", {'buyer_id': buyer_id, "discount_list": discount_list, 'cuisine_list': cuisine_list, 'restaurant_list': restaurant_list, 'cart_list': cart_list})


def buyer_payment(request):
    if "buyer_id" in request.session:
        buyer_id = request.session['buyer_id']
    else:
        buyer_id = False
    discount_list = Discount.objects.all()
    cuisine_list = Cuisine.objects.all()
    restaurant_list = Restaurant.objects.all()
    cart_list = Cart.objects.filter(reg_user_id=buyer_id)
    return render(request, "buyer/buyer_payment.html", {'buyer_id': buyer_id, "discount_list": discount_list, 'cuisine_list': cuisine_list, 'restaurant_list': restaurant_list, 'cart_list': cart_list})


def buyer_removeDish(request, id):
    cart = Cart.objects.get(id=id)
    cart.delete()
    return redirect('buyer_viewCart')


def buyer_logout(request):
    request.session.delete()
    return redirect('buyer_dashboard')


def buyer_feedback(request):
    if request.method == "POST":
        if "buyer_id" in request.session:
            buyer_id = request.session['buyer_id']
        else:
            buyer_id = False
        buyer = Reg_user.objects.get(id=buyer_id)
        name = buyer.fname + " " + buyer.lname
        email = buyer.email
        feedback_message = request.POST.get('feedback_message')
        feedback_date_time = datetime.datetime.now()

        feedback = Feedback(name=name, email=email, feedback_date_time=feedback_date_time,
                            feedback_message=feedback_message)
        feedback.save()
        return redirect('buyer_dashboard')
    else:
        if "buyer_id" in request.session:
            buyer_id = request.session['buyer_id']
        else:
            buyer_id = False
        buyer_list = Reg_user.objects.get(id=buyer_id)

        return render(request, "buyer/buyer_feedback.html", {"buyer_list": buyer_list})


def buyer_addOnlineOrder(request):
    if "buyer_id" in request.session:
        buyer_id = request.session['buyer_id']
    else:
        buyer_id = False
    buyer = Reg_user.objects.get(id=buyer_id)
    cart_by_buyer_id = Cart.objects.filter(reg_user_id=buyer_id)
    total_amount = 0
    restaurant_id = 0
    discounted_price = 0
    final_price = 0
    i = 0
    for cart in cart_by_buyer_id:
        dish_price = cart.total_amount
        dish_id = cart.dish_id.id
        dish = Dish.objects.get(id=dish_id)
        i = i+1
        if(i == 1):
            restaurant_id = cart.dish_id.restaurant_id
        discount = Discount.objects.get(restaurant_id=restaurant_id)
        if(discount.discount_value == 0):
            discounted_price = dish_price
            final_price = final_price + discounted_price
            order_date_time = datetime.datetime.now()
            order = Order(payment_type="Online", order_date_time=order_date_time,
                          status="new", total_amount=discounted_price, reg_user_id=buyer, dish_id=dish)
            order.save()

        else:
            discounted_price = (dish_price*discount.discount_value)/100
            final_price = final_price + discounted_price
            order_date_time = datetime.datetime.now()
            order = Order(payment_type="Online", order_date_time=order_date_time,
                          status="new", total_amount=discounted_price, reg_user_id=buyer, dish_id=dish)
            order.save()
        cart = Cart.objects.get(id=cart.id)
        cart.delete()
        MERCHANT_KEY = '@mlnvyM0TkiXkv8K'
        param_dict = {
            'MID': 'ONphQY43540204822882',
            'ORDER_ID': str(order.id),
            'TXN_AMOUNT': str(final_price),
            'CUST_ID': buyer.email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'Webstaging',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': 'http://127.0.0.1:8000/handlerequest',
        }
        param_dict['CHECKSUMHASH'] = checksum.generate_checksum(
            param_dict, MERCHANT_KEY)
        return render(request, "buyer/paytm.html", {"param_dict": param_dict})

    return render(request, "buyer/paytm.html", {"param_dict": param_dict})


def buyer_thankyou(request):
    if "buyer_id" in request.session:
        buyer_id = request.session['buyer_id']
    else:
        buyer_id = False
    cuisine_list = Cuisine.objects.all()
    restaurant_list = Restaurant.objects.all()
    return render(request, "buyer/buyer_thankyou.html",{"buyer_id": buyer_id, 'cuisine_list': cuisine_list, 'restaurant_list': restaurant_list})


@csrf_exempt
def handlerequest(request):
    MERCHANT_KEY = '@mlnvyM0TkiXkv8K'

    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            Checksum = form[i]

    verify = checksum.verify_checksum(response_dict, MERCHANT_KEY, Checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' +
                  response_dict['RESPMSG'])
    # return render(request, 'buyer/buyer_thankyou.html', {'response': response_dict})
    return redirect('buyer_thankyou')


def buyer_addOfflineOrder(request):
    if "buyer_id" in request.session:
        buyer_id = request.session['buyer_id']
    else:
        buyer_id = False
    buyer = Reg_user.objects.get(id=buyer_id)
    cart_by_buyer_id = Cart.objects.filter(reg_user_id=buyer_id)
    total_amount = 0
    restaurant_id = 0
    discounted_price = 0
    final_price = 0
    i = 0
    for cart in cart_by_buyer_id:
        dish_price = cart.total_amount
        dish_id = cart.dish_id.id
        dish = Dish.objects.get(id=dish_id)
        i = i+1
        if(i == 1):
            restaurant_id = cart.dish_id.restaurant_id
        discount = Discount.objects.get(restaurant_id=restaurant_id)
        if(discount.discount_value == 0):
            discounted_price = dish_price
            final_price = final_price + discounted_price
            order_date_time = datetime.datetime.now()
            order = Order(payment_type="Offline", order_date_time=order_date_time,
                          status="new", total_amount=discounted_price, reg_user_id=buyer, dish_id=dish)
            order.save()

        else:
            discounted_price = (dish_price*discount.discount_value)/100
            final_price = final_price + discounted_price
            order_date_time = datetime.datetime.now()
            order = Order(payment_type="Offline", order_date_time=order_date_time,
                          status="new", total_amount=discounted_price, reg_user_id=buyer, dish_id=dish)
            order.save()
        cart = Cart.objects.get(id=cart.id)
        cart.delete()
    return redirect('buyer_thankyou')


def buyer_trackOrder(request):
    if "buyer_id" in request.session:
        buyer_id = request.session['buyer_id']
    else:
        buyer_id = False
    assigned_agent = Assigned_agent.objects.filter(reg_user_id=buyer_id)
    order_list = Order.objects.filter(
        ~Q(status='delivered'), reg_user_id=buyer_id)



    return render(request, 'buyer/buyer_trackOrder.html', {"order_list": order_list, "assigned_agent": assigned_agent})

def buyer_orderHistory(request):
    if "buyer_id" in request.session:
        buyer_id = request.session['buyer_id']
    else:
        buyer_id = False
    assigned_agent = Assigned_agent.objects.filter(reg_user_id=buyer_id)
    order_list = Order.objects.filter(status="delivered", reg_user_id=buyer_id)

    total_amount =0
    for item in order_list:
        total_amount += item.total_amount
    print(":::::::::::::::::",total_amount)
    return render(request, 'buyer/buyer_orderHistory.html', {"order_list": order_list, "assigned_agent": assigned_agent,'total_amount':total_amount})
