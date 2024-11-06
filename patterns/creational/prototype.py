from __future__ import annotations

import copy


class Entity:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent: Container):
        self.parent = parent


class Container:
    def __init__(self, integer: int, objects: list, ref: Entity):
        self.int = integer
        self.objects = objects
        self.ref = ref

    def __copy__(self):
        objects = copy.copy(self.objects)
        ref = copy.copy(self.ref)

        new = self.__class__(
            self.int, objects, ref
        )
        new.__dict__.update(self.__dict__)

        return new

    def __deepcopy__(self, memo=None):
        if memo is None:
            memo = {}

        objects = copy.deepcopy(self.objects, memo)
        ref = copy.deepcopy(self.ref, memo)

        new = self.__class__(
            self.int, objects, ref
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memo)

        return new


def main():
    """
    Adding elements to `shallow_copied_container`'s objects adds it to `container`'s objects.
    Changing objects in the `container`'s objects changes that object in `shallow_copied_container`'s objects.
    Adding elements to `deep_copied_container`'s objects doesn't add it to `container`'s objects.
    Changing objects in the `container`'s objects doesn't change that object in `deep_copied_container`'s objects.
    id(deep_copied_container.ref.parent): 140189526982288
    id(deep_copied_container.ref.parent.ref.parent): 140189526982288
    ^^ This shows that deepcopied objects contain same reference, they are not cloned repeatedly.
    """
    objects = [1, {1, 2, 3}, [1, 2, 3]]
    ref = Entity()
    container = Container(23, objects, ref)
    ref.set_parent(container)

    shallow_copied_container = copy.copy(container)

    shallow_copied_container.objects.append("another object")
    if container.objects[-1] == "another object":
        print(
            "Adding elements to `shallow_copied_container`'s "
            "objects adds it to `container`'s objects."
        )
    else:
        print(
            "Adding elements to `shallow_copied_container`'s "
            "objects doesn't add it to `container`'s objects."
        )

    container.objects[1].add(4)
    if 4 in shallow_copied_container.objects[1]:
        print(
            "Changing objects in the `container`'s objects "
            "changes that object in `shallow_copied_container`'s objects."
        )
    else:
        print(
            "Changing objects in the `container`'s objects "
            "doesn't change that object in `shallow_copied_container`'s objects."
        )

    deep_copied_container = copy.deepcopy(container)

    deep_copied_container.objects.append("one more object")
    if container.objects[-1] == "one more object":
        print(
            "Adding elements to `deep_copied_container`'s "
            "objects adds it to `container`'s objects."
        )
    else:
        print(
            "Adding elements to `deep_copied_container`'s "
            "objects doesn't add it to `container`'s objects."
        )

    container.objects[1].add(10)
    if 10 in deep_copied_container.objects[1]:
        print(
            "Changing objects in the `container`'s objects "
            "changes that object in `deep_copied_container`'s objects."
        )
    else:
        print(
            "Changing objects in the `container`'s objects "
            "doesn't change that object in `deep_copied_container`'s objects."
        )

    print(
        f"id(deep_copied_container.ref.parent): "
        f"{id(deep_copied_container.ref.parent)}"
    )
    print(
        f"id(deep_copied_container.ref.parent.ref.parent): "
        f"{id(deep_copied_container.ref.parent.ref.parent)}"
    )
    print(
        "^^ This shows that deepcopied objects contain same reference, they "
        "are not cloned repeatedly."
    )


if __name__ == '__main__':
    main()
