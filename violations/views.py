from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Violation
from .serializers import ViolationSerializer

@api_view(['POST'])
def ingest_violation(request):
    serializer = ViolationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"violation_id": serializer.instance.id}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_violations(request, license_plate):
    violations = Violation.objects.filter(license_plate=license_plate).order_by('-violation_datetime')
    serializer = ViolationSerializer(violations, many=True)
    return Response(serializer.data)

@api_view(['PATCH'])
def update_violation_status(request, pk):
    violation = get_object_or_404(Violation, pk=pk)
    new_status = request.data.get("status")
    if new_status not in ["pending", "approved", "rejected"]:
        return Response({"error": "Invalid status"}, status=400)
    violation.status = new_status
    violation.save()
    return Response({"status": "updated"})
