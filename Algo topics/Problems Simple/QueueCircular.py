# Queue - insert into circular queue
def circular_insert(queue, data):
    # empty queue
    if queue.front is None:
        self.front = self.back = 0

    # full queue
    if (queue.back + 1) % queue.size == queue.front:
        return print("Queue overflow!")

    # boundary case
    elif queue.back == queue.size - 1:
        queue.back = 0
    else:
        queue.back += 1

    queue[queue.back] = data