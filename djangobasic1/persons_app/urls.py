from django.urls import path
from persons_app.views import index_view, person_detail_view

urlpatterns = [
    path("index/", index_view),
    path("details/<int:person_id>/", person_detail_view)
]