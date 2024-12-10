from django.http import HttpResponse
import logging

log = logging.getLogger('ping')

def ping(request):
    log.info(f'ping is calling')
    return HttpResponse("pong")
