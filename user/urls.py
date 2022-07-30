from django.urls import path
from user import views
from django.contrib.auth import views as core_views
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from user import views as core_views
from user.views import CustomLoginView  
from user.forms import LoginForm


# from .views import registration_view

urlpatterns = [
    path('', core_views.home, name='home'),
    path('signup/', core_views.signup, name='signup'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='login.html',
                                           authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='index.html'), name='logout'),
    path('accounts/', include('allauth.urls')),
    # /accounts/google/login/?process=login
    # path('', core_views.home, name='home'),
]