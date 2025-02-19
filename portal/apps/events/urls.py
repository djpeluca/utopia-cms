# -*- coding: utf-8 -*-
from views import calendar, day_detail, event_detail

from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', calendar, name='events-calendar'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$', calendar,
        name='events-calendar'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', day_detail,
        name='events-day_detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<event_slug>[\w-]+)/$',
        event_detail, name='events-event_detail'),
]
