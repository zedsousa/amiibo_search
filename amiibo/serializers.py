from rest_framework import serializers
from .models import Amiibo

class AmiiboSerializer(serializers.Serializer):
    amiiboSeries = serializers.CharField()
    character = serializers.CharField()
    gameSeries = serializers.CharField()
    head = serializers.CharField()
    image = serializers.CharField()
    name = serializers.CharField()
    tail = serializers.CharField()
    type = serializers.CharField(max_length=50)
    '''
    def create(self, validated_data):
        return Amiibo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.amiiboSeries = validated_data.get('amiiboSeries', instance.amiiboSeries)
        instance.character = validated_data.get('character', instance.character)
        instance.gameSeries = validated_data.get('gameSeries', instance.gameSeries)
        instance.head = validated_data.get('head', instance.head)
        instance.image = validated_data.get('image', instance.image)
        instance.name = validated_data.get('name', instance.name)
        instance.tail = validated_data.get('tail', instance.tail)
        instance.type = validated_data.get('type', instance.type)
        instance.save()
        return instance    
    '''
    class Meta:
        model = Amiibo
        fields = "__all__"
 
    