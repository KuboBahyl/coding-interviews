# you are given class Moving Average. Impelement self.update() and self.average(), both in O(1)
class MA(object):
    def __init__(self, maxsize=0):
        self.maxsize = maxsize
        self.size = 0
        self.queue = [None] * maxsize
        self.front = 0
        self.back = -1
        self.avg = 0
        self.lost_recently = None

    def update(self, new_value):
        self.back = (self.back + 1) % self.maxsize
        if self.back == self.front:
            self.lost_recently = self.queue[self.back]
        self.queue[self.back] = new_value

        if self.size < self.maxsize:
            self.size += 1
        else:
            self.front = (self.front + 1) % self.maxsize

    def average(self):
        if not self.lost_recently:
            queue_sum = self.avg * (self.size - 1) + self.queue[self.back]
            self.avg = queue_sum / self.size
            return self.avg
        else:
            self.avg += (self.queue[self.back] - self.lost_recently) / self.maxsize
            return self.avg


# Time: update O(1) + average O(1)
ma = MA(5)
for i in range(1, 20):
    ma.update(i)
    print(ma.average())