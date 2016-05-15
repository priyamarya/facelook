from django.conf.urls import url
from .views import login, register, logout, user_details_entry, user


urlpatterns = [
    url(r'^login/$', login, name="login"),
    url(r'^register/$', register),
    url(r'^logout/$', logout),
    url(r'^userdetailsentry/$', user_details_entry),
    url(r'^(?P<username>\w+)$', user),



]
