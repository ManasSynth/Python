
# Chapter 3: Lists and Tuples

This chapter introduces **Lists** and **Tuples** in Python. We’ll explore how to define and work with them, understand the differences between the two, and dive into useful methods and slicing techniques.

## 🚀 Introduction
Lists and Tuples are both sequence data types in Python that can store a collection of items. However, they serve different purposes based on their characteristics, making them essential for different scenarios.

## 📝 Lists in Python

### What is a List?
A **List** is an ordered, mutable collection that can hold items of different data types. Lists are created using square brackets `[]`.

### Initializing a List
```python
# Example of list initialization
fruits = ["apple", "banana", "cherry", "date"]
```

### List Slicing
List slicing allows you to access a portion of the list. You can specify a range of indices using the `:` operator.

```python
# Example of list slicing
print(fruits[1:3])  # Output: ['banana', 'cherry']
```

#### Negative Indexing in List Slicing
Negative indexing starts from the end of the list, allowing you to access elements in reverse order.

```python
# Example of negative indexing
print(fruits[-3:])  # Output: ['banana', 'cherry', 'date']
```

### List Methods
Python provides various built-in methods to manipulate lists:

- `append()` - Adds an item to the end of the list.
- `sort()` - Sorts the list in ascending order by default.
- `sort(reverse=True)` - Sorts the list in descending order.
- `reverse()` - Reverses the order of the list.
- `insert(index, item)` - Inserts an item at the specified index.

```python
# Examples of list methods
numbers = [4, 2, 9, 1, 7]

# Append
numbers.append(5)
print(numbers)  # Output: [4, 2, 9, 1, 7, 5]

# Sort
numbers.sort()
print(numbers)  # Output: [1, 2, 4, 5, 7, 9]

# Sort in reverse order
numbers.sort(reverse=True)
print(numbers)  # Output: [9, 7, 5, 4, 2, 1]

# Reverse
numbers.reverse()
print(numbers)  # Output: [1, 2, 4, 5, 7, 9]

# Insert
numbers.insert(2, 10)
print(numbers)  # Output: [1, 2, 10, 4, 5, 7, 9]
```

## 🔄 Tuples in Python

### What is a Tuple?
A **Tuple** is an ordered, immutable collection that can also hold items of different data types. Tuples are created using parentheses `()`.

### Initializing a Tuple
```python
# Example of tuple initialization
colors = ("red", "green", "blue")
```

### Differences Between Lists and Tuples
| Aspect              | List                               | Tuple                              |
|---------------------|-----------------------------------|------------------------------------|
| Mutability         | Mutable (can be changed)           | Immutable (cannot be changed)      |
| Syntax             | Defined with `[]` (square brackets) | Defined with `()` (parentheses)    |
| Methods            | Many built-in methods for modification | Fewer methods (mainly for access) |

### Tuple Slicing
Similar to lists, tuples can be sliced using the `:` operator.

```python
# Example of tuple slicing
print(colors[0:2])  # Output: ('red', 'green')
```

### Tuple Methods
Tuples have limited methods because they are immutable:

- `count(item)` - Returns the number of times an item appears in the tuple.
- `index(item)` - Returns the index of the first occurrence of an item.

```python
# Example of tuple methods
nums = (1, 2, 3, 2, 4)

# Count
print(nums.count(2))  # Output: 2

# Index
print(nums.index(3))  # Output: 2
```

## 🧑‍💻 Practice
Explore more about lists and tuples through the [examples](examples/) and challenge yourself with the [exercises](exercises/).

## 📚 Resources
- [Python Official Documentation](https://docs.python.org/3/tutorial/)
- [W3Schools Python Lists](https://www.w3schools.com/python/python_lists.asp)
- [W3Schools Python Tuples](https://www.w3schools.com/python/python_tuples.asp)
