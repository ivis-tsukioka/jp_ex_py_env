from notebook.base.handlers import APIHandler
from tornado import web

class EnvironmentVariableHandler(APIHandler):
    @web.authenticated
    def get(self):
        variable_name = self.get_argument('variable_name', default=None)
        if variable_name:
            variable_value = os.getenv(variable_name)
            response = {
                'value': variable_value
            }
            self.finish(response)
        else:
            self.set_status(400)
            self.finish({'error': 'Variable name is required.'})