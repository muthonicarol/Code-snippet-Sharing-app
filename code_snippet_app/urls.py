from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name = 'home'),
    path('accounts/login/',views.login_view, name = 'login'),
    path('register/', views.register, name = 'register'),
    path('snippets/',views.snippets_list, name = 'snippets_list'),
    path('snippets/<int:pk>/', views.snippet_detail, name = 'snippet_detail'),
    path ('snippet_create/',views.snippet_create, name = 'snippet_create'),
    path('logout/', views.logout_view, name='logout_view'),
    path('snippet/<int:pk>/delete/', views.snippet_delete, name='snippet_delete')

]
