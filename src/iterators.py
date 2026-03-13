
class Groceries:

    def __init__(self, grocery_list: list[str]):
        self.grocery_list = grocery_list

    def __getitem__(self, index):
        return self.grocery_list[index]

    def __len__(self):
        return len(self.grocery_list)

    def __repr__(self):
        return f"Groceries({', '.join(self.grocery_list)})"


class GroceryIterator:

    def _compute_stop_index(self):
        try:
            return self.grocery_list.index("onions")
        except ValueError:
            return len(self.grocery_list)

    def __init__(self, grocery_list: list[str]):
        self.grocery_list = grocery_list
        self.index = 0
        self.stop_index = self._compute_stop_index()

    # note that here we chose to put the iterator in the same object class
    # rather than creating a separate iterator class
    # an alernative would be to create a separate class GroceryIterator
    # then iter would return an instance of that class
    def __iter__(self):
        # reset index for iteration
        self.index = 0
        return self

    def __next__(self):

        # Here we demonstrate an application level halting operation
        # Imagine we could put anything here to break a continuously running
        # loop (although we would want to use an event loop instead)
        if self.index < self.stop_index:
            if self.index >= len(self.grocery_list):
                print("Finished grocery shopping!")
            else:
                print("Ew, gross. Will not buy onions. No more groceries")
            raise StopIteration

        item = self.grocery_list[self.index]
        self.index += 1
        return item

    def __len__(self):
        return self.stop_index

    def __repr__(self):
        return f"Groceries({', '.join(self.grocery_list[:self.stop_index])})"


class GroceryIterable:

    def __init__(self, grocery_list: list[str]):
        self.grocery_list = grocery_list

    # note that here we use instead an iterable pattern
    # instead of returning itself, it instead returns another object
    # that is an iterator (the list)
    # an iterator is always an iterable
    # an iterator must return itself in __iter__
    # an iterable must return an iterator
    def __iter__(self):
        # we create an iterator because a python list
        # is an iterable, not an iterator
        return iter(self.grocery_list)
        return self.grocery_list

    def __len__(self):
        return len(self.grocery_list)

    def __repr__(self):
        return f"Groceries({', '.join(self.grocery_list)})"


def main():
    groceries = Groceries(["milk", "eggs", "bread", "cereal", "onions", "cake"])

    # in a for loop, python first looks for __iter__
    # if that's not present, it looks to __getitem__
    # if that's not present, it raises TypeError
    print("Groceries without halting using getitem")
    for item in groceries:
        print(item)

    print("Groceries with halting using an iterator")
    grocery2 = GroceryIterator(["milk", "eggs", "bread", "cereal", "onions", "cake"])
    for item in grocery2:
        print(item)

    grocery3 = GroceryIterable(["milk", "eggs", "bread", "cereal", "onions", "cake"])
    for item in grocery3:
        print(item)


if __name__ == "__main__":
    main()
