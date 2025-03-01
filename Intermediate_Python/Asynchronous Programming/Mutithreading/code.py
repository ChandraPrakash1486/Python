import threading
import time
import queue
import concurrent.futures

###########################################################
# Basic Threading - Using threading.Thread class directly #
###########################################################

def basic_thread_function(name, delay):
    """
    A basic function to be executed in a thread.
    
    Args:
        name: Name of the thread
        delay: Time to sleep between prints
    """
    print(f"Thread {name}: starting")
    time.sleep(delay)
    print(f"Thread {name}: finishing")

# Create thread objects
thread1 = threading.Thread(target=basic_thread_function, args=("One", 2))
thread2 = threading.Thread(target=basic_thread_function, args=("Two", 4))

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()

print("All basic threads done!")

###############################################
# Thread with a class that inherits Thread    #
###############################################

class MyThread(threading.Thread):
    """Custom thread class that inherits from threading.Thread."""
    
    def __init__(self, name, delay):
        """
        Initialize the thread.
        
        Args:
            name: Name of the thread
            delay: Sleep time between prints
        """
        threading.Thread.__init__(self)  # Call parent constructor
        self.name = name
        self.delay = delay
    
    def run(self):
        """Override the run method - executed when the thread starts."""
        print(f"Custom Thread {self.name}: starting")
        time.sleep(self.delay)
        print(f"Custom Thread {self.name}: finishing")

# Create and start custom thread objects
custom_thread1 = MyThread("A", 1)
custom_thread2 = MyThread("B", 2)

custom_thread1.start()
custom_thread2.start()

custom_thread1.join()
custom_thread2.join()

print("All custom threads done!")

####################################
# Thread Synchronization with Lock #
####################################

# Shared resource
counter = 0
counter_lock = threading.Lock()  # Create a lock object

def increment_counter(amount, repeats):
    """
    Increment a shared counter with lock protection.
    
    Args:
        amount: Amount to increment by each time
        repeats: Number of times to increment
    """
    global counter
    
    for _ in range(repeats):
        # Acquire the lock before accessing shared resource
        counter_lock.acquire()
        try:
            # Critical section - only one thread can execute this at a time
            counter += amount
            # Simulate some work
            time.sleep(0.001)
        finally:
            # Ensure the lock is released even if an exception occurs
            counter_lock.release()

# With statement context manager syntax for locks (cleaner approach)
def increment_with_context(amount, repeats):
    """Increment counter using lock with context manager."""
    global counter
    
    for _ in range(repeats):
        with counter_lock:  # Automatically acquires and releases the lock
            counter += amount
            time.sleep(0.001)

# Create and start threads for synchronized increment
thread_inc1 = threading.Thread(target=increment_with_context, args=(1, 100))
thread_inc2 = threading.Thread(target=increment_with_context, args=(2, 100))

thread_inc1.start()
thread_inc2.start()

thread_inc1.join()
thread_inc2.join()

print(f"Final counter value: {counter}")

#########################################
# RLock (Reentrant Lock) Demonstration #
#########################################

# RLock allows the same thread to acquire the lock multiple times
reentrant_lock = threading.RLock()

def outer_function():
    """Function that acquires the lock and calls another function."""
    with reentrant_lock:
        print("Outer function acquired lock")
        inner_function()  # This would deadlock with a regular Lock

def inner_function():
    """Function that also tries to acquire the same lock."""
    with reentrant_lock:  # With RLock, this is allowed for the same thread
        print("Inner function also acquired lock")

# Demonstrate RLock
thread_rlock = threading.Thread(target=outer_function)
thread_rlock.start()
thread_rlock.join()

#####################################
# Thread Communication with Events  #
#####################################

# Event object to signal between threads
event = threading.Event()

def waiter():
    """Thread that waits for an event to be set."""
    print("Waiter: Waiting for event")
    event.wait()  # Block until the event is set
    print("Waiter: Event received, proceeding")

def setter():
    """Thread that sets an event after a delay."""
    print("Setter: Sleeping before setting event")
    time.sleep(2)
    print("Setter: Setting event")
    event.set()  # Set the event, unblocking all waiting threads

# Create and start the threads
waiter_thread = threading.Thread(target=waiter)
setter_thread = threading.Thread(target=setter)

waiter_thread.start()
setter_thread.start()

waiter_thread.join()
setter_thread.join()

# Reset the event for reuse
event.clear()

#####################################
# Thread Communication with Queues  #
#####################################

# Thread-safe queue for communication
task_queue = queue.Queue()

def producer(items):
    """
    Produce items and put them in the queue.
    
    Args:
        items: List of items to produce
    """
    for item in items:
        print(f"Producer: Adding {item} to queue")
        task_queue.put(item)
        time.sleep(0.5)
    
    # Add sentinel value to signal end of production
    task_queue.put(None)
    print("Producer: Done")

def consumer():
    """Consume items from the queue until receiving sentinel value."""
    while True:
        item = task_queue.get()
        if item is None:  # Check for sentinel value
            break
            
        print(f"Consumer: Got {item} from queue")
        task_queue.task_done()  # Mark task as done
        time.sleep(1)
    
    print("Consumer: Done")

# Create and start producer and consumer threads
producer_thread = threading.Thread(target=producer, args=([1, 2, 3, 4, 5],))
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

#################################################
# Thread Pool Executor (from Python 3.2+)      #
#################################################

def task_function(name):
    """Function to be executed by thread pool."""
    print(f"Task {name}: Starting")
    # Simulate work
    time.sleep(1)
    print(f"Task {name}: Completed")
    return f"Result {name}"

