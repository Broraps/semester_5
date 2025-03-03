import streamlit as st
import numpy as np
import time

# Linear Search
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Binary Search (Requires sorted array)
def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Interpolation Search (Requires sorted and uniformly distributed array)
def interpolation_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high and x >= arr[low] and x <= arr[high]:
        pos = low + ((high - low) // (arr[high] - arr[low]) * (x - arr[low]))
        if arr[pos] == x:
            return pos
        elif arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1
    return -1

# Streamlit Interface
st.title("Aplikasi Linear Search, Binary Search, or Interpolation Search")

# Input Section
n = st.number_input("Jumlah Data:", min_value=1, value=100) 

# Generate non-duplicate random data within the specified range
data = np.random.permutation(n) + 1  # Generates numbers from 1 to n without duplicates

# Display unsorted data
st.subheader("Data Sebelum Terurut:")
st.write(data)  # Display all elements as there are no duplicates

# Sorting Options and Run Button
sort_option = st.checkbox("Urutkan Data (Untuk Binary dan Interpolation Search)")

# Sort data if checkbox is selected
if sort_option:
    data.sort()
    st.subheader("Data Setelah Terurut:")
    st.write(data)  # Display sorted data

# Input for search value
search_value = st.number_input("Nilai yang Dicari:", min_value=1, max_value=n)

# Search Method Options
st.subheader("Pilih Algoritma Pencarian dan Tekan 'Run'")

# Linear Search
if st.button("Run Linear Search"):
    start_time = time.time()
    result = linear_search(data, search_value)
    end_time = time.time()
    time_taken = end_time - start_time

    # Display Result
    if result != -1:
        st.success(f"Linear Search: Data ditemukan pada indeks {result}")
    else:
        st.error("Linear Search: Data tidak ditemukan")
    st.info(f"Waktu proses: {time_taken:.6f} detik")

# Binary Search
if st.button("Run Binary Search"):
    if not sort_option:
        st.warning("Data harus terurut untuk Binary Search. Silakan centang 'Urutkan Data'.")
    else:
        start_time = time.time()
        result = binary_search(data, search_value)
        end_time = time.time()
        time_taken = end_time - start_time

        # Display Result
        if result != -1:
            st.success(f"Binary Search: Data ditemukan pada indeks {result}")
        else:
            st.error("Binary Search: Data tidak ditemukan")
        st.info(f"Waktu proses: {time_taken:.6f} detik")

# Interpolation Search
if st.button("Run Interpolation Search"):
    if not sort_option:
        st.warning("Data harus terurut untuk Interpolation Search. Silakan centang 'Urutkan Data'.")
    else:
        start_time = time.time()
        result = interpolation_search(data, search_value)
        end_time = time.time()
        time_taken = end_time - start_time

        # Display Result
        if result != -1:
            st.success(f"Interpolation Search: Data ditemukan pada indeks {result}")
        else:
            st.error("Interpolation Search: Data tidak ditemukan")
        st.info(f"Waktu proses: {time_taken:.6f} detik")
