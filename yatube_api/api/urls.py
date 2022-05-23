from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowsViewSet


router = routers.DefaultRouter()
router.register(prefix='posts', viewset=PostViewSet, basename='post')
router.register(prefix='groups', viewset=GroupViewSet, basename='group')
router.register(prefix=r'posts/(?P<post_id>[0-9]+)/comments',
                viewset=CommentViewSet,
                basename='comment'
                )
router.register(prefix='follow', viewset=FollowsViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),
]
