import multiprocessing
import random
import timeit

from src.lab04.io_txt_csv import write_csv
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort


def timed_worker(fn, data, connection):
    connection.send(timeit.timeit(lambda: fn(data), number=1))
    connection.close()


def limited_time(fn, data):
    receiver, sender = multiprocessing.Pipe(duplex=False)
    process = multiprocessing.Process(target=timed_worker, args=(fn, data, sender))
    process.start()
    sender.close()
    process.join(60)
    if process.is_alive():
        process.terminate()
        process.join()
        result = ">60"
    elif receiver.poll():
        result = receiver.recv()
    else:
        raise RuntimeError(f"Ошибка замера {fn.__name__}")
    receiver.close()
    return result


def main():
    random.seed(42)
    rows = []

    def record(task, n, impl, seconds):
        value = f"{seconds:.6f}" if isinstance(seconds, float) else seconds
        rows.append((task, n, impl, value))
        print(f"{task:12} {n:8} {impl:20} {value:>12}", flush=True)
        write_csv(rows, "data/lab07/bench.csv", ("task", "n", "impl", "seconds"))

    print(f"{'task':12} {'n':>8} {'impl':20} {'seconds':>12}", flush=True)
    for n in (1000, 10000, 100000):
        data = [random.randint(-100000, 100000) for _ in range(n)]
        for fn in (bubble_sort, insertion_sort, selection_sort, sorted):
            seconds = limited_time(fn, data) if n == 100000 and fn is not sorted else timeit.timeit(lambda: fn(data), number=1)
            record("sort", n, fn.__name__, seconds)
    data = [random.randint(-100000, 100000) for _ in range(100000)]
    queries = [random.randint(-100000, 100000) for _ in range(10000)]
    record("search_setup", len(data), "sorted", timeit.timeit(lambda: sorted(data), number=1))
    ordered = sorted(data)
    for fn, values in ((linear_search, data), (binary_search, ordered)):
        record("search", len(data), fn.__name__, timeit.timeit(lambda: [fn(values, x) for x in queries], number=1))
    for n in (1000, 10000):
        data = [random.randint(0, 1000) for _ in range(n - 2)] + [10000, 20000]
        for fn in (two_sum_brute, two_sum_fast):
            record("two_sum", n, fn.__name__, timeit.timeit(lambda: fn(data, 30000), number=1))


if __name__ == "__main__":
    main()
