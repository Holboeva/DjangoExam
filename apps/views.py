from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, UpdateView, ListView, DetailView

from apps.forms import RegisterForm, LoginForm, EditProfileForm
from apps.models import User, Category, Product


class RegisterView(CreateView):
    queryset = User.objects.all()
    form_class = RegisterForm
    template_name = 'apps/register.html'
    success_url = reverse_lazy('login')


class UserLoginView(FormView):
    form_class = LoginForm
    template_name = 'apps/login.html'
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        password = form.cleaned_data.get('password')
        username = form.cleaned_data.get('username')
        query = User.objects.filter(username=username)
        if query.exists():
            user = query.first()
            if user.check_password(password):
                login(self.request, user)
            else:
                messages.error(self.request, 'Mahfiy raqam xato')
                return redirect('login')
        else:
            messages.error(self.request, 'Foydalanuvchi topilmadi')
            return redirect('login')
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'apps/profile.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class EditProfileView(UpdateView):
    queryset = User.objects.all()
    form_class = EditProfileForm
    template_name = 'apps/profile.html'
    success_url = reverse_lazy('password_change')


class HomePage(ListView):
    queryset = Category.objects.all()
    context_object_name = 'categories'
    template_name = 'apps/category_product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    context_object_name = 'product'
    template_name = 'apps/product_detail.html'
