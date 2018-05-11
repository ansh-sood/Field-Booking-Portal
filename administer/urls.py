from django.conf.urls import url

from . import views

app_name = 'administer'

urlpatterns = [
    url(r'administer/', views.administer, name='administer'),
    url(r'(?P<user_id>[0-99]+)/approve/', views.approve, name='approve'),
    url(r'(?P<user_id>[0-99]+)/reject/', views.reject, name='reject'),
    url(r'search/', views.search, name='search'),
    url(r'history/', views.history, name='history'),
    url(r'reset_calender/', views.reset_calender, name='reset_calender'),
]
