from django.forms import ModelForm


from django import forms

from purelight.models import Media

class PostForm(forms.Form):

    class Meta:
        model = Media
        fields = ('healer','title','teaserdescription','price','category','url','description','howtouse','cautions','offer')