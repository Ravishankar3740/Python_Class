from django.db import models
from django.db.models.signals import post_save
# from twilio.rest import Client
# Create your models here.
class Enquiryuser(models.Model):
    username = models.CharField(max_length=255)
    email_Id = models.EmailField()
    phone_no = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    details = models.TextField() 

    def __str__(self) -> str:
        return self.phone_no

# def sendsms(sender,instance,**kwargs):
#     # Your Account SID from twilio.com/console
#     account_sid = "AC8a8db2a840158b85038e90f5883acb1e"
#     # Your Auth Token from twilio.com/console
#     auth_token  = "0a9d6cf5c30ef4042622ec5e643c8976"

#     client = Client(account_sid, auth_token)

#     message = client.messages.create(
#     to="+91" + str(instance.phone_no),
#     from_="+12153986380",
#     body="Your Regestration is Succesful! Wel-come To Super Gym ")



# post_save.connect(sendsms,sender = registeruser)



