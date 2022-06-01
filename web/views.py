import json
from multiprocessing import context
from urllib import response
from django.shortcuts import render, redirect
import uuid

import requests

# Create your views here.


def index(request):
    return render(request, 'index.html')

def chat(request):
    rand_id = uuid.uuid4()
    context = {
        'rand_id': rand_id
    }
    return render(request, 'chat.html', context)


def reply(request):
    if request.method == 'POST':
        data = request.POST
        message = data['message']
        if message == '':
            return redirect('web:index')
        
        Uuid = "ANDYTHEROBOT"
        api_url = "http://api.brainshop.ai/get?bid=166926&key=fRQsjcbtcV9VP2nK&uid=[" + Uuid + "]&msg=[" + message + "]"
        response = requests.get(api_url)
        json_response = json.loads(response.text)
        reply = json_response['cnt']

        context = {
            'reply': reply,
            'message': message,
            'replied': 'replied'
        }
        return render(request, 'chat.html', context)
    return render(request, 'chat.html')