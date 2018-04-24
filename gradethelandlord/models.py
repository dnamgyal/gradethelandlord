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
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('F', 'F'),
        )

        SATISFACTORY = (
        ('Very dissatisfied', 'Very dissatisfied'),
        ('Somewhat dissatisfied', 'Somewhat dissatisfied'),
        ('Neither satisfied nor dissatisfied', 'Neither satisfied nor dissatisfied'),
        ('Somewhat satisfied', 'Somewhat satisfied'),
        ('Very satisfied', 'Very satisfied'),
        )

        HELPFUL = (
        ('Not at all helpful', 'Not at all helpful'),
        ('Not so helpful', 'Not so helpful'),
        ('Somewhat helpful', 'Somewhat helpful'),
        ('Very helpful', 'Very helpful'),
        ('Extremely helpful', 'Extremely helpful'),
        )

        YES_NO = (
        ('Yes', 'Yes'),
        ('No', 'No'),)

        STAY = (
        ('Less than 6 months', 'Less than 6 months'),
        ('6 months', '6 months'),
        ('10 months', '10 months'),
        ('12 months', '12 months'),
        ('More than a year', 'More than a year'),
        )

        AGREE = (
        ('Strongly disagree', 'Strongly disagree'),
        ('Disagree', 'Disagree'),
        ('Neutral', 'Neutral'),
        ('Agree', 'Agree'),
        ('Strongly agree', 'Strongly agree'),
        )

        user_name = models.CharField(max_length=100)
        pub_date = models.DateField('date published')

        landlord = models.ForeignKey(Landlord)
        address = models.CharField(max_length=200, blank=False, default="")
        length_of_stay = models.CharField(max_length=20, choices=STAY, blank=False)

        move_in_condition = models.CharField(max_length=5, choices=SATISFACTORY, blank=False, default="1")
        apartment_condition = models.CharField(max_length=5, choices=SATISFACTORY, blank=False, default="1")
        maintenance_efficiency = models.CharField(max_length=5, choices=SATISFACTORY, blank=False, default="1")

        treatment_by_your_landlord = models.CharField(max_length=5, choices=SATISFACTORY, blank=False, default="1")
        communication_with_your_landlord = models.CharField(max_length=5, choices=SATISFACTORY, blank=False, default="1")
        landlord_helpfulness = models.CharField(max_length=5, choices=HELPFUL, blank=False, default="1")

        overall_rating = models.CharField(max_length=5, choices=RATING_CHOICES, blank=False, default="1")
        rent_again = models.CharField(choices=YES_NO, max_length=5, blank=False, default="1")
        additional_comments = models.CharField(max_length=1000, blank=True, null=True)
