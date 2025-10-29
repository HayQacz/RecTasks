from django import forms

class PeselForm(forms.Form):
    pesel = forms.CharField(
        label="Enter PESEL number",
        max_length=11,
        min_length=11,
        widget=forms.TextInput(attrs={'placeholder': 'ex. 12345678901'})
    )

    def clean_pesel(self):
        pesel = self.cleaned_data.get('pesel')

        if not pesel.isdigit():
            raise forms.ValidationError("Only numbers are allowed")

        weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        check_sum = 0

        try:
            for i in range(10):
                check_sum += int(pesel[i]) * weights[i]
        except Exception:
            raise forms.ValidationError("An error occurred while calculating the checksum")

        control_number = (10 - (check_sum % 10)) % 10

        if control_number != int(pesel[10]):
            raise forms.ValidationError("Invalid PESEL number. Control number is incorrect")

        return pesel