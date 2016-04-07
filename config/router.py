from rest_framework import routers

from users.apis import UserViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r"user", UserViewSet, base_name="user")
