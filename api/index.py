from app import app
from vercel_wsgi import handle_wsgi

def handler(event, context):
    return handle_wsgi(app, event, context)
