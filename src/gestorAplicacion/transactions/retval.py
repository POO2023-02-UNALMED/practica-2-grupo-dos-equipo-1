class Retval:
    def __init__(self, message="", ok=False):
        self.message = message
        self.ok = ok

    def getMessage(self):
        return self.message

    def isOk(self):
        return self.ok
