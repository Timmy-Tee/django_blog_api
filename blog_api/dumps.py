

 # author = serializers.CharField(max_length=255)
     # comments = serializers.CharField(max_length=255)
     # blog = serializers.IntegerField()
     
     # def create(self, validated_data):
     #      try:
     #           blog = Blog.objects.get(id=validated_data['blog'])
     #           data = validated_data.copy()
     #           data['blog'] = blog
     #           comment = Comment.objects.create(**data)
               
     #           if comment:
     #                total_comments = Comment.objects.filter(blog = blog).count()
     #                blog.totalComments = total_comments
     #                blog.save()
               
     #      except Blog.DoesNotExist:
     #           raise NotFound(detail="This blog does not exist")
     #      return(validated_data)


        
    

        
# class GetSingleCommentViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
    
#     def retrieve(self, request, *args, **kwargs):
#         blogid = kwargs.get('blogid')
#         commentid = kwargs.get('commentid')
#         if not blogid:
#             return Response({'error': "BlogID is not passed"}, status=status.HTTP_400_BAD_REQUEST)
        
#         if not commentid:
#             return Response({'error': "CommentID is not passed"}, status=status.HTTP_400_BAD_REQUEST)
        
#         queryset = self.get_queryset().filter(id=commentid)
#         serializer = self.get_serializer(queryset, many=False)
#         return Response(serializer.data, status=status.HTTP_200_OK)



# class GetCommentsForASingleBlog(APIView):
#      def get(self, request, blogid):
#           try:
#                blog = Blog.objects.get(id=blogid)
#                comments = Comment.objects.filter(blog=blog)
#                serializer = CommentSerializer(comments, many=True)     
#                return Response({"blog_title": blog.title ,'comments': serializer.data})
               
#           except Blog.DoesNotExist:
#                return Response({'message': 'Sorry Not Found'})



#   # To create Comments for a particular blog post
# class CreateBlogComment(APIView):    
#     def post(self, request, blogid):
#         data = request.data.copy()
#         data['blog'] = blogid
        
#         serializer = CreateBlogCommentSerializer(data=data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save() 
#             return Response({"message": "Comment Created Successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)



# class GetCommentsForASingleBlog(APIView):
#      def get(self, request, blogid):
#           try:
#                blog = Blog.objects.get(id=blogid)
#                comments = Comment.objects.filter(blog=blog)
#                serializer = CommentSerializer(comments, many=True)     
#                return Response({"blog_title": blog.title ,'comments': serializer.data})
               
#           except Blog.DoesNotExist:
#                return Response({'message': 'Sorry Not Found'})


























# from rest_framework import mixins,viewsets
# from rest_framework.views import APIView
# from django.shortcuts import get_object_or_404
# from rest_framework.parsers import MultiPartParser, FormParser
# from rest_framework import status
# from rest_framework.response import Response
# from . serializers import *
# from . models import Blog

# class GetAllBlogPostView(APIView):
#     def get(self, request):
#         blog = Blog.objects.all()      
#         serializer = BlogSerializer(blog, many=True)
        
#         for blog in blog:
#             comment = Comment.objects.filter(blog=blog).count()
#             blog.totalComments = comment
#             blog.save()
            
#         return Response(serializer.data, status=status.HTTP_200_OK)
          
# #   # To get all blog post and individual post
# class BlogPostViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
    
#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = self.get_serializer(queryset, many=True)
#         for blog in queryset:
#             comment = Comment.objects.filter(blog=blog).count()
#             blog.totalComments = comment
                        
#             blog.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)


# #   # To create Blog Posts
# class CreateBlogPostViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
#     parser_classes = [MultiPartParser, FormParser]
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer


# #   # To create Comments for a particular blog post
# class CreateBlogComment(APIView):    
#     def post(self, request, blogid):
#         data = request.data.copy()
#         data['blog'] = blogid
        
