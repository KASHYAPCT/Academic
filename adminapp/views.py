from django.shortcuts import*
from django.contrib.auth import*
from .models import *


def Login(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
        user = authenticate(request, username=username1, password=password1)

        if user is not None:
            login(request, user)

            # Check if user is a superuser
            if user.is_superuser:
                return redirect('dashboard')  # Redirect to superuser dashboard

            # Check if user is a student
            elif user.is_stud:
                return redirect('student_dashboard')  # Redirect to student dashboard

            # Check if user is faculty
            elif user.is_fac:
                return redirect('staffdashboard')  # Redirect to faculty dashboard

        else:
            error = "Invalid username / password"
            return HttpResponse(error)

    else:
        return render(request, "login.html")

# @login_required(login_url='/login/')  
def dashboard(request):
    current_page = 'dashboard'
    context = {
        'current_page': current_page,
    }
    return render(request, 'admin_app/pages/dashboard.html', context)

def logout_view(request):
    logout(request)
    return redirect('Login')



def Addstaff(request):
    if request.method == 'POST':
        # Retrieve data from the form
        fac_id = request.POST['fac_id']
        depart_id = request.POST['depart_id']
        name = request.POST['name']
        password = request.POST['password']
        dob = request.POST['dob']
        place = request.POST['place']
        address = request.POST['address']
        email = request.POST['email']

        # Create a new user/staff record
        # Replace `User.objects.create` with the model and fields used in your project
        User.objects.create_user(
            id=fac_id,
            department=depart_id,
            username=name,
            password=password,  
            dob=dob,
            place=place,
            address=address,
            email=email,
            is_fac=True
        )
       
        # Redirect to the dashboard or another page
        return redirect('dashboard') 
    else:
        # Render the form page
        return render(request, 'admin_app/pages/Addstaff.html')

def staffdashboard(request):
    current_page = 'staffdashboard'
    context = {
        'current_page': current_page,
    }
    return render(request, 'admin_app/pages/staffdashboard.html', context)