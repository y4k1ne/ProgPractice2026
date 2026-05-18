import cv2
import numpy as np
import threading
import multiprocessing
import time


def blur(file_name):
    image = cv2.imread(file_name)

    if image is None:
        print(f"Could not read image: {file_name}")
        return

    cv2.GaussianBlur(image, (9, 9), 0)


def threads():
    threads = []
    start = time.time()

    for _ in range(100):
        t = threading.Thread(target=blur, args=("input-image-of-wood.jpg",))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return time.time() - start


def processes():
    processes = []
    start = time.time()

    for _ in range(100):
        p = multiprocessing.Process(target=blur, args=("input-image-of-wood.jpg",))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    return time.time() - start


if __name__ == "__main__":
    thread_time = threads()
    print(f"Threading time: {thread_time:.3f} seconds")

    process_time = processes()
    print(f"Multiprocessing time: {process_time:.3f} seconds")

    if thread_time < process_time:
        print("Threading was faster.")
    elif process_time < thread_time:
        print("Multiprocessing was faster.")
    else:
        print("Both methods took the same time.")