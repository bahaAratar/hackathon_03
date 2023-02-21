from rest_framework import serializers
from applications.feedback.models import Comment, Rating

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    
    class Meta:
        model = Comment 
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating 
        fields = ('rating', )

