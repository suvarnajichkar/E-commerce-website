from django.db import models
# Create your models here.

class Category(models.Model):
	category_name = models.CharField(max_length=100)
	category_desc = models.TextField(blank=True,null=True)

	def __str__(self):
		return self.category_name


class SubCategory(models.Model):
	category_name =  models.ForeignKey(to=Category,on_delete=models.CASCADE)
	subcategory_name = models.CharField(max_length=100)
	subcategory_desc = models.TextField(blank=True,null=True)

	def __str__(self):
		return self.subcategory_name


class Product(models.Model):
	category_name =  models.ForeignKey(to=Category,on_delete=models.CASCADE)
	SubCategory_name =  models.ForeignKey(to=SubCategory,on_delete=models.SET_NULL, null=True)
	product_name = models.CharField(max_length=100)
	product_desc = models.TextField(blank=True,null=True)
	price = models.IntegerField()
	stock_quantity = models.IntegerField()
	images = models.ImageField(upload_to= 'images/')

	def __str__(self):
		return self.product_name









