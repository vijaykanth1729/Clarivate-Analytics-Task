from rest_framework import viewsets
from rest_framework import filters
from .models import UserInfo
from .serializers import  UserInfoSerializer

class UserInfoView(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['id','first_name', 'last_name', 'email']
    ordering_fields = ('id','first_name', 'last_name', 'email')
