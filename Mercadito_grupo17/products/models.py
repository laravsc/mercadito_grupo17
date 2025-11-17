from django.conf import settings
from django.db import models
from django.utils.text import slugify

class Product(models.Model):
    SALE = "sale"
    EXCHANGE = "exchange"
    TYPE_CHOICES = [
        (SALE, "Venta"),
        (EXCHANGE, "Intercambio"),
    ]

    SIZE_S = "S"
    SIZE_M = "M"
    SIZE_L = "L"
    SIZE_XL = "XL"
    TALLE_CHOICES = [
        (SIZE_S, "S"),
        (SIZE_M, "M"),
        (SIZE_L, "L"),
        (SIZE_XL, "XL"),
    ]

    title = models.CharField("Título", max_length=200)
    slug = models.SlugField("Slug", max_length=220, unique=True, blank=True)
    description = models.TextField("Descripción", blank=True)
    price = models.DecimalField("Precio", max_digits=10, decimal_places=2, null=True, blank=True)
    type = models.CharField("Tipo", max_length=20, choices=TYPE_CHOICES, default=SALE)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="products", null=True, blank=True)
    
    # nuevo campo talle (size)
    talle = models.CharField("Talle", max_length=10, choices=TALLE_CHOICES, blank=True, null=True)

    # imagen principal (opcional)
    main_image = models.ImageField("Imagen principal", upload_to="products/main/", null=True, blank=True)

    is_active = models.BooleanField("Activo", default=True)
    created_at = models.DateTimeField("Creado", auto_now_add=True)
    updated_at = models.DateTimeField("Actualizado", auto_now=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        # autogenerar slug básico si no existe
        if not self.slug:
            base = slugify(self.title)[:200]
            slug = base
            i = 1
            from django.db.models import Q
            while Product.objects.filter(slug=slug).exists():
                slug = f"{base}-{i}"
                i += 1
            self.slug = slug
        super().save(*args, **kwargs)