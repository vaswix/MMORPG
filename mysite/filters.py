import django_filters

from mysite.models import Advert


class ReplyFilter(django_filters.FilterSet):
    class Meta:
        model = Advert
        fields = ['category', 'title']
