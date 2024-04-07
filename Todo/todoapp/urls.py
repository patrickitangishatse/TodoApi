from django.urls import path
from .views import TaskListCreate, TaskRetrieveUpdateDestroy
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView



urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),
    path('tasks/<int:id>/', TaskRetrieveUpdateDestroy.as_view(), name='task-retrieve-update-destroy')
]
