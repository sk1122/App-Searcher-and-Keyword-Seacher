from django.contrib import admin
from .models import GooglePlayModel, AppleAppModel, Keyword


admin.site.register(GooglePlayModel)

admin.site.register(AppleAppModel)

admin.site.register(Keyword)
