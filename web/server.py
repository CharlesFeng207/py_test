from aiohttp import web

from web.handers import Handers
from aiohttp_session import setup, get_session, session_middleware
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from cryptography import fernet
import base64


app = web.Application()
app.add_routes(Handers.routes)

# secret_key must be 32 url-safe base64-encoded bytes
fernet_key = fernet.Fernet.generate_key()
secret_key = base64.urlsafe_b64decode(fernet_key)
setup(app, EncryptedCookieStorage(secret_key))

# All registered resources in a router can be viewed using the
for resource in app.router.resources():
    print(resource)

web.run_app(app)
