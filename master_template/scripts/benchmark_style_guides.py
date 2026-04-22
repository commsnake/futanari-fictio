import time
import re
import os
import sys
from scripts.test_style_guides import check_file

def benchmark():
    files = [
        'style_guides/gritty_blue_collar_futanari.txt',
        'style_guides/contemporary_realistic.txt'
    ]

    # Increase the number of iterations to get a measurable time
    iterations = 1000

    # Suppress print output from check_file during benchmark once
    original_stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')

    try:
        start_time = time.perf_counter()
        for _ in range(iterations):
            for filepath in files:
                check_file(filepath)
        end_time = time.perf_counter()
    finally:
        sys.stdout.close()
        sys.stdout = original_stdout

    total_time = end_time - start_time
    print(f"Total time for {iterations} iterations: {total_time:.4f} seconds")
    print(f"Average time per iteration: {total_time / iterations:.6f} seconds")

if __name__ == '__main__':
    benchmark()
