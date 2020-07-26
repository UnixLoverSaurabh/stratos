from celery import shared_task
from first_app.models import Employee

from djangoRedis.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

@shared_task(bind=True)
def my_task(self, seconds):
        for i in range(seconds):
                print(i)
        return 'Done!'

@shared_task
def save_new_employee(emp_id):
        empDetails = Employee.objects.get(id=emp_id)
        print(str(empDetails.id) + " " + empDetails.first_name + " " + empDetails.last_name + " " + empDetails.email + " " + str(empDetails.contact))
        empDetails.last_name.replace('Kumar', 'Rock')
        print(str(empDetails.id) + " " + empDetails.first_name + " " + empDetails.last_name + " " + empDetails.email + " " + str(empDetails.contact))
        empDetails.save()

@shared_task
def show_all_employee():
        all_emp = Employee.objects.all()
        for event in all_emp:
                print(str(event.id) + " " + event.first_name + " " + event.last_name + " " + event.email + " " + str(event.contact))
                print()
        print('Is the complete function dont execute if any statement is wrong?')
        print()
        # return all_emp

@shared_task
def send_email_task(subject, message, recepient):
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)