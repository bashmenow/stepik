class PositivList(list):
    def append(self, x):
        if x <= 0:
            raise NonPositiveError
        else:
            super().append(x)


class NonPositiveError(Exception):
    pass

