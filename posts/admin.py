from django.contrib import admin

# Register your models here.

#下２行を追加すると、adminサイトで参照できるようになる
from .models import Post

admin.site.register(Post)