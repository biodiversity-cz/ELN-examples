AUTH_PROVIDERS = [
    {
        "type": "local",
        "allow_registration": True,
        "default_system_role": "admin",
    },
]
SERVER_NAME = "localhost:8002"
SECRET_KEY = "e9eiMU9ZK9vSadVSRw76"
SQLALCHEMY_DATABASE_URI = "postgresql://kadi:kadi@postgres/kadi"
STORAGE_PATH = "/opt/kadi/storage"
MISC_UPLOADS_PATH = "/opt/kadi/uploads"
SMTP_HOST = "localhost"
SMTP_PORT = 25
SMTP_USERNAME = ""
SMTP_PASSWORD = ""
MAIL_NO_REPLY = "no-reply@localhost:8002"
CELERY_BROKER_URL = "redis://redis:6379/0"
RATELIMIT_STORAGE_URI = "redis://redis:6379/0"
ELASTICSEARCH_HOSTS = "http://elastic:9200"