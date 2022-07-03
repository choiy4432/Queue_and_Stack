class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        assert not self.is_empty()
        return self.items.pop()

    def size(self):
        return len(self.items)


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        assert not self.is_empty()
        return self.items.pop()

    def size(self):
        return len(self.items)
      
class Queue_new:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
    

    def is_empty(self):
        return self.stack1.items == [] #스택이 비어있는지 확인하는 함수. 비어있을 경우 True, 아닐 경우 False 를 return 한다.

    def enqueue(self, item):
        
        while len(self.stack1.items) != 0:
            self.stack2.push(self.stack1.pop()) #stack1의 내용이 이미 존재할 경우, 해당 내용들을 하나씩 제거하면서  stack2 에 push
        self.stack1.push(item) #stack1 에 입력받은 item을 push
        while len(self.stack2.items) != 0:
            self.stack1.push(self.stack2.pop()) #기존에 존재했던 stack1 의 item 을 다시 저장한 item 뒤에 push
        
    def dequeue(self):
        assert not self.stack1.is_empty(), "No input" #입력받은 item 이 없을 경우 assertion error 출력
        return self.stack1.pop() #입력받은 item 하나를 pop

    def size(self):
        return len(self.stack1.items) #stack1 의 item 개수를 출력



class Stack_new:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()
    
 
    def is_empty(self):
        return self.queue1.items == [] #큐가 비어있는지 확인하는 함수

    def push(self, item):
        while len(self.queue1.items) != 0:
            self.queue2.enqueue(self.queue1.dequeue())
        self.queue1.enqueue(item)
        while len(self.queue2.items) != 0:
            self.queue1.enqueue(self.queue2.dequeue()) #위의 Queue_new 의 enqueue 함수와 동일

    def pop(self):
        assert not self.queue1.is_empty(), "No input"
        return self.queue1.dequeue() #위의 Queue_new 의 dequeue 함수와 동일

    def size(self):
        return len(self.queue1.items) #queue의 크기를 출력
    
