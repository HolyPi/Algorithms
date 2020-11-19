
from sorting_iterative import insertion_sort

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
     
    if len(numbers) <= 1:
        return numbers

    maxim = max(numbers) + 1
    count = [0] * (maxim + 1)

    for i in numbers:
        count[i] += 1

    i = 0
    for j in range(maxim):
        for k in range(count[j]):
            numbers[i] = j
            i += 1
    return numbers
    

def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    
    if len(numbers) <= 1:
        return numbers

    length = len(numbers)
    maxim = max(numbers) + 1
    size = maxim // length + 1
    bucket_list = []
    result = []

        
    for i in range(length):
        bucket_list.append([])
    
    for i in range(length):
        j = int (numbers[i] // size)
        if j != length:
            bucket_list[j].append(numbers[i])
        else:
            bucket_list[length].append(numbers[i])

    k = 0
    for bucket in bucket_list:
        insertion_sort(bucket)
        for i in bucket:
            numbers[k] = i
            k += 1



    