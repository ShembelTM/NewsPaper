from django.urls import path
from .views import PostsList, PostsDetail, NewsFilter


urlpatterns = [
   path('', PostsList.as_view()),
   path('<int:pk>', PostsDetail.as_view()),
   path('search', NewsFilter.as_view()),
]