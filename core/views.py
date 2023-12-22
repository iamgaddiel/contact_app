from typing import Any
from django.db import models
from django.http import HttpRequest, HttpResponse
from django.shortcuts import resolve_url
from django.views.generic import DetailView, UpdateView
from django.db.models.query import QuerySet
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .forms import CreateUserForm, UpdateUserForm
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView



class LandingPageView(TemplateView):
    template_name = 'core/landing_page.html'


    
# Create your views here.
def core_index_view(request) -> HttpResponse:
    template_name = 'core/index.html'
    return render(request, template_name)


def core_about_view(request) -> HttpResponse:
    template_name = 'core/about.html'
    return render(request, template_name)


def core_contact_view(request) -> HttpResponse:
    template_name = 'core/contact.html'
    return render(request, template_name)


def create_user_view(request) -> HttpResponse:
    template_name = 'core/create_user.html'

    if request.method == 'POST':
        create_user_form = CreateUserForm(request.POST)
        if create_user_form.is_valid():
            # first_name = create_user_form.cleaned_data.get('first_name')
            create_user_form.save()
            return redirect('create_user_success')

    context= {
        'create_user_form': CreateUserForm()
    }
    return render(request, template_name, context)


def create_user_success_view(request) -> HttpResponse:
    template_name = 'core/create_user_success.html'
    return render(request, template_name)


class Profile(DetailView):
    template_name='core/profile.html'

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> User:
        user_id = self.kwargs.get('pk')
        return User.objects.get(pk=user_id)
    

class ProfileUpdate(UpdateView):
    template_name = 'core/profile_update.html'
    form_class = UpdateUserForm
    model = User
    # success_url = ''

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> User:
        user_id = self.kwargs.get('pk')
        return User.objects.get(pk=user_id)
    
    def get_success_url(self) -> str:
        user = self.request.user
        return resolve_url('profile', pk=user.pk)


class Login(LoginView):
    template_name='core/login.html'
    
    def get_success_url(self) -> str:
        url = resolve_url(to='contact_list')
        if self.request.user.is_superuser:
            url = resolve_url(to='admin_user_list')
        return url

# FBV -> Function Based View(s)
# CBV -> Class Based View(s)
