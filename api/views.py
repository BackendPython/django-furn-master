from .serializer import *
from furn.models import *
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

# main API
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


