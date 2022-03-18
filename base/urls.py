from django.urls import path
from . import views

urlpatterns = [
    path("", views.homePage, name="home"),
    path("project/<str:pk>/", views.projectPage, name="project"),
    path("add-project/", views.createProject, name="add-project"),
    path("edit-project/<str:pk>", views.editProject, name="edit-project"),
    path("inbox/", views.inboxPage, name="inbox"),
    path("message/<str:pk>", views.messagePage, name="message"),
    path("add-skill/", views.addSkill, name="add-skill"),
    path("add-endorsement/", views.addEndorsement, name="add-endorsement"),
    path("add-comment/", views.addComment, name="add-comment"),
]