class Target:
    def request(self) -> str:
        return "Target: The default target's behavior."


class Adaptee:
    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target):
    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"


def client_code(target: Target) -> None:
    print(target.request())


def main() -> None:
    """
    >>> print("Client: I can work just fine with the Target objects:")
    Client: I can work just fine with the Target objects:
    >>> target = Target()
    >>> client_code(target)
    Target: The default target's behavior.
    >>>
    >>>
    >>> adaptee = Adaptee()
    >>> print("Client: The Adaptee class has a weird interface. See, I don't understand it:")
    Client: The Adaptee class has a weird interface. See, I don't understand it:
    >>> print(f"Adaptee: {adaptee.specific_request()}")
    Adaptee: .eetpadA eht fo roivaheb laicepS
    >>> print("Client: But I can work with it via the Adapter:")
    Client: But I can work with it via the Adapter:
    >>> adapter = Adapter(adaptee)
    >>> client_code(adapter)
    Adapter: (TRANSLATED) Special behavior of the Adaptee.
    """
    target = Target()
    client_code(target)
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    client_code(adapter)


if __name__ == "__main__":
    main()
