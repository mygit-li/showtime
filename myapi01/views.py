from myapi01.models import Students
from myapi01.serializers import StudentSerializer
from rest_framework import generics
from snippets.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'students': reverse('students-list', request=request, format=format)
    })


class StudentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Students.objects.using('ora1').all()
    serializer_class = StudentSerializer
