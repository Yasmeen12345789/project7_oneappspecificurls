from django.urls import path
from mi.views import *

urlpatterns=[
    
    path('rohit/',rohit,name='rohit'),
    path('sachin/',sachin,name='sachin')
]