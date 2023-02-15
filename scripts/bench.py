"""
    Benchmark list creation
"""
import sys
import os
import re
import time # .sleep(), .time(), .time_ns()
import numpy as np

def main():
    count = 10000000

    time_comp = 0
    t1 = time.time()
    a = [ 0 for _ in range(count) ]
    time_comp = time.time() - t1
    
    time_star = 0
    t2 = time.time()
    b = [0] * count
    time_star = time.time() - t2

    print(f"Comp: {time_comp}")
    print(f"Star: {time_star}")
    print(f"Prop: {time_comp / time_star}")


if __name__ == "__main__":
    main()
