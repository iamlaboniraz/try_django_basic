from django.urls import path
from .views import (
    ArticleCreateView,
    ArticleDeleteView,
    ArticleDetailView,
    ArticleListView,
    ArticleUpdateView,
   

)
app_name ="articles"
urlpatterns = [
    path('',ArticleListView.as_view(),name="article_list" ),
    path('<int:id>/ ',ArticleDetailView.as_view(),name="article-detail" ),
    path('create/',ArticleCreateView.as_view(),name="article_create" ),
    path('<int:id>/update/',ArticleUpdateView.as_view(),name="article_update" ),
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    #path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
    #path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
]