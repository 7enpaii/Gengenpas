class List:
    def __init__(self):
        self.items = []

    def __contains__(self, item):
        return item in self.items

    def __iter__(self):
        while len(self.items):
            yield self.items.pop(0)

    def __len__(self):
        return len(self.items)

    def append(self, item, front=False):
        for _ in (item, item.lower(), item.title(), item.upper()):
            if _ in self.items:
                continue
            if front:
                self.items.insert(0, _)
            else:
                self.items.append(_)
