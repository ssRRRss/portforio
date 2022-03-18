from django.shortcuts import render, redirect
from .models import projectData, skill, Message, Endorsement, Comment
from .forms import ProjectForm, MessageForm, SkillForm, EndorsementForm, CommentForm
from django.contrib import messages


def homePage(request):
    projects = projectData.objects.all()
    detailskills = skill.objects.exclude(body="")
    skills = skill.objects.filter(body="")
    endorsements = Endorsement.objects.filter(approved=True)
    form = MessageForm()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message was successfully sent!!')
            return redirect("home")
    context = {"projects": projects, "skills": skills,
               "detailskills": detailskills, "form": form, "endorsements": endorsements}
    return render(request, "base/templates/home.html", context)


def projectPage(request, pk):
    project = projectData.objects.get(id=pk)
    count = Comment.objects.count()
    comments = Comment.objects.all().order_by("-created_at")
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = project
            comment.save()
            messages.success(
                request, 'Thank you!!  your comment was successfully added!!')
            return redirect("project", pk)
    context = {"project": project, "count": count,
               "comments": comments, "form": form}
    return render(request, "base/templates/project.html", context)


def createProject(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your projects was successfully added!!")
            return redirect("home")
    context = {"form": form}
    return render(request, "base/templates/project_form.html", context)


def editProject(request, pk):
    project = projectData.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {"form": form}
    return render(request, "base/templates/project_form.html", context)


def inboxPage(request):
    inbox = Message.objects.all().order_by("is_read")
    unreadCount = Message.objects.filter(is_read=False).count()
    context = {"inbox": inbox, "unreadCount": unreadCount}
    return render(request, "base/templates/inbox.html", context)


def messagePage(request, pk):
    message = Message.objects.get(id=pk)
    message.is_read = True
    message.save()
    context = {"message": message}
    return render(request, "base/templates/message.html", context)


def addSkill(request):
    form = SkillForm()
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your skills was successfully added!!')
            return redirect("home")
    context = {"form": form}
    return render(request, "base/templates/skill_form.html", context)


def addEndorsement(request):
    form = EndorsementForm()
    if request.method == "POST":
        form = EndorsementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Thank you!!  your endorsement was successfully added!!')
            return redirect("home")
    context = {"form": form}
    return render(request, "base/templates/endorsement.html", context)


def addComment(request):
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Thank you!!  your comment was successfully added!!')
            return redirect("project")
    context = {"form": form}
    return render(request, "base/templates/project.html", context)
