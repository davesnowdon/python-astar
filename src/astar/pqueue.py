
class PriorityQueueElement(object):
    def __init__(self, priority, value):
        self.priority = priority
        self.value = value

class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def add(self, priority, value):
        element = PriorityQueueElement(priority, value)
        self.queue.append(element)
        self.__sort__()

    def add_update(self, priority, value):
        elem = self.__find__(value)
        if elem:
            elem.priority = priority
            self.__sort__()
        else:
            self.add(priority, value)

    def update_priority(self, new_priority, value):
        elem = self.__find__(value)
        if elem:
            elem.priority = priority
            self.__sort__()
        else:
            raise IndexError()

    def remove(self, value):
        raise NotImplementedError()

    def pop(self):
        if len(self.queue) > 0:
            elem = self.queue[0]
            self.queue = self.queue[1:]
            return elem.value
        else:
            raise IndexError("empty queue")

    def peek(self):
        if len(self.queue) > 0:
            return self.queue[0].value
        else:
            return None

    def __find__(self, value):
        return next((x for x in self.queue if x.value == value), None)

    def __sort__(self):
        self.queue = sorted(self.queue, key=lambda e : e.priority)

    def __len__(self):
        return self.queue.__len__()
