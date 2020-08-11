import os

SECRET_KEY = os.getenv('SECRET_KEY')

# ===================================================================
#                       File upload directories
# ===================================================================
APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
UPOLADS_FOLDER = os.path.join(APP_ROOT, "uploads/")
if not os.path.isdir(UPOLADS_FOLDER):
    os.mkdir(UPOLADS_FOLDER)

# ===================================================================
#                      MONGODB_SETTINGS
# ===================================================================
MONGODB_DB = os.getenv('MONGODB_DB')
MONGODB_HOST = os.getenv('MONGODB_HOST')
MONGODB_PORT = int(os.getenv('MONGODB_PORT'))
MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')
