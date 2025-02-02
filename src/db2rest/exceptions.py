class DB2RESTException(Exception):
    """Base exception for DB2REST client"""
    def __init__(self, message, status_code=None, response=None):
        super().__init__(message)
        self.status_code = status_code
        self.response = response