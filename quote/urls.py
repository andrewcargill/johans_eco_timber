from . import views
from django.urls import path

urlpatterns = [
    path('', views.QuoteList.as_view(), name='home'),
    path('user_home.html', views.QuoteInput, name='user_home'),
    path('quote_list.html', views.UserQuoteList.as_view(), name='quote_list'),
    # path('user_home.html', views.get_name, name='user_home'),
    path('add_item.html', views.NewItem, name='add_item'),
]