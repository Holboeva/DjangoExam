from django.contrib.auth.hashers import make_password
from django.shortcuts import render, get_object_or_404

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from apps.forms import RegisterForm, LoginForm
from apps.models import Product


def register_view(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        first_name = request.POST.get('first_name')
        username = request.POST.get('username')
        password = make_password(request.POST.get('password'))
        user = User.objects.filter(username=username)
        if not user.exists():
            User.objects.create_user(first_name=first_name, username=username, password=password)
            return render(request, 'login.html')
        return render(request, 'register.html')

def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')



def ProfileSettingsView(request):
    return render(request, 'profile_settings_update.html')

def category_view(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'category_product_list.html', context)

def product_detail_view(request, pk):
    product = get_object_or_404(Product.objects.all(), pk=pk)
    context = {
        'product': product,
    }
    return render(request, 'product_detail.html', context)
# class UserRegisterView(CreateView):
#     queryset = User.objects.all()
#     template_name = 'register.html'
#     form_class = RegisterForm
#     success_url = reverse_lazy('home')
#
#     def form_valid(self, form):
#         return super().form_valid(form)
#
#     def form_invalid(self, form):
#         return super().form_invalid(form)


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('home')

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