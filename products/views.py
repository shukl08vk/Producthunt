from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, ProdComment
from django.utils import timezone


# Create your views here.
def home(request):
    products= Product.objects
    return render(request, 'products/home.html',{'products':products})

@login_required
def create(request):
    if request.method=='POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product=Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url=request.POST['url']
            else:
                product.url='https://'+request.POST['url']
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.pub_date=timezone.datetime.now()
            product.hunter=request.user
            product.save() #insert to database
            return redirect('/products/'+str(product.id))

        else:
            return render(request, 'products/create.html',{'error':'All field are required'})

    return render(request, 'products/create.html')
@login_required
def delete(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    if request.user!=product.hunter:
        return render(request,'products/detail.html',{'product':product})
    product.delete()
    messages.success(request, "Product Deleted successfully",
                     extra_tags='alert alert-success alert-dismissible fade show')
    return HttpResponseRedirect("/")
    #return render(request,'products/detail.html',{'product':product})


def detail(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    comments=ProdComment.objects.filter(prod=product)
    return render(request,'products/detail.html',{'product':product, 'comments':comments})

@login_required(login_url='/accounts/signup')
def upvote(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    product.users.add(request.user)
    product.votes_total=product.users.count()
    product.save()
    return redirect('/products/'+str(product.id))

def prodComment(request):
    if request.method=="POST": 
        comments= request.POST.get('comments')
        user= request.user
        prodtitle=request.POST.get('ptitle')
        prod=Product.objects.get(title=prodtitle)

        comments=ProdComment(comments=comments,user=user,prod=prod)
        comments.save()
        messages.success(request,'Comment successfully posted.')


    return redirect('/products/'+str(prod.id))

