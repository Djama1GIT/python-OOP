from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters


class Originator:
    _state = None

    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Originator: My initial state is: {self._state}")

    def do_something(self) -> None:
        print("Originator: I'm doing something important.")
        self._state = self._generate_random_string(30)
        print(f"Originator: and my state has changed to: {self._state}")

    @staticmethod
    def _generate_random_string(length: int = 10) -> str:
        return "".join(sample(ascii_letters, length))

    def save(self) -> Memento:
        return ConcreteMemento(self._state)

    def restore(self, memento: Memento) -> None:
        self._state = memento.get_state()
        print(f"Originator: My state has changed to: {self._state}")


class Memento(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass

    @abstractmethod
    def get_state(self) -> str:
        pass


class ConcreteMemento(Memento):
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self) -> str:
        return self._state

    def get_name(self) -> str:
        return f"{self._date} / ({self._state[0:9]}...)"

    def get_date(self) -> str:
        return self._date


class Caretaker:
    def __init__(self, originator: Originator) -> None:
        self._mementos = []
        self._originator = originator

    def backup(self) -> None:
        print("\nCaretaker: Saving Originator's state...")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Caretaker: Restoring state to: {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        print("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.get_name())


if __name__ == "__main__":
    originator = Originator("Super")  # Originator: My initial state is: Super
    caretaker = Caretaker(originator)

    caretaker.backup()  # Caretaker: Saving Originator's state...
    originator.do_something()  # Originator: I'm doing something important.
    # Originator: and my state has changed to: fFTNvIKsSyHlcJRqeijaAzoCZbQwXu

    caretaker.backup()  # Caretaker: Saving Originator's state...
    originator.do_something()  # Originator: I'm doing something important.
    # Originator: and my state has changed to: uNklOBKvwmeToyzbnafWFSZEisdXxM

    caretaker.backup()  # Caretaker: Saving Originator's state...
    originator.do_something()  # Originator: I'm doing something important.
    # Originator: and my state has changed to: cmHavCArltYeJNQyPgFXisTuhUnwWR

    print()
    caretaker.show_history()  # Caretaker: Here's the list of mementos:
    # 2025-01-01 18:47:56 / (Super...)
    # 2025-01-01 18:47:56 / (fFTNvIKsS...)
    # 2025-01-01 18:47:56 / (uNklOBKvw...)

    print("\nClient: Now, let's rollback!\n")
    caretaker.undo()  # Caretaker: Restoring state to: 2025-01-01 18:47:56 / (uNklOBKvw...)
    # Originator: My state has changed to: uNklOBKvwmeToyzbnafWFSZEisdXxM

    print("\nClient: Once more!\n")
    caretaker.undo()  # Caretaker: Restoring state to: 2025-01-01 18:47:56 / (fFTNvIKsS...)
    # Originator: My state has changed to: fFTNvIKsSyHlcJRqeijaAzoCZbQwXu
