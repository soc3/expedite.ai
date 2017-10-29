from django.contrib import admin

from helpdesk.models import Issue, Reply, Order

# Register your models here.
admin.site.register(Order)
admin.site.register(Issue)
admin.site.register(Reply)
