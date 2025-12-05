# Futures    
# Future（未来对象/未来值）  
  
Asynchronous tasks allow multiple operations to be accomplished simultaneously.    
异步任务允许多个操作同时进行。  
  
Futures are a mechanism for handling the results of asynchronous operations.    
Future 是一种用于处理异步操作结果的机制。  
  
It acts as a placeholder for a result that will be available at a later time.    
它充当一个将来可用结果的占位符。  
  
A future is like an "I owe you" note for the result of an asynchronous task.    
Future 就像一张“我欠你”的便条，表示任务完成后会给出结果。  
  
---  
  
## Analogy: Future in Action    
## 类比：Future 的实际应用  
  
Barron and Olivia demonstrate a future in action using a kitchen analogy:    
Barron 和 Olivia 用厨房的例子演示 Future 的概念：  
  
- Barron asks Olivia to count vegetables in the pantry, representing an asynchronous task    
  Barron 让 Olivia 去储藏室数蔬菜，表示一个异步任务  
- Olivia provides an "I owe you" note (future) before leaving to complete the task    
  Olivia 在离开完成任务前，留下一张“我欠你”的便条（Future）  
- Barron continues with other work while holding onto the future    
  Barron 持有 Future，可以继续做其它工作  
- Olivia eventually returns with the result (zero vegetables), fulfilling the promise    
  Olivia 最终带着结果（没有蔬菜）回来，兑现了承诺  
- The resolved future allows Barron to make a decision (to go to the store)    
  Future 被兑现后，Barron 可以据此决定（去商店买菜）  
  
---  
  
## Working with Futures    
## 使用 Future  
  
- Futures are read-only and may not have an immediate result    
  Future 对象是只读的，结果可能不会立即可用  
- A thread might need to wait for the future to be resolved    
  线程可能需要等待 Future 被兑现（即结果可用）  
- "Resolving" or "fulfilling" a future means writing the result value to it    
  “兑现”或“完成” Future 指的是将结果写入 Future 对象  