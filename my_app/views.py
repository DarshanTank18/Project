from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout

# Create your views here.

def index(request):
    msg = ""
    if request.method == 'POST':
        roomreq = roomcheck_form(request.POST)
        if roomreq.is_valid():
            roomreq.save()
            msg = "Rooms are booked..."
            return redirect("index")
        else:
            print(roomreq.errors)
            msg = "Rooms are not available..."
            

    if request.method == 'POST':
        latest_mail = latest_form(request.POST)
        if latest_mail.is_valid():
            latest_mail.save()
            print("mail sent")
            return redirect("index")
        else:
            print("error")
    return render(request, 'index.html', {'msg': msg})

def rooms(request):
    if request.method == 'POST':
        latest_mail = latest_form(request.POST)
        if latest_mail.is_valid():
            latest_mail.save()
            print("mail sent")
            return redirect("rooms")
        else:
            print("error")
    return render(request,'rooms.html')

def about(request):
    if request.method == 'POST':
        latest_mail = latest_form(request.POST)
        if latest_mail.is_valid():
            latest_mail.save()
            print("mail sent")
            return redirect("about")
        else:
            print("error")
    return render(request,'about.html')

def blog_details(request):
    msg = ""
    if request.method == 'POST':
        latest_mail = latest_form(request.POST)
        if latest_mail.is_valid():
            latest_mail.save()
            print("mail sent")
            return redirect("blog_details")
        else:
            print("error")

        if request.method == 'POST':
            comment_req = Leave_A_Comment_form(request.POST)
            if comment_req.is_valid():
                comment_req.save()
                print("Done")
            else:
                print(comment_req.errors)
    return render(request,'blog_details.html', {'msg' : msg})

def blog(request):
    if request.method == 'POST':
        latest_mail = latest_form(request.POST)
        if latest_mail.is_valid():
            latest_mail.save()
            print("mail sent")
            return redirect("blog")
        else:
            print("error")
    return render(request,'blog.html')

def contact(request):
    if request.method == 'POST':
        contact_req = Contact_form(request.POST)
        if contact_req.is_valid():
            contact_req.save()
            print("Done")
        else:
            print(contact_req.errors)

    if request.method == 'POST':
        latest_mail = latest_form(request.POST)
        if latest_mail.is_valid():
            latest_mail.save()
            print("mail sent")
        else:
            print(latest_mail.errors)
    return render(request,'contact.html')

def room_details(request):
    msg = ""
    if request.method == 'POST':
        Reservationreq = Reservation_form(request.POST)
        if Reservationreq.is_valid():
            Reservationreq.save()
            msg = "Rooms are booked..."
            return redirect("room_details")
        else:
            print(Reservationreq.errors)
            msg = "Rooms are not available..."
    return render(request,'room_details.html',{'msg' : msg})

def login(request):
    if request.method == 'POST':
        mail = request.POST['email']
        pas = request.POST['password']

        user = register_tbl.objects.filter(email = mail, password = pas)
        if user:
            request.session['cuser'] = mail
            return redirect('index')
        else:
            print("Enter valid email or password")
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        regreq = register_form(request.POST)
        if regreq.is_valid():
            regreq.save()
            print("register sucessfully")
            return redirect('login')
        else:
            print("something went wrong")
    return render(request,'register.html')

def profile(request):
    user = request.session.get('cuser')
    data = register_tbl.objects.get(email = user)
    return render(request,'profile.html',{'user' : user, 'data' : data})

def loguot_view(request):
    logout(request)
    return redirect('register')

def update_profile(request):
    user = request.session.get('cuser')
    cuser = register_tbl.objects.get(email = user)
    if request.method == 'POST':
        updatereq = update_form(request.POST, instance = cuser)
        if updatereq.is_valid():
            updatereq.save()
            print("update sucessfully")
            return redirect("index")
        else:
            print(updatereq.errors)
            print("error")
    return render(request,'update_profile.html',{'user' : user, 'cuser' : cuser})