# Example using ThreadPoolExecutor - manages a pool of threads
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # Submit tasks and get Future objects
    future1 = executor.submit(task_function, "A")
    future2 = executor.submit(task_function, "B")
    future3 = executor.submit(task_function, "C")
    
    # Get results as they complete (blocking)
    print(f"Result from future1: {future1.result()}")
    print(f"Result from future2: {future2.result()}")
    print(f"Result from future3: {future3.result()}")
    
    # Map function to an iterable
    task_names = ["D", "E", "F"]
    results = executor.map(task_function, task_names)
    
    # Process results in order of submission
    for result in results:
        print(f"Map result: {result}")

################################################
# Daemon Threads - terminate when main exits   #
################################################

def daemon_worker():
    """Function for a daemon thread that runs continuously."""
    count = 0
    while True:
        count += 1
        print(f"Daemon working... count: {count}")
        time.sleep(0.5)

# Create a daemon thread
daemon_thread = threading.Thread(target=daemon_worker)
daemon_thread.daemon = True  # Set as daemon

# Start the daemon thread
daemon_thread.start()

# Main thread work
print("Main thread working...")
time.sleep(2)  # Let daemon run for a bit
print("Main thread exiting - daemon thread will be terminated")
# No need to join daemon threads

################################################
# Threading Timer - delayed thread execution    #
################################################

def delayed_task():
    """Function to execute after a delay."""
    print("Delayed task executing!")

# Create a timer thread
timer = threading.Timer(2.0, delayed_task)
timer.start()

print("Timer started, waiting for delayed task...")
# Timer can be cancelled before it executes
# timer.cancel()

################################################
# Thread Local Storage                         #
################################################

# Thread-local data is isolated to each thread
thread_local = threading.local()

def thread_with_local_data(name):
    """Function that uses thread-local storage."""
    # Each thread has its own 'value'
    thread_local.value = name
    print(f"Thread {name}: thread_local.value = {thread_local.value}")
    time.sleep(0.5)
    # The value is preserved within the thread
    print(f"Thread {name} checking again: thread_local.value = {thread_local.value}")

# Create threads that use thread-local storage
thread_local1 = threading.Thread(target=thread_with_local_data, args=("X",))
thread_local2 = threading.Thread(target=thread_with_local_data, args=("Y",))

thread_local1.start()
thread_local2.start()

thread_local1.join()
thread_local2.join()

################################################
# Threading Barrier                            #
################################################

# Barrier for thread synchronization
barrier = threading.Barrier(3)  # Wait for 3 threads

def barrier_task(name):
    """Function that waits at a barrier before proceeding."""
    print(f"Thread {name} waiting at barrier")
    
    # Wait at the barrier - blocks until 3 threads reach this point
    barrier.wait()
    
    print(f"Thread {name} passed barrier")

# Create threads that will synchronize at the barrier
barrier_thread1 = threading.Thread(target=barrier_task, args=("P",))
barrier_thread2 = threading.Thread(target=barrier_task, args=("Q",))
barrier_thread3 = threading.Thread(target=barrier_task, args=("R",))

barrier_thread1.start()
barrier_thread2.start()
time.sleep(1)
print("Main thread: About to start the last thread to trigger the barrier")
barrier_thread3.start()  # This will allow all threads to proceed

barrier_thread1.join()
barrier_thread2.join()
barrier_thread3.join()

################################################
# Threading Semaphore                          #
################################################

# Semaphore for limiting concurrent access
semaphore = threading.Semaphore(2)  # Allow 2 concurrent accesses

def semaphore_task(name):
    """Function that uses a semaphore to limit concurrency."""
    with semaphore:
        print(f"Thread {name} acquired semaphore")
        time.sleep(1)  # Simulate work while holding the semaphore
        print(f"Thread {name} releasing semaphore")

# Create several threads that will compete for the semaphore
sem_threads = []
for i in range(5):
    thread = threading.Thread(target=semaphore_task, args=(f"S{i}",))
    sem_threads.append(thread)
    thread.start()

# Wait for all semaphore threads to complete
for thread in sem_threads:
    thread.join()

################################################
# Condition Variables                          #
################################################

# Condition for more complex synchronization
condition = threading.Condition()
shared_resource = []

def consumer_with_condition():
    """Consumer thread that waits for items using a condition."""
    with condition:
        while not shared_resource:  # Check if resource is empty
            print("Consumer: Waiting for resource")
            condition.wait()  # Release lock and block until notified
        
        # Resource is now available
        item = shared_resource.pop(0)
        print(f"Consumer: Consumed {item}")

def producer_with_condition():
    """Producer thread that adds items and notifies using a condition."""
    with condition:
        print("Producer: Adding to resource")
        shared_resource.append("item")
        
        # Notify one waiting thread that resource is available
        print("Producer: Notifying")
        condition.notify()
        # Could use condition.notify_all() to wake all waiting threads

# Create and start condition threads
cond_consumer = threading.Thread(target=consumer_with_condition)
cond_producer = threading.Thread(target=producer_with_condition)

cond_consumer.start()
time.sleep(1)  # Ensure consumer starts waiting first
cond_producer.start()

cond_consumer.join()
cond_producer.join()

################################################
# Current Thread Information                   #
################################################

def show_thread_info():
    """Display information about the current thread."""
    current = threading.current_thread()
    print(f"Current thread: {current.name}, ID: {current.ident}")
    print(f"Is daemon: {current.daemon}")
    print(f"Thread is alive: {current.is_alive()}")
    
    # Get all active threads
    print("Active threads:")
    for thread in threading.enumerate():
        print(f" - {thread.name}")
    
    # Get count of active threads
    print(f"Active thread count: {threading.active_count()}")

# Run in main thread
show_thread_info()

# Run in a new thread
info_thread = threading.Thread(target=show_thread_info, name="InfoThread")
info_thread.start()
info_thread.join()