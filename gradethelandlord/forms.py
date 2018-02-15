from django.forms import ModelForm, Textarea, RadioSelect
from gradethelandlord.models import Review, Landlord

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['address', 'length_of_stay', 'move_in_condition', 'apartment_condition', 'maintenance_efficiency', 'treatment_by_your_landlord', 'communication_with_your_landlord', 'landlord_helpfulness', 'overall_rating', 'rent_again', 'comment']
        widgets = {'comment': Textarea(attrs={'rows': 5, 'placeholder': "Anything else you'd like to add?"})}

class AddLandlordForm(ModelForm):
    class Meta:
        model = Landlord
        fields = ['name',]
