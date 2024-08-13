from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Currency
from .serializers import CurrencySerializer
from .serializers import RateRequestSerializer

class CurrencyList(generics.ListCreateAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

class CurrencyRateView(APIView):
    def get(self, request):
        # Pass query parameters to the serializer
        serializer = RateRequestSerializer(data=request.query_params)
        
        if serializer.is_valid():
            from_currency = serializer.validated_data['from_currency']
            to_currency = serializer.validated_data['to_currency']

            # Get the rates from the database
            from_rate = get_object_or_404(Currency, code=from_currency).rate
            to_rate = get_object_or_404(Currency, code=to_currency).rate

            # Calculate the exchange rate
            exchange_rate = to_rate / from_rate

            return Response({
                'from': from_currency,
                'to': to_currency,
                'rate': exchange_rate
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        