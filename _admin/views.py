from django.shortcuts import render, resolve_url
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.models import User
from .forms import UserUpdateForm



class ListUsers(ListView):
    template_name = '_admin/user_list.html'
    model = User


class UserDetailView(DetailView):
    template_name = '_admin/user_detail.html'
    model = User
    context_object_name = 'object'

class UserDeleteView(DeleteView):
    template_name='_admin/user_delete.html'
    model = User

    def get_success_url(self) -> str:
        return resolve_url(to='admin_user_list')
    
class UserUpdateView(UpdateView):
    template_name = '_admin/user_update.html'
    model = User
    form_class = UserUpdateForm

    def get_success_url(self, **kwargs) -> str:
        contact_id = self.object.pk
        return resolve_url('admin_user_detail', pk=contact_id)