from django.shortcuts import render,redirect
from .models import UserProfile


def next(request):
    return render(request,'next.html')

def index(request):
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        age =  request.POST.get('age')


        UserProfile.objects.create(
            username=username,
            email=email,
            phone_number=phone_number,
            gender=gender,
            age=age
        )
        return redirect('next')


    return render(request,'index.html')


