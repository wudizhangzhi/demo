# encoding: utf-8

from rest_framework import serializers

from movies.models import Movies, SubMovies


class MoviesShowSerializers(serializers.ModelSerializer):

    class Meta:
        model = Movies
        fields = '__all__'


class TvShowSerializers(serializers.ModelSerializer):
    class Meta:
        model = SubMovies
        fields = '__all__'
