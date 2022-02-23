from django.urls import path
from.import views
urlpatterns = [

    path("regiterdetails/",views.regiterdetails, name="regiterdetails"),

    path("",views.dam, name="gym"),

    path("Home/",views.Home, name="Home"),

    path("About_Us/",views.about, name="AboutUs"),

    path("Services/",views.Services, name="Services"),

    path("Contact_Us/",views.contact, name="ContactUs"),
]

