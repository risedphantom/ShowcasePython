from django.http import HttpResponse
from website.apps import WebsiteConfig as settings
import random


# Greeting
def greeting(request):
    pos = random.randint(0, 3)

    response = {
        'friend': settings.friend_ans[pos],
        'enemy': settings.enemy_ans[pos],
        'anonymous': settings.anon_ans[pos],
        'soon': settings.soon_ans[pos],
    }.get(request.GET['type'], 'Всего хорошего!')

    return HttpResponse(response)
