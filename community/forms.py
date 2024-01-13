from django.forms import ModelForm
from .models import room

class roomform(ModelForm):
    class Meta:
        model=room
        # fields=['topic','name','desc']
        fields='__all__'