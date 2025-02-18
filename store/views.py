from django.shortcuts import render
from .models import Category,Product,ProductImage,Order
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from .forms import ContactForm,OrderForm
from django.core.mail import send_mail
from django.conf import settings




# Create your views here.
def home(request):
    products = Product.objects.all()
    return render (request,'khorshani/home.html', {'products':products});

def product(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'khorshani/product.html', {'categories': categories,'products': products},)

def product_list(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = category.products.all()  # Uses the related_name 'projects'
    return render(request, 'khorshani/category_detail.html', {'category': category, 'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    images = product.images.all()  # Uses the related_name 'images'
    return render(request, 'khorshani/productdetail.html', {'product': product, 'images': images})


def ingrediant(request):
    return render(request, 'khorshani/ingrediant.html')
def recipe(request):
    return render(request, 'khorshani/recipe.html')
def about(request):
    return render(request, 'khorshani/about.html')
def contact(request):
    return render(request, 'khorshani/contact.html')

def contactc(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()

            # Get the form data to send in the email
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            description = form.cleaned_data['description']
            
            # Compose the email content
            subject = f'New Contact Message from {name}'
            message = f"Name: {name}\nEmail: {email}\nPhone: {mobile}\nMessage: {description}"
            recipient_email = 'najus777@gmail.com'  # Replace with the recipient's email address
            
            try:
                # Send the email using Django's send_mail function
                send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient_email])

                # Redirect to success page or any other appropriate page
                return redirect('store:messagesuccess')  # You can change 'Warzone:success' to your actual success URL
            except Exception as e:
                # Handle any errors that occur while sending the email
                print(f"Error sending email: {e}")
                return render(request, 'khorshani/contact.html', {'form': form, 'error': 'There was an error sending the email. Please try again.'})

    else:
        form = ContactForm()

    return render(request, 'khorshani/contact.html', {'form': form})
def success(request):
    return render(request, 'khorshani/success.html')
def messagesuccess(request):
    return render(request, 'khorshani/messagesuccess.html')

def order_page(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Associate the product with the order
            order = form.save(commit=False)
            order.product = product
            order.save()
            return redirect('store:success')  # Redirect to the order confirmation page
    else:
        form = OrderForm()

    return render(request, 'khorshani/order.html', {'form': form, 'product': product})





