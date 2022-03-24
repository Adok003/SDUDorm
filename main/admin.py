from django.contrib import admin
from .models import User, Block, Floor, Room, Entry

admin.site.register(User)
admin.site.register(Block)
admin.site.register(Floor)
admin.site.register(Room)
admin.site.register(Entry)

