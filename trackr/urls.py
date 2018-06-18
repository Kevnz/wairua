from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.homePage, name='index'),
    path('register', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile', views.profile, name='profile'),
    path('profile/edit', views.update_profile, name='profile_edit')
]
