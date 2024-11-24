from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List


class Navigator:
    def __init__(self, strategy: AbstractRouteBuilder) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> AbstractRouteBuilder:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: AbstractRouteBuilder) -> None:
        self._strategy = strategy

    def build_route(self) -> None:
        result = self._strategy.do_route(["a", "b", "c", "d", "e"])
        print(" -> ".join(result))


class AbstractRouteBuilder(ABC):
    @abstractmethod
    def do_route(self, data: List):
        pass


class RouteBuilder(AbstractRouteBuilder):
    def do_route(self, data: List) -> List:
        return sorted(data)


class RevRouteBuilder(AbstractRouteBuilder):
    def do_route(self, data: List) -> List:
        return list(reversed(sorted(data)))


def main():
    """
    >>> navi = Navigator(RouteBuilder())
    >>> navi.build_route()
    a -> b -> c -> d -> e
    >>>
    >>> navi.strategy = RevRouteBuilder()
    >>> navi.build_route()
    e -> d -> c -> b -> a
    """
    navigator = Navigator(RouteBuilder())
    print("Client: Strategy is set to normal route.")
    navigator.build_route()
    print()

    print("Client: Strategy is set to reverse route.")
    navigator.strategy = RevRouteBuilder()
    navigator.build_route()


if __name__ == "__main__":
    main()
