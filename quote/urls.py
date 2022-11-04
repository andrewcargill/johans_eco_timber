from . import views
from django.urls import path

urlpatterns = [
    path('', views.QuoteList.as_view(), name='home'),
    path('user_home.html', views.get_name, name='user_home'),
]