from django.contrib.auth.models import User, Group 
from .models import Answer, AnswerOption, Poll, Question
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
                model = Group
                fields = ('url', 'name')

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Question
		fields = ('url', 'poll', 'text', 'question_type')

class PollSerializer(serializers.HyperlinkedModelSerializer):
	questions = QuestionSerializer(many=True, read_only=True)
	class Meta:
		model = Poll
		fields = ('url', 'name', 'description', 'start_date', 'end_date', 'questions')
		read_only_fields = ('start_date','questions')

class AnswerOptionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = AnswerOption
		fields = ('url', 'variant', 'question')

class AnswerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Answer
		fields = ('url', 'text', 'variants', 'user', 'question')
		read_only_fields = ('user',)