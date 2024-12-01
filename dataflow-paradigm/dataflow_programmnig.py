from multiprocessing import Queue, Process

def producer(data, output_queue):
    for number in data:
        output_queue.put(number)
    output_queue.put(None)  # Signal the end of data

def filter_even(input_queue, output_queue):
    while True:
        number = input_queue.get()
        if number is None:  # End signal
            output_queue.put(None)
            break
        if number % 2 == 0:
            output_queue.put(number)

def calculate_square(input_queue, output_queue):
    while True:
        number = input_queue.get()
        if number is None:  # End signal
            break
        output_queue.put(number ** 2)

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6]
    producer_queue = Queue()
    filter_queue = Queue()
    result_queue = Queue()

    # Create processes
    producer_process = Process(target=producer, args=(data, producer_queue))
    filter_process = Process(target=filter_even, args=(producer_queue, filter_queue))
    calculate_process = Process(target=calculate_square, args=(filter_queue, result_queue))

    # Start processes
    producer_process.start()
    filter_process.start()
    calculate_process.start()

    # Collect results
    producer_process.join()
    filter_process.join()
    calculate_process.join()

    results = []
    while not result_queue.empty():
        results.append(result_queue.get())
    print("Squares of even numbers:", results)
