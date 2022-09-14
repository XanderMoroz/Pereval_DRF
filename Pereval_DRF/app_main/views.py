from rest_framework import viewsets
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import generics
from .models import *
from .serializers import PerevalAddSerializer, PerevalDetailSerializer


class PerevalAPIView(generics.CreateAPIView):
    """Класс работы с БД для первого спринта"""
    queryset = PerevalAdd.objects.all()
    serializer_class = PerevalAddSerializer

    def post(self, request):
        """
        Переопределение метода POST
        :param request: Json для полей модели перевала (PerevalAdd)
        :return: JsonResponse пример: { "status": 200, "message": null, "id": 42 }
        """
        pereval = PerevalAddSerializer(data=request.data)
        try:
            if pereval.is_valid(raise_exception=True):
                pereval.save()
                data = {
                    'status': '200',
                    'message': 'null',
                    'id': f'{pereval.instance.id}'
                }
                return JsonResponse(data, status=200, safe=False)
        except Exception as exc:
            data = {
                'status': '400',
                'message': f'Bad Request: {exc}',
                'id': 'null'
            }
        return JsonResponse(data, status=400, safe=False)

class PerevalDetail(generics.UpdateAPIView):
    """Класс работы с БД для второго спринта"""
    serializer_class = PerevalAddSerializer

    def get_object(self, pk):
        return PerevalAdd.objects.get(pk=pk)

    def get(self, *args, **kwargs):
        """
        Переопределение метода GET для вывода записи по id
        :param request: Json для полей модели перевала (PerevalAdd)
        :return: JsonResponse пример: {"state": "0", "message": "PerevalAdd matching query does not exist."}
        """
        pk = kwargs.get('pk', None)
        try:
            data = PerevalDetailSerializer(PerevalAdd.objects.get(pk=pk)).data
            responseData = {'state': '1', 'message': f'{data}'}
            return JsonResponse(responseData)
        except Exception as exc:
            responseData = {'state': '0', 'message': f'{exc}'}
            return JsonResponse(responseData)




