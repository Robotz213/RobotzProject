def debug() -> bool:
    
    return True

def beta_test() -> bool:
    
    return False

def MySQL() -> dict:
    
    return {
        "DBLogin": "robotz",
        "DBPassword": "52CLMze4NfxeXrr5",
        "DBHost": "195.200.1.226",
        "Database": "robotz"
        
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

