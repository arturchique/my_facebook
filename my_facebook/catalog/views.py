from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from .forms import RegisterForm
from django.contrib.auth import authenticate
from django.db import IntegrityError


class HomeView(TemplateView):
    template_name = "home.html"


def test(request):
    users = User.objects.all()
    return render(
        request,
        'test.html',
        context={
            'users': users
        },
    )


class RegisterView(TemplateView):
    template_name = "registration/register.html"

    def dispatch(self, request, *args, **kwargs):
        form = RegisterForm()
        try:
            if request.method == 'POST':
                form = RegisterForm(request.POST)
                if form.is_valid():
                    self.create_new_user(form)
                    messages.success(request, u"Вы успешно зарегистрировались!")
                    return redirect(reverse("login"))
            context = {
                'form': form,
            }
            return render(request, self.template_name, context)
        except IntegrityError:
            context = {
                'form': form,
                'user_error': "Пользователь с таким именем уже существует",
            }
            return render(request, self.template_name, context)

    def create_new_user(self, form):
        email = None
        if 'email' in form.cleaned_data:
            email = form.cleaned_data['email']
        User.objects.create_user(form.cleaned_data['username'], email, form.cleaned_data['password'],
                                 first_name=form.cleaned_data['first_name'],
                                 last_name=form.cleaned_data['last_name'])


class LogoutView(View):
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return redirect("/")


class ProfileView(TemplateView):
    template_name = "registration/profile.html"