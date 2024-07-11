from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import User
from .forms import UserModelForm

class UsersCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserModelForm
    template_name = 'new_user.html'
    success_url = '/users/'
    success_message = "%(name)s foi criado com sucesso!"

class UsersListView(ListView):
    model = User
    template_name = 'users.html'
    context_object_name = 'usuarios'
    
    def get_queryset(self):
        users = super().get_queryset().order_by('name')
        search = self.request.GET.get('search')
        if search:
            users = users.filter(name__icontains=search)
        return users

class UsersUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserModelForm
    template_name = 'user_update.html'
    success_url = reverse_lazy('home')
    success_message = "%(name)s foi atualizado com sucesso!"

class UsersDeleteView(SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'user_delete.html'
    context_object_name = 'usuario'
    success_url = reverse_lazy('home')
    success_message = "O usuário foi deletado com sucesso!"
