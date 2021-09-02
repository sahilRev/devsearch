from django.forms import ModelForm, fields, widgets
from django import forms
from .models import Project

class ProjectForm(ModelForm):
    '''Inheriting ModelForm makes this class as a form object; declaring class Meta with same as below variable names in mandatory'''
    class Meta:
        model = Project
        fields = ['title','description','featured_image','demo_link','source_link','tags']
        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
            'description':forms.Textarea(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm , self).__init__(*args, **kwargs)

            # self.fields['title'].widget.attrs.update(
            #     {'class':'input' , 'placeholder':'Add Title'}
            #     )

        for name,field in self.fields.items():
                field.widget.attrs.update(
                    {'class':'input'}
                )