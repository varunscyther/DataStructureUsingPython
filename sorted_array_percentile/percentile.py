import datetime
import math
import random


def find_percentile(a, b, p) :
    def get_val(arr, i) :
        if 0 <= i < len(arr) :
            return arr[i]
        return math.inf * (-1 if i < 0 else 1)
    a = sorted(a)
    b = sorted(b)
    k = math.ceil((len(a) + len(b)) * p / 100)
    start = max(0, k - len(b))
    end = min(len(a), k)
    while start <= end :
        a_left_size = (start + end) // 2
        b_left_size = k - a_left_size
        a_left = get_val(a, a_left_size - 1)
        a_right = get_val(a, a_left_size)
        b_left = get_val(b, b_left_size - 1)
        b_right = get_val(b, b_left_size)
        if a_left > b_right :
            end = a_left_size - 1
        elif b_left > a_right :
            start = a_left_size + 1
        else :
            return max(a_left, b_left)


def reference_solution(a, b, p) :
    merged_array = a + b
    sorted_merged_array = sorted(merged_array)
    k = math.ceil((len(a) + len(b)) * p / 100)
    return sorted_merged_array[k - 1]


def test_find_percentile(a, b, p, expected_answer) :
    # run the solution and compare to the expected answer
    actual_answer = find_percentile(a, b, p)
    error_str = 'Test failed for following arrays a : {0} , b : {1} with percentage(p) : {2}' \
                '\nActual answer : {3}' \
                '\nExpected answer : {4}\n'
    assert actual_answer == expected_answer, error_str.format(a, b, p, actual_answer, expected_answer)
    print("Well done. Unit tests passed !!!!")


def run_unit_tests() :
    print("Running unit tests !!!!")
    # run several test_find_percentile for different tests
    test_a, test_b, test_p = [1, 2, 7, 8, 10], [6, 12], 50
    test_find_percentile(test_a, test_b, test_p, 7)

    test_a, test_b, test_p = [1, 2, 7, 8], [6, 12], 50
    test_find_percentile(test_a, test_b, test_p, 6)

    test_a, test_b, test_p = [15, 20, 35, 40, 50], [], 30
    test_find_percentile(test_a, test_b, test_p, 20)

    test_a, test_b, test_p = [15, 20], [25, 40, 50], 40
    test_find_percentile(test_a, test_b, test_p, 20)
    print("End of unit tests !!!!")


def run_stress_test(max_test_size, max_attempts, max_right_boundary) :
    print("Running stress tests !!!!")
    random.seed(100)
    for attempt in range(max_attempts) :
        for size in range(1, max_test_size) :
            percentage, random_array_1, random_array_2 = generate_random_test(max_right_boundary, size)
            reference_solution_result = reference_solution(random_array_1, random_array_2, percentage)
            start_time = datetime.datetime.now()
            test_find_percentile(random_array_1, random_array_2, percentage, reference_solution_result)
            end_time = datetime.datetime.now()
            find_percentile_working_time = end_time - start_time
            execution_time = find_percentile_working_time.total_seconds() * 1000
            print("The execution time for p-th percentile calculation for following array's is (in milli seconds)  : %f" % execution_time)
    print("End of stress tests !!!!")


# find_percentile works 10 seconds on the max test
def run_max_test(max_right_boundary, max_test_size) :
    print("Running max test !!!!")
    random.seed(100)
    # generate arrays a and b of maximum possible sizes
    percentage, random_array_1, random_array_2 = generate_random_test(max_right_boundary, max_test_size)
    # len(a), len(b) <= 150000 for the problem
    reference_solution_result = reference_solution(random_array_1, random_array_2, percentage)
    start_time = datetime.datetime.now()
    test_find_percentile(random_array_1, random_array_2, percentage, reference_solution_result)
    end_time = datetime.datetime.now()
    find_percentile_working_time = end_time - start_time
    execution_time = find_percentile_working_time.total_seconds() * 1000
    print("The max test execution time for p-th percentile calculation is (in milli seconds)  : %f" % execution_time)
    print("End of max test !!!!")


def generate_random_test(max_right_boundary, size) :
    random_array_1 = random.sample(range(0, max_right_boundary), size)
    random_array_2 = random.sample(range(0, max_right_boundary), size)
    percentage = random.choice([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    return percentage, random_array_1, random_array_2


# some test code
if __name__ == "__main__" :
    run_unit_tests()
    run_stress_test(max_test_size=100, max_attempts=100, max_right_boundary=100)
    run_max_test(max_right_boundary=200000, max_test_size=200000)
