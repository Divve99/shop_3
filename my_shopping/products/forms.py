from django import forms


class MyForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    address = forms.CharField(label='Address', max_length=25)
    age = forms.CharField(label='Age', max_length=100)
    CHOICES = [('yes', 'Yes, I am happy!'),
               ('no', 'No, I am not happy.')]
    is_happy = forms.ChoiceField(label='Are you happy?', choices=CHOICES, widget=forms.RadioSelect)
    CHOICES = [('yes', 'female'),
               ('yes', 'male'),
               ('no', 'other')]
    is_gender = forms.ChoiceField(label='Gender?', choices=CHOICES, widget=forms.RadioSelect)

    def clean(self):
        super(MyForm, self).clean()

        name = self.cleaned_data.get('name')
        address = self.cleaned_data.get('address')
        age = self.cleaned_data.get("age")

        if len(name) > 30:
            self._errors['name'] = self.error_class([
                'Maximum 30 characters.'])
        if len(address) > 25:
            self._errors['address'] = self.error_class([
                'Maximum 25 characters.'])
        if len(age) > 10:
            self._erors['age'] = self.error_class([
                'Maximum age limit greater than 10.'])

        return self.cleaned_data
