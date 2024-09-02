from django.urls import path, include
from .views import BlogPostViewSet, CreateBlogComment, CreateBlogPostViewSet, GetSingleBlogCommentViewSet, CreateCommentReplyViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'blog', BlogPostViewSet, basename='home')
router.register(r'create_blog', CreateBlogPostViewSet, basename='create_blog')
# router.register(r'get_comment', GetSingleCommentViewSet, basename='get_comment')
urlpatterns = router.urls

urlpatterns = [
     path('', include(router.urls)),
     path('create_blog_comment/<int:blogid>/', CreateBlogComment.as_view({'post': 'create'})),
     path('single_blog_comment/<int:blogid>/', GetSingleBlogCommentViewSet.as_view({'get': 'list'})),
     path('single_blog_comment/<int:blogid>/<int:commentid>/', GetSingleBlogCommentViewSet.as_view({'get': 'retrieve'})),
     path('get_comment_reply/<int:commentid>/', CreateCommentReplyViewSet.as_view({'get': 'list'})),
     path('create_comment_reply/<int:commentid>/', CreateCommentReplyViewSet.as_view({'post': 'create'})),
]