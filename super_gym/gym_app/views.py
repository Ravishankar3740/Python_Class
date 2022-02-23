from typing import ContextManager
from django.shortcuts import render,HttpResponse
from.forms import RegisterForm
from .models import Enquiryuser
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
# Create your views here.
def regiterdetails(request):
    
    if request.method == 'POST':
        formf = RegisterForm(request.POST)
        print(formf.is_valid)
        if formf.is_valid():
            
            formf.save()
            
            mail_subject = 'Python Class Enquiry'
            idd = Enquiryuser.objects.filter(phone_no = formf.cleaned_data['phone_no']).last()

            message = render_to_string('gym_app/send_enquiey.html', {
				'user': idd,
				
			})
            to_email = ['sohailbadeghar561@gmail.com', "ravi.birajdar8880@gmail.com", "sunil.jokare@gmail.com"]
            email_send = EmailMessage(
						mail_subject, message, to=[to_email]
			)
            email_send.content_subtype = 'html'
            email_send.send()
            print("send")
            return render(request,"gym_app/en_done.html")
    else:
        return render(request,"gym_app/Enquiry.html")




def Home(request):
    return HttpResponse("WEL COME TO SUPER GYM")

def about(request):
    return HttpResponse("THIS IS ABOUT US")

def Services(request):
    return HttpResponse("THIS IS ABOUT SERVICES")

def contact(request):
    return render(request,"gym_app/Enquiry.html")    

  

def dam(request):
    return render (request,"gym_app/gym.html")    

