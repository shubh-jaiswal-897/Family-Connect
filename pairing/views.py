from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from pairing.models import PairingToken
from pairing.serializers import PairingTokenSerializer
from django.utils import timezone
import qrcode
import io
import base64

class CreatePairingQRView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.role != 'PARENT':
            return Response({'error': 'Only parents can generate pairing codes.'}, status=status.HTTP_403_FORBIDDEN)
            
        token = PairingToken.objects.create(parent=request.user)
        
        # Generate QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(str(token.token))
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        
        return Response({
            'token': token.token,
            'expires_at': token.expires_at,
            'qr_code_base64': img_str
        })
