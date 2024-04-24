from rest_framework.permissions import BasePermission
from healthlink.utils.exceptions import NotHealthcareProvider


class IsHealthcareProvider(BasePermission):
    """
    Permission class to check if the user is a healthcare provider.
    """

    def has_permission(self, request, view):
        """
        Check if the user is a healthcare provider.
        """

        if request.user.role == "doctor" or request.user.role == "patient":
            return True
        raise NotHealthcareProvider()

    def has_object_permission(self, request, view, obj):
        """
        Check if the user is a healthcare provider.
        """

        if request.user.role == "doctor" or request.user.role == "patient":
            return True
        raise NotHealthcareProvider()
