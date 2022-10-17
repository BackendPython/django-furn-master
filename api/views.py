from .serializer import *
from furn.models import *
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


# ---------------------------------------------------------------- Carousel REST API ----------------------------------------------------------------

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

# ---------------------------------------------------------------- Carousel REST API ----------------------------------------------------------------

# ---------------------------------------------------------------- Arrival REST API ----------------------------------------------------------------

# get arrival
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def arrival(request):
    arrival = Arrival.objects.all()
    serializer = ArrivalApi(arrival, many=True)
    return Response(serializer.data)

# add arrival
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def arrival_add(request):
    serializer = ArrivalApi(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# search arrival with id
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def arrival_single(request, pk):
    arrival = Arrival.objects.get(id=pk)
    serializer = ArrivalApi(arrival, many=False)
    return Response(serializer.data)

# edit arrival
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def arrival_single_edit(request, pk):
    arrival = Carousel.objects.get(id=pk)
    serializer = ArrivalApi(instance=arrival, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# delete arrival
@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))
def arrival_single_delete(request, pk):
    arrival = Arrival.objects.get(id=pk)
    arrival.delete()
    return Response("Successfull deleted")

# ---------------------------------------------------------------- Arrival REST API ----------------------------------------------------------------

