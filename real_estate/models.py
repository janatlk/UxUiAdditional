from django.db import models

class Companies(models.Model):
    title = models.CharField(max_length=67)
    logo = models.ImageField(
        upload_to='logos'
    )
    description = models.TextField()
    def __str__(self):
        return self.title

class Property(models.Model):
    company_linked = models.ForeignKey(Companies, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
class Image(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return f"Image for {self.property.title}"