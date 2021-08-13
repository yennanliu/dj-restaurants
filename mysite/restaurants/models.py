from django.db import models


# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        """
        :returns: name string
        """
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=3, decimal_places=0)
    comment = models.CharField(max_length=50, blank=True)
    is_spicy = models.BooleanField(default=False)
    # after django 2x, for FK, 1 to 1, we need add on_delete
    # https://www.itread01.com/content/1545016715.html
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __unicode__(self):
        """
        :returns: name string
        """
        return self.name

    class Meta:

        """Meta: attribute, options"""

        ordering = ['price']

class Comment(models.Model):
    content = models.CharField(max_length=255)
    visitor = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    class Meta:
        permissions = (
            ("can_comment", "Can comment"),
        )
