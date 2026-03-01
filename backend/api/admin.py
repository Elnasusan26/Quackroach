from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils import timezone
from django.utils.html import format_html
from datetime import timedelta
from .models import Vault, Letter, Executor

User = get_user_model()

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Updated list_display to include our new custom method
    list_display = ('email', 'full_name', 'is_staff', 'is_active', 'check_in_status', 'date_joined')
    search_fields = ('email', 'full_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    ordering = ('-date_joined',)
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('full_name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'full_name'),
        }),
    )

    def check_in_status(self, obj):
        """
        Highlights the last login status. 
        Red if inactive > 30 days, Green if active.
        """
        last_seen = obj.last_login or obj.date_joined
        if not last_seen:
            return "No Data"
        
        limit = timezone.now() - timedelta(days=30)
        formatted_date = last_seen.strftime("%b %d, %Y")
        
        if last_seen < limit:
            # Return red text for inactive users
            return format_html(
                '<span style="color: #f87171; font-weight: bold;">{} (Inactive)</span>',
                formatted_date
            )
        # Return green for active users
        return format_html(
            '<span style="color: #4ade80;">{} (Active)</span>',
            formatted_date
        )

    check_in_status.short_description = 'Last Check-in'

# --- Legacy Models ---
@admin.register(Vault)
class VaultAdmin(admin.ModelAdmin):
    list_display = ('user', 'item_count', 'updated_at')
    readonly_fields = ('ciphertext', 'iv', 'salt')

@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'user', 'created_at')
    readonly_fields = ('ciphertext', 'iv', 'salt')

@admin.register(Executor)
class ExecutorAdmin(admin.ModelAdmin):
    list_display = ('name', 'relationship', 'user', 'status', 'is_verified')
    list_editable = ('status', 'is_verified')