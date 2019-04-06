from django import forms
from tinymce import TinyMCE
from .models import Post, Comment


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Post
        fields = ['title', 'overview', 'content', 'thumbnail', 'categories']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['name', 'email', 'website', 'content']
        labels = {
            'content': "Enter Message"
        }
