from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response

from ..models import Remark
from .serializers import RemarkSerializer

from pitches.models import Pitch

class RemarkViewSet(viewsets.ModelViewSet):
    queryset = Remark.objects.all()
    serializer_class = RemarkSerializer
    permission_classes = (permissions.IsAuthenticated, )

class AccountRemarkAPIView(generics.ListCreateAPIView):
    serializer_class = RemarkSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        meeting_param = self.request.query_params.get('meeting', None)
        if (meeting_param):
            try:
                queryset = Remark.objects.filter(account=self.request.user.id)
                if not queryset.exists():
                    raise Remark.DoesNotExist
                return queryset
            except Remark.DoesNotExist:
                return Response({'error', 'Remark does not exists.'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error', 'Add parameter meeting.'}, status=status.HTTP_400_BAD_REQUEST)

class PitchRemarkAPIView(generics.ListAPIView):
    serializer_class = RemarkSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        meeting_param = self.request.query_params.get('meeting', None)
        if (meeting_param):
            try:
                pitch = Pitch.objects.get(account=self.request.user.id)
                if not pitch.exists():
                    raise Pitch.DoesNotExist
                queryset = Remark.objects.filter(pitch=pitch.id, account=self.request.user.id, meeting=meeting_param)
                if not queryset.exists():
                    raise Remark.DoesNotExist
                return queryset
            except Remark.DoesNotExist:
                return Response({'error', 'Remark does not exists.'}, status=status.HTTP_404_NOT_FOUND)
            except Pitch.DoesNotExist:
                return Response({'error', 'Pitch does not exists.'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error', 'Add parameter meeting.'}, status=status.HTTP_400_BAD_REQUEST)