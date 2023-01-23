from django import forms


class NewEntry(forms.Form):
        title = forms.CharField(label="",max_length=50, widget= forms.TextInput (attrs={'placeholder':'Title'}))
        content = forms.CharField(label="",max_length=1e9,widget=forms.Textarea (attrs={'placeholder':'Content'}))