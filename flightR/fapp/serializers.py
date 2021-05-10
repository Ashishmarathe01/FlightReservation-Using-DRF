from rest_framework import serializers
from .models import Flight,Reservation,Passenger
import re

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flight
        fields='__all__'

    def validate_flightNumber(self,flightNumber)   :
        if (re.match("^[a-zA-Z0-9]*$",flightNumber)==None):
            raise serializers.ValidationError("chek your data")
        return flightNumber    


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


