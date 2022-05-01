from queue import Queue


rtt_data_queue = Queue()

def batch_enqueue(q,data):
    for v in data:
        q.put(chr(v))

def batch_dequeue(q):
    return [q.get() for i in range(0,q.qsize())]

s = 'afafafaf'

data_q = Queue()


data_q.put(s)

#batch_enqueue(data_q, s)


print(type(data_q.get()))