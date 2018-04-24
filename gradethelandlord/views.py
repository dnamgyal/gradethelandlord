from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .forms import ReviewForm, AddLandlordForm
from .models import Landlord, Review
import datetime
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')

def landlord_list(request):
    landlords = Landlord.objects.all().order_by('name')
    form = AddLandlordForm()
    return render(request, 'landlord_list.html', {'landlords':landlords, 'form': form})

@login_required
def landlord_detail(request, landlord_id):
    landlord = get_object_or_404(Landlord, pk=landlord_id)
    form = ReviewForm()
    return render(request, 'landlord_detail.html', {'landlord': landlord})

def review_list(request):
    review_list = Review.objects.order_by('-pub_date')
    return render(request, 'review_list.html', {'review_list':review_list})

def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'review_detail.html', {'review': review})

def user_review_list(request, username=None):
    if not username:
        username = request.user.username
    review_list = Review.objects.filter(user_name=username).order_by('-pub_date')
    context = {'review_list':review_list, 'username':username}
    return render(request, 'user_review_list.html', context)

@login_required
def add_review(request, landlord_id):
    landlord = get_object_or_404(Landlord, pk=landlord_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = Review()
        review.landlord = landlord
        review.user_name = request.user
        review.address = form.cleaned_data['address']
        review.length_of_stay = form.cleaned_data['length_of_stay']
        review.move_in_condition = form.cleaned_data['move_in_condition']
        review.apartment_condition = form.cleaned_data['apartment_condition']
        review.maintenance_efficiency = form.cleaned_data['maintenance_efficiency']
        review.treatment_by_your_landlord = form.cleaned_data['treatment_by_your_landlord']
        review.communication_with_your_landlord = form.cleaned_data['communication_with_your_landlord']
        review.landlord_helpfulness = form.cleaned_data['landlord_helpfulness']
        review.overall_rating = form.cleaned_data['overall_rating']
        review.rent_again = form.cleaned_data['rent_again']
        review.additional_comments = form.cleaned_data['additional_comments']
        review.pub_date = datetime.datetime.now()
        review.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('landlord_detail', args=(landlord.id,)))
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'landlord': landlord, 'form': form})

@login_required
def add_landlord(request):
    landlords = Landlord.objects.all()
    form = AddLandlordForm(request.POST)
    if form.is_valid():
        l = Landlord()
        l.name = form.cleaned_data['name']
        l.save()
        return HttpResponseRedirect(reverse('landlord_list'))
    else:
        form = AddLandlordForm()
    return render(request, 'landlord_list.html', {'landlords': landlords, 'form': form})



def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        landlords = Landlord.objects.filter(name__icontains=q)
        return render(request, 'search_result.html',
                      {'landlords': landlords, 'query': q})
    else:
        return render(request, 'home.html')
