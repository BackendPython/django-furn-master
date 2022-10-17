from .serializer import *
from furn.models import *
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

# main API
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def carousel_api(request):
    carousel = Carousel.objects.all()
    serializer = CarouselApi(carousel, many=True)
    return Response(serializer.data)


