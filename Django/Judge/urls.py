from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('user/<int:uid>/', views.user),
    path('problem/', views.problem_list),
    path('problem/<int:pid>/', views.problem),  # problem id
    path('problem/<int:pid>/submit', views.submit),  # problem id
    path('problem/<int:pid>/submitted', views.submitted),  # problem id
    path('status/', views.status),
]
