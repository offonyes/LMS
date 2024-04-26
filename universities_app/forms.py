from django import forms
from universities_app.models import Subject, Student, Assignment, AssignmentResponse


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


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['description', 'assignment_file', 'deadline']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'})
        }


class AssignmetResponseForm(forms.ModelForm):
    class Meta:
        model = AssignmentResponse
        fields = ['student_note', 'assignment_file']
