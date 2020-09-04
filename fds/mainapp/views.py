from django.shortcuts import render, redirect
from . models import Restaurant


def res_login(request):
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
