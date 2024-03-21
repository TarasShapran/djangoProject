SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'BEARER': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        },
    },
    'USE_SESSION_AUTH': None
}