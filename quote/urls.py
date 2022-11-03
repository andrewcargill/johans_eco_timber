from . import views
from django.urls import path

urlpatterns = [
    path('', views.QuoteList.as_view(), name='home'),
    path('user_home3.html', views.QuoteList.as_view(), name='user_home'),
    path('user_home.html', views.User.as_view(), name='user_home'),
]