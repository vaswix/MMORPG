from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.views.generic.edit import FormMixin

from .filters import ReplyFilter
from .forms import AdvertCreationForm, ReplyCreationForm
from .models import Advert, Reply


class AdvertList(ListView):
    model = Advert
    template_name = 'index.html'
    ordering = '-id'


class AdvertDetail(FormMixin, DetailView):
    model = Advert
    template_name = 'detail_advert.html'
    form_class = ReplyCreationForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.advert = self.object
        form.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('advert_detail', kwargs={'pk': self.kwargs.get('pk')})


class AdvertCreate(LoginRequiredMixin, CreateView):
    template_name = 'create_advert.html'
    form_class = AdvertCreationForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('advert_list')


class ReplyList(LoginRequiredMixin, ListView):
    model = Advert
    template_name = 'list_reply.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ReplyFilter(self.request.GET, Advert.objects.filter(author=self.request.user))
        return context


class ReplyDelete(LoginRequiredMixin, DeleteView):
    model = Reply
    template_name = 'confirm_delete_reply.html'
    success_url = reverse_lazy('reply_list')


class AcceptReply(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        advert = Advert.objects.filter(pk=self.kwargs.get('advert_pk'))
        reply_pk = self.kwargs.get('reply_pk')
        advert.update(accepted_reply_id=reply_pk)
        user_email = Reply.objects.filter(id=reply_pk).values('author__email')[0].get('email')

        # Отправка по email

        send_mail(
            subject=f'Ваша запись была принята пользователем {self.request.user}',
            message=f'Пользователь {self.request.user} принял вашу запись',
            from_email='Lack10000@yandex.ru',
            recipient_list=[user_email]
        )

        return redirect('reply_list')
