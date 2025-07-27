from django.contrib import admin

# Register your models here.
from .models import store,App,ChaiCertificate,ChaiReview

class ChaiReviewInline(admin.TabularInline):
    model=ChaiReview
    extra=2

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display=("name","type","date_added")
    inlines=[ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display=('name','location')
    
    filter_horizontal=('chai_varieties',)



class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display=('chai','certificate_number')

admin.site.register(App,ChaiVarietyAdmin)
admin.site.register(store,StoreAdmin)
admin.site.register(ChaiCertificate,ChaiCertificateAdmin)
