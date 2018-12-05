from django.http import HttpResponse, HttpResponseBadRequest

from DjanGIUnchained import models
from django.core import serializers
# Create your views here.


def all_piece_types(request):
    """
        The mighty power of the request that requests all the piece types
    :param request: literally the request
    :return: all objects serialized as a JSON with a HTTP response
    """
    query_repsonse = models.PieceType.objects.all()
    return HttpResponse(serializers.serialize('json', query_repsonse))


def all_pieces_from_this_type(request):
    """
        The mighty power of the request that requests all the piece types
    :param request: literally the request
    :return: all objects serialized as a JSON with a HTTP response
    """
    piece_type_pk = None
    if request.method == 'GET' and 'id' in request.GET:
        piece_type_pk = request.GET['id']
    if piece_type_pk is not None:
        query_repsonse = models.Pieces.objects.filter(type_id=piece_type_pk)
        return HttpResponse(serializers.serialize('json', query_repsonse))
    else:
        error_str = '<h1> BAD REQUEST </h1> <p>It is required to receive an id as argument as follows ' \
                    '\"127.0.0.1:8000/pieces_from_type?id=[a-zA-Z]+\"</p>'
        return HttpResponseBadRequest(error_str)


def piece_data(request):
    """
        The mighty power of the request that requests all the piece types
    :param request: literally the request
    :return: all objects serialized as a JSON with a HTTP response
    """
    piece_id = None
    if request.method == 'GET' and 'id' in request.GET:
        piece_id = request.GET['id']
    if piece_id is not None:
        query_repsonse = models.Pieces.objects.filter(id=piece_id)
        return HttpResponse(serializers.serialize('json', query_repsonse))
    else:
        error_str = '<h1> BAD REQUEST </h1> <p>It is required to receive an id as argument as follows ' \
                    '\"127.0.0.1:8000/pieces_from_type?id=[a-zA-Z]+\"</p>'
        return HttpResponseBadRequest(error_str)
