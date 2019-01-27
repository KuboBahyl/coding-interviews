# Queue - delete from priority queue: let it be max
def priority_delete(queue):
    if queue.size == 0:
        return print("Queue underflow!")

    idx_max = 0
    for i in range(self.back + 1):
        if queue.queue[i] > queue.queue[max]:
            max = i

    del queue[max]