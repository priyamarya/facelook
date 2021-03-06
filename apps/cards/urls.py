from django.conf.urls import url
from .views import all_cards, view_card, new_card, likes


urlpatterns = [
    url(r'^all/$', all_cards, name="all"),
    url(r'^newcard/$', new_card),
    url(r'^all/(?P<card_id>\d+)/$', view_card ),
    url(r'^likes/(?P<card_id>\d+)/$', likes, name="like"),
]
