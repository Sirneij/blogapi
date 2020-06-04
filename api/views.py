from rest_framework import viewsets #generics, permissions
from django.contrib.auth import get_user_model
from posts.models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly

#class PostList(generics.ListCreateAPIView):
   # permission_classes = (permissions.IsAuthenticated,)
    #queryset = Post.objects.all()
    #serializer_class = PostSerializer

#class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthorOrReadOnly,)
    #queryset = Post.objects.all()
    #serializer_class = PostSerializer

#class UserList(generics.ListCreateAPIView):
    #queryset = get_user_model().objects.all()
    #serializer_class = UserSerializer

#class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    #queryset = get_user_model().objects.all()
    #serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
