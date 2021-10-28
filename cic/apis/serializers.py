from rest_framework import serializers
from .models import Organization, Person


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    affiliations = OrganizationSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Person
        fields = ('id', 'first_name', 'last_name', 'orcid', 'emails', 'private_emails', 'keywords', 'affiliations')
        depth = 1


class CreatePersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'

    def create(self, validated_data, ):
        organizations = validated_data.pop('affiliations')
        new_person = Person.objects.create(**validated_data)
        for org in organizations:
            new_person.affiliations.add(org)
        new_person.save()
        return new_person


