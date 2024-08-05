from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name = 'home'),
    path('login/',views.login_view, name = 'login'),
    path('register/', views.register, name = 'register'),
    path('snippets/',views.snippets_list, name = 'snippets_list'),
    path('snippets/<int:pk>/', views.snippets_detail, name = 'snippets_list'),
    path ('snippet_create/',views.snippet_create, name = 'snippet_create')

]
