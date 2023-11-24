from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # you need a path to login only if you want to your login in a different page than your home page ex:
    # path('login/', views.login_user, name='login'),  
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('profile/', views.profile, name='profile'),
    path('appliances/', views.appliances, name='appliances'),
    path('delete_kichen_appliance/<int:pk>', views.delete_kichen_appliance, name='delete_kichen_appliance'),
    path('add_kitchen_record/', views.add_kitchen_record, name='add_kitchen_record'),
]
