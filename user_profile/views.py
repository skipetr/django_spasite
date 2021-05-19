from django.contrib.auth.models import User
from django.http import HttpResponse
from .serializers import UserSerializer, UserSerializerDetail, CycleSerializer, CycleSerializerDetail
from .models import MainCycle
from rest_framework import generics
import services


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerDetail


class CycleList(generics.ListAPIView):
    queryset = MainCycle.objects.all()
    serializer_class = CycleSerializer

class CycleDetail(generics.RetrieveAPIView):
    queryset = MainCycle.objects.all()
    serializer_class = CycleSerializerDetail


def call_click(request):
    coinsCount = services.clicker_services.call_click(request)
    return HttpResponse(coinsCount)

def buy_boost(request):
    clickPower = services.clicker_services.buy_boost(request)
    return clickPower
