from django.shortcuts import*
from django.contrib.auth import*
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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
    staff_count = User.objects.filter(is_fac=True).count()
    stud_count = User.objects.filter(is_stud=True).count()
    current_page = 'dashboard'
    context = {
        'current_page': current_page,
        'staff_count':staff_count,
        'stud_count':stud_count
    }
    return render(request, 'admin_app/pages/dashboard.html', context)

def logout_view(request):
    logout(request)
    return redirect('Login')



def Addstaff(request):
    if request.method == 'POST':
        # Retrieve data from the form
        fac_id = request.POST['fac_id']
        name = request.POST['name']
        password = request.POST['password']
        dob = request.POST['dob']
        place = request.POST['place']
        address = request.POST['address']
        email = request.POST['email']
        photo = request.FILES['photo']

        # Create a new user/staff record
        # Replace `User.objects.create` with the model and fields used in your project
        User.objects.create_user(
            id=fac_id,
            username=name,
            password=password,  
            dob=dob,
            place=place,
            address=address,
            email=email,
            image=photo,
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

def add_stud(request):
    if request.method == 'POST':
        studid = request.POST.get('studid')
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        place = request.POST.get('place')
        photo = request.FILES.get('photo')
        phoneno = request.POST.get('phoneno')
        address = request.POST.get('address')
        name = request.POST.get('username')
    
        try:
            stud= User.objects.create(
                id=studid,
                username=name,
                last_name=lname,  
                email=email,
                dob=dob,
                place=place,
                image=photo,
                phone_number=phoneno,
                address=address,
                first_name=fname,
                is_stud=True
            )
            messages.success(request, f"Stud member {stud.firstname} added successfully!")
            return redirect('dashboard')  # Adjust the redirection as needed
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")

    return render(request,'admin_app/pages/Addstud.html')


  
def staff_list(request):
    current_page = 'stafflist'
    facultys = User.objects.filter(is_fac=True)
    context = {
        'current_page': current_page,
        'facultys': facultys
        }
    return render(request, 'admin_app/pages/stafflist.html', context)

def stud_list(request):
    current_page = 'studlist'
    students = User.objects.filter(is_stud=True)
    context = {
        'current_page': current_page,
        'students': students
        }
    return render(request, 'admin_app/pages/studlist.html', context)