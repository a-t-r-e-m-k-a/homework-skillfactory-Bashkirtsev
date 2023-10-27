from django.urls import path
from .views import NewsList, NewsDetail, PostCreate, PostUpdate, PostDelete, PostSearch

urlpatterns = [
   path('', NewsList.as_view()),
   path('<int:pk>', NewsDetail.as_view()),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('search/', PostSearch.as_view(), name='post_search')
]
