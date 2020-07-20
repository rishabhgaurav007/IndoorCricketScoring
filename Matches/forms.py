from django import forms

PLAYER = [
    ('0','NotOut'),
    ('1', 'Nikhil'),
    ('2', 'Ronit'),
    ('3', 'Any'),
    ('4', 'Mithi'),
    ('5', 'Ratn'),
    ('6', 'Sarthak'),
    ('7', 'Kaju'),
    ('8', 'Aman'),
    ('9', 'Yash'),
    ('10', 'Manglam'),
    ('11', 'Shivam'),
    ('12', 'Ayushman'),
]

class UserForm(forms.Form):
    run = forms.IntegerField(label="run")
    bowler=forms.CharField(label="Bowler", widget = forms.Select(choices=PLAYER))
    crypto=forms.CharField(label="crypto")