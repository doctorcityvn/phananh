from __future__ import unicode_literals

from django.contrib import admin
from .models import Division, Patient

class DivisionModelAdmin(admin.ModelAdmin):
    list_filter = ('active',)
    list_display = ('namediv', 'active', )

class PatientModelAdmin(admin.ModelAdmin):
    readonly_fields = ('image_tag',)    
    list_display = ('namepatient', 'age','place','symptom','diagnosis','doctor', 'prescription')

admin.site.register(Division, DivisionModelAdmin)
admin.site.register(Patient, PatientModelAdmin)