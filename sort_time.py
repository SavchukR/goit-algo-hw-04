import random
import timeit
import matplotlib.pyplot as plt
import numpy as np

def get_ds(number):
    random_data = [random.randint(0, number) for _ in range(number)]
    sorted_data = sorted(random_data)
    reversed_data = sorted_data[::-1]
    return random_data, sorted_data, reversed_data

def test(algorithm, data):
    data_copy = data.copy()
    start_time = timeit.default_timer()
    algorithm(data_copy)
    end_time = timeit.default_timer()
    return end_time - start_time


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


repetitions = 2

results = []
algorythms = { 'Insert': lambda x: insertion_sort(x), 'Merge': lambda x: merge_sort(x), 'Timsort': lambda x: sorted(x) }

for size in [100, 1000]:
    
    random_ds, sorted_ds, reversed_ds = get_ds(size)
    
    dstype = { 'random': random_ds, 'sorted': sorted_ds, 'reversed': reversed_ds }

    for alg_name, alg_code in algorythms.items():
        
        for dstype_name in dstype:
            ds = dstype[dstype_name]
            
            for attempt in range(repetitions):
                
                print(f"Test size {size} for {alg_name} for {dstype_name} dataset, attempt {attempt}")

                time = test(alg_code, ds)
        
                results.append({'alg': alg_name, 'attempt': attempt, 'size': size, 'time': time, 'dstype': dstype_name })

from prettytable import PrettyTable
    
t = PrettyTable(['alg', 'attempt', 'size', 'dstype', 'time'])
    
for k in results:
    values = [ v for index, v in k.items() ]
    t.add_row(values)

print(t)

print("press any key...")
input()