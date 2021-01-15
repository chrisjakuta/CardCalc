from django.contrib import admin
from .models import AirTimeProvider, MTNProvider, AIRTELProvider, GLOProvider, AirtimeCardPurchase

# admin.site.register(AirTimeProvider)
admin.site.register(MTNProvider)
admin.site.register(AIRTELProvider)
admin.site.register(GLOProvider)
admin.site.register(AirtimeCardPurchase)