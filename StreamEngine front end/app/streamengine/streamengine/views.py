from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
import json
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from .forms import CustomUserCreationForm
from .models import Channel, CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class ChannelDetailView(DetailView):
    # slug_field = 'slug'
    # slug_url_kwarg = 'slug'

    model = Channel
    template_name = 'channel_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


def index(request):
    return render(request, 'index.html')


def channel(request):
    return render(request, 'channel.html')


def profile(request):
    user = CustomUser.objects.get(username='tom')
    channel = Channel.objects.get(creator=user)

    context = {
        'channelStreamkey': channel.streamkey,
        'channelTitle': channel.title,
        'channelSlug': channel.slug,
    }

    return render(request, 'profile.html', context)


def streamAuth(request, key):
    c = False
    try:
        Channel.objects.get(streamkey=key)
        c = Channel.objects.get(streamkey=key)
    except:
        c = False
    if(c != False):
        data = [{
        'channel_title': c.title,
        'cid': c.cid,
        'creator': c.creator.username,
        'authorized': 'true',
        'live': c.is_live
    }]

    else:
        data = [{
        'authorized': 'false'
    }]

    return JsonResponse(data, safe=False)


def go_live(request):
    if request.method == 'POST':
    
        payload = json.loads(
                  request.body.decode('utf-8'))
        c = False
        key = data = payload['key']
        try:
                Channel.objects.get(streamkey=key)
                c = Channel.objects.get(streamkey=key)
        except:
                c = False

        if(c != False):
                c.is_live = True
                c.save()
                data = [{
                'channel': c.title,
                'live': c.is_live
            }]

        else:
                data = [{
                'authorized': 'false'
            }]
     

        
        return  JsonResponse(data, safe=False)

def stop_live(request):
    if request.method == 'POST':
    
        payload = json.loads(
                  request.body.decode('utf-8'))
        c = False
        key = data = payload['key']
        try:
                Channel.objects.get(streamkey=key)
                c = Channel.objects.get(streamkey=key)
        except:
                c = False

        if(c != False):
                c.is_live = False
                c.save()
                data = [{
                'channel': c.title,
                'live': c.is_live
            }]

        else:
                data = [{
                'authorized': 'false'
            }]
     

        
        return  JsonResponse(data, safe=False)
