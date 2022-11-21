from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Create your models here.
class provider(models.Model):
    name  = models.CharField(max_length=200)
    info = models.TextField()

class productType(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

class Product(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=9)
    type = models.ForeignKey('productType', related_name='type', blank=True, on_delete=  models.CASCADE,) # we set blank = True but eventually we would unset it
    provider = models.ForeignKey('provider', on_delete = models.CASCADE, related_name='provider', blank=True) # we set blank = True but eventually we would unset it
    # image = models.ImageField(upload_to='products', blank=True) needs to install Pillow

class Cart(models.Model):
    # def __init__(self, request, *args, **kwargs) -> None:
    #     #user = Token.objects.get(key='token string').user to make it more secure we could check if the user that creates the cart is the same that it is being passed to the cart
    #     self.user = request.user 
    #     #request.auth
    #     super().__init__(*args, **kwargs)
    creation_date = models.DateTimeField(verbose_name=('creation date'), auto_now=True)
    checked_out = models.BooleanField(default=False, verbose_name= ('checked out'))
    class Meta:
        verbose_name = ('cart')
        verbose_name_plural = ('carts')
        ordering = ('-creation_date',)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def add(self, product, amount = 1):
        item,_ = CartItem.objects.get_or_create(product = product)
        item.quantity =+1
        price = product.price
        self.total += price * amount
        items = self.item.all()
        return item.all(), self.total
        
    def create(cls, user):
        cart = cls(user=user)
        # do something with the book
        return cart

    def remove(self, product, amount = 1):
        item = CartItem.objects.fiter(product = product)
        if item:
            item.quantity =-1
            if item.quantity <= 0:
                CartItem.objects.fiter(product = product).delete()
        price = product.price
        self.total -= price * amount
        items = self.item.all()
        return items, self.total



class CartItem(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='item')

