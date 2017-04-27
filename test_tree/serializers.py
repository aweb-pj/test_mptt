from rest_framework import serializers
from test_tree.models import Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name','parent','pk')


