from notebook import notebookapp
import os

def _jupyter_server_extension_paths():
    return [{
        "module": "my_extension"
    }]

def _load_jupyter_server_extension(nbapp):
    env_variables = os.environ
    header = f"Environment Variables: {env_variables}"
    nbapp.log.info(header)
    nbapp.web_app.settings['headers'].add_header('X-Environment-Variables', header)