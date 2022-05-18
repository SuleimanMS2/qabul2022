import json
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from telegram import Update
from django.views.decorators.csrf import csrf_exempt
from .qabul_bot.bot import bot, dispatcher

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import *
from django.http.response import JsonResponse


@method_decorator(csrf_exempt, 'dispatch')
class Master(View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        try:
            body = request.body
            data = json.loads(body)
            update: Update = Update.de_json(data, bot)
            dispatcher.process_update(update)
        except Exception as e:
            pass
        return HttpResponse('ok', status=200)


class ViloyatList(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request, format=None):
        viloyat = request.data['viloyat']
        tuman = {}
        if viloyat:
            tumanlar = Viloyat.objects.get(id=viloyat).viloyat_id.all()
            tuman = {p.name: p.id for p in tumanlar}
        return JsonResponse(data=tuman, safe=False)
