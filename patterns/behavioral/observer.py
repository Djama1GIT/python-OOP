from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass


class Store(Subject):
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def buy_new_books(self) -> None:
        self.notify()

    def __repr__(self):
        return f"Store [Observers: {len(self._observers)}]"


class Man(Observer):
    def update(self, subject: Subject) -> None:
        print("Man: Reacted to the event")


class SubStore(Observer):
    def update(self, subject: Subject) -> None:
        print("SubStore: Reacted to the event")


def main():
    """
    >>> (store := Store())
    Store [Observers: 0]
    >>>
    >>> man = Man()
    >>> store.attach(man)
    Subject: Attached an observer.
    >>>
    >>> sub_store = SubStore()
    >>> store.attach(sub_store)
    Subject: Attached an observer.
    >>>
    >>> store
    Store [Observers: 2]
    >>> store.buy_new_books()
    Man: Reacted to the event
    SubStore: Reacted to the event
    >>> store.buy_new_books()
    Man: Reacted to the event
    SubStore: Reacted to the event
    >>>
    >>> store.detach(man)
    >>> store
    Store [Observers: 1]
    >>>
    >>> store.buy_new_books()
    SubStore: Reacted to the event
    """
    store_ = Store()

    man_ = Man()
    store_.attach(man_)

    store_.buy_new_books()


if __name__ == '__main__':
    main()
