from . import views
from django.urls import path

urlpatterns = [
    path('', views.QuoteList.as_view(), name='home'),
    path('about.html', views.About.as_view(), name='about'),
    path('about_enquiry_system.html', views.AboutEnquiry.as_view(), name='about_enquiry_system'),
    path('new_enquiry.html', views.QuoteInput, name='new_enquiry'),
    path('quote_list.html', views.UserQuoteList.as_view(), name='quote_list'),
    # path('new_enquiry.html', views.get_name, name='new_enquiry'),
    path('add_item.html', views.NewItem, name='add_item'),
    path('<int:id>/', views.QuoteDetail.as_view(), name='quote_detail'),
    path('<int:pk>/update/', views.QuoteUpdate.as_view(), name='quote_update'),
    path('<int:pk>/delete/', views.QuoteDelete.as_view(),
         name='quote_delete'),

]