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
from rest_framework.exceptions import ValidationError
from app.permissions import *



class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



class PollViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        user_is_admin = False
        queryset = Poll.objects.all()
        if isinstance(self.request.user, AnonymousUser):
            user_is_admin = False
        else:
            user_is_admin = 'admin' in map(str, self.request.user.groups.all())
        if not user_is_admin:
            queryset = Poll.objects.filter(end_date__gte=datetime.now())
        return queryset

    serializer_class = PollSerializer
    permission_classes = [IsAdminOrReadOnly]


class AnswerOptionViewSet(viewsets.ModelViewSet):
    queryset = AnswerOption.objects.all()
    serializer_class = AnswerOptionSerializer
    permission_classes = [IsAdminOrReadOnly]
    

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminOrReadOnly]

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def create(self, request):
        serializer = AnswerSerializer(data=request.data, context={'request': request})
        serializer.is_valid()
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        raise ValidationError