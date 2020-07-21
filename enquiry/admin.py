from django.contrib import admin
from .models import Enquiry, Visitor


class EnquiryAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    readonly_fields = ['name', 'email', 'phone', 'message', 'address', ]


class VisitorAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    readonly_fields = ['name', 'visit', ]


admin.site.register(Enquiry, EnquiryAdmin)
admin.site.register(Visitor, VisitorAdmin)
