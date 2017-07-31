from django.views import generic
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.mail import send_mail

from urun.forms import CommentForm, ContactForm
from urun.models import Product, Vendor, Comment


class VendorCreate(CreateView):
    model = Vendor
    fields = ['name']


class ProductCreate(CreateView):
    model = Product
    fields = ['vendor', 'name', 'description', 'image', 'price', 'performance', 'design']

class ProductUpdate(UpdateView):
    model = Product
    fields = ['vendor', 'name', 'description', 'image', 'price', 'performance', 'design']
    template_name = 'urun/product_form_update.html'

class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('Anasayfa')
    template_name = 'urun/product_form_delete.html'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class CommentCreate(CreateView):
    form_class = CommentForm
    template_name = "urun/comment_form.html"
    def get_form_kwargs(self):
        form_veri = super().get_form_kwargs()
        if self.request.method in ["POST", "PUT"]:
            kullanici_veri = form_veri["data"].copy()
            kullanici_veri["product"] = self.kwargs["pk"]
            form_veri["data"] = kullanici_veri
        return form_veri


class AnasayfaView(generic.ListView):
    model = Product

class SssView(generic.TemplateView):
    template_name = "urun/sss.html"

class ProductDetailView(generic.DetailView):
    model = Product

class ContactFormView(generic.FormView):
    form_class = ContactForm
    template_name = "urun/contact.html"
    success_url = "/"

    def form_valid(self, form):
        data = form.cleaned_data
        from django.conf import settings
        send_mail("Oneriyorum ContactForm : {}".format(data["title"]),
                "Sistemden size gelen bir mesaj var\n---\n{}\n---\neposta: {}\nip: {}".format(data["content"], data["email"], self.request.META["REMOTE_ADDR"]),
                settings.DEFAULT_FROM_EMAIL,
                ["sahinelif.mail@gmail.com"])
        return super().form_valid(form)



