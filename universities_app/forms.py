from django import forms
from universities_app.models import Subject, Student


class LecturerForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['description', 'syllabus']


class StudentForm(forms.ModelForm):
    subjects = forms.ModelMultipleChoiceField(queryset=Subject.objects.all(), required=False,
                                              widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Student
        fields = ['subjects']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user:
            self.fields['subjects'].queryset = Subject.objects.filter(faculties=self.user.student.faculty)

    def clean_subjects(self):
        selected_subjects = self.cleaned_data.get('subjects')
        if selected_subjects and len(selected_subjects) > 7:
            raise forms.ValidationError("You can select up to 7 subjects.")
        return selected_subjects
