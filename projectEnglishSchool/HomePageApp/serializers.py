from rest_framework.serializers import ModelSerializer

from .models import DatePerson


class OrderSerializer(ModelSerializer):
    class Meta:
        model = DatePerson
        fields = ['name','second_name','age']