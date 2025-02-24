import sorting_method

def reverse_array(arr, number_of_elements):
    for i in range(number_of_elements):
        arr.append(number_of_elements - i)
    return arr

def sorted_array(arr, number_of_elements):
    for i in range(number_of_elements):
        arr.append(i)
    return arr

def random_array(arr, number_of_elements):
    import random
    for i in range(number_of_elements):
        arr.append(random.randint(0, 100))
    return arr


    print("10 elements")
    print("Worst Cases")
    print("Bubble sort compares and swaps:", sorting_method.bubble_sort(reverse_array([], 10)))
    print("Modified Bubble sort compares and swaps:", sorting_method.modified_bubble_sort(reverse_array([], 10)))
    print("Comb sort compares and swaps:", sorting_method.comb_sort(reverse_array([], 10)))

    print("Average Cases")
    print("Bubble sort compares and swaps:", sorting_method.bubble_sort(random_array([], 10)))
    print("Modified Bubble sort compares and swaps:", sorting_method.modified_bubble_sort(random_array([], 10)))
    print("Comb sort compares and swaps:", sorting_method.comb_sort(random_array([], 10)))

    print("Best Cases")
    print("Bubble sort compares and swaps:", sorting_method.bubble_sort(sorted_array([], 10)))
    print("Modified Bubble sort compares and swaps:", sorting_method.modified_bubble_sort(sorted_array([], 10)))
    print("Comb sort compares and swaps:", sorting_method.comb_sort(sorted_array([], 10)))
    print("\n")

    print("100 elements")
    print("Worst Cases")
    print("Bubble sort compares and swaps:", sorting_method.bubble_sort(reverse_array([], 100)))
    print("Modified Bubble sort compares and swaps:", sorting_method.modified_bubble_sort(reverse_array([], 100)))
    print("Comb sort compares and swaps:", sorting_method.comb_sort(reverse_array([], 100)))

    print("Average Cases")
    print("Bubble sort compares and swaps:", sorting_method.bubble_sort(random_array([], 100)))
    print("Modified Bubble sort compares and swaps:", sorting_method.modified_bubble_sort(random_array([], 100)))
    print("Comb sort compares and swaps:", sorting_method.comb_sort(random_array([], 100)))

    print("Best Cases")
    print("Bubble sort compares and swaps:", sorting_method.bubble_sort(sorted_array([], 100)))
    print("Modified Bubble sort compares and swaps:", sorting_method.modified_bubble_sort(sorted_array([], 100)))
    print("Comb sort compares and swaps:", sorting_method.comb_sort(sorted_array([], 100)))
    print("\n")

    print("1000 elements")
    print("Worst Cases")
    print("Bubble sort compares and swaps:", sorting_method.bubble_sort(reverse_array([], 1000)))
    print("Modified Bubble sort compares and swaps:", sorting_method.modified_bubble_sort(reverse_array([], 1000)))
    print("Comb sort compares and swaps:", sorting_method.comb_sort(reverse_array([], 1000)))

    print("Average Cases")
    print("Bubble sort compares and swaps:", sorting_method.bubble_sort(random_array([], 1000)))
    print("Modified Bubble sort compares and swaps:", sorting_method.modified_bubble_sort(random_array([], 1000)))
    print("Comb sort compares and swaps:", sorting_method.comb_sort(random_array([], 1000)))

    print("Best Cases")
    print("Bubble sort compares and swaps:", sorting_method.bubble_sort(sorted_array([], 1000)))
    print("Modified Bubble sort compares and swaps:", sorting_method.modified_bubble_sort(sorted_array([], 1000)))
    print("Comb sort compares and swaps:", sorting_method.comb_sort(sorted_array([], 1000)))
    print("\n")

    print("5000 elements")
    print("Worst Cases")
    print("Bubble sort compares and swaps:", sorting_method.bubble_sort(reverse_array([], 5000)))
    print("Modified Bubble sort compares and swaps:", sorting_method.modified_bubble_sort(reverse_array([], 5000)))
    print("Comb sort compares and swaps:", sorting_method.comb_sort(reverse_array([], 5000)))

    print("Average Cases")
    print("Bubble sort compares and swaps:", sorting_method.bubble_sort(random_array([], 5000)))
    print("Modified Bubble sort compares and swaps:", sorting_method.modified_bubble_sort(random_array([], 5000)))
    print("Comb sort compares and swaps:", sorting_method.comb_sort(random_array([], 5000)))

    print("Best Cases")
    print("Bubble sort compares and swaps:", sorting_method.bubble_sort(sorted_array([], 5000)))
    print("Modified Bubble sort compares and swaps:", sorting_method.modified_bubble_sort(sorted_array([], 5000)))
    print("Comb sort compares and swaps:", sorting_method.comb_sort(sorted_array([], 5000)))
    print("\n")

    print("10000 elements")
    print("Worst Cases")
    print("Bubble sort compares and swaps:", sorting_method.bubble_sort(reverse_array([], 10000)))
    print("Modified Bubble sort compares and swaps:", sorting_method.modified_bubble_sort(reverse_array([], 10000)))
    print("Comb sort compares and swaps:", sorting_method.comb_sort(reverse_array([], 10000)))

    print("Average Cases")
    print("Bubble sort compares and swaps:", sorting_method.bubble_sort(random_array([], 10000)))
    print("Modified Bubble sort compares and swaps:", sorting_method.modified_bubble_sort(random_array([], 10000)))
    print("Comb sort compares and swaps:", sorting_method.comb_sort(random_array([], 10000)))

    print("Best Cases")
    print("Bubble sort compares and swaps:", sorting_method.bubble_sort(sorted_array([], 10000)))
    print("Modified Bubble sort compares and swaps:", sorting_method.modified_bubble_sort(sorted_array([], 10000)))
    print("Comb sort compares and swaps:", sorting_method.comb_sort(sorted_array([], 10000)))
    print("\n")

    print("20000 elements")
    print("Worst Cases")
    print("Bubble sort compares and swaps:", sorting_method.bubble_sort(reverse_array([], 20000)))
    print("Modified Bubble sort compares and swaps:", sorting_method.modified_bubble_sort(reverse_array([], 20000)))
    print("Comb sort compares and swaps:", sorting_method.comb_sort(reverse_array([], 20000)))

    print("Average Cases")
    print("Bubble sort compares and swaps:", sorting_method.bubble_sort(random_array([], 20000)))
    print("Modified Bubble sort compares and swaps:", sorting_method.modified_bubble_sort(random_array([], 20000)))
    print("Comb sort compares and swaps:", sorting_method.comb_sort(random_array([], 20000)))

    print("Best Cases")
    print("Bubble sort compares and swaps:", sorting_method.bubble_sort(sorted_array([], 20000)))
    print("Modified Bubble sort compares and swaps:", sorting_method.modified_bubble_sort(sorted_array([], 20000)))
    print("Comb sort compares and swaps:", sorting_method.comb_sort(sorted_array([], 20000)))
    print("\n")

    print("50000 elements")
    print("Worst Cases")
    print("Bubble sort compares and swaps:", sorting_method.bubble_sort(reverse_array([], 50000)))
    print("Modified Bubble sort compares and swaps:", sorting_method.modified_bubble_sort(reverse_array([], 50000)))
    print("Comb sort compares and swaps:", sorting_method.comb_sort(reverse_array([], 50000)))

    print("Average Cases")
    print("Bubble sort compares and swaps:", sorting_method.bubble_sort(random_array([], 50000)))
    print("Modified Bubble sort compares and swaps:", sorting_method.modified_bubble_sort(random_array([], 50000)))
    print("Comb sort compares and swaps:", sorting_method.comb_sort(random_array([], 50000)))

    print("Best Cases")
    print("Bubble sort compares and swaps:", sorting_method.bubble_sort(sorted_array([], 50000)))
    print("Modified Bubble sort compares and swaps:", sorting_method.modified_bubble_sort(sorted_array([], 50000)))
    print("Comb sort compares and swaps:", sorting_method.comb_sort(sorted_array([], 50000)))
