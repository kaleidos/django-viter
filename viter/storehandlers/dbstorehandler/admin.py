from django.contrib import admin
from viter.storehandlers.dbstorehandler.models import Invitation, InvitationUsage

class InvitationUsageInline(admin.TabularInline):
    model = InvitationUsage

class InvitationAdmin(admin.ModelAdmin):
    model = Invitation
    inlines = [InvitationUsageInline]
admin.site.register(Invitation, InvitationAdmin)
