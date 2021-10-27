
"""
我们希望所有的代码片段都可以被任何人看到，但也要确保只有创建代码片段的用户才能更新或删除它。

为此，我们将需要创建一个自定义权限。
"""

from rest_framework import permissions

class IsOwnerOrReayOnly(permissions.BasePermission):
    """
    自定义权限只允许对象的所有者编辑它
    """

    def has_object_permission(self, request, view, obj):
        # 读取权限允许任何请求,
        # 所以我们总是允许GET， HEAD或OPTION请求。
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
