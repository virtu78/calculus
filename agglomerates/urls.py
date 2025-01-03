"""
Схемы URL  для  agglomerates
"""

from django.urls import re_path
from . import views


app_name='agglomerates'
urlpatterns = [
  
    re_path(r'^$', views.index, name='index'),
    re_path(r'^new_entry/(?P<id>\d+)/$', views.new_entry, name='new_entry'),
    re_path(r'^new_date/$', views.new_date, name='new_date'),
    re_path(r'^all_dates/$', views.all_dates, name='all_dates'),
    re_path(r'^all_dates/(?P<id>\d+)/$', views.single_date, name='single_date'),
    re_path(r'^table/$', views.table, name='table'),
    
     re_path(r'^edit_actual/(?P<id>\d+)/$', views.edit_actual_output, name='edit_actual_output'),
     re_path(r'^export/xls/$', views.export_in_excel, name='export_in_excel'), 
     re_path(r'^import/$', views.import_from_excel, name='import_from_excel'),
     
    

]
handler404 = 'agglomerates.pageNotFound'