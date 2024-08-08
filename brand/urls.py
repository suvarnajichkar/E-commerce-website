from django.urls import path

from brand.views import *

urlpatterns = [
	# category
	path('',CategoryView.as_view(),name='category'),
	path('categoryupdate/<int:id>/',CategoryUpdate.as_view(),name='categoryupdate'),
	path('categorydelete/<int:id>/',CategoryDelete.as_view(),name='categorydelete'),

	# Subcategory
	path('subcategory/<int:id>/',SubcategoryView.as_view(),name='subcategory'),
	path('updatesubcategory/<int:id>',Subcategoryupdate.as_view(),name="updatesubcategory"),
	path('deletesubcategory/<int:id>',Subcategorydelete.as_view(),name='deletesubcategory'),

	# product
	path('product/<int:id>/',ProductView.as_view(),name='product'),
	path('updateproduct/<int:id>/',Productupdate.as_view(),name='updateproduct'),
	path('delteteproduct/<int:id>/',Productdelete.as_view(),name='deleteproduct'),
		
]
