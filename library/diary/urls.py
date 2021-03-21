from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import *

app_name = 'diary'

urlpatterns = [
    path('', DiaryHome.as_view(), name='diary/index'),
    path('log/<blog_id>', csrf_exempt(DiaryLogEntryView.as_view()), name='diary/log'),
    path('about/', About.as_view(), name='home/index'),
    path('contact/', Contact.as_view(), name='contact/index'),
    path('interests/', Minigame.as_view(), name='interests/index'),
    # path('address/get', csrf_exempt(GetAddress.as_view()), name='index'),
]