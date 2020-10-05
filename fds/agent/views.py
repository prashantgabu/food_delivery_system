from django.shortcuts import render, redirect
from django.contrib import messages
from mainapp.models import Restaurant, Delivery_agent, Order, Cuisine, Report, Dish, Ambience, Verification, Assigned_agent,Reg_user
from django.core.mail import send_mail
from . models import Agent_docs


def agent_login(request):
    try:
        if request.method == "POST":
            email = request.POST.get('email')
            password = request.POST.get('password')
            agent = Delivery_agent.objects.get(email=email)
            check_auth = agent.email == email and agent.password == password
            request.session['agent_id'] = agent.id
            if (check_auth):
                return redirect('agent_dashboard')
            else:
                messages.error(request, 'Password incorrect.')
                return redirect('agent_login')
        else:
            return render(request, 'agent/agent_login.html')
    except Delivery_agent.DoesNotExist:
        agent = None
        return render(request, 'agent/agent_login.html')


def agent_register(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        password = request.POST.get('password')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        mobile_no = request.POST.get('mobile_no')
        agent = Delivery_agent(
            fname=fname, lname=lname, email=email, password=password, status="notverified", dob=dob, address=address, mobile_no=mobile_no, pincode=pincode)
        agent.save()
        print("Agent object:", agent)
        return redirect('agent_login')
    else:
        return render(request, 'agent/agent_register.html')


def agent_dashboard(request):
    return render(request, 'agent/agent_dashboard.html')


def agent_editProfile(request):
    agent_list = Delivery_agent.objects.get(id=request.session['agent_id'])
    return render(request, 'agent/agent_editProfile.html', {"agent_list": agent_list})


def agent_updateProfile(request):
    agent = Delivery_agent.objects.get(id=request.session['agent_id'])
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    address = request.POST.get('address')
    pincode = request.POST.get('pincode')
    mobile_no = request.POST.get('mobile_no')
    profile_pic = request.FILES.get('profile_pic', False)
    if(profile_pic == False):
        agent.profile_pic = agent.profile_pic
    else:
        agent.profile_pic = profile_pic
    agent.fname = fname
    agent.lname = lname
    agent.address = address
    agent.pincode = pincode
    agent.mobile_no = mobile_no
    agent.save()
    return redirect('agent_dashboard')


def agent_changePassword(request):
    return render(request, 'agent/agent_changePassword.html')


def agent_updatePassword(request):
    agent = Delivery_agent.objects.get(id=request.session['agent_id'])
    oldpassword = request.POST.get('oldpassword')
    newpassword = request.POST.get('newpassword')
    if(agent.password == oldpassword):
        agent.password = newpassword
        agent.save()
        return redirect('agent_dashboard')
    else:
        return redirect('agent_changePassword')


def agent_verification(request):
    if request.method == "POST":
        driving_license = request.FILES['driving_license']
        aadhar_card = request.FILES['aadhar_card']
        passbook = request.FILES['passbook']
        agent_id = request.session['agent_id']
        agent = Delivery_agent.objects.get(id=agent_id)
        agent.status = "pending"
        agent.save()
        agent_docs = Agent_docs(driving_license=driving_license,
                                aadhar_card=aadhar_card, passbook=passbook, agent_id=agent)
        agent_docs.save()
        return redirect('agent_verification')
    else:
        agent_id = request.session['agent_id']
        agent = Delivery_agent.objects.get(id=agent_id)
        agent_docs_list = Agent_docs.objects.filter(agent_id=agent)
        return render(request, 'agent/agent_verification.html', {'agent_docs_list': agent_docs_list})


def agent_viewNewOrder(request):
    order_list = Order.objects.filter(status="new")
    print("ORDERLIST-", order_list)
    return render(request, 'agent/agent_viewNewOrder.html', {'order_list': order_list})


def agent_acceptOrder(request, id):
    agent_id = request.session['agent_id']
    agent=Delivery_agent.objects.get(id=agent_id)
    
    order = Order.objects.get(id=id)


    buyer_id = order.reg_user_id.id
    
    buyer=Reg_user.objects.get(id=buyer_id)
    
    order.status = "accepted"
    
    
    assigned_agent = Assigned_agent(
        agent_id=agent, order_id=order, reg_user_id=buyer)
    assigned_agent.save()
    order.save()
    return redirect('agent_viewAcceptedOrder')


def agent_viewAcceptedOrder(request):
    agent_id = request.session['agent_id']
    order_list = Order.objects.filter(status="accepted")
    return render(request, 'agent/agent_viewAcceptedOrder.html', {'order_list': order_list})


def agent_viewOrderHistory(request):
    agent_id = request.session['agent_id']
    order_list = Order.objects.filter(agent_id=agent_id, status="completed")
    return render(request, 'agent/agent_viewOrderHistory.html', {'order_list': order_list})
