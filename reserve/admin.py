from django.contrib import admin

from social_django.models import Association, Nonce, UserSocialAuth
from oauth2_provider.models import (
    AccessToken,
    Application,
    Grant,
    IDToken,
    RefreshToken,
)
from .models import (
    Place,
    Reserve,
    PlaceReservePeriod,
    PlaceAdministrator,
    Category,
)

admin.site.unregister(Association)
admin.site.unregister(Nonce)
admin.site.unregister(UserSocialAuth)
admin.site.unregister(AccessToken)
admin.site.unregister(Application)
admin.site.unregister(Grant)
admin.site.unregister(IDToken)
admin.site.unregister(RefreshToken)
admin.site.register(Category)
admin.site.register(Place)
admin.site.register(PlaceAdministrator)
admin.site.register(Reserve)
admin.site.register(PlaceReservePeriod)
