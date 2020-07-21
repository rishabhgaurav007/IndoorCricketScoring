from django.contrib import admin
from django.urls import path
from Matches import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('',views.index,name='home'),
    path('<int:pk>/',views.show,name='show'),
    path('scores/',views.score,name='score')
]