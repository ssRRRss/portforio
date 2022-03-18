from django.forms import ModelForm, Textarea
from .models import projectData, Message, skill, Endorsement, Comment


class ProjectForm(ModelForm):
    class Meta:
        model = projectData
        fields = ["title", "thumbnail", "body"]

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update(
            {"class": "form-control"}
        )
        self.fields["body"].widget.attrs.update(
            {"class": "form-control"}
        )


class SkillForm(ModelForm):
    class Meta:
        model = skill
        fields = "__all__"
        exclude = ["id"]

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update(
            {"class": "form-control"}
        )
        self.fields["body"].widget.attrs.update(
            {"class": "form-control"}
        )


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ["name", "email", "subject", "body"]
        # exclude = ["is_read"]
        widgets = {
            "name": Textarea(attrs={'rows': 1, 'cols': 70}),
            "email": Textarea(attrs={'rows': 1, 'cols': 70}),
            "subject": Textarea(attrs={'rows': 1, 'cols': 70}),
            "body": Textarea(attrs={'rows': 5, 'cols': 70}),
        }

        def __init__(self, *args, **kwargs):
            super(MessageForm, self).__init__(*args, **kwargs)
            self.fields["name"].widget.attrs.update(
                {"class": "form-control"}
            )
            self.fields["email"].widget.attrs.update(
                {"class": "form-control"}
            )
            self.fields["subject"].widget.attrs.update(
                {"class": "form-control"}
            )
            self.fields["body"].widget.attrs.update(
                {"class": "form-control"}
            )


class EndorsementForm(ModelForm):
    class Meta:
        model = Endorsement
        fields = "__all__"
        exclude = ["featured"]

    def __init__(self, *args, **kwargs):
        super(EndorsementForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {"class": "form-control"}
        )
        self.fields["body"].widget.attrs.update(
            {"class": "form-control"}
        )


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        exclude = ["project"]

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {"class": "form-control"}
        )
        self.fields["body"].widget.attrs.update(
            {"class": "form-control"}
        )
