from django.urls import path # type: ignore
# from . import views
from.views import AddPostView, ArticleDetailView, IndexView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView
urlpatterns = [
#    path('', views.index,name="index"),
    path('', IndexView.as_view(), name='index'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'), 
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/<int:pk>/edit', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('category/<str:cats>/', CategoryView, name='category'),
]