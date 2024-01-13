from django.urls import path
from . import views

urlpatterns=[
    path('',views.showusers),
    path('signup/',views.signup),
    path('deleteuser/<int:uid>/',views.deleteuser),
    path('userbyid/<int:uid>/',views.getuserbyid),
]