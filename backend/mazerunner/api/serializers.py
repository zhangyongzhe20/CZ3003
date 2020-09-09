from rest_framework import serializers
from users.models import Student , User

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ('account', 'password', 'name')

    def create(self , validated_data):
        user = User(
            account = validated_data['account'],
            password = validated_data['password'],
            name = validated_data['name']
        )
        user.save()
        return user
        
    def update(self , instance , validated_data):
        instance.account = validated_data.get('account', instance.account)
        instance.password = validated_data.get('password', instance.password)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class StudentAccountSerializer(serializers.ModelSerializer):
    class Meta :
        model = Student
        fields = UserAccountSerializer.Meta.fields + ('distanceToNPC','overallScore','Ranking','containBonus','role')
        
