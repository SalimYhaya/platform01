from django.db import models
from django.contrib.auth.models import User

# موديل الشركة
class Company(models.Model):
    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=10, unique=True) # مثل AAPL أو TSLA
    current_price = models.FloatField()

# موديل التنبيه
class PriceAlert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    target_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
