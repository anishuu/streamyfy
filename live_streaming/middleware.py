from datetime import datetime
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from .models import UserAccount

class PlanExpirationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            user = request.user
            current_time = datetime.now().date()
            if hasattr(user, 'useraccount') and user.useraccount.plan_expiration_date:
                if user.useraccount.plan_expiration_date < current_time:
                    # Expired plan, logout the user
                    user.useraccount.plan_expiration_date = None
                    user.useraccount.save()
                    return redirect('logout')  # Redirect to your logout view name
        return None
