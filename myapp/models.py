from django.db import models
from django.utils import timezone
class LayoutDetals(models.Model):
    layout_name = models.CharField(max_length=100)
    layout_image = models.ImageField(upload_to='layout_images/')

    def __str__(self):
        return self.layout_name

class TableDetails(models.Model):
    binserial_no = models.CharField(max_length=100)
    bin_location = models.CharField(max_length=100)
    projectname = models.CharField(max_length=100)
    component1 = models.CharField(max_length=100)  
    component2 = models.CharField(max_length=100)
    testing = models.CharField(max_length=100)
    remarks = models.CharField(max_length=100)
    employeecode = models.CharField(max_length=100)
    layout = models.ForeignKey(LayoutDetals, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return f"{self.binserial_no} - {self.projectname} ({self.layout.layout_name})"
