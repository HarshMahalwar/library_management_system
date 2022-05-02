from django.forms import ModelForm
from .models import book, Topic, participant, Issue


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'
        labels = {
            'name': 'Topic name'
        }


class participantForm(ModelForm):
    class Meta:
        model = participant
        fields = '__all__'
        labels = {
            'name': 'Participant name'
        }


class bookForm(ModelForm):
    class Meta:
        model = book
        fields = '__all__'
        labels = {
            'desc': 'Description'
        }

    def __init__(self, *args, **kwargs):
        super(bookForm, self).__init__(*args, **kwargs)
        self.fields['topic'].empty_label = "click here to select the topic"

class IssuerForm(ModelForm):
    class Meta:
        model = Issue
        fields = '__all__'
        labels = {
            'host': 'Issuer'
        }

    def __init__(self, *args, **kwargs):
        super(IssuerForm, self).__init__(*args, **kwargs)
        self.fields['host'].empty_label = "click here to select the Issuer"
        self.fields['participant'].empty_label = "click here to select the Participant"
        self.fields['book'].empty_label = "click here to select the book"