from django.conf.urls import url

from . import views

app_name = 'main'

urlpatterns = [
    url(r'search/', views.search, name='search'),
    # url(r'create_calender/', views.calender, name='create_calender'),
    # url(r'delete_calender/', views.delete_calender, name='delete_calender'),
    url(r'(?P<date_id>[0-99]+)/select_date/', views.select_date, name='select_date'),
    url(r'(?P<object_id>[0-99]+)/update/', views.update, name='update'),
    url(r'notify/', views.notify, name='notify'),

]