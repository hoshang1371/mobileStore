from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import RegexValidator

from django_jalali.db import models as jmodels
from django.utils.timezone import now

from mobileStore_order.models import Order
from django.contrib.auth import get_user_model

User = get_user_model()

class PostPrice(models.Model):
    title = models.CharField(max_length=150, verbose_name='هزینه ارسال ')
    price = models.IntegerField(verbose_name='هزینه ی پست')

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'هزینه ارسال'

class PostAddress(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(verbose_name='آدرس')
    post_code = models.CharField(max_length=20,verbose_name='کد پستی')


    class Meta:
        verbose_name = 'اطلاعات پست'
        verbose_name_plural = 'اطلاعات پست'

    def __str__(self):
        return self.owner.get_full_name()
    
Carrier_CHOICES = (
    ('1','پست'),
    ('2','تیپاکس'),
    ('3','باربری'),
)  
    
class PostAddressDetail(models.Model):
    # ToDO: شاید باید نال پذیر باشد در اردر دیتیل سبد خرید ساخته میشود بون نوع حمل
    carrierDetails = models.CharField(max_length=20, choices=Carrier_CHOICES, default=1, verbose_name='روش ارسال')
    #! 
    PostPriceSelected = models.ForeignKey(PostPrice,blank = True, null = True, on_delete=models.CASCADE, verbose_name=' هزینه ارسال انتخابی ')
    trackingNumber = models.CharField(max_length=20,blank = True, null = True,verbose_name='شماره پیگیری')
    addressSelected = models.ForeignKey(PostAddress, on_delete=models.CASCADE, verbose_name=' آدرس انتخابی ')
    OrderDetailSelected = models.OneToOneField(Order, on_delete=models.CASCADE, verbose_name=' سبد خرید انتخابی  ')
    isResive = models.BooleanField(default=False)

    carried = jmodels.jDateTimeField(blank = True, null = True, verbose_name='تاریخ حمل شده')
    sentToShippingUnit = jmodels.jDateTimeField(blank = True, null = True, verbose_name='تاریخ ارسال شده به واحد حمل')
    collected = jmodels.jDateTimeField(blank = True, null = True, verbose_name='تاریخ جمع آوری شده')
    collecting = jmodels.jDateTimeField(blank = True, null = True, verbose_name='تاریخ در حال جمع اوری')
    Ongoing = jmodels.jDateTimeField(blank = True, null = True, verbose_name='تاریخ در دست اقدام')
    processing = jmodels.jDateTimeField(blank = True, null = True, verbose_name='تاریخ در حال پردازش')
    confirmedPayment = jmodels.jDateTimeField(blank = True, null = True, verbose_name='تاریخ پرداخت تایید شده')

    class Meta:
        verbose_name = 'اطلاعات آدرس انتخابی'
        verbose_name_plural = 'اطلاعات آدرس'

    def __str__(self):
        return self.addressSelected.address

# payment_METHOD= (
#     ('1','پرداخت توسط فیش بانکی'),
#     ('2','زرین پال'),
# )
payment_METHOD= (
    ('1','پرداخت توسط فیش بانکی'),
    ('2','زرین پال'),
)

# code_regex = RegexValidator(regex=r'^\d{25}$')
code_regex = RegexValidator(regex=r'^\d{10}$')

class PaymentMethodeDetail(models.Model):
    OrderDetailSelected = models.OneToOneField(Order, on_delete=models.CASCADE, verbose_name=' سبد خرید انتخابی انتخابی ')
    PaymentDetails = models.CharField(max_length=20, choices=payment_METHOD, default=1, verbose_name='روش پرداخت')
    isTermsAndRules = models.BooleanField(default=False, verbose_name=' پذیرفتن شرایط ')
    # TermsAndRules_field = models.TextField(blank = True, null = True, verbose_name=' شرایط ')
    # peymentCode = models.CharField(validators=[code_regex],max_length=150, verbose_name=' کد پرداخت ',blank=True,null=True)
    peymentCode = models.CharField(max_length=150, verbose_name=' کد پرداخت ',blank=True,null=True)
    peymentDate = jmodels.jDateTimeField(blank = True, null = True, verbose_name='تاریخ پرداخت')

    # payment_tracking_number =models.CharField(validators=[code_regex],max_length=25 ,null=True, blank=True,verbose_name='شماره پیگیری')

    class Meta:
        verbose_name = 'جزئیات پرداخت'
        verbose_name_plural = 'جرئیات پرداخت'