from django.contrib import admin
from . import models
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# for slug fields. auto fillup slug fields in admin panale
class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', )}

class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', )}

admin.site.register(models.DesignationModel, DesignationAdmin)
admin.site.register(models.SpecializationModel, SpecializationAdmin)
admin.site.register(models.AvailableTimeModel)


class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'fee', 'meet_link']

    def name(self, obj):
        return obj.user.username

    # def save_model(self, request, obj, form, change):
    #     obj.save()
    #     email_subject = "Your Online Appointment is Running"
    #     email_body = render_to_string('confirm_email.html')
            
    #     email = EmailMultiAlternatives(email_subject , '', to=[obj.user.email])
    #     email.attach_alternative(email_body, "text/html")
    #     email.send()

admin.site.register(models.DoctorModel, DoctorAdmin)
admin.site.register(models.ReviewModel)