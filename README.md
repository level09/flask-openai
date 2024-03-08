# Flask-OpenAI Extension

The Flask-OpenAI extension provides a simple and intuitive way to integrate OpenAI's API into your Flask applications. With minimal setup, you can start leveraging the power of AI models in your Flask projects, whether it's for generating text, code, or any other application supported by OpenAI.

## Features

- Easy integration of OpenAI's API into Flask applications.
- Automatic management of OpenAI API keys.
- Efficient handling of API client instances throughout the application lifecycle.

## Installation

Install Flask-OpenAI using pip:

```
pip install flask-openai
```

## Quick Start

1. **Set up your Flask application**

First, ensure you have Flask installed. If not, you can install it using pip:

```
pip install Flask
```

Then, set up a basic Flask application:

```python
from flask import Flask
app = Flask(__name__)
```

2. **Configure the Flask-OpenAI extension**

Import and initialize the `OpenAI` extension, passing your Flask app object to it. Don't forget to set the `OPENAI_API_KEY` in your app's configuration:

```python
from flask_openai import OpenAI

app.config['OPENAI_API_KEY'] = 'your_openai_api_key_here'
openai_extension = OpenAI(app)
```

Alternatively, if you are using a factory function to create your Flask app, you can set up the OpenAI extension like this:

```python
openai_extension = OpenAI()

def create_app():
    app = Flask(__name__)
    app.config['OPENAI_API_KEY'] = 'your_openai_api_key_here'
    openai_extension.init_app(app)
    return app
```

3. **Use the OpenAI client in your application**

Now, you can access the OpenAI client in your route handlers using `openai_extension.client`. Here's an example of how to generate text with the OpenAI API:

```python
@app.route('/generate-text')
def generate_text():
    completion = openai.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
        ]
    )

    return completion.choices[0].message.content

```

## Documentation

For more information on OpenAI's API and its capabilities, visit [OpenAI API documentation](https://openai.com/api/).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## Support

If you have any questions or encounter any issues, please open an issue on the project's GitHub page.

## Acknowledgements

This project is not officially associated with OpenAI. All trademarks are the property of their respective owners.
