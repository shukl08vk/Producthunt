from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=255)
    pub_date=models.DateTimeField()
    body=models.TextField()
    url=models.TextField()
    image=models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    votes_total = models.IntegerField(default=1)
    hunter=models.ForeignKey(User,on_delete=models.CASCADE)
    users = models.ManyToManyField(User,related_name='vote_count')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    
class ProdComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comments= models.TextField()
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    prod=models.ForeignKey(Product,on_delete=models.CASCADE)
    parent=models.ForeignKey('self', on_delete= models.CASCADE, null=True)
    timestamp= models.DateTimeField(default=now)

    def __str__(self):
        return self.comments[0:13]+'... '+ 'by '+ self.user.username


