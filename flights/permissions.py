from rest_framework.permissions import BasePermission
from datetime import date

class IsTrue(BasePermission):
    message = "SecondCase"

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or (obj.user == request.user):
            return True
        else:
            return False

class IsValid(BasePermission):
    message = "ThirdCase"
    #tomorrow = datetime.date.today() + datetime.timedelta(days=3)

    def has_object_permission(self, request, view, obj):
        tomorrow = (obj.date - date.today()).days
        if (tomorrow) > 3 :
            return True
        else:
            return False

#tomorrow = datetime.date.today() + datetime.timedelta(days=1)
