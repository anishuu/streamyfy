import os
import django

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stremyfy.settings')
django.setup()

# Import the UserAccount model
from live_streaming.models import UserAccount

def delete_all_user_accounts():
    # Delete all UserAccount instances
    UserAccount.objects.all().delete()
    print("All UserAccount instances have been deleted.")

if __name__ == "__main__":
    delete_all_user_accounts()
