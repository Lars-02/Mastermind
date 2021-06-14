from .app.controller import HelloWorld


class Routes:
    def __init__(self, api):
        api.add_resource(HelloWorld, '/')
