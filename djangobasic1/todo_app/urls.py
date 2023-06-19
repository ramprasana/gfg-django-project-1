from django.urls import path
from todo_app.views import index_view, update_view, delete_view, create_view

urlpatterns = [
    path("list/", index_view, name="todo_list_view"),
    path("create/", create_view, name="todo_create_view"),
    path("update/<int:todo_id>/", update_view, name="todo_list_update"),
    path("delete/<int:todo_id>/", delete_view, name="todo_list_delete")
]