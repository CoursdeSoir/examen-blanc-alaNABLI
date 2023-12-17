from django.contrib import admin
from .models import Projet
from .models import Developpeur

# Register your models here.

#admin.site.register(Projet)
admin.site.register(Developpeur)


class type_filter(admin.SimpleListFilter):
    title = 'type de projet et effectif'
    parameter_name = 'type'

    def lookups(self, request, model_admin):
        return (
            ('Web', ('Projet web')),
            ('Mobile', ('Projet mobile')),
            ('Desktop', ('Projet desktop')),
            ('Manque_effectif', ('Projet sans effectif')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'Web':
            return queryset.filter(type='w')
        if self.value() == 'Mobile':
            return queryset.filter(type='m')
        if self.value() == 'Desktop':
            return queryset.filter(type='d')
        if self.value() == 'Manque_effectif':
            return queryset.filter(effectif='manque')

class Developpeur_Inline(admin.TabularInline):
    model = Developpeur

@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ('date_debut', 'date_fin', 'besoin', 'createur', 'type', 'effectif')
    search_fields = ('createur',)
    list_per_page = 10
    list_filter = (type_filter,)
    inlines = [Developpeur_Inline]

