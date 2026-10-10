from rest_framework import serializers
from ...models import ContactRequest

class ContactRequestSerilazer(serializers.ModelSerializer):
    class Meta:
        model = ContactRequest
        fields = [
            "name",
            "phone",
            "email",
            "subject",
            "message",
        ]
