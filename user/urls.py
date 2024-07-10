from django.urls import path

from .views import UsersCreateView, UsersListView, UsersUpdateView, UsersDeleteView

urlpatterns = [
  path("", UsersListView.as_view(), name="home"),
  path("create", UsersCreateView.as_view(), name="new_user"),
  path("delete/<int:pk>", UsersDeleteView.as_view(), name="delete_user"),
  path("update/<int:pk>", UsersUpdateView.as_view(), name="update_user")
]