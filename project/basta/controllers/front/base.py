class Front:
    def __call__(self, request=None, response=None):
        self.request = request
        self.response = response

        if self.request and hasattr(self, 'process_request'):
            if response := self.process_request():
                return response

        if self.response and hasattr(self, 'process_response'):
            self.process_response()
