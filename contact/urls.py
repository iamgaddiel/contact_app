from django.urls import path
from .views import (
    create_contact_view, 
    list_contact_view, 
    contact_detail_view,
    contact_delete_view,
    contact_delete_confirm_view,
    contact_update_view,
    search_contact_view,
    ContactListView,
    ContactDetailView
)


urlpatterns = [
    path('', ContactListView.as_view(), name='contact_list'),
    path('contact_detail/<int:pk>', ContactDetailView.as_view(), name='contact_detail'),
    
    # path('', list_contact_view, name='contact_list'),
    path('add_contact/', create_contact_view, name='contact_create'),
    # path('contact_detail/<int:contact_id>', contact_detail_view, name='contact_detail'), # url/<data_type[int, str, uuid]:params>
    path('contact_delete/<int:contact_id>', contact_delete_view, name='contact_delete'), 
    path('contact_delete_confirm/<int:contact_id>', contact_delete_confirm_view, name='contact_delete_confirm'), 
    path('update/<int:contact_id>', contact_update_view, name='contact_update'), 
    path('search/', search_contact_view, name='search_contact'), 
]
