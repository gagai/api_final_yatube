from rest_framework import serializers

from posts.models import Comment, Group, Post, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(many=False,
                                          slug_field='username',
                                          read_only=True
                                          )

    class Meta:
        model = Post
        fields = ('__all__')
        read_only_fields = ('author',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(many=False,
                                          slug_field='username',
                                          read_only=True
                                          )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('author', 'post')


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(many=False,
                                        read_only=True,
                                        slug_field='username',
                                        )
    following = serializers.SlugRelatedField(
        many=False,
        read_only=False,
        queryset=User.objects.all(),
        slug_field='username',
        required=True,
    )

    class Meta:
        model = Follow
        fields = ('__all__')
        read_only_fields = ('user',)
