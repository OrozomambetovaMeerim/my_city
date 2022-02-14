from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ProposalListSerializer, ProposalCreateSerializer
from .serializers import ProposalListSerializer
from .models import Proposal

class ProposalListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # return Response({'test'})
        proposals = Proposal.objects.all()
        proposals_json = ProposalListSerializer(proposals, many=True)
        return Response(data=proposals_json.data)


class ProposalCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.POST
        Serializer = ProposalCreateSerializer(data=data)


