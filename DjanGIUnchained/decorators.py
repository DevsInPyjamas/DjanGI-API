import json

from django.http import HttpResponse
from DjanGIUnchained import models


def cross_origin(func):
    def cross_origin_decorator(request):
        response = func(request)
        if isinstance(response, HttpResponse):
            response['Access-Control-Allow-Origin'] = '*'
            if request.method == 'OPTIONS':
                response['Access-Control-Allow-Headers'] = 'x-session-user'
                response['Access-Control-Allow-Methods'] = 'GET, POST, DELETE'
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
            logged_user = models.User.objects.filter(name=header_request)
            if len(logged_user) < 1:
                response = {'error': 'No existent user provided as session user'}
            else:
                response = func(request, logged_user[0])
        else:
            response = {'error': 'No user provided as session user'}
        return response

    return with_session_decorator
