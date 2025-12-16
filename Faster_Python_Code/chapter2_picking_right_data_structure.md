# Big O Notation
![img.png](images/Chapter2_Picking_right_data_structure/img.png)
![img_1.png](images/Chapter2_Picking_right_data_structure/img_1.png)
![img_2.png](images/Chapter2_Picking_right_data_structure/img_2.png)

# bisect (log(n))
![img_3.png](images/Chapter2_Picking_right_data_structure/img_3.png)

# deque
![img_4.png](images/Chapter2_Picking_right_data_structure/img_4.png)
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
![img_5.png](images/Chapter2_Picking_right_data_structure/img_5.png)

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

### 4. **Performance Characteristics**
| Operation            | heapq   | deque  |  
|-----------------------|----------|---------|  
| Append to end         | O(log n) | O(1)    |  
| Append to front       | O(log n) | O(1)    |  
| Pop from end          | O(log n) | O(1)    |  
| Pop from front        | O(log n) | O(1)    |  
| Find min/max          | O(1)     | O(n)    |  
| Find arbitrary element| O(n)     | O(n)    |  
  
### 5. When to Choose Which?  
  
#### Choose `heapq` when:  
- You need priority-based processing  
- You want to find top-N or bottom-N elements efficiently  
- You're merging multiple sorted inputs  
- You need real-time median/percentile calculation  
  
#### Choose `deque` when:  
- You need FIFO queue or LIFO stack behavior  
- You want a fixed-size sliding window of recent elements  
- You're implementing producer-consumer patterns  
- You need efficient append/pop at both ends  
- You need thread-safe queue operations

## Hybrid Approach
```python
from collections import deque
import heapq
import time

class PriorityWindowProcessor:
    """Process highest priority items within a time window"""
    def __init__(self, window_size=1000):
        self.heap = []  # Priority queue
        self.window = deque(maxlen=window_size)  # Recent items
        self.counter = 0
        
    def add_item(self, priority, data):
        # Add to both structures
        heapq.heappush(self.heap, (priority, self.counter, data))
        self.window.append((priority, data))
        self.counter += 1
        
    def process_priority(self):
        """Process highest priority item"""
        if self.heap:
            priority, _, data = heapq.heappop(self.heap)
            return f"Processing priority {priority}: {data}"
        return None
    
    def get_recent_items(self):
        """Get items in recent window"""
        return list(self.window)
 ```

## Memory Layout Visualization
```text
heapq (Binary Heap as Array):
Index:  0    1    2    3    4    5    6
Value: [1]  [3]  [2]  [7]  [4]  [5]  [6]
Tree:      1
          / \
         3   2
        / \ / \
       7  4 5  6

deque (Block-based Linked List):
Blocks: [Block1] ↔ [Block2] ↔ [Block3]
         | | |      | | |      | | |
         v v v      v v v      v v v
```

## Common Pitfalls
### heapq Pitfalls:
* Not thread-safe: Requires external locking
* Only min-heap: Need to invert values for max-heap behavior
* No built-in update: Need manual implementation for priority updates
* All operations modify list: May affect other references to the list

### deque Pitfalls:
* No random access optimization: deque[i] is O(n) not O(1)
* No sorting: Need to convert to list for sorting operations
* Memory overhead: More memory per element than list
* Not for priority operations: Poor for finding min/max

## Advanced Usage Pattern
### 1. Combining for Streaming Top-K
```python
class StreamingTopK:
    def __init__(self, k):
        self.k = k
        self.heap = []  # Min-heap of top-k elements
        self.window = deque(maxlen=1000)  # Recent elements
        
    def add(self, value, item):
        # Keep recent items in window
        self.window.append((value, item))
        
        # Maintain top-k in heap
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, (value, item))
        elif value > self.heap[0][0]:
            heapq.heapreplace(self.heap, (value, item))
```

### 2. Priority Queue with Time-based Eviction
```python
class TimePriorityQueue:
    def __init__(self, ttl_seconds=3600):
        self.heap = []
        self.expiry_queue = deque()  # Track insertion times
        
    def push(self, priority, item):
        expiry = time.time() + self.ttl_seconds
        heapq.heappush(self.heap, (priority, expiry, item))
        self.expiry_queue.append((expiry, priority, item))
        
    def pop(self):
        self._clean_expired()
        if self.heap:
            return heapq.heappop(self.heap)
        return None
        
    def _clean_expired(self):
        current = time.time()
        while (self.expiry_queue and 
               self.expiry_queue[0][0] < current):
            self.expiry_queue.popleft()
```

## Summary Table: ETL Application Focus  
  
| ETL Task                  | Recommended Data Structure | Why                                      |  
|---------------------------|----------------------------|------------------------------------------|  
| **Task Scheduling**       | `heapq`                   | Priority-based execution                 |  
| **Data Buffering**        | `deque`                   | FIFO processing, memory limits           |  
| **Sliding Window Aggregation** | `deque(maxlen=N)`         | Automatic window maintenance             |  
| **Top-N Query**           | `heapq`                   | Memory-efficient partial sorting         |  
| **Stream Merging**        | `heapq`                   | Efficient K-way merge                    |  
| **Rate Limiting**         | `deque`                   | Track timestamps in sliding window       |  
| **Data Validation**       | `deque`                   | Maintain recent records for comparison   |  
| **Batch Processing**      | `deque`                   | Queue for producer-consumer pattern      |  
`Beyond above, there are more libraries could leverage, explore by yourself.`