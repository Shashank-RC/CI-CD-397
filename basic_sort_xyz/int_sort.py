# =========================================================================
#
#  Copyright Ziv Yaniv
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0.txt
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# =========================================================================

"""
This module provides implementations for sorting lists of integers using
Bubble Sort, Quick Sort, and Insertion Sort algorithms.
"""


def bubble(int_list):
    n = len(int_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if int_list[j] > int_list[j + 1]:
                int_list[j], int_list[j + 1] = int_list[j + 1], int_list[j]
    return int_list


def quick(int_list):
    if len(int_list) <= 1:
        return int_list
    pivot = int_list[len(int_list) // 2]
    left = [x for x in int_list if x < pivot]
    middle = [x for x in int_list if x == pivot]
    right = [x for x in int_list if x > pivot]
    return quick(left) + middle + quick(right)


def insertion(int_list):
    for i in range(1, len(int_list)):
        key = int_list[i]
        j = i - 1
        while j >= 0 and int_list[j] > key:
            int_list[j + 1] = int_list[j]
            j -= 1
        int_list[j + 1] = key
    return int_list
