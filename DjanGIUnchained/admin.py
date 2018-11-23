from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Pieces)
admin.site.register(PieceType)
admin.site.register(User)
admin.site.register(Permission)
admin.site.register(Role)

