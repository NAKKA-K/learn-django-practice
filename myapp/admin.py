from django.contrib import admin
from .models import Post, Comment
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _
from .models import User
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)


class MyUserChangesForm(UserChangeForm):
  class Meta:
    model = User
    fields = '__all__'

class MyUserCreationForm(UserCreationForm):
  class Meta:
    model = User
    fields = ('email',)

class MyUserAdmin(UserAdmin):
  fieldsets = (
      (None, {'fields': ('email', 'password')}),
      (_('Personal info'), {'fields': ('first_name', 'last_name', 'school_year', 'school_class', 'school_number')}),
      (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                     'groups', 'user_permissions' )}),
      (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
  )
  add_fieldsets = (
      (None, {
          'classes': ('wide',),
          'fields': ('email', 'password1', 'password2'),
      }),
  )
  form = MyUserChangesForm
  add_form = MyUserCreationForm
  list_display = ('email', 'first_name', 'last_name', 'is_staff')
  list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
  search_fields = ('email', 'first_name', 'last_name')
  ordering = ('email',)

admin.site.register(User, MyUserAdmin)
