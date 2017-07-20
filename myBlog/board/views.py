from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import Message
import time
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def index(request):
    if 'submit' in request.POST:
        # if 'submit' in request.POST:
        user_message = request.POST['user_message']
        user_name = request.POST['user_name']
        if user_message.strip() != '':
            if user_name == '':
                user_name = 'NO_ONE'
            now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            Message.objects.create(message_text=user_message, message_name=user_name, support=0, pub_date=now)
        return HttpResponseRedirect('/board/')

    elif 'msg_id' in request.GET:
        msg_id = request.GET.get('msg_id')
        count = Message.objects.get(id=msg_id).support
        msg = Message.objects.get(id=msg_id)
        msg.support = count + 1
        msg.save()
        return HttpResponseRedirect('/board/')
    else:
        message_list = Message.objects.order_by('-pub_date')
        template = loader.get_template('board/index.html')
        context = {
            'message_list': message_list,
        }
        return HttpResponse(template.render(context, request))

