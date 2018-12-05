from django.core import serializers
from django.http import HttpResponse, HttpResponseBadRequest

from DjanGIUnchained import models
# Create your views here.
from DjanGIUnchained.decorators import cross_origin, returns_json


@cross_origin
@returns_json
def all_piece_types(request):
    """
        The mighty power of the request that requests all the piece types
    :param request: literally the request
    :return: all objects serialized as a JSON with a HTTP response
    """
    query_repsonse = models.PieceType.objects.all()
    dicted_response = [i.to_dict() for i in query_repsonse]
    return dicted_response


@cross_origin
@returns_json
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
        dicted_response = [i.to_dict() for i in query_repsonse]
        return dicted_response
    else:
        error_str = {'error': 'BAD REQUEST: It is required to receive an id as argument as follows '
                              '127.0.0.1:8000/pieces_from_type?id=[a-zA-Z]'}
        return HttpResponseBadRequest(error_str)


@cross_origin
@returns_json
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
        dicted_response = [i.to_dict() for i in query_repsonse]
        return dicted_response
    else:
        error_str = {'error': 'BAD REQUEST: It is required to receive an id as argument as follows '
                              '127.0.0.1:8000/pieces_from_type?id=[a-zA-Z]'}
        return HttpResponseBadRequest(error_str)
