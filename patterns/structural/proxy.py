from abc import ABC, abstractmethod
from random import random
from time import time, sleep


class AbstractSubject(ABC):
    @abstractmethod
    def request(self) -> None:
        pass


class Subject(AbstractSubject):
    def request(self) -> None:
        print("RealSubject: Handling request.")


class Proxy(AbstractSubject):
    def __init__(self, real_subject: Subject) -> None:
        self._real_subject = real_subject
        self.start_time = None

    def request(self) -> None:
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        self.start_time = time()
        sleep(random())
        return True

    def log_access(self) -> None:
        print(f"Proxy: Logging the time of request took {time() - self.start_time:2f} seconds.")


def client_code(subject: AbstractSubject) -> None:
    # ...

    subject.request()

    # ...


if __name__ == "__main__":
    print("Client: Executing the client code with a real subject:")
    real_subject = Subject()
    client_code(real_subject)  # Client: Executing the client code with a real subject:
    # RealSubject: Handling request.

    print("")

    print("Client: Executing the same client code with a proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)  # Proxy: Checking access prior to firing a real request.
    # RealSubject: Handling request.
    # Proxy: Logging the time of request took 0.737962 seconds.
