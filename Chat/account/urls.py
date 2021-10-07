from django.urls import path
from .views import *


urlpatterns = [
    path('signup/',signup,name='signup'),
    path('logout/',logout_request,name='logout'),
    path('login/',login_request,name='login'),

]