from rest_framework import serializers
from .models import Post

# Create your serializers here.


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'description',
            'owner',
        ]
