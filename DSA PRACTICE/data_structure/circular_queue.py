class CircularQueue:
    def __init__(self,max_size):
        
        
        self.max_size=max_size
        self.queue=[None]*max_size

        self.front=-1
        self.rear=-1


    def is_full(self):
        return (self.rear+1)%self.max==self.front


    def is_empty(self):
        return self.front==-1
    

    





