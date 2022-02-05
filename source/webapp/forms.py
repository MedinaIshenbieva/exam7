from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from webapp.models import Poll, Choice, Answer


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        exclude = []
        widgets = {
            'choices': forms.CheckboxSelectMultiple
        }

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data['title']
        if len(title) < 5:
            self.add_error('title', ValidationError(
                f"Значение должно быть длиннее 5 символов {title} не подходит"))


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="Найти")


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ("answer",)


class AnswerChoiceForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ("question",)


class PollDeleteForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ("title",)

    def clean_title(self):
        if self.instance.title != self.cleaned_data.get("title"):
            raise ValidationError("Название Опроса не соответствует")
        return self.cleaned_data.get("title")
