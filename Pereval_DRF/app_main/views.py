from rest_framework import viewsets
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import generics, viewsets, mixins
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
                data = {'status': '200', 'message': 'null', 'id': f'{pereval.instance.id}'}
                return JsonResponse(data, status=200, safe=False)

        except Exception as exc:
            responseData = {'status': '400', 'message': f'Bad Request: {exc}', 'id': 'null'}
            return JsonResponse(responseData, status=400, safe=False)


class PerevalDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):

    queryset = PerevalAdd.objects.all()
    serializer_class = PerevalDetailSerializer

    def update(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)

        try:
            instance = PerevalAdd.objects.get(pk=pk)
        except:
            return Response({"error": "Такого перевала не существует"}, status=400)

        if instance.status != "N":
            return Response({"message": "Перевал на модерации, вы не можете его изменить",
                             "state": 0}, status=400)
        else:
            # для метода upd обязательно нужно передать instance, иначе сериализатор будет воспринимать это как create
            serializer = PerevalDetailSerializer(data=request.data, instance=instance)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"state": 1}, status=200)
