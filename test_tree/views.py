from rest_framework import generics,status
from test_tree.models import Genre
from test_tree.serializers import GenreSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import os


class GenreView(generics.ListAPIView):

    serializer_class = GenreSerializer

    def get_queryset(self):
        rname = self.kwargs['rname']
        query_set = Genre.objects.all().filter(name=rname)
        return query_set


def serialize_node(node):
    obj = {'name':node.name,'children':[]}
    for child in node.get_children():
        obj['children'].append(serialize_node(child))
    return obj


@api_view(['GET'])
def get_tree(request):
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'root.json')
    with open(file_path,"r") as f:
        root_json = json.load(f)
        root_pk = root_json['pk']
        json_object = serialize_node(Genre.objects.all().filter(pk=root_pk)[0])
        return Response(data=json_object)


@api_view(['POST'])
def create_node(request):
    # for parent field: the pk of parent is ok
    input_data = request.data
    serializer = GenreSerializer(data=input_data)
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)
    else:
        return Response(data=serializer.errors,status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update_node(request):
    # for parent field: the pk of parent is ok
    input_data = request.data
    primary_key = input_data['pk']
    node = Genre.objects.all().filter(pk=primary_key)[0]
    serializer = GenreSerializer(node,data=input_data)
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)
    else:
        return Response(data=serializer.errors,status=status.HTTP_404_NOT_FOUND)