from django.db import models

class Library(models.Model):

  title = models.CharField(max_length=50)
  address = models.CharField(max_length=50)
  
  class Meta:
    verbose_name = ("Library")
    verbose_name_plural = ("libraries")

  def __str__(self):
    return self.verbose_name

  def get_absolute_url(self):
    return reverse("library_detail", kwargs={"pk": self.pk})

