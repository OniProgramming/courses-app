from django import forms



# Create your forms here.

# cretaing the contact form for pricing page
class ContactForm(forms.Form):
	first_name = forms.CharField(widget=forms.TextInput(attrs = {'placeholder': 'First Name', 'class': 'form-control'}), max_length=50)
	last_name = forms.CharField(widget=forms.TextInput(attrs = {'placeholder': 'Last Name', 'class': 'form-control'}), max_length=50)
	email_address = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' :'Email', 'class': 'form-control'}), max_length=100)
	message = forms.CharField(widget = forms.Textarea(attrs = {'placeholder': 'Type here your question', 'class': 'form-control'}), max_length = 5000)
 

        
