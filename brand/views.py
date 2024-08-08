from django.shortcuts import render,redirect
from django.views import View
from.models import*

# Create your views here.
class CategoryView(View):
	def get(self,request):
		categoryobj= Category.objects.all()
		return render (request,'category.html',{'categoryobj':categoryobj})
	
	def post(self,request):
		category_name = request.POST.get('category_name')
		category_desc =request.POST.get('category_desc')

		Category.objects.create(category_name=category_name,
								category_desc=category_desc)
		return redirect('/')

class CategoryUpdate(View):
	def get(self,request,id=None):
		categoryobj = Category.objects.get(id=id)
		return render(request,'editcategory.html',{'categoryobj':categoryobj})
	
	def post(self,request,id):
		category_name = request.POST.get('category_name')
		category_desc =request.POST.get('category_desc')

		categoryobj = Category.objects.get(id=id)
		
		categoryobj.category_name=category_name
		categoryobj.category_desc=category_desc
		categoryobj.save()
		return redirect('/')

class CategoryDelete(View):
	def get(self,request,id=None):
		
		return render(request,'category.html')
	def post(self,request,id=None):
		categoryobj= Category.objects.get(id=id)
		categoryobj.delete()
		return redirect('/')

class SubcategoryView(View):
    def get(self, request, id=None):
        categoryobj = Category.objects.get(id=id)
        subcategoryobj = SubCategory.objects.filter(category_name=categoryobj)
        return render(request, 'subcategory.html', {'categoryobj': categoryobj, 'subcategoryobj': subcategoryobj})

    def post(self, request, id=None):
					subcategory_name = request.POST.get('subcategory_name')
					subcategory_desc = request.POST.get('subcategory_desc')
					categoryobj = Category.objects.get(id=id)
					SubCategory.objects.create(
						category_name=categoryobj,
						subcategory_name=subcategory_name,
						subcategory_desc=subcategory_desc
						)
					return redirect(f'/subcategory/{id}/')
 
class Subcategoryupdate(View):
	def get(self,request,id=None):
		subcategoryobj=SubCategory.objects.get(id=id)
		return render(request,'editsubcategory.html',{'subcategoryobj':subcategoryobj})
	
	def post(self,request,id=None):
		subcategory_name = request.POST.get('subcategory_name')
		subcategory_desc = request.POST.get('subcategory_desc')
		subcategoryobj = SubCategory.objects.get(id=id)
		subcategoryobj.subcategory_name=subcategory_name
		subcategoryobj.subcategory_desc=subcategory_desc
		subcategoryobj.save()
		return redirect(f'/subcategory/{subcategoryobj.category_name.id}')
	
class Subcategorydelete(View):
	def get(self,request):
		return render(request,'subcategory.html')
	
	def post(self,request,id=None):
		subcategoryobj = SubCategory.objects.get(id=id)
		subcategoryobj.delete()
		return redirect(f'/subcategory/{subcategoryobj.category_name.id}')
	
class ProductView(View):
	def get(self,request,id=None):
		subcategoryobj = SubCategory.objects.get(id=id)
		productobj = Product.objects.filter(SubCategory_name = subcategoryobj)
		return render(request,'product.html',{'subcategoryobj':subcategoryobj,'productobj':productobj})
	
	def  post(self,request,id=None):
		product_name = request.POST.get('product_name')
		product_desc = request.POST.get('product_desc')
		price = request.POST.get('price')
		stock_quantity = request.POST.get('stock_quantity')
		images = request.FILES.get('images')
		subcategoryobj= SubCategory.objects.get(id=id)
		categoryobj =  subcategoryobj.category_name

		Product.objects.create( SubCategory_name=subcategoryobj,
						 category_name=categoryobj,
						 product_name = product_name,
						 product_desc = product_desc,
						 images=images,
						 price =price,
						 stock_quantity=stock_quantity)
		return redirect(f'/product/{id}/')

class Productupdate(View):
    def get(self, request, id=None):
        productobj = Product.objects.get(id=id)
        return render(request, 'editproduct.html', {'productobj': productobj})
    
    def post(self, request, id=None):
					product_name = request.POST.get('product_name')
					product_desc = request.POST.get('product_desc')
					price = request.POST.get('price')
					stock_quantity = request.POST.get('stock_quantity')
					images = request.FILES.get('images')

					productobj = Product.objects.get(id=id)
					productobj.product_name = product_name
					productobj.product_desc = product_desc
					productobj.price = price
					productobj.stock_quantity = stock_quantity
					productobj.images = images
					
					productobj.save()
					return redirect(f'/product/{productobj.SubCategory_name.id}')


	
class Productdelete(View):
	def get(self,request,id=None):
		return render(request,'product.html')
	
	def post(self,request, id=None):
		productobj = Product.objects.get(id=id)
		productobj.delete()
		return redirect(f'/product/{productobj.SubCategory_name.id}')


					
					
					
					


					






		
		


					




		

