import pytz
from datetime import datetime

def get_local_time():
    timezone = pytz.timezone('Your/Timezone')  # Adjust to your timezone
    return datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")