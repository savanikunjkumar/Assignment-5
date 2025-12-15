

## Task 1: Create a Dictionary of Student Marks

### Problem Statement

* Create a dictionary where student names are keys and their marks are values.
* Take a student name as input from the user.
* Display the marks of the entered student.
* Show an appropriate message if the student name is not found.

### Program Description

The program stores student names and marks in a dictionary. It then checks whether the entered name exists in the dictionary and prints the corresponding marks.

### Sample Code

```python
students = {
    "Aman": 76,
    "Priya": 89,
    "Rahul": 82,
    "Neha": 91
}

student_name = input("Enter student name: ")

if student_name in students:
    print("Marks:", students[student_name])
else:
    print("Sorry, student not found.")
```

### Sample Output

```
Enter student name: Priya
Marks: 89
```

---

##  Task 2: Demonstrate List Slicing

### Problem Statement

* Create a list of numbers from 1 to 10.
* Extract the first five elements from the list.
* Reverse the extracted elements.
* Print both the extracted list and the reversed list.

### Program Description

This program demonstrates list slicing in Python by extracting and reversing elements using simple slicing techniques.

### Sample Code

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

first_five = numbers[:5]
reversed_list = first_five[::-1]

print("Extracted list:", first_five)
print("Reversed list:", reversed_list)
```

### Sample Output

```
Extracted list: [1, 2, 3, 4, 5]
Reversed list: [5, 4, 3, 2, 1]
```

---

## How to Run

1. Make sure Python is installed on your system.
2. Save the programs in `.py` files.
3. Run the files using:


---

### ✨ Author

Student Assignment Submission
