from django import forms
from .models import Chapter

class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название главы'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите содержимое главы',
                'rows': 8
            }),
        }
        labels = {
            'title': 'Название главы',
            'content': 'Содержание главы',
        }
