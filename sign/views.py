import json
import random

from django.contrib.auth import login
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from sign.forms import CustomUserCreationForm
from sign.models import OneTimeCode


class SignUpView(View):

    def get(self, request, *args, **kwargs):
        form = CustomUserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('advert_list')


def send_one_time_code(request):
    data = json.loads(request.body)
    email = data.get('email')
    if email is not None:
        one_time_code = random.randint(1000, 9999)
        print(one_time_code)
        OneTimeCode.objects.create(code=one_time_code, email=data['email'])

        # send_mail(
        #     subject=f'Подтверждение почты',
        #     message=f'Код подтверждения вашей почты: {one_time_code}',
        #     from_email='Lack10000@yandex.ru',
        #     recipient_list=[email],
        # )

        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'failed'})


def valid_code(request):
    data = json.loads(request.body)
    email = data.get('email')
    code = data.get('one_time_code')
    if email and code is not None:
        if OneTimeCode.objects.filter(code=int(code), email=email).exists():
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'wrong code'})
    else:
        return JsonResponse({'status': 'failed'})
