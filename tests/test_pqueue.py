from astar import PriorityQueue

def test_add_extends_queue():
    queue = PriorityQueue()
    assert len(queue) == 0
    queue.add(5, object())
    queue.add(1, object())
    assert len(queue) == 2

def test_pop_in_prioty_order():
    queue = PriorityQueue()
    queue.add(5, 5)
    queue.add(1, 1)
    first = queue.pop()
    assert first == 1
    second = queue.pop()
    assert second == 5

def test_peek_gets_correct_item():
    queue = PriorityQueue()
    queue.add(5, 5)
    queue.add(1, 1)
    assert queue.peek() == 1

def test_add_update_handles_new_item():
    queue = PriorityQueue()
    queue.add(5, 5)
    queue.add_update(1, 1)
    assert queue.peek() == 1

def test_add_update_changes_priority_of_existing_item():
    queue = PriorityQueue()
    queue.add(5, 5)
    queue.add(1, 1)
    queue.add_update(0, 5)
    assert queue.peek() == 5
