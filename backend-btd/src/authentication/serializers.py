from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import CustomUser, Brewery, Beer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['fav_color'] = user.fav_color
        return token

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class BreweryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brewery
        fields = ('id', 'name')
class BeerSerializer(serializers.ModelSerializer):
    brewery = BreweryNameSerializer(many=False, read_only=True)
    class Meta:
        model = Beer
        fields = ('id', 'brewery', 'name', 'style', 'rating', 'abv', 'description', 'release_date', 'image_url')
class BrewerySerializer(serializers.ModelSerializer):
    beers = BeerSerializer(many=True, read_only=True)
    class Meta:
        model = Brewery
        fields = ('id', 'name', 'location', 'latitude', 'longitude', 'website_url', 'logo_url', 'image_url', 'beers')