from typing import Union, Generator


class UniqueIterator:
    class GenericItem:
        def __init__(self, e):
            self.value = e

        def __hash__(self):
            return self.value.__hash__()

        def __eq__(self, other):
            return self.value == other.value

    class StringItem(GenericItem):
        def __init__(self, item: str, ignore_case: bool = False):
            super().__init__(item)
            self.ignore_case = ignore_case

        def __hash__(self) -> int:
            key = self.value if not self.ignore_case else self.value.lower()
            return key.__hash__()

        def __eq__(self, other) -> bool:
            return self.value == other.value if not self.ignore_case else self.value.lower() == other.value.lower()

    def __init__(self, obj: Union[list, Generator], ignore_case: bool = False, **kwargs):
        items = [
            UniqueIterator.StringItem(e, ignore_case)
            if isinstance(e, str)
            else
            UniqueIterator.GenericItem(e)
            for e in obj
        ]
        self._unique_items = iter([e.value for e in set(items)])

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._unique_items)
