from django.http import HttpResponse, JsonResponse
from rest_framework import status
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser

from .models import *

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_data(request):
    try:
        data=icc.objects.all().values()
        print(data)
        return JsonResponse({"data":list(data),},safe=False)
    except Exception as e:
        return JsonResponse({"message":"oops!,Something went Wrong"})
    
    
    
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_detail_view(request):
    user = request.user
    groups = user.groups.values_list('name', flat=True)

    user_data = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'is_superadmin': user.is_superuser,
        'groups': list(groups),
    }
    return JsonResponse({"data":user_data})
    
    
