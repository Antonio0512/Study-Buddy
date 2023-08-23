from django import forms
from django.forms import ModelForm

from ..rooms.models import Room
from ..topics.models import Topic


class RoomCreateForm(ModelForm):
    topic = forms.ModelChoiceField(
        queryset=Topic.objects.all(),
        required=False,  # Make the topic field not required
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    new_topic = forms.CharField(max_length=100, required=False, label="Add New Topic")

    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']

    def clean(self):
        cleaned_data = super().clean()
        topic_name = cleaned_data.get('topic')
        new_topic_name = cleaned_data.get('new_topic')

        if new_topic_name and topic_name != new_topic_name:
            topic, created = Topic.objects.get_or_create(name=new_topic_name)
            cleaned_data['topic'] = topic

        return cleaned_data
