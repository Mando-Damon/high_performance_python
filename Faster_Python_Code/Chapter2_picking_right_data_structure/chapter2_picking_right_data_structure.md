# Big O Notation
![img.png](img.png)
![img_1.png](img_1.png)
![img_2.png](img_2.png)

# bisect (log(n))
![img_3.png](img_3.png)

# deque
![img_4.png](img_4.png)
## Scenarios for Using deque

### 1. If you need to maintain a sliding window or the most recent N records:  
sliding_window = deque(maxlen=N)  
  
### 2. If you need an efficient producer-consumer queue:  
queue = deque()  
queue.append(item)         # Producer adds an item  
item = queue.popleft()     # Consumer retrieves an item  
  
### 3. If you need to limit memory usage and automatically discard old data:  
fixed_size_queue = deque(maxlen=fixed_size)  
  
### 4. If you need queue operations in a multithreaded environment:  
thread_safe_queue = deque()  
  
## Scenarios for NOT Using deque  
### 1. If you need random access to elements in the middle:  
random_access_list = [1, 2, 3, 4]  
element = random_access_list[2]  # Access an element at index 2  
  
### 2. If you need sorting or prioritization:  
import heapq  
priority_queue = []  
heapq.heappush(priority_queue, (priority, item))  # Add item with priority  
highest_priority_item = heapq.heappop(priority_queue)  # Remove highest-priority item  
  
### 3. If you only need a simple LIFO stack:  
lifo_stack = []  
lifo_stack.append(item)  # Push item to stack  
item = lifo_stack.pop()  # Pop item from stack  

# heapq
![img_5.png](img_5.png)

```python
import heapq

data = [3, 1, 4, 1, 5, 9, 2, 6]
heapq.heapify(data)  # inplace change to heap 
# data: [1, 1, 2, 3, 5, 9, 4, 6]
# heap[0] always the minimum
```
## heapq Big O
* heappush() - O(log n)
* heappop() - O(log n)
* heap[0] - O(1)
* heapify() - O(n)

## heapq vs deque Comparison

| Feature | heapq | deque |
|---------|-------|-------|
| **Data Structure** | Binary Heap (Min-Heap) | Double-Ended Queue |
| **Access Min/Max** | O(1) access to smallest element | O(1) access to both ends |
| **Insertion/Deletion** | O(log n) push/pop | O(1) at both ends |
| **Random Access** | Not supported | Supported but O(n) |
| **Ordering Property** | Partially ordered (heap property) | No ordering |
| **Memory Usage** | In-place operations, memory efficient | Extra pointer overhead |
| **Thread Safety** | No (requires external locking) | Yes (atomic operations) |
| **Typical Use Cases** | Priority queue, Top-N, merging sorted streams | Queue, stack, buffer, sliding window |
| **Built-in Size Limit** | No | Yes (`maxlen` parameter) |
| **Element Removal** | Only min element (O(log n)) | Any end (O(1)) |
| **Sorting** | Maintains heap invariant | No sorting capabilities |
| **Best For** | Priority-based processing, partial sorting | Sequential processing, FIFO/LIFO operations |

## Key Differences Explained

### 1. **Data Structure**
- **heapq**: Binary tree stored as array, maintaining heap property
- **deque**: Linked list of blocks, optimized for append/pop at both ends

### 2. **Access Patterns**
- **heapq**: Always access smallest element via `heap[0]`
- **deque**: Access both front and back via `[0]` and `[-1]`

### 3. **Use Case Scenarios**
```python
# heapq: When you need priority-based processing
import heapq
tasks = []
heapq.heappush(tasks, (2, "Low priority task"))
heapq.heappush(tasks, (1, "High priority task"))
heapq.heappop(tasks)  # Returns (1, "High priority task")

# deque: When you need queue/stack behavior
from collections import deque
queue = deque()
queue.append("item1")  # Enqueue
queue.popleft()        # Dequeue
stack = deque()
stack.append("item1")  # Push
stack.pop()            # Pop
```

Beyond above, there are more libraries could leverage, explore by yourself.