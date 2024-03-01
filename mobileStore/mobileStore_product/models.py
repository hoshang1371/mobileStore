from django.db import models
import os
from extentions.images import make_thumbnail, make_thumbnail_vue
from django.db.models import Q

from mobileStore_product_category.models import ProductCategory
# from mobileStore_product.models import Product
# from django.contrib.auth.models import User
# from mobileStore_Social.models import User

from django.core.validators import MinValueValidator, MaxValueValidator

from django.contrib.auth import get_user_model

User = get_user_model()

from django.db.models import Avg
from django.conf import settings

from django_jalali.db import models as jmodels
from django.utils.timezone import now


import pytz
import jdatetime

import convert_numbers
from extentions.time import getDuration

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"

def upload_mobile_image_tumpnail_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products\\tumpnail\\{final_name}"

def upload_vue_image_tumpnail_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products\\tumpnail_vue\\{final_name}"

def upload_gallery_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/galleries/{final_name}"

class ProductsManager(models.Manager):
    def get_active_products(self):
        return self.get_queryset().filter(active=True)

    def get_products_by_category(self ,category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name ,active=True)

    def get_by_id(self, product_id):
        qs = self.get_queryset().filter(id=product_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def search(self,query):
        lookup = (
                    Q(title__icontains=query) | 
                    Q(description__icontains=query)|
                    Q(tag__title__icontains=query))
        return self.get_queryset().filter(lookup, active=True).distinct()
    

class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    code = models.CharField(max_length=150, verbose_name='کد')
    place = models.CharField(max_length=150, verbose_name='مکان کالا', null=True, blank=True)
    number = models.CharField(max_length=150, verbose_name='تعداد', null=True, blank=True)
    brand = models.CharField(max_length=150, verbose_name='برند', null=True, blank=True)
    description = models.TextField(verbose_name='توضیحات')
    smallDescription = models.TextField(max_length=150,verbose_name='کوتاه توضیحات')
    price = models.IntegerField(verbose_name='قیمت')
    priceOff = models.IntegerField(verbose_name='قیمت تخفیف', null=True, blank=True)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر')
    mobile_image_tumpnail = models.ImageField(upload_to= upload_mobile_image_tumpnail_path, null=True, blank=True, verbose_name='تصویر_بند_انگشتی')
    thumbnail = models.ImageField(upload_to='upload/', blank=True, null=True)
    active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')
    categories = models.ManyToManyField(ProductCategory, blank =True, verbose_name='دسته بندی ها')
    visit_count = models.IntegerField(default=0, verbose_name='تعداد بازدید ها')
    vige = models.BooleanField(default=False, verbose_name='ویژه / غیرویژه')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    # slug = models.SlugField()

    # similars = models.ManyToManyField(Product)

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/products/{self.id}/{self.title.replace(' ', '-')}"
    
    def get_image(self):
        if self.image:
            # return 'http://127.0.0.1:8000' + self.image.url
            return settings.ALLOWED_HOSTS[0] + self.image.url
        return ''
    
    # def get_thumbnail(self):
    #     if self.mobile_image_tumpnail:
    #         return 'http://127.0.0.1:8000' + self.mobile_image_tumpnail.url
    #     else:
    #         if self.image:
    #             make_thumbnail(self.mobile_image_tumpnail, self.image, (50, 50), 'thumb')
    #             # self.mobile_image_tumpnail = self.make_thumbnail(self.image)
    #             self.save()


    #             return 'http://127.0.0.1:8000' + self.mobile_image_tumpnail.url
    #         else:
    #             return ''

    #! change url    
    def get_thumbnail(self):
        if self.thumbnail:
            # return 'http://127.0.0.1:8000' + self.thumbnail.url
            return settings.ALLOWED_HOSTS[0] + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = make_thumbnail_vue(self.image)
                self.save()

                # return 'http://127.0.0.1:8000' + self.thumbnail.url
                return settings.ALLOWED_HOSTS[0] + self.thumbnail.url
            else:
                return ''


    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        # print(f"image : {self.image}")
        make_thumbnail(self.mobile_image_tumpnail, self.image, (50, 50), 'thumb')
        super(Product, self).save(*args, **kwargs)

    @property
    def no_of_ratings(self):
        sum=0
        ratings = Rating.objects.filter(product=self)
        return len(ratings)

    @property
    def avg_rating(self):
        sum=0
        ratings = Rating.objects.filter(product=self)
        for rating in ratings:
            sum=sum+rating.stars

        if len(ratings)>0:
            return sum/len(ratings)
        else:
            return 0

    def __str__(self):
        return self.title
    
    def int_average_rating(self) -> int:
        return int(Rating.objects.filter(product=self).aggregate(Avg("stars"))["stars__avg"] or 0)
    
    def float_average_rating(self) -> float:
        return (Rating.objects.filter(product=self).aggregate(Avg("stars"))["stars__avg"] or 0)%1
    
    # def get_like(self) -> int:
    #     print("kiri")
    #     return Likes.objects.filter(product=self)

class ProductGallery(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    image = models.ImageField(upload_to=upload_gallery_image_path, verbose_name='تصویر')
    product = models.ForeignKey(Product,on_delete=models.CASCADE, verbose_name='محصول')

    class Meta:
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصاویر'

    def __str__(self):
        return self.title


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    class Meta:
        verbose_name = 'ستاره'
        verbose_name_plural = 'ستاره ها'

    def __str__(self):
        return f"{self.product.title}: {self.stars}"
    
class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    likes = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('user', 'product',)
        verbose_name = 'پسندیدن'
        verbose_name_plural = 'پسندیدن'


class CustomerComment(models.Model):

    CommentProduct = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول پیام')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر پیام')

    parent = models.ForeignKey(
        'self', 
        default=None, 
        null=True, 
        blank=True,
        on_delete=models.CASCADE,
        related_name='replies', 
        verbose_name='زیر دسته')
    # parent = models.OneToOneField('self', default=None, null=True, blank=True, on_delete=models.CASCADE,related_name='children', verbose_name='زیر دسته')

    # subject = models.CharField(max_length=200 , verbose_name='عنوان پیام',
    #                             null=True, blank=True)
    text = models.TextField(verbose_name='متن پیام',
                            null=True, blank=True)
    
    # created = models.DateTimeField(auto_now_add=True) 
    # updated = models.DateTimeField(auto_now=True) 

    # created = jmodels.jDateTimeField(default=now,blank = True, null = True, verbose_name='تاریخ ایجاد سبد شمسی')

    created = jmodels.jDateTimeField(auto_now_add=True,blank = True, null = True, verbose_name='تاریخ ایجاد پیام شمسی')
    updated = jmodels.jDateTimeField(auto_now=True,blank = True, null = True, verbose_name='تاریخ تغییر پیام شمسی')

    is_ok = models.BooleanField(verbose_name='تایید شده / نشده' ,default=False)

    # ansewerText = models.TextField(verbose_name='پاسخ متن پیام',
    #                        null=True, blank=True)

    def time_calc(self):
        now = jdatetime.datetime.utcnow().replace(tzinfo=pytz.timezone('Asia/Tehran')) 
        return getDuration(self.updated, now)

    def like_comment_calc(self):
        numberLikeC =LikesCustomerComment.objects.filter(CustomerComment_id=self.id,CustomerComment__CommentProduct_id=self.CommentProduct.id,likes=True).count()
        return(convert_numbers.english_to_persian(str(int(numberLikeC))))
    
    def is_liked(self):
        isLiked =LikesCustomerComment.objects.filter(CustomerComment_id=self.id,CustomerComment__CommentProduct_id=self.CommentProduct.id,likes=True).count()
        return(convert_numbers.english_to_persian(str(int(isLiked))))
    
        # return f"{now-self.updated}".replace("days", "روز")

        # Date = str(now-self.updated).split('.')
        # Date =Date[0].split(',')
        # Date= convert_numbers.english_to_persian(str(Date))
        # print(self.updated)
        # day = Date[0]
        # time = Date[1]
        # print(f"finalDate={Date[0]}")getDuration
        # print((now-self.updated).days)

        # print(getDuration(self.updated, now))

    
    class Meta:
        verbose_name = ' نظرات کاربران '
        verbose_name_plural='نظرات در مورد کالا کاربران'

    def __str__(self):
        return self.text
    

class LikesCustomerComment(models.Model):
    # TODO: nyazi be user nadare
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    CustomerComment = models.ForeignKey(CustomerComment, on_delete=models.CASCADE)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE) CommentProduct
    likes = models.BooleanField(default=False)


    # def like_comment_calc(self):
    #     return("koko")
    
    class Meta:
        unique_together = ('user', 'CustomerComment',)
        verbose_name = 'پسندیدن نظرات'
        verbose_name_plural = 'پسندیدن نظرات'