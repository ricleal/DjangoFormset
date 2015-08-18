from django.db import models
from django.core.urlresolvers import reverse

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        '''
        Once a musician is created get his detail!
        '''
        return reverse('app1:detailmusician', kwargs={'pk': self.pk})

class Album(models.Model):
    STARS = (
        (1, '*'),
        (2, '**'),
        (3, '***'),
        (4, '****'),
        (5, '*****'),
    )
    stars = dict(STARS)

    artist = models.ForeignKey(Musician)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField(choices=STARS)

    def __str__(self):
        return str(self.artist) + " - " + self.name + ' (' + self.stars[self.num_stars] + ')'

    def get_absolute_url(self):
        '''
        Once a musician is created get his detail!
        '''
        return reverse('app1:detailalbum', kwargs={'pk': self.pk})
