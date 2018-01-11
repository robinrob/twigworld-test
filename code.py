#!/usr/bin/env python


def split_array(arr, n_chunks):
    if n_chunks in [0, 1]:
        return [arr]

    remainder = len(arr) % n_chunks
    # Find what the chunk size for all elements would be with no remainder - this will be the chunk size of all but
    # the final chunk in the case where remainder > 0.
    chunk_size = (len(arr) + remainder) // n_chunks
    items_added = 0

    result = []

    # Add all whole chunks to result
    for i in range(0, n_chunks):
        chunk = arr[i*chunk_size:(i+1)*chunk_size]
        if len(chunk) > 0:
            result.append(chunk)
            items_added += len(chunk)

    remaining_elements = len(arr) - items_added

    if remaining_elements > 0:
        # In the case where the number of elements in the final chunk will be LARGER than the chunk size, we append the
        # remaining elements to the final chunk.
        if len(result) == n_chunks:
            result[-1].extend(arr[-remaining_elements:])

        # In the case where the number of elements in the final chunk will be SMALLER than the chunk size, we
        # add the remaining elements as the final chunk.
        elif len(result) < n_chunks:
            result.append(arr[-remaining_elements:])

    return result
