import openai
from flask import current_app

class OpenAI:
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        # Ensure the OPENAI_API_KEY is set in the app config, with a default value if not present.
        app.config.setdefault('OPENAI_API_KEY', '')

        # Use the new Flask 3.0 way to clean up: Use the 'teardown_appcontext' decorator or method
        @app.teardown_appcontext
        def teardown(exception=None):
            ctx = app.app_context().push()
            if hasattr(ctx, 'openai_client'):
                del ctx.openai_client

        # Storing the teardown function for reference; not strictly necessary but keeps the pattern consistent
        self.teardown = teardown

    @property
    def client(self):
        ctx = current_app.app_context()
        if not hasattr(ctx, 'openai_client'):
            # Initialize the OpenAI client using the API key from app config and store it in the app context.
            ctx.openai_client = openai.OpenAI(api_key=current_app.config['OPENAI_API_KEY'])
        return ctx.openai_client
