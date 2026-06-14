# notices/forms.py
from django import forms
from .models import Notice


class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'content', 'category', 'attachment']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
            'attachment': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }
