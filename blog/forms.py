from django import forms
from django.core.validators import ValidationError
from blog.models import Message



class ContactUsForm(forms.Form):
    BIRTH_YEAR_CHOICES = ["1980", "1981", "1982"]
    FAVORITE_COLORS_CHOICES = {
        "blue": "Blue",
        "green": "Green",
        "black": "Black",
    }

    name = forms.CharField(max_length=10, label='Your message')
    text = forms.CharField(max_length=10, label='Your message')
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES, attrs={"class": "form-control"}))
    colors = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    fileupload = forms.FileField(widget=forms.FileInput(attrs={"class": "form"}), required=True)


    def clean(self):
        name = self.cleaned_data.get('name')
        print(name)
        text = self.cleaned_data.get('text')
        print(text)

        if name == text:
            raise ValidationError('name and text are same', code='name_and_text')


    def clean_name(self):
        name = self.cleaned_data.get('name')
        if 'a' in name:
            raise ValidationError('a can not be in name', code='a_in_name')
        return name

class MessagesForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a title',
                'style': 'max-width: 300px;'}),
            'text': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a text'})

        }


