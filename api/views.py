from .serializer import *
from furn.models import *
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


# get carusel
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def carousel(request):
    carousel = Carousel.objects.all()
    serializer = CarouselApi(carousel, many=True)
    return Response(serializer.data)

# add carousel
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def carousel_add(request):
    serializer = CarouselApi(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# search carousel with id
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def carousel_single(request, pk):
    carousel = Carousel.objects.get(id=pk)
    serializer = CarouselApi(carousel, many=False)
    return Response(serializer.data)

# edit carousel
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def carousel_single_edit(request, pk):
    carousel = Carousel.objects.get(id=pk)
    serializer = CarouselApi(instance=carousel, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# delete carousel
@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))
def carousel_single_delete(request, pk):
    krasovka = Carousel.objects.get(id=pk)
    krasovka.delete()
    return Response("Successfull deleted")