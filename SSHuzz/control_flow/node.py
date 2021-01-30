class Node:

    def __init__(self, block_id: int, addr: int):
        self.id = block_id
        self.addr = addr
        self.parents = set()
        self.children = set()
