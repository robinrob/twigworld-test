#!/usr/bin/env python


def split_array(arr, n_chunks):
    if n_chunks in [0, 1]:
        return [arr]

    remainder = len(arr) % n_chunks
    chunk_size = (len(arr) + remainder) // n_chunks
    items_added = 0

    result = []

    for i in range(0, n_chunks):
        chunk = arr[i*chunk_size:(i+1)*chunk_size]
        if len(chunk) > 0:
            result.append(chunk)
            items_added += len(chunk)

    remaining_elements = len(arr) - items_added

    if remaining_elements > 0:
        if len(result) == n_chunks:
            result[-1].extend(arr[-remaining_elements:])
        else:
            result.append(arr[-remaining_elements:])

    return result
