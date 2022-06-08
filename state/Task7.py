from .models import Product

Product = Product.objects.create(
    product_name="eva",
    product_category="soap",
    price="100"
)


Product = Product.objects.all()

Product = Product.objects.filter(name="eva")


product = Product.objects.get(id=1)

Product = Product.objects.get(id=2)
product.price = "100"
Product.save()
