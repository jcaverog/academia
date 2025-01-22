from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView
from cursos.forms import RegistroUsuarioForm
from cursos.models import curso


# Create your views here.

class ListaCursosView(LoginRequiredMixin, ListView):
    model = curso
    template_name = 'cursos/lista_cursos.html'

    context_object_name = 'cursos'

    def get_queryset(self):
        if self.request.user.rol == 'admin':
            return curso.objects.all()
        return curso.objects.filter(estado=True)


class CustomLoginView(LoginView):
    template_name = "registro/login.html"
    def form_invalid(self, form):
        messages.error(self.request,  'Usuario o contraseña incorrecto. Por favor ingrese nuevamente')
        return super().form_valid(form)

class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Sesion cerrada correctamente')
        response = redirect('login')
        response['Cache-Control']= 'no-cache, no-store, must-revelidate'
        response['Pragma'] = 'no cache'
        response['Expires'] = '0'
        return response

class RegistroUsuarioView(CreateView):
    form_class = RegistroUsuarioForm
    template_name = 'registro/registro.html'
    success_url = reverse_lazy('lista_cursos.html')


    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        messages.success(self.request, "Se ha registrado exitosamente")
        return response

    def form_invalid(self, form):
         for field, erros in form.errors.items():
             for error in erros:
                 messages.error(self.request, f"{field}: {error}")
         return super().form_invalid(form)