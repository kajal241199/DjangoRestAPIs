from django.urls import path, include
from .views import article_list, article_detail, ArticleAPIView, ArticleDetail

urlpatterns = [
    #path('article/', article_list),
    path('article/', ArticleAPIView.as_view()),
    #path('detail/<int:pk>/', article_detail),
    path('detail/<int:id>/', ArticleDetail.as_view() ),
]