from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ["author", "created_at", "updated_at"]

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("제목은 5자 이상이어야 합니다.")
        return value

    # TODO: CommentSerializer 정의 후 아래 주석 해제
    # comments = CommentSerializer(many=True, read_only=True)
