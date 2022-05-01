from queue import Queue


rtt_data_queue = Queue()

def batch_enqueue(q,data):
    for v in data:
        q.put(chr(v))

def batch_dequeue(q):
    return [q.get() for i in range(0,q.qsize())]

s = [0x30,0x31,0x32,0x33,0x34,0x35]

data_q = Queue()


batch_enqueue(data_q, s)

print(''.join(batch_dequeue(data_q)))