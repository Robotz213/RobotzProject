from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do .env
load_dotenv()

def debug() -> bool:
    
    return True

def beta_test() -> bool:
    
    return False

def MySQL() -> dict:
    return {
        "DBLogin": os.getenv("DB_LOGIN"),
        "DBPassword": os.getenv("DB_PASSWORD"),
        "DBHost": os.getenv("DB_HOST"),
        "Database": os.getenv("DATABASE")
    }
def permissions_policy() -> dict:
    
    # Configurando Permissions-Policy sem 'browsing-topics'
    return {
    'accelerometer': 'none',
    'ambient-light-sensor': 'none',
    'autoplay': 'self',
    'camera': 'none',
    'clipboard-read': 'self',
    'clipboard-write': 'self',
    'display-capture': 'none',
    'document-domain': 'none',
    'encrypted-media': 'self',
    'fullscreen': 'self',
    'geolocation': 'self',
    'gyroscope': 'none',
    'magnetometer': 'none',
    'microphone': 'none',
    'midi': 'none',
    'payment': 'none',
    'picture-in-picture': 'self',
    'publickey-credentials-get': 'self',
    'sync-xhr': 'self',
    'usb': 'none',
    'xr-spatial-tracking': 'none',
    # Remove 'browsing-topics'
}

def csp() -> dict: 
    return {
    'default-src': [
        "'self'",
        'https://cdn.jsdelivr.net'
    ],
    'img-src': [
        "'self'",
        'data:'
    ],
    'style-src': [
        "'self'",
        'https://cdn.jsdelivr.net'
    ],
    'script-src': [
        "'self'",
        'https://cdn.jsdelivr.net'
    ]
}

