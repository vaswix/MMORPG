from django.urls import path

from sign.views import SignUpView, send_one_time_code, valid_code

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('confirmation/send_one_time_code/', send_one_time_code, name='send_one_time_code'),
    path('confirmation/valid_code/', valid_code, name='valid_code'),
]
