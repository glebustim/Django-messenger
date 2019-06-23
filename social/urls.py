from django.contrib import admin
from django.urls import path, include
from social import views

urlpatterns = [
    path('manage/', admin.site.urls),
    path('', views.main),
    path('rooms', views.rooms, name='index'),
    path('users', views.users),
    path('user<int:id>', views.user),
    path('action', views.action),
    path('room<int:id>', views.room),
    path('', include('django.contrib.auth.urls')),
    path('register', views.RegisterFormView.as_view(), name='register'),
    path('manage_access_users',views.manage_access_users),
]