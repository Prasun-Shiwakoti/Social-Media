from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("edit-profile", views.editProfile, name="editProfile"),
    path("edit-password", views.editPassword, name="editPassword"),
    path("messages", views.messages, name="messages"),
    path("login", views.login, name="login"),
    path("register", views.register, name="login"),
    path("logout", views.logout, name="logout"),
    path("post", views.addPost, name="addPost"),
    path("changepp", views.changePP, name="changePP"),
    path("addComment", views.addComment, name="addComment"),
    path("addFriend", views.addFriend, name="addFriend"),
    path("changeStatus", views.changeStatus, name="changeStatus"),
    path("likePost", views.likePost, name="likePost"),
    path("timeline", views.timeline, name="timeline"),
    path("searchUser", views.searchUser, name="searchUser"),
    

    

]