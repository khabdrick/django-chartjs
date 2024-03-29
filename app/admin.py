from django.contrib import admin
from app.models import *
from django.db.models.functions import TruncDay
from django.db.models import Count
from django.core.serializers.json import DjangoJSONEncoder
import json


# Register your models here.

class WriterAdmin(admin.ModelAdmin):

    ## change_list.html
    def changelist_view(self, request, extra_context=None):
        # Aggregate new writer per day
        chart_data = (
    	    Writer.objects.annotate(date=TruncDay("createdDate"))
            .values("date")
            .annotate(y=Count("id"))
            .order_by("-date")
        )

        # Serialize and attach the chart data to the template context
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        print("Json %s"%as_json)
        extra_context = extra_context or {"chart_data": as_json}
        # Call the superclass changelist_view to render the page
        
        return super().changelist_view(request, extra_context=extra_context)


admin.site.register(Writer, WriterAdmin)
admin.site.register(Article)