from django.db import models

# Create your models here.

class Order(models.Model):
    subtotal = models.DecimalField(max_digits=16, decimal_places=2)
    total = models.DecimalField(max_digits=16, decimal_places=2)
    shipping = models.DecimalField(max_digits=16, decimal_places=2)
    user = models.ForeignKey(
        'account.Account',
        related_name = 'order',
        on_delete = models.SET_NULL,
        null=True,
        blank=True
    )
    is_done = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Order'

    
    def __str__(self) -> str:
        return f"{self.user.email} - {self.total}"