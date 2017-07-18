from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import Message


def index(request):
    message_list = Message.objects.order_by('-pub_date')
    template = loader.get_template('board/index.html')
    context = {
        'message_list': message_list,
    }
    return HttpResponse(template.render(context, request))