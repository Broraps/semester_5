import streamlit as st
import numpy as np
import time
from concurrent.futures import ThreadPoolExecutor

# Linear Search Algorithm
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Binary Search Algorithm
def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Interpolation Search Algorithm
def interpolation_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high and arr[low] <= x <= arr[high]:
        if low == high:
            if arr[low] == x:
                return low
            return -1

        pos = low + ((high - low) // (arr[high] - arr[low]) * (x - arr[low]))

        if arr[pos] == x:
            return pos
        elif arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1

    return -1

# Generate Random Data
def generate_random_data(size):
    start_time = time.time()
    data = np.random.randint(1, size + 1, size).tolist()
    end_time = time.time()
    return data, end_time - start_time

# Parallel Execution
def parallel_search(arr, x, n_threads):
    sorted_arr = sorted(arr)
    results = {}
    with ThreadPoolExecutor(max_workers=n_threads) as executor:
        futures = {
            "Linear Search": executor.submit(linear_search, arr, x),
            "Binary Search": executor.submit(binary_search, sorted_arr, x),
            "Interpolation Search": executor.submit(interpolation_search, sorted_arr, x),
        }
        for key, future in futures.items():
            results[key] = future.result()
    return results

# Serial Execution
def serial_search(arr, x):
    sorted_arr = sorted(arr)
    return {
        "Linear Search": linear_search(arr, x),
        "Binary Search": binary_search(sorted_arr, x),
        "Interpolation Search": interpolation_search(sorted_arr, x)
    }

# Streamlit UI
st.title("Parallel Searching Algorithms")
st.write("This app performs linear, binary, and interpolation search either serially or in parallel.")

# Input size and target
size = st.number_input("Enter the number of random elements to generate (e.g., 100):", min_value=1, value=100)
target = st.number_input("Enter the number to search for:", min_value=1, value=50)
execution_mode = st.selectbox("Select execution mode:", ["Serial", "Parallel"])
n_threads = st.number_input("Number of threads (for parallel execution):", min_value=1, value=4, step=1, disabled=(execution_mode == "Serial"))
algorithm = st.selectbox("Select search algorithm:", ["Linear Search", "Binary Search", "Interpolation Search", "All"])

if st.button("Run Search"):
    st.write("Generating random data...")
    data, gen_time = generate_random_data(size)
    st.write(f"Data generated in {gen_time:.4f} seconds.")
    st.dataframe(data[:100], height=200)  # Display only the first 100 elements if the data is large

    st.write("Executing search...")
    start_time = time.time()
    
    if execution_mode == "Parallel":
        results = parallel_search(data, target, n_threads)
    else:
        results = serial_search(data, target)

    end_time = time.time()

    if algorithm == "All":
        st.write("Results:")
        for algo, result in results.items():
            st.write(f"{algo}: {'Found at index ' + str(result) if result != -1 else 'Not found'}")
    else:
        result = results[algorithm]
        st.write(f"{algorithm}: {'Found at index ' + str(result) if result != -1 else 'Not found'}")

    st.write(f"Total execution time: {end_time - start_time:.4f} seconds")
