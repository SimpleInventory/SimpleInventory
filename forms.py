from .models import Card
from .models import Board
from .models import Stage
from django.forms import ModelForm

class CardForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CardForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'mdl-textfield__input'
            field.widget.attrs['rows'] = 3

    class Meta:
        model = Card
        fields = ['name', 'quantity', 'notes', 'stage', 'board']

class BoardForm(ModelForm):
    class Meta:
        model = Board
        fields = ['name', 'desc', 'active']

class StageForm(ModelForm):
    class Meta:
        model = Stage
        fields = ['name', 'index', 'archived']
