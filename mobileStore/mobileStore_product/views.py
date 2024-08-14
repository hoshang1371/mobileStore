from django.shortcuts import render


from rest_framework.views import APIView
from .models import CustomerComment, Product, ProductGallery,Rating,Likes, LikesCustomerComment
from .serializers import CustomerCommentSerializer, DeleteCustomerCommentSerializer, \
                            LikesCustomerCommentSerializer, PostCustomerCommentSerializer, \
                            ProductDetailProductGallerySerializer, ProductDitailSerializer,\
                            ProductSerializer,StarSerializer,LikeSerializer,\
                            AllProductCustomerCommentSerializer
from rest_framework.response import Response
from django.db.models import Q
from django.http import Http404

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status, authentication, permissions
from django.db.models import Avg
import convert_numbers

# Create your views here.
# def index(request: HttpRequest) -> HttpResponse:
#     posts = Post.objects.all()
#     for post in posts:
#         rating = Rating.objects.filter(post=post, user=request.user).first()
#         post.user_rating = rating.rating if rating else 0 
#     return render(request, "index.html", {"posts": posts})
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,DestroyAPIView,CreateAPIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# from account.models import User

class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all().filter(active=True)[0:8]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class AllProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all().filter(active=True)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
class PopularProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all().filter(active=True).order_by('-visit_count')[0:10]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
class PopularVigeList(APIView):
    def get(self, request, format=None):
        products = Product.objects.filter(vige=True).filter(active=True)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
class priceOffList(APIView):
    def get(self, request, format=None):
        products = Product.objects.filter(~Q(priceOff__isnull=True)).filter(active=True)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
class ProductDetail(APIView):

    def get_object(self, product_id, product_title):
        try:
            return Product.objects.filter(id=product_id).get(title=product_title)
        except Product.DoesNotExist:
            #ToDO : beter Template
            raise Http404
        
    # def get(self,request, product_id, product_title, format=None):
    def get(self,request, product_id, format=None):
        # product = self.get_object(product_title, product_title)
        # product = Product.objects.filter(id=product_id)[0]
        product = Product.objects.filter(id=product_id)[0]
        # serializer = ProductSerializer(product)
        serializer = ProductDitailSerializer(product)
        return Response(serializer.data)
    

class ProductDetailProductGallery(ListAPIView):
        # queryset = ProductGallery.objects.filter(product_id=product_id)
        serializer_class = ProductDetailProductGallerySerializer
        model = serializer_class.Meta.model
        def get_queryset(self):
            product_id = self.kwargs['product_id']
            queryset = self.model.objects.filter(product_id=product_id)
            return queryset


# class ProductDetailProductGallery(APIView):
#     def get(self,request, product_id, format=None):
#         productGallery =  ProductGallery.objects.filter(product_id=product_id)
#         serializer = ProductDetailProductGallerySerializer(productGallery, many=True)
#         return Response(serializer.data)

@api_view(['POST'])
# @authentication_classes([authentication.TokenAuthentication])
# @permission_classes([permissions.IsAuthenticated])
def SetStar(request):
    # serializer = StarSerializer(data=request.data)
    # serializer = StarSerializer

    # if serializer.is_valid():
    #      return Response({"message": "product is added"})
    if request.method == 'POST':
        return Response({"message": "product is added"})


# class SetStarClass(APIView):
#     queryset = Rating.objects.all()[0]
#     serializer_class = StarSerializer

#     def post(self, request, *args, **kwargs):
#         print("kkkk")
#         return Response({"message": "product is added"})
    


class SetStarClass(ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = StarSerializer
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        user = Token.objects.get(pk=request.auth).user

        if Rating.objects.filter(user=user,product_id=request.data["product"]).exists():
            rat= Rating.objects.filter(user=user,product_id=request.data["product"])
            rat.update(stars=request.data["stars"])
        else:
            rat = Rating.objects.create(stars=request.data["stars"], product_id=request.data["product"],user_id=user.id)

        rats= Rating.objects.filter(product_id=request.data["product"]).all()
        print(rats)
        rati= int(rats.aggregate(Avg("stars"))["stars__avg"] or 0)
        ratf= (rats.aggregate(Avg("stars"))["stars__avg"] or 0)%1
        # return Response(request.data)
        return Response({            
            "ratI" : rati,
            "ratF" : ratf
            })
    

#TODO: change ListCreateAPIView
class LikesCustomerCommentClass(ListCreateAPIView):
    queryset = LikesCustomerComment.objects.all()
    serializer_class = LikesCustomerCommentSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request,CustomerComment_id, *args, **kwargs):
        user = Token.objects.get(pk=request.auth).user
        if LikesCustomerComment.objects.filter(user=user,CustomerComment_id=CustomerComment_id).exists():
            likC = LikesCustomerComment.objects.filter(user=user,CustomerComment_id=CustomerComment_id).first()

        else:
            likC = LikesCustomerComment.objects.create(user=user,CustomerComment_id=CustomerComment_id)

        likC.likes = not likC.likes
        likC.save()
        numberLikeC = LikesCustomerComment.objects.filter(CustomerComment_id=CustomerComment_id,likes=True)
        return Response({
            "like" : likC.likes,
            "numberLike": convert_numbers.english_to_persian(str(numberLikeC.count()))
        })
    

    

