import json

from django.http import HttpResponse
from DjanGIUnchained import models


def cross_origin(func):
    def cross_origin_decorator(request):
        response = func(request)
        if isinstance(response, HttpResponse):
            response['Access-Control-Allow-Origin'] = '*'
        return response

    return cross_origin_decorator


def returns_json(func):
    def returns_json_decorator(request):
        response = func(request)
        if isinstance(response, HttpResponse):
            response['Content-Type'] = 'application/json; charset=utf-8'
        else:
            response = HttpResponse(json.dumps(response))
            response['Content-Type'] = 'application/json; charset=utf-8'
        return response

    return returns_json_decorator


def with_session(func):
    def with_session_decorator(request):
        if 'HTTP_X_SESSION_USER' in request.META:
            header_request = request.META['HTTP_X_SESSION_USER']
            logged_user = models.User.objects.get(name=header_request)
            response = func(request, logged_user)
        else:
            response = {'error': 'No user provided as session user'}
        return response

    return with_session_decorator
