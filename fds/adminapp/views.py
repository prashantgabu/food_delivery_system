from django.shortcuts import render, redirect
from django.contrib import messages
from .  models import Admin_tb
from mainapp.models import Restaurant, Delivery_agent, Order, Cuisine,Report


def a_login(request):
    try:
        if request.method == "POST":
            email = request.POST.get('email')
            password = request.POST.get('password')
            admin = Admin_tb.objects.get(email=email)
            check_auth = admin.email == email and admin.password == password
            if (check_auth):
                return redirect('a_dashboard')
            else:
                messages.error(request, 'Password incorrect.')
                return redirect('a_login')
        else:
            return render(request, 'admin/a_login.html')
    except Admin_tb.DoesNotExist:
        admin = None
        return render(request, 'admin/res_login.html')


def a_dashboard(request):
    return render(request, "admin/a_dashboard.html")


def a_viewRestaurant(request):
    restaurant_list = Restaurant.objects.filter(status="verified")
    return render(request, "admin/a_viewRestaurant.html", {'restaurant_list': restaurant_list})


def a_restaurantRequest(request):
    restaurant_list = Restaurant.objects.filter(status="pending")
    return render(request, "admin/a_restaurantRequest.html", {'restaurant_list': restaurant_list})


def a_viewAgent(request):
    agent_list = Delivery_agent.objects.filter(status="verified")
    return render(request, "admin/a_viewAgent.html", {'agent_list': agent_list})


def a_agentRequest(request):
    agent_list = Delivery_agent.objects.filter(status="pending")
    return render(request, "admin/a_agentRequest.html", {'agent_list': agent_list})


def a_newOrder(request):
    order_list = Order.objects.filter(status="new")
    return render(request, "admin/a_newOrder.html", {'order_list': order_list})


def a_ongoingOrder(request):
    order_list = Order.objects.filter(status="ongoing")
    return render(request, "admin/a_ongoingOrder.html", {'order_list': order_list})


def a_completedOrder(request):
    order_list = Order.objects.filter(status="completed")
    return render(request, "admin/a_completedOrder.html", {'order_list': order_list})


def a_addCuisine(request):
    if request.method == "POST":
        cuisinename = request.POST.get('cuisinename')
        cuisineimage = request.FILES['cuisineimage']

        cuisine = Cuisine(cuisine_name=cuisinename, cuisine_photo=cuisineimage)
        cuisine.save()
        return redirect('a_viewCuisine')
    else:
        return render(request, 'admin/a_addCuisine.html')


def a_viewCuisine(request):
    cuisine_list = Cuisine.objects.all()
    return render(request, 'admin/a_viewCuisine.html', {"cuisine_list": cuisine_list})


def a_editCuisine(request, id):

    cuisine_list = Cuisine.objects.get(id=id)
    return render(request, 'admin/a_editCuisine.html', {"cuisine_list": cuisine_list})


def a_updateCuisine(request, id):
    if request.method == "POST":
        cuisine = Cuisine.objects.get(id=id)
        cuisinename = request.POST.get('cuisinename')
        cuisineimage = request.FILES.get('cuisineimage', False)
        if(cuisineimage == False):
            cuisine.cuisine_photo = cuisine.cuisine_photo
        else:
            cuisine.cuisine_photo = cuisineimage
        cuisine.name = cuisinename
        cuisine.save()

        return redirect('a_viewCuisine')


def a_deleteCuisine(request, id):
    cuisine = Cuisine.objects.get(id=id)
    cuisine.delete()
    return redirect('a_viewCuisine')


def a_foodReport(request):
    report_list = Report.objects.filter(report_type="food")
    return render(request, 'admin/a_foodReport.html', {"report_list": report_list})


def a_agentReport(request):
    report_list = Report.objects.filter(report_type="agent")
    return render(request, 'admin/a_agentReport.html', {"report_list": report_list})


def a_viewBuyer(request):
    buyer_list = Report.objects.all()
    return render(request, 'admin/a_viewBuyer.html', {"buyer_list": buyer_list})
