from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from main.models import Product
from main.forms import ProductForm

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    product_list = Product.objects.all()
    filter_type = request.GET.get('filter', 'all')
    category = request.GET.get("category")

    if filter_type == 'all':
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    if category and category != "all":
        product_list = product_list.filter(category=category)

    context = {
        'app_name' : 'Tendhang',
        'npm' : '2406351024',
        'name': request.user.username,
        'class': 'PBP E',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'categories': Product.CATEGORY_CHOICES,  
    }

    return render(request, "main.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,    
            'category': product.category,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'stock': product.stock,
            'sold': product.sold,
            'is_featured': product.is_featured,
            'size': product.size,
            'id_user': product.user.id,
        }
        for product in product_list
    ]
    return JsonResponse(data, safe=False)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,    
            'category': product.category,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'stock': product.stock,
            'sold': product.sold,
            'is_featured': product.is_featured,
            'size': product.size,
            'id_user': product.user.id,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
         return JsonResponse({'detail': 'Not found'}, status=404)

def show_xml_by_id(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        xml_data = serializers.serialize("xml", [product])
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse("Product not found", status=404)
    
def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, 'add_product.html', context)

@login_required(login_url='/login')
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product}
    return render(request, 'product_detail.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)

    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')
    context = {
        'form': form
    }
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse("main:show_main"))

@csrf_exempt
def ajax_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True, "message": "Akun berhasil dibuat!"})
        else:
            errors = [err for err_list in form.errors.values() for err in err_list]
            return JsonResponse({"success": False, "message": errors[0]})
    return JsonResponse({"success": False, "message": "Invalid request"}, status=400)

@csrf_exempt
def ajax_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = JsonResponse({"success": True, "message": "Login berhasil!"})
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            errors = [err for err_list in form.errors.values() for err in err_list]
            return JsonResponse({"success": False, "message": errors[0]})
    return JsonResponse({"success": False, "message": "Invalid request"}, status=400)

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = request.POST.get("name")
    description = request.POST.get("description")
    category = request.POST.get("category")
    price = request.POST.get("price")
    thumbnail = request.POST.get("thumbnail")
    stock = request.POST.get("stock")
    size = request.POST.get("size")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    user = request.user

    new_product = Product(
        name=name, 
        description=description,
        category=category,
        price=price,
        thumbnail=thumbnail,
        is_featured=is_featured,
        stock=stock,
        size=size,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
@login_required
def edit_product_ajax(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=product_id, user=request.user)

        product.name = request.POST.get("name")
        product.description = request.POST.get("description")
        product.category = request.POST.get("category")
        product.price = request.POST.get("price") or 0
        product.thumbnail = request.POST.get("thumbnail", "")
        product.stock = request.POST.get("stock") or 0
        product.size = request.POST.get("size", "")
        product.is_featured = request.POST.get("is_featured") == "on"

        product.save()

        return JsonResponse({
            "status": "success",
            "message": "Product updated successfully!"
        })

    return JsonResponse({
        "status": "error",
        "message": "Invalid request method."
    }, status=400)

def delete_product_ajax(request, product_id):
    try:
        product = get_object_or_404(Product, id=product_id)
        product.delete()
        
        return JsonResponse({'status': 'success', 'message': f'Produk berhasil dihapus.'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': f'Gagal menghapus: {e}'}, status=400)