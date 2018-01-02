from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('user/', views.user),
    path('problem/', views.problem_list),
    path('problem/<int:pid>', views.problem),  # problem id
    path('status/', views.status),
]
