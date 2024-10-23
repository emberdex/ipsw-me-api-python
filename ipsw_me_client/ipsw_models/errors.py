class NotFoundError(Exception):
    def __init__(self, resource_type: str):
        super().__init__(f'No {resource_type} found.')


class APIServerError(Exception):
    def __init__(self, status_code: int):
        super().__init__(f'Server error occurred when invoking ipsw.me API: HTTP {status_code}')
