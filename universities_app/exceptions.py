class DeadlineNotFitException(Exception):
    def __init__(self, message="Deadline does not fit the criteria"):
        self.message = message
        super().__init__(self.message)