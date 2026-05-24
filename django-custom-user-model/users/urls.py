from django.urls import path

from .views import RegisterView, TodoListCreateView, TodoDetailView


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("<int:user_id>/todos/", TodoListCreateView.as_view(), name="todos"),
    path("<int:user_id>/todos/<int:id>/", TodoDetailView.as_view(), name="todo"),
]
