from django.forms import ModelForm
from .models import FieldVisit

class FieldVisitForm(ModelForm):
    class Meta:
        model = FieldVisit
        fields = '__all__'
