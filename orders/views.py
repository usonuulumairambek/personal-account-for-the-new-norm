from django.shortcuts import render
from django.core.mail import send_mail

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import OrderModels, ClientModels, NanoModels, FeedBackModels
from .serializer import OrderModelsSerializer, ClientModelsSerializer, NanoModelsSerializer, FeedBackSerializer
from unnamed_project.settings import EMAIL_HOST_USER


class OrderSafeAndSendEmailViewSet(viewsets.ModelViewSet):
    serializer_class = OrderModelsSerializer
    queryset = OrderModels
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        send_mail('Новый заказ', f'Пользователь {data["first_name"]} заказал {data["product"]}.\n'
                  f'Его данные: номер телефона-{data["phone"]}, адрес-{data["address"]}',
                  EMAIL_HOST_USER, ['nnormalkg@gmail.com'])
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class OrderSafeAndSendClientViewSet(viewsets.ModelViewSet):

    serializer_class = ClientModelsSerializer
    queryset = ClientModels
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        data = request.data['phone_number']
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        send_mail('отправить', f'номер телефона {data}',
                  EMAIL_HOST_USER, ['jumagylov655@gmail.com'])
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class OrderSafeAndSendNanoViewSet(viewsets.ModelViewSet):

    serializer_class = NanoModelsSerializer
    queryset = NanoModels
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        send_mail('nano.kg:',
                  f'имя - {data["name"]},.\n'
                  f'e-mail - {data["email"]}',
                  EMAIL_HOST_USER, ['jumagylov655@gmail.com'])
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class OrderSafeAndSendFeedBackViewSet(viewsets.ModelViewSet):
    queryset = FeedBackModels.objects.all()
    serializer_class = FeedBackSerializer
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        send_mail(data['feed_user'], data['feed_text'], data['feed_mail'], ['mnkvk@mail.ru'])
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

