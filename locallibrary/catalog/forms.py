# archivo forms.py
from django import forms
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from catalog.models import BookInstance, Book
from django_select2 import forms as s2forms


class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text=_(
        "Enter a date between now and 4 weeks (default 3)."))

    def clean_renewal_date(self):
        '''Valida que la fecha no sea en el pasado y no más de 4 semanas en el futuro'''
        data = self.cleaned_data['renewal_date']

        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(
                _('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data

# Ahora el mismo formulario con un modelForm


class RenewBookModelForm(forms.ModelForm):
    def clean_due_back(self):
        data = self.cleaned_data['due_back']

        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(
                _('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data

    class Meta:
        model = BookInstance
        fields = ['due_back', 'status']
        labels = {'due_back': _('Renewal date')}
        help_texts = {'due_back': _(
            'Enter a date between now and 4 weeks (default 3).')}


class ContactForm(forms.Form):
    ''' Contact form '''
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    from_email.widget.attrs.update({'class': 'form-control'})
    subject.widget.attrs.update({'class': 'form-control'})
    message.widget.attrs.update({'class': 'form-control'})


class AutorWidget(s2forms.ModelSelect2Widget):
    search_fields = ['first_name__icontains', 'last_name__icontains']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'summary', 'genre', 'language']
        widgets = {
            'author': AutorWidget, # 'select2'
        }
