from django import forms
class ContactForm(forms.Form):
    Type_id = forms.CharField(label="ID",max_length=30,initial=1)
    codepatientp = forms.CharField(label="Code:",max_length=254,initial="BN" )
    namepatient = forms.CharField(label="Họ tên: ",max_length=2000,initial="Nguyễn")
    age = forms.CharField(label="Tuổi: ",max_length=2000,initial="40")
    place = forms.CharField(label="Địa chỉ: ",max_length=2000,initial="Thanh Xuân")
    city = forms.CharField(label="City: ",max_length=2000,initial="Hà Nội")



    def clean(self):
        cleaned_data = super(ContactForm, self).clean()

