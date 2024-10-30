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

import pytest
import numpy as np
from basic_sort_UNIQUE_SUFFIX.int_sort import (
    bubble,
    quick,
    insertion,
)  # Import sorting functions


def is_sorted(int_list):
    """
    Check if a list is sorted in ascending order.

    Parameters:
        int_list (list of int): List of integers to check.

    Returns:
        bool: True if sorted in ascending order, False otherwise.
    """
    return all(int_list[i] <= int_list[i + 1] for i in range(len(int_list) - 1))


@pytest.fixture
def int_lists():
    """
    Fixture that creates test data for all sorting tests.

    Returns:
        list: A list of lists of integers to be used as test cases.
    """
    return [[3, 2, 1], [1, 1, 1], np.random.randint(low=-10, high=200, size=5).tolist()]


def test_bubble(int_lists):
    for int_list in int_lists:
        sorted_list = bubble(int_list.copy())  # Ensure original list isn't modified
        assert is_sorted(sorted_list), f"Bubble sort failed on {int_list}"


def test_quick(int_lists):
    for int_list in int_lists:
        sorted_list = quick(int_list.copy())  # Ensure original list isn't modified
        assert is_sorted(sorted_list), f"Quick sort failed on {int_list}"


def test_insertion(int_lists):
    for int_list in int_lists:
        sorted_list = insertion(int_list.copy())  # Ensure original list isn't modified
        assert is_sorted(sorted_list), f"Insertion sort failed on {int_list}"
