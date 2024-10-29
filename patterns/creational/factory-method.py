from __future__ import annotations

import random
from abc import ABC, abstractmethod

printers_history = []
print_history = []


class AbstractPrinter(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def __repr__(self):
        return self.__class__.__name__

    def print_welcome_message(self) -> str:
        product = self.factory_method()
        result = product.print('Welcome message')

        return result


class Printer(AbstractPrinter):
    def factory_method(self) -> AbstractCartridge:
        printers_history.append(f"{self.__class__.__name__}")
        return Cartridge()


class StrangePrinter(AbstractPrinter):
    def factory_method(self) -> AbstractCartridge:
        printers_history.append(f"{self.__class__.__name__}")
        return StrangeCartridge()


class RandomPrinter(AbstractPrinter):
    def factory_method(self) -> AbstractCartridge:
        printers_history.append(f"{self.__class__.__name__}")
        return RandomCartridge()


class AbstractCartridge(ABC):
    def __repr__(self):
        return self.__class__.__name__

    @abstractmethod
    def print(self, text: str) -> str:
        pass


class Cartridge(AbstractCartridge):
    def print(self, text: str) -> str:
        text_to_print = text.strip()
        print_history.append(text_to_print)

        return text_to_print


class StrangeCartridge(AbstractCartridge):
    def print(self, text: str) -> str:
        text_to_print = ''.join(reversed(text)).strip()
        print_history.append(text_to_print)

        return text_to_print


class RandomCartridge(AbstractCartridge):
    def print(self, text: str) -> str:
        letters = list(text)
        random.shuffle(letters)

        text_to_print = ''.join(letters).strip()
        print_history.append(text_to_print)

        return text_to_print


def test_printer(printer: AbstractPrinter) -> None:
    """
    >>> print("App: Launched with the Printer.")
    App: Launched with the Printer.
    >>> test_printer(Printer())
    Welcome message
    >>> print("App: Launched with the StrangePrinter.")
    App: Launched with the StrangePrinter.
    >>> test_printer(StrangePrinter())
    egassem emocleW

    >>> RandomPrinter().factory_method()
    RandomCartridge

    >>> print('Print history:')
    Print history:
    >>> print(*print_history, sep='\\n')
    Welcome message
    egassem emocleW

    >>> print('Printers history:')
    Printers history:
    >>> print(*printers_history, sep='\\n')
    Printer
    StrangePrinter
    RandomPrinter
    """
    print(printer.print_welcome_message())


if __name__ == '__main__':
    test_printer(Printer())
    test_printer(StrangePrinter())
    test_printer(RandomPrinter())
