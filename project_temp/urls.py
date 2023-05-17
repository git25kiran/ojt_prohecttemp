
from django.contrib import admin
from django.urls import path
from temp_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/' , views.home_view),
    path('task1/' , views.task1_view),
    path('task2/' , views.task2_view),
    path('task3/' , views.task3_view),


]