class LikeStarClass(ListCreateAPIView):
    queryset = Likes.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,) 
    # permission_classes = (IsAuthenticated,)

    def get(self, request,product_id, *args, **kwargs):
        # print("product_id=",product_id)
        # print("request.auth=",request.auth)
        if request.auth is not None:
            user = Token.objects.get(pk=request.auth).user
            # print("user=",user)
            if Likes.objects.filter(user=user,product_id=product_id).exists():
                lik = Likes.objects.filter(user=user,product_id=product_id).first()
            else:
                lik = Likes.objects.create(user=user,product_id=product_id,likes=False)
            # print("lik=",lik)
            likeBool = lik.likes

        else:
            likeBool =False


        numberLike = Likes.objects.filter(product=product_id,likes=True)
        return Response({
            # "like" : lik.likes,
            "like" : likeBool,
            "numberLike": numberLike.count()
        })
    
    def post(self, request,product_id, *args, **kwargs):
        user = Token.objects.get(pk=request.auth).user
        if Likes.objects.filter(user=user,product_id=request.data["product"]).exists():
            lik = Likes.objects.filter(user=user,product_id=request.data["product"]).first()
            # print("lik=",lik)
            # print("lik.likes=",lik.likes)
        else:
            lik = Likes.objects.create(user=user,product_id=request.data["product"])
        lik.likes = not lik.likes
        lik.save()
        numberLike = Likes.objects.filter(product_id=request.data["product"],likes=True)
        return Response({
            "like" : lik.likes,
            "numberLike": numberLike.count()
        })

class CustomerCommentClass(ListCreateAPIView):
# class CustomerCommentClass(RetrieveAPIView):
    queryset = CustomerComment.objects.all()
    serializer_class = CustomerCommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


    def getId(self,serial,usr=None):
        # print("!!!!!!!!!!!!!!")
        # print(serial["id"])
        # print(usr)

        serial['is_user'] = False
        if usr is not None:
            if usr.username == serial['user']:
                serial['is_user'] = True



        serial['is_liked'] = False
        if LikesCustomerComment.objects.filter(
            user=usr,
            CustomerComment_id=serial["id"],
            likes= True
            ).exists():
                # print("-------------")
                # print(serial["id"])
                serial['is_liked'] = True
                # boolLike= LikesCustomerComment.objects.filter(
                #     user=usr,
                #     # pk=serial["id"],
                #     CustomerComment_id=serial["id"],
                #     likes= True   
                #     ).first()
                # print(f"boolLike.id={boolLike.id}")
                # print(f"boolLike.user={boolLike.user}")
        # else:
        #     serial['is_liked'] = False
        if serial["replies"] != []:
            self.getId(serial["replies"][0],usr)

    def get(self, request,product_id, *args, **kwargs):


        # comments = CustomerComment.objects.filter(CommentProduct=product_id,is_ok=True)
        # comments = CustomerComment.objects.get(CommentProduct=product_id,is_ok=True) .order_by('-created')

        comments = CustomerComment.objects.get_queryset().filter(
            CommentProduct_id=product_id,
            is_ok=True,
            parent=None,
            # replies=None,
            ).order_by('-created')
        serializer = CustomerCommentSerializer(comments, many=True)


        if request.auth is not None:
            user = Token.objects.get(pk=request.auth).user
            print(user)
        else:
            user = None

        for serial in serializer.data:
            self.getId(serial,usr=user)
        return Response(serializer.data)


class AllProductCustomerCommentClass(ListCreateAPIView):
# class CustomerCommentClass(RetrieveAPIView):
    queryset = CustomerComment.objects.all()
    serializer_class = AllProductCustomerCommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        u = Token.objects.get(pk=request.auth).user
        print(u)
        # user = User.objects.filter(email=u)[0]
        comments = CustomerComment.objects.get_queryset().filter(
            user=u,
            ).order_by('-created')
        serializer = AllProductCustomerCommentSerializer(comments, many=True)
        print(comments)
        # print(serializer)
        return Response(serializer.data)
        # return Response({'success': 'password changed successfully'}, status=200)



class DeleteCustomerComment(DestroyAPIView):
    queryset = CustomerComment.objects.all()
    serializer_class = DeleteCustomerCommentSerializer
    permission_classes = [IsAuthenticated]

class PostCustomerComment(CreateAPIView):   
    # serializer_class = PostCustomerCommentSerializer
    serializer_class = CustomerCommentSerializer
    queryset = CustomerComment.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = Token.objects.get(pk=request.auth).user
        # print(f"user={user}")
        # print(request.data["text"])
        # print(request.data["product"])
        # print(request.data["parent"])



        comments = CustomerComment.objects.create(
            user_id= user.pk,
            CommentProduct_id=request.data["product"],
            text=request.data["text"],
            is_ok=False,
            parent_id=request.data["parent"],
        )
        return Response({
            "ok":"ok"
        })
    

@api_view(['POST'])
def search(request):
    query = request.data.get('query','')
    print(query)
    if query:
        products = Product.objects.filter(
                                        Q(title__icontains=query)|
                                        Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
         return Response({"products":[]})
    
