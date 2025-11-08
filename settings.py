import os
from dotenv import load_dotenv

load_dotenv()


API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')

# ID or invite link will do
TO_CHANNEL = os.getenv('TO_CHANNEL')
FROM_CHANNEL = os.getenv('FROM_CHANNEL')

# where to save the session, if empty will prompt login every time
SESSION_PATH = os.getenv('SESSION_PATH')