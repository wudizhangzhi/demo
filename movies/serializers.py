# encoding: utf-8

from rest_framework import serializers

from movies.models import Movies


class MoviesShowSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'
