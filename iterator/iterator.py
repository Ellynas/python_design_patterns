from typing import Optional, Iterator, Iterable


class Node(Iterable):
    def __init__(self, value, left: Optional["Node"] = None, right: Optional["Node"] = None):
        self.right = right
        self.left = left
        self.value = value

        self.parent: Optional[Node] = None

        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

    def __iter__(self) -> Iterator["Node"]:
        return InOrderIterator(self)


class InOrderIterator(Iterator):
    """
    problem with that : it cannot be recursive, leading to a more complicated implementation
    """
    def __init__(self, root: Node):
        self.root: Node = root
        self.current: Node = self.root
        self.yielded_start = False
        while self.current.left:
            self.current = self.current.left

    def __next__(self) -> Node:
        if not self.yielded_start:
            self.yielded_start = True
            return self.current

        if self.current.right:
            self.current = self.current.right
            while self.current.left:
                self.current = self.current.left
            return self.current
        else:
            p = self.current.parent
            while p and self.current == p.right:
                self.current = p
                p = p.parent
            if p:
                self.current = p
                return self.current
            else:
                raise StopIteration


def traverse_in_order(root: Node):
    """
    recursive implem
    """
    def traverse(current: Node) -> Iterator[Node]:
        if current.left:
            for left in traverse(current.left):
                yield left
        yield current
        if current.right:
            for right in traverse(current.right):
                yield right

    for node in traverse(root):
        yield node


if __name__ == "__main__":
    #   1
    #  / \
    # 2   3

    # in-order: 213
    # preorder: 123
    # postorder: 231

    ROOT = Node(1, Node(2), Node(3))

    # manualy iterate
    IT = iter(ROOT)
    print([next(IT).value for _ in range(3)])

    # iterate using synthax sugar (implicit)
    for x in ROOT:
        print(x.value)

    # iterate using a recursive method
    for y in traverse_in_order(ROOT):
        print(y.value)
