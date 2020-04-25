"""
@author: Thomason
@contact: ThomasonZhao@outlook.com 
@create: 2020/4/25 12:34 PM 
"""
from django import forms


class AddForm(forms.Form):
    name = forms.CharField()
    headimg = forms.FileField()
