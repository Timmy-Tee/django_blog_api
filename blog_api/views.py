from rest_framework import mixins,viewsets
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.response import Response
from . serializers import BlogSerializer ,CreateBlogCommentSerializer, CommentSerializer ,ReplySerializer
from . models import Blog, Comment, Reply
          

#   # To get all blog post and individual post
class BlogPostViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        for blog in queryset:
            comment = Comment.objects.filter(blog=blog).count()
            blog.totalComments = comment
                        
            blog.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


#   # To create Blog Posts
class CreateBlogPostViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    parser_classes = [MultiPartParser, FormParser]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


#   # To create Comments for a particular blog post
class CreateBlogComment(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CreateBlogCommentSerializer
    
    # def list(self, r)
    
    def create(self, request, *args, **kwargs):
        blogid  = kwargs.get('blogid')
        if not blogid:
            return Response({'error': "BlogId is not Passed"}, status=status.HTTP_400_BAD_REQUEST)
        
        data = request.data.copy()
        data['blog'] = blogid
        
        serializer = self.get_serializer(data = data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response({'message': "Created Successfully", 'data': serializer.data}, status=status.HTTP_201_CREATED)




# # Get All Comments for a single blog post

class GetSingleBlogCommentViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin ,viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'commentid'
    
    def list(self, request, *args, **kwargs):
        blogid = kwargs.get('blogid')
        if not blogid:
            return Response({'error': "BlogId is not Passed"}, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = self.get_queryset().filter(blog_id=blogid)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, *args, **kwargs):
        blogid = kwargs.get('blogid')
        commentid = kwargs.get('commentid')

        if not blogid:
                return Response({'error': "BlogId is not Passed"}, status=status.HTTP_400_BAD_REQUEST)
            
        if not commentid:
                return Response({'error': "CommentID is not Passed"}, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = self.get_queryset().filter(blog_id=blogid, id=commentid).first()
        if not queryset:
            return Response({'error': "Sorry This Comment Does not exist"}, status=status.HTTP_204_NO_CONTENT)
        
        serializer = self.get_serializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
        
        
class CreateCommentReplyViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    
    def list(self, request, *args, **kwargs):
        commentid = kwargs.get('commentid')
        if not commentid:
            return Response({'error': "Sorry This There is not Commentid Passed"}, status=status.HTTP_400_BAD_REQUEST)

        queryset = self.get_queryset().filter(comment_id = commentid)
        serializer = self.get_serializer(queryset, many="True")
        
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    
    def create(self, request, *args, **kwargs):
        commentid = kwargs.get('commentid')
        print(commentid)
        if not commentid:
            return Response({'error': "Sorry This There is not Commentid Passed"}, status=status.HTTP_400_BAD_REQUEST)

        data = request.data.copy()
        data['comment'] = commentid
        serializer = self.get_serializer(data = data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response({'message': "Created Successfully", 'data': serializer.data}, status=status.HTTP_201_CREATED)
        

    
    