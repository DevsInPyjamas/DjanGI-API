from django.conf.urls import url, include
from DjanGIUnchained import views

# thanks to
# https://stackoverflow.com/questions/43304923/typeerror-at-admin-set-object-is-not-reversible-and-argument-to-reverse-m?noredirect=1&lq=1
urlpatterns = [
    url(r'^all_types$', views.all_piece_types, name='Type pieces'),
    url(r'^pieces_from_type$', views.all_pieces_from_this_type, name='All Type Pieces'),
    url(r'^piece$', views.piece_data, name='All Type Pieces')
]
