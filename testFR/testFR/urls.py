from django.conf.urls import url, include
from rest_framework import routers
from app import views

router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'answer-options', views.AnswerOptionViewSet)
router.register(r'answers', views.AnswerViewSet)
router.register(r'polls', views.PollViewSet, basename='poll')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]