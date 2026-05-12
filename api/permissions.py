from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsReaderOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsJournalistForCreate(BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":
            return request.user.is_authenticated and request.user.is_journalist()

        return True


class IsEditorOrJournalistForEdit(BasePermission):
    def has_permission(self, request, view):
        if request.method in ["PUT", "PATCH", "DELETE"]:
            return (
                request.user.is_authenticated
                and (
                    request.user.is_editor()
                    or request.user.is_journalist()
                )
            )

        return True


class ArticleRolePermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if request.method == "POST":
            return request.user.is_authenticated and request.user.is_journalist()

        if request.method in ["PUT", "PATCH", "DELETE"]:
            return (
                request.user.is_authenticated
                and (
                    request.user.is_editor()
                    or request.user.is_journalist()
                )
            )

        return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return obj.approved or (
                request.user.is_authenticated
                and (
                    request.user.is_editor()
                    or obj.author == request.user
                )
            )

        if request.method in ["PUT", "PATCH"]:
            return (
                request.user.is_authenticated
                and (
                    request.user.is_editor()
                    or obj.author == request.user
                )
            )

        if request.method == "DELETE":
            return (
                request.user.is_authenticated
                and (
                    request.user.is_editor()
                    or obj.author == request.user
                )
            )

        return False
