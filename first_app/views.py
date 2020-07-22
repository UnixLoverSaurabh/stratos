from django.shortcuts import render
from first_app.models import Topic, Webpage, AccessRecord
from first_app import forms

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request,'first_app/index.html',context=date_dict)

def form_name_view(request):
    form = forms.FormName()
    
    if request.method == 'POST':
        form= forms.FormName(request.POST)
        if form.is_valid():
            print("Form validation successed")
            print("Name: " + form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print("Text: " + form.cleaned_data['text'])

    return render(request, 'first_app/form_page.html', {'form': form})

def other(request):
    return render(request, 'first_app/other.html')

def relative(request):
    return render(request, 'first_app/relative_url_templates.html')