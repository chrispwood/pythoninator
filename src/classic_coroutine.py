import pathlib
from collections.abc import Generator
from dataclasses import dataclass
from typing import Union

@dataclass
class GroceryList:
    items: list[str]

    def __repr__(self):
        return "\n".join(
            f"  {index}. {item}"
            for index, item in enumerate(self.items, start=1)
        )


class Sentinel:
    def __repr__(self):
        return '<Sentinel>'


STOP = Sentinel()
SendType = Union[str, Sentinel]


def grocery_list_coroutine(verbose: bool = True) -> Generator[None, SendType, GroceryList]:
    """
    A coroutine that collects grocery items.
    """
    groc_list = GroceryList([])

    while True:
        item = yield # we don't return the list in the yield. This pattern simply collects items
        if isinstance(item, Sentinel):
            break
        if verbose:
            print(f"Adding {item} to the grocery list.")
        groc_list.items.append(item)

    return groc_list


def finalize_coroutine(coroutine: Generator[None, SendType, GroceryList]) -> GroceryList:
    try:
        coroutine.send(STOP)
    except StopIteration as e:
        return e.value

def main():
    # Calculate path relative to the script file
    script_path = pathlib.Path(__file__).resolve()
    # Assuming grocery_list.txt is in the project root, one level up from 'src'
    file_path = script_path.parent.parent / "grocery_list.txt"

    result = None

    coroutine_groceries = grocery_list_coroutine(False)
    next(coroutine_groceries) # advance to first yield

    try:
        with open(file_path, "r") as file:
            for line in file:
                item = line.strip()

                if item.lower() == 'onions':
                    print("ew, onions. No more groceries.")
                    break

                coroutine_groceries.send(item)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

    result = finalize_coroutine(coroutine_groceries)

    print(f"Your grocery list is:\n{result}")


if __name__ == "__main__":
    main()
