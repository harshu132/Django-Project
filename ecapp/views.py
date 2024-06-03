from django.db.models import Count
from django.shortcuts import render
from django.views import View
from . models import Product,Customer
from . forms import CustomerProfileForm, CustomerRegistrationForm
from django.contrib import messages

from django.views.generic import TemplateView

class ProfileView(TemplateView):
    template_name = 'ecapp/profile.html'

def home(request):
    # Logic for the home view
    return render(request, 'ecapp/home.html')

def about(request):
    # Logic for the home view
    return render(request, 'ecapp/about.html')

def contact(request):
    # Logic for the home view
    return render(request, 'ecapp/contact.html')

class CategoryView(View):
    def get(self, request,val):
       product = Product.objects.filter(category=val)
       title = Product.objects.filter(category=val).values('title')
       return render(request, 'ecapp/category.html',locals())
    
class CategoryTitle(View):
    def get(self, request,val):
       product = Product.objects.filter(title=val)
       title = Product.objects.filter(category=product[0].category).values('title')
       return render(request, 'ecapp/category.html',locals())    

class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,"ecapp/productdetail.html",locals())


class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request, 'ecapp/customerregistrstion.html',locals())
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations! User Register Successfully")
        else:
            messages.error(request,"Invalid Input Data")
        return render(request,'ecapp/customerregistrstion.html',locals())  

class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request, 'ecapp/profile.html',locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer(user=user,name=name,locality=locality,mobile=mobile,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,"Congratulations!  Your Profile Save Successfully")
        else:
            messages.warning(request,"Invalid Input Data")    
        return render(request, 'ecapp/profile.html',locals())          
    
def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'ecapp/address.html',locals())    