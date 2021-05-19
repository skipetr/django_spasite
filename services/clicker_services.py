from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user_profile.models import MainCycle, Boost


def main_page(request):
    user = User.objects.filter(id=request.user.id)
    if len(user) != 0:
        mainCycle = MainCycle.objects.get(user=request.user)
        return (False, 'index.html', {'user':user[0], 'mainCycle':mainCycle})
    else:
        return (True, 'login', {})


def call_click(request):
    mainCycle = MainCycle.objects.get(user=request.user)
    mainCycle.Click()
    mainCycle.save()
    return (mainCycle.coinsCount)

@api_view(['POST'])
def buy_boost(request):
    boost_level = request.data['boost_level']
    cycle = MainCycle.objects.get(user=request.user)
    boost = Boost.objects.get_or_create(mainCycle=cycle, level=boost_level)[0]
    click_power, coins_count, level, price = boost.upgrade()
    boost.save()
    return Response({"clickPower": click_power, "coinsCount":coins_count, 'level':level, 'price':price})
