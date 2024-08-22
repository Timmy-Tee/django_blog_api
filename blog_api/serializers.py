from rest_framework import serializers
from . models import *
from rest_framework.exceptions import NotFound


class BlogSerializer(serializers.ModelSerializer):
     class Meta:
          model = Blog
          exclude = ['createdAt']
          
     def retrieve(self, instance):
          print(instance)
          
          
                     
class CommentSerializer(serializers.ModelSerializer):
     class Meta:
          model = Comment
          exclude = ['blog', 'createdAt', 'totalReplies']
     

class CreateBlogCommentSerializer(serializers.ModelSerializer):
     class Meta: 
          model = Comment
          fields = ['author', 'blog', 'comments']
          
          
     def create(self, validated_data):
          try:
               print(f'{validated_data['blog']}')
               blog = Blog.objects.get(id = validated_data['blog'].id)
               print(f'{blog}')
               created_comment = Comment.objects.create(**validated_data)
               if created_comment: 
                    comment = Comment.objects.filter(blog = validated_data['blog']).count()   
                    blog.totalComments = comment
                    blog.save()
               else:
                    raise ValueError("Error Creating A Comment")
               
               return validated_data
          except Blog.DoesNotExist:
               raise ValueError("This Blog Post Does Not Exist")
          
    
    
class ReplySerializer(serializers.ModelSerializer):
     class Meta:
          model = Reply
          exclude = ['createdAt']
     
     def create(self, validated_data):
          comment = Comment.objects.filter(id = validated_data['comment'].id).first()
          if not comment:
               raise ValueError("Sorry This Comment Does not Exist")
          Reply.objects.create(**validated_data)
          
          return (validated_data)
     