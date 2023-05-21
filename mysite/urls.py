from django.urls import path

from mysite.views import AdvertList, AdvertDetail, AdvertCreate, ReplyList, ReplyDelete, AcceptReply

urlpatterns = [
    path('', AdvertList.as_view(), name='advert_list'),
    path('advert/<int:pk>', AdvertDetail.as_view(), name='advert_detail'),
    path('advert_create/', AdvertCreate.as_view(), name='advert_create'),
    path('reply_list/', ReplyList.as_view(), name='reply_list'),
    path('reply_delete/<int:pk>/', ReplyDelete.as_view(), name='reply_delete'),
    path('accept_reply/<int:advert_pk>/<int:reply_pk>', AcceptReply.as_view(), name='accept_reply')
]
