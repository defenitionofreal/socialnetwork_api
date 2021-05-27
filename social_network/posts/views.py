from rest_framework import viewsets
from .models import Post, Like
from .serializers import PostSerializer, PostLikeSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView


class PostViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        try:
            post = Like.objects.get(post_id=pk, liker_id=request.user.id)
            return Response({'status': 'You have already liked'})
        except Like.DoesNotExist:
            Like.objects.create(post_id=pk, liker_id=request.user.id)
            return Response({'status': 'You have liked the post'})

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def unlike(self, request, pk=None):
        try:
            post = Like.objects.get(post_id=pk, liker_id=request.user.id)
            post.delete()
            return Response({'status': "You've unliked the post"})
        except Like.DoesNotExist:
            return Response({'status': "You've already unliked the post"})




class PostLikesAnalyticsApiView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        likes = Like.objects.filter(liked_at__range=[kwargs['date_from'], kwargs['date_to']])
        if len(likes) > 0:
            serializer = PostLikeSerializer(likes, many=True)
            return Response({'Total Likes': len(likes),
                             'Full analytics': serializer.data})
        else:
            return Response({'message': "No likes"})






