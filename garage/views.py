from django.http import Http404
from django.shortcuts import render, redirect
from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView, ListView, DetailView
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import *
from .models import *


class ListCars(LoginRequiredMixin, ListView):
    queryset = Cars.objects.select_related().order_by('date_of_issue').annotate(cnt=Sum('type_of_repair__price'))
    context_object_name = 'cars'
    template_name = 'garage/cars_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Автомобили в работе'
        return context
    

class ListManufact(ListView):
    template_name = 'garage/manufact_view.html'
    queryset = Manufacturers.objects.select_related()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список производителей'
        return context


class ListPrice(ListView):
    model = PriceList
    template_name = 'garage/price_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Прайс-лист'
        return context


class CreateCar(CreateView):
    form_class = CarForm
    template_name = 'garage/base_form.html'
    success_url = reverse_lazy('cars_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['btn_accept'] = 'Добавить'
        context['btn_clear'] = 'Очистить'
        context['title'] = 'Добавить автомобиль'
        return context


class CreateManufact(CreateView):
    form_class = ManufactForm
    template_name = 'garage/base_form.html'
    success_url = reverse_lazy('manufact_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['btn_accept'] = 'Добавить'
        context['btn_clear'] = 'Очистить'
        context['title'] = 'Добавить Производителя'
        return context


class CreateCarModel(CreateView):
    form_class = CarModelForm
    success_url = reverse_lazy('manufact_list')
    template_name = 'garage/base_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['btn_accept'] = 'Добавить'
        context['btn_clear'] = 'Очистить'
        context['title'] = 'Добавить Модель'
        return context


class CreatePrice(CreateView):
    form_class = PriceForm
    template_name = 'garage/base_form.html'
    success_url = reverse_lazy('price_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['btn_accept'] = 'Добавить'
        context['btn_clear'] = 'Очистить'
        context['title'] = 'Добавить услугу'
        return context


class CreateMechanics(CreateView):
    form_class = MechanicsForm
    template_name = 'garage/base_form.html'
    success_url = reverse_lazy('Home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить механика'
        context['btn_accept'] = 'Добавить'
        context['btn_clear'] = 'Очистить'
        return context


class CreateOwners(CreateView):
    form_class = OwnerForm
    template_name = 'garage/base_form.html'
    success_url = reverse_lazy('add_owners')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить клиента'
        context['btn_accept'] = 'Добавить'
        context['btn_clear'] = 'Очистить'
        return context


class UpdateCar(UpdateView):
    model = Cars
    form_class = CarForm
    template_name = 'garage/base_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактировать авто'
        context['btn_accept'] = 'Изменить'
        context['btn_clear'] = 'Очистить'
        return context


class UpdateManufact(UpdateView):
    model = Manufacturers
    form_class = ManufactForm
    template_name = 'garage/base_form.html'
    success_url = reverse_lazy('manufact_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Изменить производителя'
        context['btn_accept'] = 'Изменить'
        context['btn_clear'] = 'Очистить'
        return context


class UpdateModelCar(UpdateView):
    model = CarModels
    form_class = CarModelForm
    template_name = 'garage/base_form.html'
    success_url = reverse_lazy('manufact_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['btn_accept'] = 'Изменить'
        context['btn_clear'] = 'Очистить'
        context['title'] = self.object.title
        return context


class UpdatePrice(UpdateView):
    model = PriceList
    form_class = PriceForm
    template_name = 'garage/base_form.html'
    success_url = reverse_lazy('price_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['btn_accept'] = 'Изменить'
        context['btn_clear'] = 'Очистить'
        context['title'] = self.object.type_of_repair
        return context


class DetailCars(DetailView):
    template_name = 'garage/cars_detail.html'

    def get_queryset(self):
        return Cars.objects.annotate(cnt=Sum('type_of_repair__price')).filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.gov_number
        return context


class HelpPage(TemplateView):
    template_name = 'garage/help.html'


class CreateUser(CreateView):
    form_class = UserForm
    template_name = 'garage/base_form.html'
    success_url = reverse_lazy('Home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация пользователя'
        context['btn_accept'] = 'Зарегистрироваться'
        context['btn_clear'] = 'Очистить'
        return context


def index(request):
    return render(request, 'garage/base.html', {'title': 'Главная'})


def auth_user(request):
    if request.method == 'POST':
        form = UserAuthentication(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Home')
        else:
            messages.error(request, 'Неверный логин либо пароль')
            return redirect('auth')
    else:
        form = UserAuthentication()     
    return render(request, 'garage/base_form.html', {'title': 'Авторизация', 'form': form, 'btn_accept': 'Войти', 'btn_clear': 'Очистить'})


def logout_user(request):
    logout(request)
    return redirect ('Home')

