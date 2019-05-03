from __future__ import unicode_literals

from django.contrib import admin
from .models import Division, Patient, Service, Trieuchung, Trieuchungtq, Trieuchungcb, Ketluan, Xlkhancap, Donthuoc, Typeservice, Medicine


class TrieuchungcbInLine(admin.StackedInline):
    model = Trieuchungcb
    extra = 1

class TrieuchungtqInLine(admin.StackedInline):
    model = Trieuchungtq
    extra = 1
class KetluanInLine(admin.StackedInline):
    model = Ketluan
    extra = 1
class ServiceInLine(admin.StackedInline):
    model = Service
    extra = 1
class XlkhancapInLine(admin.StackedInline):
    model = Xlkhancap
    extra = 1
class DonthuocInLine(admin.StackedInline):
    model = Donthuoc
    extra = 1

class TrieuchungModelAdmin(admin.ModelAdmin):
    list_display = ('codetrieuchung','trieuchung1','nhomcoquan' )

class TrieuchungtqModelAdmin(admin.ModelAdmin):
    list_display = ('codepatient','codetrieuchung','status1','lankham','date','codepatient_id'  )
class TrieuchungcbModelAdmin(admin.ModelAdmin):
    list_display = ('codepatient','codetrieuchung','status1','lankham','date','codepatient_id'  )

class ServiceModelAdmin(admin.ModelAdmin):

    list_display = ('codeservice','codepatient_id','status','lankham','date' )

class TypeserviceModelAdmin(admin.ModelAdmin):

    list_display = ('codeservice','name_serv'  )
class XlkhancapModelAdmin(admin.ModelAdmin):

    list_display = ('codepatient','name_xlkc','status', 'lankham','date', 'codepatient_id'  )

class MedicineModelAdmin(admin.ModelAdmin):

    list_display = ('codemedicine','name_medi','dosage','function1', 'sideeffect')

class DonthuocModelAdmin(admin.ModelAdmin):

    list_display = ('codedonthuoc','codepatient_id','soluong','dvtinh', 'lankham','date')

class KetluanModelAdmin(admin.ModelAdmin):
    list_display = ('bacsy','codepatient','lankham','date', 'name_ketluan','codepatient_id'  )



class DivisionModelAdmin(admin.ModelAdmin):
    list_filter = ('active',)
    list_display = ('namediv', 'active', )

class PatientModelAdmin(admin.ModelAdmin):
    #inlines = [TrieuchungtqInLine, TrieuchungcbInLine]



    list_display = ('codepatientp', 'namepatient', 'age','place','City')

admin.site.register(Donthuoc, DonthuocModelAdmin)
admin.site.register( Medicine, MedicineModelAdmin)
admin.site.register(Division, DivisionModelAdmin)
admin.site.register(Patient, PatientModelAdmin)
admin.site.register(Service, ServiceModelAdmin)
admin.site.register(Typeservice, TypeserviceModelAdmin)
admin.site.register(Ketluan, KetluanModelAdmin)
admin.site.register(Xlkhancap, XlkhancapModelAdmin)
admin.site.register(Trieuchungtq, TrieuchungtqModelAdmin)
admin.site.register(Trieuchungcb, TrieuchungcbModelAdmin)
admin.site.register(Trieuchung, TrieuchungModelAdmin)