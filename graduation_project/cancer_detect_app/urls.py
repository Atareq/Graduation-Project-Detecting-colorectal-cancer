from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name = 'home'),
    path('about-us',views.about,name = 'about'),
    path('help',views.help,name = 'help'),
    path('contact',views.contact,name = 'contact'),
    path('profile/', views.profile, name='profile'),
    path('profile-info/', views.profile_info, name='profile_info'),
    path('search/', views.search_results, name='search_results'),
    path('edit-test-result/<int:test_result_id>/', views.edit_test_result, name='edit-test-result'),
    path('delete-test-result/<int:test_result_id>/', views.delete_test_result, name='delete-test-result'),
    #authentication 
    path('register/',views.register,name = 'register'),
    path('login/', views.login_view, name='login'),
]