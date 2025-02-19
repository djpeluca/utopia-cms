# -*- coding: utf-8 -*-

# © Copyright 2009 Andre Engelbrecht. All Rights Reserved.
# This script is licensed under the BSD Open Source Licence
# Please see the text file LICENCE for more information
# If this script is distributed, it must be accompanied by the Licence

import csv

from django.conf import settings
from django.contrib import admin
from django.http import HttpResponse
from adzone.models import *
from adzone.form import UploadFileForm


class AdvertiserAdmin(admin.ModelAdmin):
    search_fields = ['company_name', 'website']
    list_display = ['company_name', 'website', 'user']
    raw_id_fields = ['user']


class AdCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    list_display = ['title', 'slug']


class AdZoneAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'description']


class AdBaseAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'start_showing', 'stop_showing', 'category', 'zone']
    list_filter = ['start_showing', 'stop_showing', 'category', 'zone']
    search_fields = ['title', 'url']

    class Media:
        # jquery loaded again (admin uses custom js namespaces)
        js = ('admin/js/jquery%s.js' % ('' if settings.DEBUG else '.min'), 'js/adbase_admin.js')


class AdClickAdmin(admin.ModelAdmin):
    search_fields = ['ad', 'source_ip']
    list_display = ['ad', 'click_date', 'source_ip']
    list_filter = ['click_date', 'ad']
    date_hierarchy = 'click_date'
    actions = ['download_clicks']

    def download_clicks(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="clicks.csv"'
        writer = csv.writer(response)
        writer.writerow(('Title',
                         'Advertised URL',
                         'Source IP',
                         'Timestamp',
                         'Advertiser ID',
                         'Advertiser name',
                         'Zone'))
        queryset = queryset.select_related('ad', 'ad__advertiser')
        for impression in queryset:
            writer.writerow((impression.ad.title,
                             impression.ad.url,
                             impression.source_ip,
                             impression.click_date.isoformat(),
                             impression.ad.advertiser.pk,
                             impression.ad.advertiser.company_name,
                             impression.ad.zone.title))
        return response
    download_clicks.short_description = "Download selected Ad Clicks"

    def get_queryset(self, request):
        qs = super(AdClickAdmin, self).get_queryset(request)
        return qs.select_related('ad').only('ad__title',
                                            'click_date',
                                            'source_ip',)


class AdImpressionAdmin(admin.ModelAdmin):
    search_fields = ['ad', 'source_ip']
    list_display = ['ad', 'impression_date', 'source_ip']
    list_filter = ['impression_date', 'ad']
    date_hierarchy = 'impression_date'
    actions = ['download_impressions']

    def get_queryset(self, request):
        qs = super(AdImpressionAdmin, self).get_queryset(request)
        return qs.select_related('ad').only('ad__title',
                                            'impression_date',
                                            'source_ip')

    def download_impressions(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="impressions.csv"'
        writer = csv.writer(response)
        writer.writerow(('Title',
                         'Advertised URL',
                         'Source IP',
                         'Timestamp',
                         'Advertiser ID',
                         'Advertiser name',
                         'Zone'))
        queryset = queryset.select_related('ad', 'ad__advertiser')
        for impression in queryset:
            writer.writerow((impression.ad.title,
                             impression.ad.url,
                             impression.source_ip,
                             impression.impression_date.isoformat(),
                             impression.ad.advertiser.pk,
                             impression.ad.advertiser.company_name,
                             impression.ad.zone.title))
        return response
    download_impressions.short_description = "Download selected Ad Impressions"


class TextAdAdmin(AdBaseAdmin):
    search_fields = ['title', 'url', 'content']


class BannerAdAdmin(AdBaseAdmin):
    form = UploadFileForm
    list_display = [
        'title', 'content_basename', 'mobile_content_basename',
        'start_showing', 'stop_showing', 'category', 'zone']
    search_fields = ['title', 'url', 'content', 'mobile_content']


admin.site.register(Advertiser, AdvertiserAdmin)
admin.site.register(AdCategory, AdCategoryAdmin)
admin.site.register(AdZone, AdZoneAdmin)
admin.site.register(TextAd, TextAdAdmin)
admin.site.register(BannerAd, BannerAdAdmin)
admin.site.register(AdClick, AdClickAdmin)
admin.site.register(AdImpression, AdImpressionAdmin)
