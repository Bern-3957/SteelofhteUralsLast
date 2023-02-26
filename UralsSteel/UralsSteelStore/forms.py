from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


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

class BasketRequestForm(forms.Form):
    DELIVERY_CHOICES = [('Самовывоз', 'Самовывоз'),
                        ('Доставка собственным транспортом', 'Доставка собственным транспортом'),
                        ('Доставка Транспортной компаней', 'Доставка Транспортной компаней'),
                        ]
    delivery_radio = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=DELIVERY_CHOICES,
        attrs={
            'class': 'basket_order_common_variants_item_inp',
        }))
    PAY_CHOICES = [('Наличными при самовывозе', 'Наличными при самовывозе'),
                        ('Оплата по счету', 'Оплата по счету'),
                        ('Оплата по квитанции', 'Оплата по квитанции'),
                        ('Оплата картой при самовывозе', 'Оплата картой при самовывозе'),
                        ]
    pay_radio = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=PAY_CHOICES,
        attrs={
            'class': 'basket_order_common_variants_item_inp',
        }))

    full_name = forms.CharField(max_length=20, label='ФИО', widget=forms.TextInput(
        attrs={
            'placeholder': 'Фамилия Имя Отчество',
            'class': 'full_name_inp-order',
            'id': 'full_name_inp',
        }))

    email = forms.EmailField(label='Email', widget=forms.TextInput(
        attrs={
            'placeholder': 'Email',
            'class': 'email_inp-order',
        }))
    phone_number = forms.CharField(max_length=11, label='Телефон', widget=forms.TextInput(
        attrs={
            'placeholder': '+7 (___)___-__-__',
            'class': 'ph_number_inp-order',
        }))
    comment = forms.CharField(label='Комментарий к заказу', widget=forms.Textarea(

        attrs={
            'cols': 10,
            'rows': 30,
            'placeholder': 'Ваш комментарий...',
            'class': 'comments_textarea-order',
        }))
    checkb = forms.BooleanField(label='Я согласен на обработку персональных данных', initial=True, widget=forms.CheckboxInput(
        attrs={
            'class': 'checkbox_inp',
        }))

class RegistrationUserForm(UserCreationForm):

    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'registration_form_item_inp'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'registration_form_item_inp'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'registration_form_item_inp'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'registration_form_item_inp'}))


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class AuthorisationUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'authorisation_form_item_inp'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'authorisation_form_item_inp'}))

