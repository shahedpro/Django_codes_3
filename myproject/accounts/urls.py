from django.urls import path
from .views import signup_view, login_view, logout_view, profile_view, change_password

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('change_password/', change_password, name='change_password'),
]
