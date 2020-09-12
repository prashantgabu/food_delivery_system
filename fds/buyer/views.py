from django.shortcuts import render, redirect
from django.contrib import messages
from mainapp.models import Reg_user, Restaurant, Delivery_agent, Order, Cuisine, Report, Dish, Ambience, Verification, Discount, Cart
from django.core.mail import send_mail


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
                messages.error(request, 'Password incorrect.')
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
        price = dish_by_id.price
        print("PRICE AND QTY", price, quantity)
        total_amount = (float(price)*float(quantity))
        print("Total Amount",total_amount)
        restaurant_id = dish_by_id.restaurant_id.id
        discount = Discount.objects.get(restaurant_id=restaurant_id)
        discount_id = discount.id
        buyer=Reg_user.objects.get(id=buyer_id)
        cart = Cart(total_amount=total_amount, status="added", quantity=quantity,
                    discount_id=discount, dish_id=dish_by_id, reg_user_id=buyer)
        cart.save()
        return redirect('buyer_viewCart')

def buyer_viewCart(request):
    if "buyer_id" in request.session:
        buyer_id = request.session['buyer_id']
    else:
        buyer_id = False
    discount_list = Discount.objects.all()
    cuisine_list = Cuisine.objects.all()
    restaurant_list = Restaurant.objects.all()
    cart_list=Cart.objects.filter(reg_user_id=buyer_id)
    return render(request, "buyer/buyer_viewCart.html", {'buyer_id': buyer_id, "discount_list": discount_list, 'cuisine_list': cuisine_list, 'restaurant_list': restaurant_list,'cart_list': cart_list})

def buyer_removeDish(request, id):
    cart = Cart.objects.get(id=id)
    cart.delete()
    return redirect('buyer_viewCart')


def buyer_logout(request):
    request.session.delete()
    return redirect('buyer_dashboard')
