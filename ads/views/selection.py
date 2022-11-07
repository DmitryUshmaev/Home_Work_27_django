from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ads.models import Selection
from ads.serializers import SelectionListSerializer, SelectionDetailSerializer, SelectionSerializer
from permissions import IsOwnerSelection


class SelectionViewSet(ModelViewSet):
    queryset = Selection.objects.all()

    default_serialize = SelectionSerializer
    serializer_classes = {
        'retrieve': SelectionListSerializer,
        'list': SelectionDetailSerializer
    }

    default_permissions = [AllowAny()]
    permissions = {
        'update': [IsAuthenticated(), IsOwnerSelection()],

    }

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permissions)