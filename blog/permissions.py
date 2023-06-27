from rest_framework.permissions import BasePermission, SAFE_METHODS


class CustomBlogsPermission(BasePermission):

    def has_permission(self, request, view):
        # List is allowed to any request,
        # Create is only allowed to authenticated users.
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Retrieve is allowed to any authenticated request,
        # Put, patch, delete are only allowed to the author of a post.
        if request.method in SAFE_METHODS and request.user.is_authenticated:
            return True
        return obj.author == request.user
    

class CustomCommentPermission(BasePermission):
    
    # staff users can list, 
    # authenticated users can create,
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_staff
        return request.user.is_authenticated
    
    # staff can retrieve and delete.
    # author of a comment can retrieve, update, delete.
    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        elif request.method in ['GET', 'DELETE']:
            return request.user.is_staff
        return False