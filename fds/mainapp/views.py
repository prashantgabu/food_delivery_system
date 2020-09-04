from django.shortcuts import render, redirect
from . models import Restaurant, Dish
from django.contrib import messages


def res_login(request):
    try:
        if request.method == "POST":
            email1 = request.POST.get('email')
            password = request.POST.get('password')
            restaurant = Restaurant.objects.get(email=email1)
            check_auth = restaurant.email == email1 and restaurant.password == password
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
        dishimage = request.POST.get('dishimage')
        cuisine = request.POST.get('cuisine')
        dish = Dish(
            dish_name=dishname, price=dishprice, dish_description=dishdescription, customization=customization, dish_photo=dishimage)
        dish.save()
        print("Dish object:", dish)
        return redirect('res_viewDish')
    else:
        return render(request, 'backend/res_addDish.html')


def res_viewDish(request):
    return render(request, 'backend/viewDish.html')
