from django.urls import path, include
from SerializeApp import views

urlpatterns = [
    path('', views.getdata),
    #path('', views.serializeToJSONdata),
    #path('', views.serializeToJSONLdata),
    path('1/', views.deserializedata),
]