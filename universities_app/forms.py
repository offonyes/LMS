from django import forms
from universities_app.models import Subject, Student


class LecturerForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['description', 'syllabus']


class StudentForm(forms.ModelForm):
    subjects = forms.ModelMultipleChoiceField(queryset=Subject.objects.all(), required=False, widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Student
        fields = ['subjects']
