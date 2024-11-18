from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from django.contrib.auth.models import User

@api_view(['GET'])
def hello_world(request):
    superusers = User.objects.filter(is_superuser=True)
    for user in superusers:
        print(user.username)
    dataA = request.data.get('a')
    dataB = request.data.get('b')
    # varData = dataA + dataB
    # Access specific fields from the data if needed
    varDict = {"value":"varData"}
    return Response(varDict)

@api_view(['POST'])
def add_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  # Saves the new Product to the database
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def product_list(request):
    """
    Retrieve all products by their name from the request payload.
    """
    product_name = request.data.get('name', None)  # Get the 'name' from request body

    if product_name is not None:
        # Retrieve all products with the specified name
        products = Product.objects.filter(name=product_name)

        if products.exists():
            serializer = ProductSerializer(products, many=True)  # Serialize multiple products
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    return Response({"detail": "Name is required."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def edit_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()  # Updates the existing Product in the database
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# views.py
@api_view(['DELETE'])
def delete_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    product.delete()  # Deletes the Product instance from the database
    return Response({"message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


