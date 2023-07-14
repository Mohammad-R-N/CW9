from django.urls import path,include
from . import views


urlpatterns = [
    path('comment/', views.BlogCommentView.as_view()),
    path('post/', views.BlogPostView.as_view()),
]
