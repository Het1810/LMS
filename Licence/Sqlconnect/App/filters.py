# filters.py
import django_filters
from django import forms
# from datetime import datetime
from django.forms.widgets import DateInput
from .models import CreLogs, CreActions, CreModules, CustomUser


# class DateInput(forms.DateInput):
#     input_type = 'date'
#

class LogFilter(django_filters.FilterSet):
    intuserid = django_filters.ModelChoiceFilter(queryset=CustomUser.objects.all(), label='User', empty_label='All',widget=forms.Select(attrs={'style': 'width: 150px;'}))
    intmoduleid = django_filters.ModelChoiceFilter(queryset=CreModules.objects.all(), label='Module', empty_label='All',widget=forms.Select(attrs={'style': 'width: 150px;'}))
    intactionid = django_filters.ModelChoiceFilter(queryset=CreActions.objects.all(), label='Action', empty_label='All',widget=forms.Select(attrs={'style': 'width: 150px;'}))
    dtdatetime = django_filters.DateTimeFilter(label='Date/Time', method='filter_datetime',widget=DateInput(attrs={'type': 'date', 'style': 'width: 150px;'}))

    def filter_datetime(self, queryset, name, value):
        if value:
            return queryset.filter(**{f'{name}__date': value})
        return queryset

    class Meta:
        model = CreLogs
        fields = ['intuserid', 'intmoduleid', 'intactionid', 'dtdatetime']

        widgets = {
            'dtdatetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
