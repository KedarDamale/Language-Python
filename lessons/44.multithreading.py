# ========================================
# MULTITHREADING IN PYTHON — FULL EXAMPLE
# ========================================

# ✅ Python’s `threading` module is used to run multiple threads (tasks) concurrently.
# ✅ A thread is the smallest unit of a process that can be scheduled for execution.
# ✅ Multithreading is useful when we want to perform multiple I/O-bound operations simultaneously.

import threading  # Used to create and manage threads
import time       # Used to simulate task duration

# ==================================================
# Let's define three different I/O-bound tasks (functions)
# ==================================================

def walk_dog(name):
    # Simulates a long-running task (8 seconds)
    print(f"[{name}] 🐕 Starting to walk the dog...")
    time.sleep(8)  # Pretend this task takes 8 seconds
    print(f"[{name}] ✅ Finished walking the dog!")

def take_out_trash():
    print("🗑️ Starting to take out the trash...")
    time.sleep(4)  # Simulates 4-second task
    print("✅ Took out the trash!")

def get_mail():
    print("📬 Starting to get the mail...")
    time.sleep(5)  # Simulates 5-second task
    print("✅ Got the mail!")

# ==================================================
# 🧠 BEFORE MULTITHREADING (SEQUENTIAL EXECUTION)
# ==================================================

start = time.time()
walk_dog("Tommy")
take_out_trash()
get_mail()
end = time.time()
print(f"⏱️ Total Time Without Threads: {end - start:.2f} seconds")

# Output will show ~17 seconds as all tasks run one after another.

# ==================================================
# ✅ USING MULTITHREADING TO PARALLELIZE TASKS
# ==================================================

# ➕ Instead of waiting for one task to finish before starting another,
# we run them simultaneously using threads.

print("\n🔁 Running tasks with multithreading...")

# Record start time
start = time.time()

# ✅ Create threads
t1 = threading.Thread(target=walk_dog, args=("Tommy",))#if a function has arguments they are suppliend via a tuple and argument called arg and , 
                                                       #is given to let python know that its a tupple as python interpretes that as string, no need to 
                                                       #give extra comma at the edn if we are suppliying two arguments
t2 = threading.Thread(target=take_out_trash)
t3 = threading.Thread(target=get_mail)

# ✅ Start threads (they begin executing in the background)
t1.start()
t2.start()
t3.start()

# ✅ .join() tells the main thread to wait for these threads to complete
t1.join()
t2.join()
t3.join()

# Record end time
end = time.time()

print(f"⏱️ Total Time With Threads: {end - start:.2f} seconds")

# Output will show ~8 seconds — total time = time of the longest task!

# ==================================================
# 💡 WHY USE join()? 
# ==================================================
# Without join(), the main program continues execution and may end
# before threads complete. join() ensures main waits for all threads.
