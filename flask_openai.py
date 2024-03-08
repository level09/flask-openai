import openai
from flask import current_app, _app_ctx_stack

import openai
from flask import current_app, _app_ctx_stack

class OpenAI:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        # Ensure the OPENAI_API_KEY is set in the app config, with a default value if not present.
        app.config.setdefault('OPENAI_API_KEY', '')
        # Register a function to be run at the end of each request, to clean up.
        app.teardown_appcontext(self.teardown)

    def teardown(self, exception):
        ctx = _app_ctx_stack.top
        if hasattr(ctx, 'openai_client'):
            del ctx.openai_client

    @property
    def client(self):
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'openai_client'):
                # Initialize the OpenAI client using the API key from app config and store it in the app context.
                ctx.openai_client = openai.OpenAI(api_key=current_app.config['OPENAI_API_KEY'])
            return ctx.openai_client
