# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from django.core.mail import send_mail
# from django.conf import settings
# from .models import Order
# from .serializers import OrderSerializer
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.filters import SearchFilter, OrderingFilter
# from django_filters.rest_framework import DjangoFilterBackend
# from ..product.models import Product

# # class OrderCreateView(APIView):
# #     def post(self, request):
# #         serializer = OrderSerializer(data=request.data)
# #         if serializer.is_valid():
# #             order = serializer.save()
# #             send_mail(
# #                 'Подтверждение заказа',
# #                 f'Ваш заказ был успешно оформлен. Номер заказа: {order.id}. Сумма заказа: {order.total_price}.',
# #                 settings.EMAIL_HOST_USER,
# #                 [request.user.email],
# #                 fail_silently=False,
# #             )
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# #     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
# #     filterset_fields = ['user', 'items']
# #     search_fields = ['items']
# #     ordering_fields = ['id']


# class OrderCreateView(APIView):
#     def post(self, request):
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             # Calculate total price
#             items = serializer.validated_data['items']
#             total_price = 0
#             for item in items:
#                 try:
#                     product = Product.objects.get(pk=item['product'].id)
#                     total_price += product.price * item['quantity']
#                 except Product.DoesNotExist:
#                     return Response({'error': 'Такого товара нет.'}, status=status.HTTP_400_BAD_REQUEST)
#             # Save order
#             order = serializer.save(total_price=total_price, user=request.user)
#             # Send confirmation email
#             subject = 'Подтверждение заказа'
#             message = f'Ваш заказ был успешно оформлен. Номер заказа: {order.id}. Сумма заказа: {order.total_price}.'
#             send_mail(
#                 subject,
#                 message,
#                 settings.EMAIL_HOST_USER,
#                 [request.user.email],
#                 fail_silently=False,
#             )
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
#     filterset_fields = ['user', 'items__product']
#     search_fields = ['items__product__name']
#     ordering_fields = ['id']


from django.core.mail import send_mail
from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.views import APIView
from .serializers import OrderSerializer
from .models import Order

class OrderCreateView(APIView):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user', 'items']
    search_fields = ['items']
    ordering_fields = ['id']

    def post(self, request):
        serializer = OrderSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            order = serializer.save()
            subject = 'Подтверждение заказа'
            message = f'Ваш заказ был успешно оформлен. Номер заказа: {order.id}. Сумма заказа: {order.total_price}.'
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [request.user.email],
                fail_silently=False,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)