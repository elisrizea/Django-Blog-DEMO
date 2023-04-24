
from .models import Posts
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['url', 'username', 'password', 'email', 'groups']

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data['password'] = make_password(password)
        return super().create(validated_data)


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('title',
                  'post_author',
                  'content',
                  'date',
                   )
        model = Posts


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title',
                  'post_author',
                  'content',
                  'date',
                  )
        model = Posts