from django.urls import path,include
from . import views


urlpatterns = [
    path('comment/', views.BlogCommentView),
    path('post/', views.BlogPostView),
]
