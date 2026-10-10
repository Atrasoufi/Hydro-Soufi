from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from apps.leads.api.serializers.base_serilizers import ContactRequestSerilazer

class ContactRequestAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ContactRequestSerilazer
    