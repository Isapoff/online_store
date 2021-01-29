from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import CategoriesList, ProductViewSet, CommentCreate, CommentUpdate, CommentDelete

router = DefaultRouter()
router.register('', ProductViewSet)



urlpatterns = [
    path('categories/', CategoriesList.as_view()),
    path('', include(router.urls)),
    path('comments/create/', CommentCreate.as_view()),
    path('comments/update/<int:pk>/', CommentUpdate.as_view()),
    path('comments/delete/<int:pk>/', CommentDelete.as_view()),
]