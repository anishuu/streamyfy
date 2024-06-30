from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPage, name='index'),
    path('home/', views.HomePage, name='home'),
    path('signup/', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('logout/', views.LogoutPage, name='logout'),
    path('payment/', views.payment, name='payment'),
    path('paymentpic/<int:user_id>/<int:plan_id>/', views.paymentpic, name='paymentpic'),
    path('receipt/', views.receipt, name='receipt'),
    path('movie/<int:Show_id>/', views.movie, name='movie'),
    path('profile/', views.profile, name='profile'),
    path('userprofile/',views.userprofile,name='userprofile')
]
