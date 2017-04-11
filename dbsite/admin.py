from django.contrib import admin
from .models import Organism,CommonName,Synonym,Links, Distribution,Subspecies_Name,Types,PhotoURLS,Comments,BiblioRefer
# Register your models here.

admin.site.register(Organism)
admin.site.register(CommonName)
admin.site.register(Synonym)
admin.site.register(Links)

admin.site.register(Distribution)
admin.site.register(Subspecies_Name)

admin.site.register(Types)
admin.site.register(PhotoURLS)

admin.site.register(Comments)
admin.site.register(BiblioRefer)