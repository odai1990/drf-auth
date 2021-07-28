from django.db.models import fields
from rest_framework import serializers

from .models import Moives

class MoiveSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','title','film_star','director','description','pg','feedback','added_by')
        model=Moives