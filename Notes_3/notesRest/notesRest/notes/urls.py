from django.urls import path
from .views import NoteListCreate, NoteDetail, NoteUpdateDelete

urlpatterns = [
    path('notes/', NoteListCreate.as_view(), name='note-list-create'),
    path('notes/<int:pk>/', NoteDetail.as_view(), name='note-detail'),
    path('tasks/<int:pk>/', NoteUpdateDelete.as_view(), name='task-update-delete'),
]
