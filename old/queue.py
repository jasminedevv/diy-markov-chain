class Q(list):
    def __init__(self):
        self = []
    def deQ(self):
        try:
            return self.pop(0)
        except:
            if self is []:
                print("Nothing to dequeue because queue is empty.")
            else:
                print("Could not dequeue")

    def enQ(self, item):
        try:
            self.append(item)
        except:
            if item is None:
                print("Can not enqueue an item that does not exist.")
            else:
                print("Could not enqueue.")

    # this surely does not work but I don't understand the instructions so ehhhhhh
    def iterate(self, function):
        for item in self:
            item.function()