from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from django.contrib import messages

from bestcar.utils import DataMixin
from sitecars import settings

from users.forms import LoginUserForms, Regestration_User_Form, UserProfile, User_Password_change_form


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForms
    template_name = 'users/login.html'
    title_page = 'Авторизация'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context)

    #def get_success_url(self):
    #return reverse_lazy('home')


#def login_user(request):
#if request.method == 'POST':
#form = LoginUserForms(request.POST)
#if form.is_valid():
#cd = form.cleaned_data
#user = authenticate(request, username=cd['username'], password = cd['password'])
#if user and user.is_active:
#login(request,user)
#return HttpResponseRedirect(reverse('home'))
#else:
#form = LoginUserForms()
#return render(request, 'users/login.html', {'form':form})


#def logout_user(request):
#logout(request)
#return HttpResponseRedirect(reverse('users:login'))

#def register(request):

#if request.method == 'POST':
#form = Regestration_User_Form(request.POST)
#if form.is_valid():
#user = form.save(commit=False)
#user.set_password(form.cleaned_data['password'])
#form.save()
#return render(request,'users/register.html')
#else:
#form = Regestration_User_Form()
#return render(request,'users/register.html',{'form':form})

class RegisterUser(CreateView):
    form_class = Regestration_User_Form
    template_name = 'users/register.html'
    extra_context = {'title': 'Регистрация'}
    success_url = reverse_lazy('users:login')


class ProfileUser(DataMixin, LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UserProfile
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, default_image=settings.DEFAULT_USER_IMAGE)

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class Users_Password_change(PasswordChangeView):
    form_class = User_Password_change_form
    success_url = reverse_lazy("users:password_change_done")
    template_name = "users/password_change_form.html"

@login_required
def delete_user(request):
        user = request.user
        user.delete()
        return HttpResponseRedirect(reverse('users:register'))
