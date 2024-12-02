from django.shortcuts import *
from django.contrib.auth import*
def Login(request):
    if request.method=='POST':
        username1=request.POST['username']
        password1=request.POST['password']
        user=authenticate(request,username=username1,password=password1)
        if user is not None and user.is_superuser==1:
            login(request,user)
            return redirect(home)
        elif user is not None and user.is_staff==0 and user.is_active==1:
            login(request,user)
            # return redirect(studlog)
        else:
            error="Invalid username / password"
            return HttpResponse(error)
    else:
      return render(request,"login.html")
   
def home(request):
    return render(request,'home.html')