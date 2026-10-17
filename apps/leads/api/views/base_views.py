from django.core.mail import EmailMessage
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from apps.leads.api.serializers.base_serilizers import ContactRequestSerilazer
from drf_spectacular.utils import extend_schema


class ContactRequestAPIView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(request=ContactRequestSerilazer)
    def post(self, request):
        serialiser = ContactRequestSerilazer(data=request.data)
        serialiser.is_valid(raise_exception=True)

        data = serialiser.validated_data

        message = f"""
        New contact request received.

        Name: {data['name']}
        Phone: {data['phone']}
        Email: {data['email']}

        Message:
        {data['message']}
        """

        email = EmailMessage(
            subject=data["subject"],
            body=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.CONTACT_EMAIL],
            reply_to=[data["email"]],
        )

        sending_code = email.send(fail_silently=False)

        if sending_code == 1:
            return Response(
                {"detail": "Your message was sent successfully."},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"detail": "sending code failed, try againg"},
                status=status.HTTP_400_BAD_REQUEST,
            )
