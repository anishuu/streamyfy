from django.contrib import admin
from .models import Plan, UserAccount, Payment, MovieTVShow, Watches

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('plan_id', 'plan_price', 'plan_duration', 'plan_type')

@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('User_id', 'First_name', 'Last_name', 'Email_id', 'Address', 'Phone_number', 'Plan')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('Transaction_id', 'Payment_time', 'Payment_date', 'Payment_method', 'Amount_paid', 'Plan', 'User')

@admin.register(MovieTVShow)
class MovieTVShowAdmin(admin.ModelAdmin):
    list_display = ('Show_id', 'Title', 'Release_date', 'Description', 'Duration', 'Views', 'Country', 'Rating', 'Genre', 'Actor', 'Actress')

@admin.register(Watches)
class WatchesAdmin(admin.ModelAdmin):
    list_display = ('User', 'Show', 'Date')

    class Meta:
        unique_together = ('User', 'Show')  # Ensure no duplicate entries
