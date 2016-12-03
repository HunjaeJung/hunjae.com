from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'', views.daily_logs_list),
]
