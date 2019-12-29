class Buffer:
    def __init__(self):
        pass

    def add(self, *a):
        self.buf = []
        for i in a:
            self.buf.append(i)
            if len(self.buf) == 5:
                print(sum(self.buf))
                self.buf.clear()

    def get_current_part(self):
        return(self.buf)