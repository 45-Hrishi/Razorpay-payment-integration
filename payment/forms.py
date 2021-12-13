from crispy_forms.layout import Layout
from django import forms
from django.db.models import fields
from .models import Donation
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = '__all__'

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'name',
            'amount',
            'phone_no',
            'email',
            Submit('submit','Submit',css_class ='button btn btn-block btn-lg btn-outline-light  mt-2 rounded-0 btn-dark'),
        )