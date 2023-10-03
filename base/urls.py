from django.urls import path
from .views import home
from .views import create
from .views import edit
from .views import delete
from .views import deleteall


urlpatterns = [
    path('home/', home, name='home'),
    path('create/', create, name='create'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('deleteall/', deleteall, name='deleteall'),

]