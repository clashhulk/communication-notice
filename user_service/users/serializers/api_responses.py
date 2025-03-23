from rest_framework import serializers


class ErrorDetailSerializer(serializers.Serializer):
    code = serializers.CharField(required=False, help_text="Error code.")
    message = serializers.CharField(
        required=False, help_text="Detailed error message.")


class MetaDataSerializer(serializers.Serializer):
    pagination = serializers.CharField(
        required=False, help_text="Details about pagination.")
    other_details = serializers.CharField(
        required=False, help_text="Other relevant meta information.")


class DataDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(help_text="Unique identifier.")
    value = serializers.CharField(help_text="A descriptive value.")


class StandardApiResponse(serializers.Serializer):
    success = serializers.BooleanField(
        help_text="Indicates if the request was successful.")
    data = DataDetailSerializer(
        help_text="Container for the response data, contents vary by request.", required=False)
    errors = ErrorDetailSerializer(
        many=True, required=False, help_text="Contains any errors encountered during the request.")
    meta = MetaDataSerializer(
        required=False, help_text="Additional metadata about the response.")
