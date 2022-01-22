from rest_framework import serializers


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        fields = ('email',)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
