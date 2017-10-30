
from django.contrib import admin
from libapp.models import Book, Dvd, Libuser, Libitem, Suggestion
import datetime

class BookInline(admin.StackedInline):
    model = Book  # This shows all fields of Book.
    fields = [('title', 'author'), 'duedate', ]   #  Customizes to show only certain fields
    extra = 0


class DvdInline(admin.TabularInline):
    model = Dvd  # This shows all fields of DVD.
    fields = [('title', 'maker', 'pubyr'), ('checked_out', 'itemtype', 'user', 'duedate'), 'rating']   #  Customizes to show only certain fields
    extra = 0


def renew(modeladmin, request, queryset):
    for obj in queryset:
        if obj.checked_out:
            queryset.update(duedate=obj.duedate + datetime.timedelta(days=21))


class LibuserAdmin(admin.ModelAdmin):
    fields = [('username'), ('first_name', 'last_name')]
    list_display = ('username', 'first_name')
    inlines = [BookInline, DvdInline]


class BookAdmin(admin.ModelAdmin):
    fields = [('title', 'author', 'pubyr'), ('checked_out', 'itemtype', 'user', 'duedate'), 'category']
    list_display = ('title', 'borrower', 'overdue')
    actions = [renew]

    def borrower(self, obj=None):
        if obj.checked_out:
            return obj.user     #Returns the user who has borrowed this book
        else:
            return ''


class DvdAdmin(admin.ModelAdmin):
    fields = [('title', 'maker', 'pubyr'), ('checked_out', 'itemtype', 'user', 'duration', 'duedate'), 'rating']
    list_display = ('title', 'rating', 'borrower', 'overdue')
    actions = [renew]

    def borrower(self, obj=None):
        if obj.checked_out:
            return obj.user     #Returns the DVD title, rating and pub year that has be borrowed
        else:
            return ''


# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Dvd, DvdAdmin)
admin.site.register(Libuser, LibuserAdmin)
admin.site.register(Suggestion)

