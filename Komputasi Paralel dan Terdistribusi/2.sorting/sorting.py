import streamlit as st
import random
import time

# Function to generate unique random data within a given range
def generate_unique_random_data(lower_bound, upper_bound):
    # Generate unique numbers within the specified range
    return random.sample(range(lower_bound, upper_bound + 1), upper_bound - lower_bound + 1)

# Selection Sort Algorithm
def selection_sort(data):
    data = data.copy()  # Prevent modifying the original data
    n = len(data)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    return data

# Bubble Sort Algorithm
def bubble_sort(data):
    data = data.copy()  # Prevent modifying the original data
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

# Quick Sort Algorithm
def quick_sort(data):
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2]
    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Streamlit App
def main():
    st.title("Sorting Algoritma Selection Sort, Bubble Sort dan Quick Sort")

    # Input for range boundaries
    lower_bound = st.number_input("Masukan Data Batas Bawah : ", value=1)
    upper_bound = st.number_input("Masukan Data Batas Atas : ", value=100)
    
    # Initialize session state for data
    if "data" not in st.session_state:
        st.session_state.data = []

    # Generate unique random data within the specified range
    if st.button("Generate Data Unik Random"):
        # Check if range is valid
        if lower_bound >= upper_bound:
            st.error("Batas Atas Harus Lebih Besar Dari Batas Bawah.")
        else:
            st.session_state.data = generate_unique_random_data(lower_bound, upper_bound)
            # Use st.text_area for scrollable output
            st.text_area("Data Random Unik:", "\n".join(map(str, st.session_state.data)), height=200)
            
    # Select sorting algorithm
    algorithm = st.selectbox("Pilih Algoritma Sorting :", ["Selection Sort", "Bubble Sort", "Quick Sort"])

    # Sort the data and measure time
    if st.button("Sort Data"):
        if st.session_state.data:
            data = st.session_state.data  # Access the data in session state
            start_time = time.time()
            
            # Perform sorting based on the selected algorithm
            if algorithm == "Selection Sort":
                sorted_data = selection_sort(data)
            elif algorithm == "Bubble Sort":
                sorted_data = bubble_sort(data)
            elif algorithm == "Quick Sort":
                sorted_data = quick_sort(data)
            
            end_time = time.time()
            elapsed_time = end_time - start_time
            st.text_area("Sorted Data:", "\n".join(map(str, sorted_data)), height=200)
            st.write(f"Time taken to sort: {elapsed_time:.6f} seconds")
        else:
            st.warning("Please generate unique random data first.")

if __name__ == "__main__":
    main()
