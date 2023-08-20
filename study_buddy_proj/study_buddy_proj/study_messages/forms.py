from django import forms

from ..study_messages.models import Message


class MessageForm(forms.ModelForm):
    message = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Write your message here ...'}), label="")

    class Meta:
        model = Message
        fields = ('message',)
