
## Variables And Datatypes


## Introduction
This chapter introduces variables and datatypes in Python, fundamental concepts that are essential for writing any Python program.

## Variables
Variables are containers for storing data values. In Python, you don’t need to declare the type of a variable; it is inferred from the value assigned.

### Creating Variables
To create a variable, simply assign a value to a name:
```python
x = 5
name = "John"
```

### Variable Naming Rules
- Names must start with a letter or an underscore.
- Names can contain letters, numbers, and underscores.
- Names are case-sensitive (`myVar` and `myvar` are different).

### Assigning Values
You can assign values to multiple variables in one line:
```python
a, b, c = 1, 2, 3
```

## Datatypes
Python supports various datatypes to work with different types of data.

### Basic Datatypes
- **Integers**: Whole numbers, e.g., `10`
- **Floats**: Decimal numbers, e.g., `10.5`
- **Strings**: Text, e.g., `"Hello"`
- **Booleans**: True or False, e.g., `True`

### Type Conversion
Convert one datatype to another using functions like `int()`, `float()`, `str()`, etc.:
```python
x = int(1.5)  # Converts float to int, result is 1
```

### Checking Datatypes
Use the `type()` function to check the datatype of a variable:
```python
type(x)  # Returns <class 'int'>
```

## Examples
Here are some practical examples of working with variables and datatypes:

```python
# Example 1: Variable assignment
x = 10
y = "Hello"
z = 3.14

# Example 2: Type conversion
a = float(10)  # Converts integer to float

# Example 3: Checking variable type
print(type(a))  # Outputs <class 'float'>
```

## Conclusion
Understanding variables and datatypes is crucial for effective programming in Python. Practice these concepts to build a strong foundation.