#         serializer = CreateBlogCommentSerializer(data=data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save() 
#             return Response({"message": "Comment Created Successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)


# class GetCommentsForASingleBlog(APIView):
#      def get(self, request, blogid):
#           try:
#                blog = Blog.objects.get(id=blogid)
#                comments = Comment.objects.filter(blog=blog)
#                serializer = CommentSerializer(comments, many=True)     
#                return Response({"blog_title": blog.title ,'comments': serializer.data})
               
#           except Blog.DoesNotExist:
#                return Response({'message': 'Sorry Not Found'})

# class GetSingleCommentViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
    





# # #  Creating Comments For A Particular blog post 
# class CreateBlogComment(APIView):          
#      def post(self, request, blogid):          
#           data = request.data.copy()
#           data['blog'] = blogid
          
#           serializer = CreateBlogCommentSerializer(data=data)
#           if serializer.is_valid(raise_exception=True):
#                serializer.save()
#                return Response({"message": "Comment Created Successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)




# # class CommentViewSet(mixins.ListModelMixin, mixins.CreateModelMixin ,viewsets.GenericViewSet):
#      # queryset = Comment.objects.all()
#      # serializer_class = CommentSerializer

     
# # class SingleBlogById(APIView):
# #      def get(self, request, id):
# #           try:
# #                blog = Blog.objects.get(id=id)
# #                serializer = BlogSerializer(blog)
# #                return Response(serializer.data, status=status.HTTP_200_OK)
# #           except Blog.DoesNotExist:
# #                return Response({"message": f'Sorry there is currently no blog post with this id {id}'}, status=status.HTTP_404_NOT_FOUND)
 
 
 
     
     
# # class GetAllBlogPost(APIView):
# #      def get(self, request):
# #           blog = Blog.objects.all().order_by('createdAt')
# #           for blog_post in blog:
# #                comment = Comment.objects.filter(blog=blog_post).count()
# #                blog_post.totalComments = comment
# #                blog_post.save()       
# #           serializer = BlogSerializer(blog, many=True)
# #           if not serializer.data:
# #                return Response({"message": 'Sorry there is currently no blog post'}, status=status.HTTP_204_NO_CONTENT)
# #           else:
# #                return Response(serializer.data, status=status.HTTP_200_OK)


# # class SingleBlogById(APIView):
# #      def get(self, request, id):
# #           try:
# #                blog = Blog.objects.get(id=id)
# #                serializer = BlogSerializer(blog)
# #                return Response(serializer.data, status=status.HTTP_200_OK)
# #           except Blog.DoesNotExist:
# #                return Response({"message": f'Sorry there is currently no blog post with this id {id}'}, status=status.HTTP_404_NOT_FOUND)
     
# #      def delete(self, request, id):
# #           blog = Blog.objects.get(id=id)
# #           blog.delete()
# #           return Response({"message": "This Blog Post Has Been Successfully Deleted"}, status=status.HTTP_200_OK)


# # class CreateBlogPost(APIView):
# #      parser_classes = (MultiPartParser, FormParser)
     
# #      def post(self, request):
# #           serializer = CreateBlogPostSerializer(data=request.data)
          
# #           if serializer.is_valid(raise_exception=True):
# #                serializer.save()
# #                return Response({'message': 'Blog Created Successfully'}, status=status.HTTP_201_CREATED)
          


        

# # # <! ---- Get All Comments For A Particular blog post -----!>
# class GetCommentsForASingleBlog(APIView):
#      def get(self, request, blogid):
#           try:
#                blog = Blog.objects.get(id=blogid)
#                comments = Comment.objects.filter(blog=blog)
#                serializer = CommentSerializer(comments, many=True)     
#                return Response({"blog_title": blog.title ,'comments': serializer.data})
               
#           except Blog.DoesNotExist:
#                return Response({'message': 'Sorry Not Found'})
          
          
# # # Get All Repleis in a particular comment