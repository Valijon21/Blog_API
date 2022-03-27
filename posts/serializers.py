from dataclasses import field
from rest_framework import serializers
from .models import Post

class  Postserializer(serializers.ModelSerilaizer):
    
    class Meta:
        model = Post
        field=('id','author','title','body','created_date')