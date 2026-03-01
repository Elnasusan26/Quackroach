from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Vault, Letter, Executor

User = get_user_model()

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # The columns shown on the main user list page
    list_display = ('email', 'full_name', 'is_staff', 'is_active', 'date_joined')
    
    # Adds a search bar to find users by email or name
    search_fields = ('email', 'full_name')
    
    # Adds a filter sidebar
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    
    # Default ordering
    ordering = ('-date_joined',)
    
    # Customizing the edit page to include 'full_name'
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('full_name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Required for UserAdmin to use email as the main ID
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'full_name'),
        }),
    )

# --- Registering Legacy Models ---

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