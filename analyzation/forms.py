from django import forms

RADIO_CHOICES_DayOrHours = [
    ('day', 'In Tagen'),
    ('hours', 'In Stunden'),
]

RADIO_CHOICES_Top5OrTop10 = [
    ('5', 'TOP 5'),
    ('10', 'TOP 10'),
]

SELECT_CHOICES_Weekday = [
    ('1', 'Montag'),
    ('2', 'Dienstag'),
    ('3', 'Mittwoch'),
    ('4', 'Donnerstag'),
    ('5', 'Freitag'),
    ('6', 'Samstag'),
    ('7', 'Sonntag'),
]


class FormDashboard(forms.Form):
    dateRange = forms.CharField(
        required=True,
        label='Zeitraum',
        # inital = "",
        widget=forms.TextInput(
            attrs={
                # aktueller Tag - 6 Tage vor heute
                "placeholder": "01.10.2020 - 06.10.2020",
                "class": "form-control needs-validation",
                "id": "dateRangePicker",
                "style": "",
                # aktueller Tag - 6 Tage vor heute
                "value": "01.10.2020 - 06.10.2020"
            }
        )
    )
    radio = forms.CharField(
        required=True,
        label='',
        widget=forms.RadioSelect(
            choices=RADIO_CHOICES_Top5OrTop10, # '5' needs to be initial
            attrs={
            }
        ),
    )


class FormSalesFilter(forms.Form):
    dateRange = forms.CharField(
        required=True,
        label='Zeitraum',
        # inital = "",
        widget=forms.TextInput(
            attrs={
                # aktueller Tag - 6 Tage vor heute
                "placeholder": "01.10.2020 - 06.10.2020",
                "class": "form-control needs-validation",
                "id": "dateRangePicker",
                "style": "",
                # aktueller Tag - 6 Tage vor heute
                "value": "01.10.2020 - 06.10.2020"
            }
        )
    )
    radioDAY = forms.CharField(
        required=True,
        label='',
        widget=forms.RadioSelect(
            choices=RADIO_CHOICES_DayOrHours, # 'day' needs to be initial
            attrs={
            }
        ),
    )
    radioTOP = forms.CharField(
        required=True,
        label='',
        widget=forms.RadioSelect(
            choices=RADIO_CHOICES_Top5OrTop10, # '5' needs to be initial
            attrs={
            }
        ),
    )
    day = forms.ChoiceField(
        required=True,
        label='Tag auswählen',
        choices=SELECT_CHOICES_Weekday,
        widget=forms.Select(
            attrs={
                'style': '', # if RADIO_CHOICES_DayOrHours = 'day' then "style":"display:hidden" else "style":""
                'class': 'form-control'
            }
        )
    )


class FormCustomerFilter(forms.Form):
    radioDAY = forms.CharField(
        required=True,
        label='',
        widget=forms.RadioSelect(
            choices=RADIO_CHOICES_DayOrHours, # 'day' needs to be initial
            attrs={
            }
        ),
    )
    day = forms.ChoiceField(
        required=True,
        label='Tag auswählen',
        choices=SELECT_CHOICES_Weekday,
        widget=forms.Select(
            attrs={
                'style': '',  # if RADIO_CHOICES_DayOrHours = 'day' then "style":"display:hidden" else "style":""
                'class': 'form-control'
            }
        )
    )
    radioTOP = forms.CharField(
        required=True,
        label='',
        widget=forms.RadioSelect(
            choices=RADIO_CHOICES_Top5OrTop10, # '5' needs to be initial
            attrs={
            }
        ),
    )


class FormEmployeeFilter(forms.Form):
    dateRange1 = forms.CharField(
        required=True,
        label='Zeitraum',
        # inital = "",
        widget=forms.TextInput(
            attrs={
                # aktueller Tag - 6 Tage vor heute
                "placeholder": "01.10.2020 - 06.10.2020",
                "class": "form-control needs-validation",
                "id": "dateRangePicker",
                "style": "",
                # aktueller Tag - 6 Tage vor heute
                "value": "01.10.2020 - 06.10.2020",
                "readonly":""
            }
        )
    )
    dateRange2 = forms.CharField(
        required=True,
        label='Zeitraum',
        # inital = "",
        widget=forms.TextInput(
            attrs={
                # aktueller Tag - 6 Tage vor heute
                "placeholder": "01.10.2020 - 06.10.2020",
                "class": "form-control needs-validation",
                "id": "dateRangePicker2",
                "style": "",
                # aktueller Tag - 6 Tage vor heute
                "value": "01.10.2020 - 06.10.2020",
                "readonly":""
            }
        )
    )