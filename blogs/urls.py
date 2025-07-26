from django.urls import path,include
from blogs.views import CommentsView,BlogView,BlogDetailView,CommentsDetailView
urlpatterns = [
    path('blog/',BlogView.as_view()),
    path('comments/',CommentsView.as_view()),
    path('blogview/<int:pk>',BlogDetailView.as_view()),
    path('CommentsView/<int:pk>',CommentsDetailView.as_view())
]
