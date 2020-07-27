from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from first_app.forms import EmployeeForm, Subscribe
from first_app.models import Employee
from .tasks import my_task, save_new_employee, show_all_employee, send_email_task

# Create your views here.

def baseTemplate(request):
        task = my_task.delay(5)
        return render(request, 'base.html', {'task_id': task.task_id})

# @require_http_methods(["GET"])
def index(request):
        submitbutton = request.POST.get('submit')
        name = ''
        email = ''
        contact = ''

        if request.method == 'POST':
                emp = EmployeeForm(request.POST)
                print("POST method called")
                if emp.is_valid():
                        # save_new_employee.delay(emp)    # celery task
                        # save_new_employee.apply_async(kwargs={'employee': emp}, serializer='json')    # celery task
                        # save_new_employee.delay(emp, ignore_result=True)    # celery task
                        save_new_employee.delay(1)

                        emp.save()
                        name = emp.cleaned_data['first_name'] + " " + emp.cleaned_data['last_name']
                        email = emp.cleaned_data['email']
                        contact = emp.cleaned_data['contact']
        else:
                emp = EmployeeForm()
                print('Get method called')

        my_dict = {'empData': emp, 'submitbutton': submitbutton, 'name': name, 'email': email, 'contact': contact}
        return render(request, 'index.html', context=my_dict)


def showDatabaseRecords(request):
        all_emp = show_all_employee.delay()
        # print('views views views views views views views views views ======================================= start')
        # print(f"id={all_emp.id}, state={all_emp.state}, status={all_emp.status} ")
        # for event in all_emp.get():
        #         print(str(event.id) + " " + event.first_name + " " + event.last_name + " " + event.email + " " + str(event.contact))
        #         print()
        # print('views views views views views views views views views ======================================= end')
        # return render(request, 'employees.html', context={'empRecords': all_emp.get()})

        empRecords = Employee.objects.all()
        return render(request, 'employees.html', context={'empRecords': empRecords})


def subscribe(request):
        sub = Subscribe()
        if request.method == 'POST':
                sub = Subscribe(request.POST)

                subject = 'Test mail from Django celery'
                message = 'Happy to send you mail. Happy tripping'
                recepient = str(sub['Email'].value())
                
                send_email_task.delay(subject, message, recepient) # celery task

                return render(request, 'success.html', {'recepient': recepient})
        return render(request, 'contact.html', {'form': sub})

def signup(request):
        signupForm = UserCreationForm()
        if request.method == 'POST':
                signupForm = UserCreationForm(request.POST)
                if signupForm.is_valid():
                        signupForm.save()

                        username = signupForm.cleaned_data.get('username')
                        raw_password = signupForm.cleaned_data.get('password')
                        user = authenticate(username=username, password=raw_password)
                        login(request, user)
                        return redirect('home')                        
        return render(request, 'signup.html', {'signupForm': signupForm})

def userProfile(request):
        return render(request, 'profile.html')