from . import views
from django.urls import path

app_name='restorapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('booking',views.booking,name='booking'),
    path('contact',views.booking,name='contact'),
    path('menu',views.menu,name='menu'),
    path('service',views.service,name='service'),
    path('team',views.team,name='team'),
    path('testimonial',views.testimonial,name='testimonial')
]