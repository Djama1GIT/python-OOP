from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request: Any) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def handle(self, request: Any) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class AuthenticationHandler(AbstractHandler):
    def handle(self, request: dict) -> Optional[str]:
        if not request.get('authenticated'):
            return "AuthenticationHandler: Authentication failed"
        return super().handle(request)


class AuthorizationHandler(AbstractHandler):
    def handle(self, request: dict) -> Optional[str]:
        if not request.get('authorized'):
            return "AuthorizationHandler: Authorization failed"
        return super().handle(request)


class RateLimitHandler(AbstractHandler):
    def __init__(self, max_requests: int):
        self.max_requests = max_requests
        self.current_requests = 0

    def handle(self, request: dict) -> Optional[str]:
        if self.current_requests >= self.max_requests:
            return "RateLimitHandler: Rate limit exceeded"
        self.current_requests += 1
        return super().handle(request)


class LoggingHandler(AbstractHandler):
    def handle(self, request: dict) -> Optional[str]:
        print(f"LoggingHandler: Logging request: {request}")
        return super().handle(request)


class ErrorHandler(AbstractHandler):
    def handle(self, request: dict) -> Optional[str]:
        return "ErrorHandler: Error occurred during processing"


def client_code(handler: Handler) -> None:
    requests = [
        {'authenticated': True, 'authorized': True},
        {'authenticated': False, 'authorized': True},
        {'authenticated': True, 'authorized': False},
        {'authenticated': True, 'authorized': True}
    ]

    for i, request in enumerate(requests):
        print(f"\nClient: Sending request {i + 1}: {request}")
        result = handler.handle(request)
        if result:
            print(f"  {result}")
        else:
            print("  Request processed successfully")


if __name__ == "__main__":
    auth_handler = AuthenticationHandler()
    authz_handler = AuthorizationHandler()
    rate_limit_handler = RateLimitHandler(max_requests=2)
    logging_handler = LoggingHandler()
    error_handler = ErrorHandler()

    auth_handler.set_next(authz_handler).set_next(rate_limit_handler).set_next(logging_handler).set_next(error_handler)

    print("Full chain: Authentication > Authorization > Rate Limit > Logging > Error")
    client_code(auth_handler)
    # Client: Sending request 1: {'authenticated': True, 'authorized': True}
    # LoggingHandler: Logging request: {'authenticated': True, 'authorized': True}
    #   ErrorHandler: Error occurred during processing
    #
    # Client: Sending request 2: {'authenticated': False, 'authorized': True}
    #   AuthenticationHandler: Authentication failed
    #
    # Client: Sending request 3: {'authenticated': True, 'authorized': False}
    #   AuthorizationHandler: Authorization failed
    #
    # Client: Sending request 4: {'authenticated': True, 'authorized': True}
    # LoggingHandler: Logging request: {'authenticated': True, 'authorized': True}
    #   ErrorHandler: Error occurred during processing

    print("\n\nPartial chain: Authorization > Rate Limit > Logging > Error")
    client_code(authz_handler)
    # Client: Sending request 1: {'authenticated': True, 'authorized': True}
    #   RateLimitHandler: Rate limit exceeded
    #
    # Client: Sending request 2: {'authenticated': False, 'authorized': True}
    #   RateLimitHandler: Rate limit exceeded
    #
    # Client: Sending request 3: {'authenticated': True, 'authorized': False}
    #   AuthorizationHandler: Authorization failed
    #
    # Client: Sending request 4: {'authenticated': True, 'authorized': True}
    #   RateLimitHandler: Rate limit exceeded
