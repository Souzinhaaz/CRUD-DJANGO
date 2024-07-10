from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import User
from .forms import UserModelForm

class UsersCreateView(CreateView):
    model = User
    form_class = UserModelForm
    template_name = 'user/user_form.html'
    success_url = '/users/'

class UsersListView(ListView):
    model = User
    template_name = 'user/users.html'
    context_object_name = 'usuarios'

class UsersUpdateView(UpdateView):
    model = User
    fields = ["name", "email", "created_at"]
    success_url = reverse_lazy('home')

class UsersDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('home')
