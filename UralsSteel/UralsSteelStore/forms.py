from django import forms

class RequestForm(forms.Form):

    full_name = forms.CharField(max_length=20, label='ФИО', widget=forms.TextInput(
        attrs={
            'placeholder': 'Фамилия Имя Отчество',
            'class': 'full_name_inp',
            'id': 'full_name_inp',
        }))

    email = forms.EmailField(label='Email', widget=forms.TextInput(
        attrs={
            'placeholder': 'Email',
            'class': 'email_inp',
        }))
    phone_number = forms.CharField(max_length=11, label='Телефон', widget=forms.TextInput(
        attrs={
            'placeholder': '+7 (___)___-__-__',
            'class': 'ph_number_inp',
        }))
    comment = forms.CharField(label='Комментарий', widget=forms.Textarea(
        attrs={
            'cols': 60,
            'rows': 10,
            'placeholder': 'Сообщение...',
            'class': 'comments_textarea',
        }))
    checkb = forms.BooleanField(label='Я согласен на обработку персональных данных', initial=True, widget=forms.CheckboxInput(
        attrs={
            'class': 'checkbox_inp',
        }))


class ModalRequestForm(forms.Form):
    full_name = forms.CharField(max_length=200, label='ФИО', widget=forms.TextInput(
        attrs={
            'placeholder': 'Фамилия Имя Отчество',
            'class': 'modal_input',
            'id': 'full_name_inp',
        }))

    email = forms.EmailField(label='Email', widget=forms.TextInput(
        attrs={
            'placeholder': 'Email',
            'class': 'modal_input',
        }))
    phone_number = forms.CharField(max_length=11, label='Телефон', widget=forms.TextInput(
        attrs={
            'placeholder': '+7 (___)___-__-__',
            'class': 'modal_input',
        }))
    comment = forms.CharField(label='Комментарий', widget=forms.Textarea(
        attrs={
            'cols': 60,
            'rows': 10,
            'placeholder': 'Сообщение...',
            'class': 'modal_textarea',
        }))
    checkb = forms.BooleanField(label='Я согласен на обработку персональных данных', initial=True, widget=forms.CheckboxInput(
        attrs={
            'class': 'modal_checkb',
        }))
