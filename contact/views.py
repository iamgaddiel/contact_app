from typing import Any
from django.db import models
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.query import Q, QuerySet #<- Learn this

from django.views.generic import ListView, DeleteView, DetailView, TemplateView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

from .forms import CreateContactForm, ContactUpdateForm
from .models import Contact




def search_contact_view(request: HttpRequest) -> HttpResponse:
    """
    Search for contacts with
    """
    # **kwargs and *args
    template_name = 'contact/search_result.html'
    context = {}
    
    query = request.GET.get('search_query')

    # Error checking
    if query is None:
        context['error_message'] = 'Query Parameter Invalid'
        return render(request, template_name, context) # <-- Function call ends here if query is None. | guard clause

    # Search DB for query
    contacts_found = Contact.objects.filter(Q(first_name=query) | Q(last_name=query))

    context['contacts'] = contacts_found
    context['query'] = query
    return render(request, template_name, context)


@login_required(login_url='/login')
def create_contact_view(request: HttpRequest) -> HttpResponse:
    """ A view to handle creating of contacts which belongs to a logged in user."""

    if request.method == 'POST':
        contact_form = CreateContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.instance.user = request.user # Set form user object to the currently logged in user
            contact_form.save()
            return redirect('contact_list')
            # form.cleaned_data.get('form_field_name) # How to get form data from submitted form

        else:
            print(contact_form.errors)

    template_name = 'contact/create_contact.html'
    context = {
        'contact_form': CreateContactForm(),
    }
    return render(request, template_name, context)


def list_contact_view(request):
    """ A view handle listing of contacts belonging to the current logged in user"""

    # .get()
    # .filter()
    # .create()
    # .all()
    # .get_or_create()
    
    # Database query
    # Model.objects.query_func(query_params)
    context = {}
    if request.user.is_authenticated:
        context['contacts'] = Contact.objects.filter(user=request.user).order_by('-first_name')

    template_name = 'contact/contact_list.html'
    return render(request, template_name, context)


@login_required(login_url='/login')
def contact_detail_view(request: HttpRequest, contact_id: int) -> HttpResponse:
    """
        This view gets contact based on the id
        prams: 
            - request
            - contact_id: the variable used for dynamic link in the app's urls.py file
    """

    template_name = 'contact/contact_detail.html'
    # Url Query parameters /link?key=value
    # Url Query parameters /link/<generated_value>
    try:
        # get the Contact belongs to the current logged in user
        context = {
            'contact': Contact.objects.get(id=contact_id, user=request.user)
        }
    except ObjectDoesNotExist:
        page_not_found_template_name = 'core/not_found.html'
        return render(request, page_not_found_template_name)

    return render(request, template_name, context)


@login_required(login_url='/login')
def contact_delete_view(request: HttpRequest, contact_id: int) -> HttpResponse:
    template_name = 'contact/contact_delete.html'
    try:
        context = {
            'contact': Contact.objects.get(id=contact_id, user=request.user)
        }
    except ObjectDoesNotExist:
        page_not_found_template_name = 'core/not_found.html'
        return render(request, page_not_found_template_name)
    
    return render(request, template_name, context)


def contact_delete_confirm_view(request: HttpRequest,contact_id: int) -> HttpResponse:
    Contact.objects.get(id=contact_id).delete()
    return redirect('contact_list')


def contact_update_view(request:HttpRequest, contact_id: int) -> HttpResponse:
    """This view enables updating of the user's contact detail """
    template_name = 'contact/contact_update.html'

    try:
        selected_contact_detail = Contact.objects.get(id=contact_id, user=request.user)

        if (request.method == 'POST'):
            update_form = ContactUpdateForm(instance=selected_contact_detail, data=request.POST, files=request.FILES)
            if update_form.is_valid():
                update_form.save()
            return redirect('contact_detail', pk=selected_contact_detail.id) # redirect to contact detail page with contact id

        # auto populate the update form UI with selected contact detail
        contact_update_form = ContactUpdateForm(instance=selected_contact_detail) 
        context = {
            'update_form': contact_update_form
        }

    except ObjectDoesNotExist:
        page_not_found_template_name = 'core/not_found.html'
        return render(request, page_not_found_template_name)
    
    return render(request, template_name, context)



class ContactListView(ListView):
    template_name = 'contact/contact_list.html'

    def get_queryset(self) -> QuerySet[Any]:
        if self.request.user.is_anonymous: return []
        return Contact.objects.filter(user=self.request.user).order_by('-first_name')
    

class ContactDetailView(LoginRequiredMixin,  DetailView):
    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Contact:
        contact_id = self.kwargs.get('pk')
        return Contact.objects.get(pk=contact_id)
