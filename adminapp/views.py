from django.shortcuts import *
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
                return redirect('faculty_dashboard')  # Redirect to faculty dashboard

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
    return redirect('home')

def Addstaff(request):
    if request.method=='POST':
        fac_id = request.POST.get('fac_id')
        depart_id = request.POST.get('depart_id')
        name = request.POST.get('name')
        password = request.POST.get('password')
        Staff.objects.create_user(fac_id=fac_id,department=depart_id,fname=name,password=password,)
        return redirect(dashboard)
    else:
        return render(request, 'admin_app/pages/Addstaff.html')