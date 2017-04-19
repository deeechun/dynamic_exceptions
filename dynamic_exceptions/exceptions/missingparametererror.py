from error import Error

class MissingParamError(Error):

    def __init__(self, err_msg):
        self.err_msg = err_msg

    def __str__(self):
        return str(self.err_msg)
