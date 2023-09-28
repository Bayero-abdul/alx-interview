# Pascal's Triangle

This project implements a Python function to generate Pascal's triangle of a specified number of rows.

## Task

Implement the `pascal_triangle(n)` function, which returns a list of lists of integers representing Pascal's triangle with `n` rows. The function should meet the following requirements:

- Returns an empty list if `n` is less than or equal to 0.
- Assumes `n` will always be an integer.

## Usage

To use the `pascal_triangle` function, import it and call it with the desired number of rows. Here's an example of how to use it:

```python
from pascal_triangle import pascal_triangle

def print_triangle(triangle):
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
```

## Output

Running the example code above with `n=5` will produce the following output:

```
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```

## Repository Structure

- `0-pascal_triangle.py`: Contains the implementation of the `pascal_triangle(n)` function.
- `0-main.py`: A sample script to demonstrate the usage of the `pascal_triangle` function.
- `README.md`: This README file.