# Find sorted arrays percentile

### _Solution explanation -_


````
def find_percentile(a, b, p) :
 
 // First evalauate the element index for the median
 // Take the sum of lenth of two array's and then find the median index based on 
 // provided percentage.
 
    k = math.ceil((len(a) + len(b)) * p / 100)
    
    // Find the start point of search
    start = max(0, k - len(b))
    // Find the end point of search
    end = min(len(a), k)
    
    // Need to iterate till the end point
    while start <= end 
        //The search for the element
        a_left_size = (start + end) // 2
        b_left_size = k - a_left_size
        // left value of a
        a_left = get_val(a, a_left_size - 1)
        // right value of a
        a_right = get_val(a, a_left_size)
        // left value of b
        b_left = get_val(b, b_left_size - 1)
        // right value of b
        b_right = get_val(b, b_left_size)
        // if a left value is greater than b right value then decrese the index by 1
        if a_left > b_right :
            end = a_left_size - 1
        // if b left value is greater than a right value then increment the index by 1
        elif b_left > a_right :
            start = a_left_size + 1
        // other wise return the max value
        else :
            return max(a_left, b_left)
            
````

````
    def get_val(arr, i) :
        if 0 <= i < len(arr) :
            return arr[i]
        return math.inf * (-1 if i < 0 else 1)
````

### _Time complexity -_
This method uses a linear and simpler approach. 

O(m + n) - Given two arrays are sorted. So they can be traversed in O(m+n) time to find pth percentile.

### Space complexity
O(1) - No extra space is required

### Correctness proof

Describe loop invariants and show initialization, maintenance and termination for them.

 * **Initialization**
 * **Maintenance**
 * **Termination** 

