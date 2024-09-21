class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        return self.priority < other.priority
def insert(heap, task):
    heap.append(task)
    i = len(heap) - 1
    while i > 0 and heap[i] < heap[(i - 1) // 2]:
        heap[i], heap[(i - 1) // 2] = heap[(i - 1) // 2], heap[i]
        i = (i - 1) // 2
def extract_min(heap):
    if len(heap) == 0:
        return None
    if len(heap) == 1:
        return heap.pop()

    root = heap[0]
    heap[0] = heap.pop()
    heapify(heap, 0)
    return root
def decrease_key(heap, i, new_priority):
    heap[i].priority = new_priority
    while i > 0 and heap[i] < heap[(i - 1) // 2]:
        heap[i], heap[(i - 1) // 2] = heap[(i - 1) // 2], heap[i]
        i = (i - 1) // 2
def is_empty(heap):
    return len(heap) == 0
