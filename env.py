import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5200")
os.environ.setdefault("SECRET_KEY", "secretkey")
os.environ.setdefault("DEBUG", "TRUE")
os.environ.setdefault("DEVELOPMENT", "TRUE")
os.environ.setdefault("DB_URL", "postgresql:///budgetmanager")