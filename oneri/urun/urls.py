from django.conf.urls import url

from urun.views import ProductDetailView, AnasayfaView, SssView, CommentCreate, ContactFormView, ProductListSearchView
from urun.views import ProductCreate, ProductUpdate, ProductDelete, VendorCreate

urlpatterns=[
    url(r"^$", AnasayfaView.as_view(), name="Anasayfa"),
    url(r"^sss$", SssView.as_view()),
    url(r'^vendor/add/$', VendorCreate.as_view(), name='vendor-add'),
    url(r'^product/add/$', ProductCreate.as_view(), name='product-add'),
    url(r'^contact/$', ContactFormView.as_view(), name='contact'),
    url(r"^product/(?P<pk>\d+)/$", ProductDetailView.as_view(), name="product-detail"),
    url(r'^product/(?P<pk>\d+)/add/', CommentCreate.as_view(), name='comment-add'),
    url(r'^product/(?P<pk>\d+)/update/$', ProductUpdate.as_view(), name='product-update'),
    url(r'^product/(?P<pk>\d+)/delete/$', ProductDelete.as_view(), name='product-delete'),
    url(r'^product/search/', ProductListSearchView.as_view(), name='product-list-search'),

]