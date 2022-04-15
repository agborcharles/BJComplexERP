from django.urls import path
from . import views

app_name = 'contact_list'

urlpatterns = [
    path('', views.contacts_home, name='contact-home'),
    #path('add-contact/', views.add_contact.as_view(), name='add-contact'),
    path('contact-detail/<slug:slug>/',views.contacts_detail, name='contact-detail'),
    #path('edit-contact/<int:pk>/', views.edit_contact.as_view(), name='edit-contact'),

]
