# Local caching of names
 
In Python, accessing global variables can be slower than accessing local variables due to the way Python handles

Below normalize2 is faster than normalize1 bcos line #21/22 saving global variables locally to avoid repeated global lookups
 ![img.png](images/Chapter3_Tricks_of_the_Trade/img.png)
 
Below normalize3 is faster than normalize2 because it caches the append function
 ![img_1.png](images/Chapter3_Tricks_of_the_Trade/img_1.png)

# Remove function calls
`TANSTAAFL: There Ain't No Such Thing As A Free Lunch`

In this example, after removing function calls, the code runs faster.
![img_2.png](images/Chapter3_Tricks_of_the_Trade/img_2.png)
![img_4.png](images/Chapter3_Tricks_of_the_Trade/img_4.png)

Another example, do not user properties unless you have a good reason
![img_3.png](images/Chapter3_Tricks_of_the_Trade/img_3.png)
![img_5.png](images/Chapter3_Tricks_of_the_Trade/img_5.png)

# Using Slots
Using `__slots__` can save memory and speed up attribute access by preventing the creation of a default `__dict__` for each instance.
Downside is you cannot add new attributes dynamically.

![img_6.png](images/Chapter3_Tricks_of_the_Trade/img_6.png)
![img_7.png](images/Chapter3_Tricks_of_the_Trade/img_7.png)

# Using built-in functions
![img_9.png](images/Chapter3_Tricks_of_the_Trade/img_9.png)
![img_8.png](images/Chapter3_Tricks_of_the_Trade/img_8.png)
use itemgetter to speed up item access in sorting, there is also attrgetter for getting attributes
![img_10.png](images/Chapter3_Tricks_of_the_Trade/img_10.png)

# Allocate
Pre-allocate lists to avoid dynamic resizing during appends.
![img_11.png](images/Chapter3_Tricks_of_the_Trade/img_11.png)
![img_12.png](images/Chapter3_Tricks_of_the_Trade/img_12.png)
Be cautious to use immutable values in initialization to avoid unintended side effects.
![img_13.png](images/Chapter3_Tricks_of_the_Trade/img_13.png)
Numpy has ultra fast array operations
![img_14.png](images/Chapter3_Tricks_of_the_Trade/img_14.png)
