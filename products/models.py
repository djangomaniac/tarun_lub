from django.db import models
from PIL import Image


class Sulfonate(models.Model):
    CATEGORY = (
        ('Sodium Petroleum Sulfonate', 'Sodium Petroleum Sulfonate'),
        ('Calcium Petroleum Sulfonate', 'Calcium Petroleum Sulfonate'),
        ('Barium Petroleum Sulfonate', 'Barium Petroleum Sulfonate'),
    )
    title = models.CharField(max_length=500, null=True)
    description_long = models.TextField(max_length=600, null=True)
    description_short = models.TextField(max_length=150, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    image_1 = models.ImageField(upload_to="product_image/", blank=True)
    image_2 = models.ImageField(upload_to="product_image/", blank=True)
    image_3 = models.ImageField(upload_to="product_image/", blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image_1.path)
        width, height = img.size  # Get dimensions
        r_img = resize_img(img, height, width)
        r_img.save(self.image_1.path)


class IndustrialLubricant(models.Model):
    CATEGORY = (
        ('Metal Working Fluids', 'Metal Working Fluids'),
        ('Compressor Oil', 'Compressor Oil'),
        ('Rust Preventive Oil', 'Rust Preventive Oil'),
        ('Aluminium Wire Drawing Oil', 'Aluminium Wire Drawing Oil'),
        ('Hydraulic Oil', 'Hydraulic Oil'),
    )
    title = models.CharField(max_length=500, null=True)
    description_long = models.TextField(max_length=600, null=True)
    description_short = models.TextField(max_length=150, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    image_1 = models.ImageField(upload_to="product_image/", blank=True)
    image_2 = models.ImageField(upload_to="product_image/", blank=True)
    image_3 = models.ImageField(upload_to="product_image/", blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image_1.path)
        width, height = img.size  # Get dimensions
        r_img = resize_img(img, height, width)
        r_img.save(self.image_1.path)


class Textile(models.Model):
    CATEGORY = (
        ('Knitting Oil', 'Knitting Oil'),
    )
    title = models.CharField(max_length=500, null=True)
    description_long = models.TextField(max_length=600, null=True)
    description_short = models.TextField(max_length=150, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    image_1 = models.ImageField(upload_to="product_image/", blank=True)
    image_2 = models.ImageField(upload_to="product_image/", blank=True)
    image_3 = models.ImageField(upload_to="product_image/", blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image_1.path)
        width, height = img.size  # Get dimensions
        r_img = resize_img(img, height, width)
        r_img.save(self.image_1.path)


class AutomotiveLubricant(models.Model):
    CATEGORY = (
        ('Engine Oil', 'Engine Oil'),
        ('Gear Oil', 'Gear Oil'),
    )
    title = models.CharField(max_length=500, null=True)
    description_long = models.TextField(max_length=600, null=True)
    description_short = models.TextField(max_length=150, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    image_1 = models.ImageField(upload_to="product_image/", blank=True)
    image_2 = models.ImageField(upload_to="product_image/", blank=True)
    image_3 = models.ImageField(upload_to="product_image/", blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image_1.path)
        width, height = img.size  # Get dimensions
        r_img = resize_img(img, height, width)
        r_img.save(self.image_1.path)


def resize_img(img, height, width):
    if width > 300 and height > 300:
        # keep ratio but shrink down
        img.thumbnail((width, height))

    # check which one is smaller
    if height < width:
        # make square by cutting off equal amounts left and right
        left = (width - height) / 2
        right = (width + height) / 2
        top = 0
        bottom = height
        img = img.crop((left, top, right, bottom))

    elif width < height:
        # make square by cutting off bottom
        left = 0
        right = width
        top = 0
        bottom = width
        img = img.crop((left, top, right, bottom))

    if width > 300 and height > 300:
        img.thumbnail((300, 300))

    return img
