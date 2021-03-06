from django.shortcuts import render
from .models import  Flight,Reservation,Passenger
from .serializers import FlightSerializer,ReservationSerializer,PassengerSerializer
from rest_framework import viewsets  # for minimizing code it will perform all key and non-key operations
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import IsAuthenticated # for token authentication 



# Create your views here.


#custome view for findingFlight
@api_view(['POST'])
def find_flight(request):
    flights=Flight.objects.filter(departureCity=request.data['departureCity'],arrivalCity=request.data['arrivalCity'],dateOfDeparture=request.data['dateOfDeparture'])
    serializer=FlightSerializer(flights ,many=True)
    return Response(serializer.data)

# for reservation
@api_view(['POST'])
def save_reservation(request):
    flight=Flight.objects.get(id=request.data['flightId'])


    passenger=Passenger()
    passenger.firstName=request.data['firstName'] 
    passenger.lastName=request.data['lastName'] 
    passenger.middleName=request.data['middleName']
    passenger.email=request.data['email']
    passenger.phone=request.data['phone']
    passenger.save()

    reservation=Reservation()
    reservation.flight=flight
    reservation.passenger=passenger

    reservation.save()
    return Response(status=status.HTTP_201_CREATED)

class FlightViewSet(viewsets.ModelViewSet): # it will handel all pkey and nonPkey operations
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes=(IsAuthenticated,) # for token security
    

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer