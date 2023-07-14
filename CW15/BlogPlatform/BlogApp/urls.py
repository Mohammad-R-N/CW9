from django.urls import path
from . import views


urlpatterns = [
    path('',views.home_page),
    path('comment/', views.BlogCommentView.as_view()),
    path('post/', views.BlogPostView.as_view()),
    path("detail/",views.BlogDetailView.as_view())
]
