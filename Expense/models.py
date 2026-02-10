from django.db import models

# Create your models here.
class Expanse(models.Model):
    title=models.CharField(max_length=60)
    amount=models.FloatField()
    transaction_type=models.CharField(choices=(('Credit','Credit'),('Debit','Debit')))

    def save(self,*args ,**kwargs):
        if self.transaction_type=='Debit':
            self.amount=self.amount*-1
        return super().save( *args ,**kwargs)

