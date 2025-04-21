from django.db import models

# Create your models here.
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    campus_id = models.IntegerField(default="", blank=True, null=False)

    # Creates model manager
    object = models.Manager()

    # Displays the object output values in the form of a string otherwise, it will just have generic campus
    def __str__(self):
        # Returns the input value of the title and instructor name
        # Field as a tuple to display in the browser instead of the default titles
        display_course = '{0.campus_name}: {0.campus_id}'.format(self)
        return display_course.format(self)


    # This is here to make sure the plural of campus comes out correctly on the screen
    class Meta:
        verbose_name_plural = "University Campuses"