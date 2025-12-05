# Sequential vs. Parallel Computing 顺序计算与并行计算  
  
## Sequential Computing 顺序计算  
  
Sequential computing is the traditional programming approach where instructions are executed one after another by a single processor, with only one instruction being executed at a time; the processor's capabilities limit the speed of execution.  
  
顺序计算是一种传统的编程方式，指令由单个处理器依次执行，每次只执行一条指令；处理器的性能限制了执行速度。  
  
Barron illustrated this concept as a single cook making a salad, which took him three minutes to complete.  
  
巴伦用一个厨师独自制作沙拉来说明这一概念，他花了三分钟完成。  
  
---  
  
## Parallel Computing 并行计算  
  
Parallel computing utilizes multiple processors working simultaneously on different parts of a task; this approach breaks down tasks into independent parts that can be executed in parallel.  
  
并行计算利用多个处理器同时处理任务的不同部分；这种方法将任务拆分为可以同时执行的独立部分。  
  
Barron and Olivia demonstrated this concept as two cooks computing in parallel to make a salad, which took them two minutes to complete—less time than it took Barron to make a salad alone using sequential computing.  
  
巴伦和奥利维亚演示了这一概念，两位厨师并行制作沙拉，仅用两分钟就完成了——比巴伦单独顺序制作沙拉的时间还短。  
  
---  
  
## Advantages of Parallel Computing 并行计算的优势  
  
- Parallel computing significantly increases the overall throughput of a program by enabling faster completion of large or complex tasks that would be impractical for a single processor; it enables the computer to accomplish more tasks in a given amount of time.  
  
  并行计算能够更快完成单个处理器难以应对的大型或复杂任务，显著提升了程序的整体吞吐量，使计算机在有限时间内完成更多任务。  
  
- Parallel computing leveraging multiple processors makes it possible to solve problems too large or complex for a single processor; in many industries, the time saved using parallel computing often outweighs the costs of investing in specialized hardware.  
  
  利用多处理器的并行计算可以解决单个处理器无法处理的庞大或复杂问题；在许多行业中，采用并行计算节省的时间通常远超投资专用硬件的成本。  
  
---  
  
## Challenges of Parallel Computing 并行计算的挑战  
  
- Implementing parallel computing increases the complexity of programming, requiring careful coordination between processors to ensure efficient execution; adding more processors doesn't always result in a proportional increase in speed due to coordination overhead.  
  
  实现并行计算会增加编程的复杂性，需要处理器之间的精细协调以确保高效执行；增加处理器数量并不总能带来成比例的速度提升，因为协调会带来额外开销。  
  
- There may be waiting times between dependent tasks, which can affect overall performance.  
  
  依赖任务之间可能会出现等待，从而影响整体性能。  
  
---  
  
## Real-World Applications 实际应用  
  
- Web search engines are one example of a real-world application that uses parallel computing to process millions of transactions every second.  
  
  网络搜索引擎就是一个利用并行计算每秒处理数百万请求的现实应用实例。  
  
- Many other industries leverage parallel computing, where time savings translate directly to cost savings.  
  
  许多其他行业也在利用并行计算，将节省的时间直接转化为成本优势。  
  
---  
  
## Key Takeaways 关键要点  
  
- Parallel computing offers significant performance benefits for tasks that can be effectively parallelized.  
  
  并行计算为那些能够高效并行化的任务带来了显著性能提升。  
  
- Implementing parallel solutions requires careful planning and coordination to overcome inherent challenges.  
  
  实施并行方案需要细致的规划和协调，以克服其固有的挑战。  
  
- Parallel computing has grown in importance across various industries due to its ability to handle complex, data-intensive tasks; it is essential for solving large-scale computing problems in modern applications.  
  
  并行计算因其能处理复杂和数据密集型任务，在各行各业变得越来越重要；它是解决现代应用中大规模计算问题的关键技术。  