from django.db.models import fields, query
from django.db.models.base import Model
from rest_framework import serializers
from superadmin.models import PostDetails, Images, Tags

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields = '__all__'
        
class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tags
        fields = '__all__'
        
class PostSerializer(serializers.ModelSerializer):
    
    Images = ImageSerializer(read_only=True)
    Tags = TagSerializer(read_only=True)
    
    class Meta:
        Model = PostDetails
        fields = '__all__'
