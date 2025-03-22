from django.contrib import admin
from .models import Review

class WordFilter(admin.SimpleListFilter):
    title = "Filter by words!"
    parameter_name = "potato"
    
    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]
        
    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            return reviews
        
class PNFilter(admin.SimpleListFilter):
    title = "Filter by review is Positive or Negative"
    parameter_name = "review_PN"
        
    def lookups(self, request, model_admin):
        return [
            ("positive", "Positive"),
            ("negative", "Negative"),
        ]
        
    def queryset(self, request, reviews):
        pn = self.value()
        if pn == "positive":
            return reviews.filter(rating__gte=3)
        elif pn == "negative":
            return reviews.filter(rating__lt=3)
        else:
            return reviews

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    
    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        WordFilter,
        PNFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )
