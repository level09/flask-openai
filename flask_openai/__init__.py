import openai
from flask import current_app, g

class OpenAI:
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('OPENAI_API_KEY', '')
        app.teardown_appcontext(self.teardown)

    def teardown(self, exception):
        client = g.pop('openai_client', None)
        if client is not None:
            # Perform any necessary cleanup for the OpenAI client
            pass

    @property
    def client(self):
        if 'openai_client' not in g:
            g.openai_client = openai.OpenAI(api_key=current_app.config['OPENAI_API_KEY'])
        return g.openai_client