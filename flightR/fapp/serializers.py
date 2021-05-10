from rest_framework import serializers
from .models import Flight,Reservation,Passenger
import re


# 3r type of validation
def isFlightValiodate(data): # it will also give alo field data  but you have to mentionn it in meta class
    print(data)
    

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flight
        fields='__all__'
#       validators=[FlightSerializer]              by mentioning this you can acees out side fn for validation
    def validate_flightNumber(self,flightNumber)   : # validate_filed name comparasry write it
        if (re.match("^[a-zA-Z0-9]*$",flightNumber)==None): # it ill matcg a-z&1-9 with flighnumber field
            raise serializers.ValidationError("chek your data")
        return flightNumber    
"""
# 2 nd type validation
    def validate(self,data): # it will give you all filed data for validating
        print('validate')
        print(data['flightNumber'])
        return data 
"""

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


