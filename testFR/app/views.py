from django.contrib.auth.models import User, Group, AnonymousUser
from datetime import datetime

from django.http import Http404, HttpRequest
from rest_framework.request import Request
from rest_framework.status import HTTP_403_FORBIDDEN
from rest_framework.views import APIView

from .models import Poll, AnswerOption, Question, Answer
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from app.serializers import (UserSerializer, PollSerializer, 
    AnswerOptionSerializer, AnswerSerializer, QuestionSerializer, GroupSerializer)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from app.permissions import *


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [UserPermission]
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PollList(viewsets.ViewSet):
    def get(self, request):
        user_is_admin = False
        queryset = Poll.objects.all()
        if isinstance(request.user, AnonymousUser):
            user_is_admin = False
        else:
            user_is_admin = 'admin' in map(str, request.user.groups.all())
        if not user_is_admin:
            queryset = queryset.filter(end_date__lte=datetime.now())
        serializer = PollSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PollSerializer(data=request.data)
        if not 'admin' in map(str, request.user.groups.all()):
            return Response(status=HTTP_403_FORBIDDEN)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PollDetail(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [IsAdminOrReadOnly]


class AnswerOptionViewSet(viewsets.ModelViewSet):
    queryset = AnswerOption.objects.all()
    serializer_class = AnswerOptionSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer