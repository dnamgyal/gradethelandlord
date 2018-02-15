from django.db import models
import numpy as np

class Landlord(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)

    def __str__(self):
        return self.name

class Review(models.Model):
        RATING_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        )
        YES_NO = (
        ('Yes', 'Yes'),
        ('No', 'No'),)

        STAY = (
        ('Less than 6 months', 'Less than 6 months'),
        ('6 months', '6 months'),
        ('10 months', '10 months'),
        ('1 year', '1 year'),
        ('2 plus years', '2 plus years'),
        )

        user_name = models.CharField(max_length=100)
        pub_date = models.DateField('date published')

        landlord = models.ForeignKey(Landlord)
        address = models.CharField(max_length=200, blank=False, null=True)
        length_of_stay = models.CharField(max_length=20, choices=STAY, blank=False, null=True)

        move_in_condition = models.CharField(max_length=5, choices=RATING_CHOICES, blank=False, null=True)
        apartment_condition = models.CharField(max_length=5, choices=RATING_CHOICES, blank=False, null=True)
        maintenance_efficiency = models.CharField(max_length=5, choices=RATING_CHOICES, blank=False, null=True)

        treatment_by_your_landlord = models.CharField(max_length=5, choices=RATING_CHOICES, blank=False, null=True)
        communication_with_your_landlord = models.CharField(max_length=5, choices=RATING_CHOICES, blank=False, null=True)
        landlord_helpfulness = models.CharField(max_length=5, choices=RATING_CHOICES, blank=False, null=True)


        overall_rating = models.CharField(max_length=5, choices=RATING_CHOICES, blank=False, null=True)
        rent_again = models.CharField(choices=YES_NO, max_length=5, blank=False, null=True)
        comment = models.CharField(max_length=1000, blank=True, null=True)
