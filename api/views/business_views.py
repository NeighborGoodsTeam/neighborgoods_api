from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.business import Business
from ..serializers import BusinessSerializer, UserSerializer

# Create your views here.
class Businesses(generics.ListCreateAPIView):
    permission_classes=(AllowAny,)
    serializer_class = BusinessSerializer
    def get(self, request):
        """Index request"""
        # Get all the businesses:
        businesses = Business.objects.all()
        # Filter the businesses by owner, so you can only see your owned businesses
        # businesses = Business.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = BusinessSerializer(businesses, many=True).data
        return Response({ 'businesses': data })

class CreateBusiness(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = BusinessSerializer
    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['business']['owner'] = request.user.id
        # Serialize/create business
        business = BusinessSerializer(data=request.data['business'])
        # If the business data is valid according to our serializer...
        if business.is_valid():
            # Save the created business & send a response
            business.save()
            return Response({ 'business': business.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(business.errors, status=status.HTTP_400_BAD_REQUEST)

class BusinessDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the business to show
        business = get_object_or_404(Business, pk=pk)
        # Only want to show owned businesses?
        if not request.user.id == business.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this business')

        # Run the data through the serializer so it's formatted
        data = BusinessSerializer(business).data
        return Response({ 'business': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate business to delete
        business = get_object_or_404(Business, pk=pk)
        # Check the business's owner agains the user making this request
        if not request.user.id == business.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this business')
        # Only delete if the user owns the  business
        business.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Remove owner from request object
        # This "gets" the owner key on the data['business'] dictionary
        # and returns False if it doesn't find it. So, if it's found we
        # remove it.
        if request.data['business'].get('owner', False):
            del request.data['business']['owner']

        # Locate Business
        # get_object_or_404 returns a object representation of our Business
        business = get_object_or_404(Business, pk=pk)
        # Check if user is the same as the request.user.id
        if not request.user.id == business.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this business')

        # Add owner to data object now that we know this user owns the resource
        request.data['business']['owner'] = request.user.id
        # Validate updates with serializer
        data = BusinessSerializer(business, data=request.data['business'])
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
