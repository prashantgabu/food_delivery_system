from django.shortcuts import render, redirect
from django.contrib import messages
from mainapp.models import Reg_user, Restaurant, Delivery_agent, Order, Cuisine, Report, Dish, Ambience, Verification
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
    return render(request, "buyer/buyer_dashboard.html")
