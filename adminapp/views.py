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
    return redirect('Login')



def Addstaff(request):
    if request.method == 'POST':
        fac_id = request.POST['fac_id']
        depart_id = request.POST['depart_id']
        name = request.POST['name']
        password = request.POST['password']

        # Fetch the User instance
        user = get_object_or_404(User, pk=fac_id)

        # Create the Staff object
        Staff.objects.create(fac_id=user, department=depart_id, fname=name)
        user.set_password(password)
        user.save()

        return redirect('dashboard')  # Use a URL name instead of a function
    else:
        return render(request, 'admin_app/pages/Addstaff.html')
