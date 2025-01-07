#Task 2-Python Programming

#1. Prime Number
 
num = int(input("Enter a Number="))
count=0
for i in range(1,num+1):
    if num % i == 0:
        count = count + 1
if count == 2:
    print(num,"is prime number")
else:
            print(num,"Is  not a Prime Number")

#2. sum of digits

def sum_of_digits(n):
    n_str = str(n)
    total = 0
    for digit in n_str:
        total += int(digit)
        
    return total
number = int(input("Enter an integer:"))
result = sum_of_digits(number)
print("The sum of the digits is:",result) 

#3. LCM and GCD

import math

def calculate_gcd_lcm(a,b):
    gcd= math.gcd(a,b)
    lcm=abs(a*b)//gcd
    return gcd ,lcm
a= int(input("Enter the first integer:"))
b= int(input("Enter the second integer:"))

gcd,lcm = calculate_gcd_lcm(a,b)

print("GCD OF",a,"and",b,"is:",gcd)
print("LCM OF",a,"and",b,"is:",lcm)

#4. list Reversal

def reverse_list(lst):
    start=0
    end=len(lst)-1
    
    while start<end:
        lst[start],lst[end]=lst[end],lst[start]
        
        start += 1
        end -= 1
        
    return lst

lst=[int(x) for x in input("enter integers separated by space:").split()]
reversed_lst=reverse_list(lst)
print("Reversed list:",reversed_lst)

#5. Sort a list

def sort_list(lst):
    n=len(lst)
    
    for i in range(n-1):
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
lst=[int(x) for x in input("enter integers separated by space:").split()]
sorted_lst=sort_list(lst)
print("Sorted list in ascending order:",sorted_lst)

#6. Remove Duplicates

def remove_dublicates(input_list):
    unique_elements=set(input_list)
    return list(unique_elements)
input_list=[2,4,6,2,8,4,23,45,6,23]
output_list=remove_dublicates(input_list)
print("Original list:",input_list)
print("List after removing duplicates:",output_list)
    
    
#7.string lenght

def string_lenght(input_string):
    count=0
    for char in input_string:
        count += 1
    return count
user_input=input("Enter a string:")
lenght = string_lenght(user_input)
print(f"The lenght of the string '{user_input}' is: {lenght}")


#8. Count of Vowels and Consonants

def count_vowels_consonants(input_string):
    vowels = set("aeiouAEIOU")
    vowel_count=0
    consonant_count =0
    
    for char in input_string:
        if char.isalpha():
            if char in vowels:
                vowel_count +=1
            else:
                consonant_count +=1
    return vowel_count , consonant_count
user_input = input("Enter a string:")
vowels, consonants = count_vowels_consonants(user_input)
print("Number of vowels:",vowels)
print("Number of consonants:",consonants)                
 
# 9. Maze Generator and Solver  

import random

def generate_maze(rows, cols):
    """Generate a random maze with walls ('#') and paths (' ')."""
    maze = [['#' for _ in range(cols)] for _ in range(rows)]
    
    # Define recursive backtracking for maze generation
    def carve_passages(x, y):
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 < nx < rows and 0 < ny < cols and maze[nx][ny] == '#':
                maze[nx][ny] = ' '
                maze[x + dx // 2][y + dy // 2] = ' '
                carve_passages(nx, ny)

    # Start carving passages from (1, 1)
    maze[1][1] = ' '
    carve_passages(1, 1)

    # Define start and end points
    maze[1][0] = 'S'  # Start
    maze[rows - 2][cols - 1] = 'E'  # End

    return maze

def display_maze(maze):
    """Print the maze in the terminal."""
    for row in maze:
        print(''.join(row))

def solve_maze(maze):
    """Solve the maze using Depth-First Search (DFS)."""
    rows, cols = len(maze), len(maze[0])
    start = (1, 0)  # Start position
    end = (rows - 2, cols - 1)  # End position
    stack = [start]
    visited = set()
    path = []

    while stack:
        x, y = stack.pop()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        path.append((x, y))
        if (x, y) == end:
            break

        # Explore neighbors (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] in {' ', 'E'}:
                stack.append((nx, ny))

    # Mark the path in the maze
    for px, py in path:
        if maze[px][py] == ' ':
            maze[px][py] = '.'

    return maze

# Main Execution
rows, cols = 21, 21  # Maze dimensions (odd numbers for proper walls and paths)
maze = generate_maze(rows, cols)
print("Generated Maze:")
display_maze(maze)

print("\nSolved Maze:")
solved_maze = solve_maze(maze)
display_maze(solved_maze)


#10. Maze Generator and Solver
import random

def generate_maze(rows, cols):
    """
    Generates a random maze using recursive backtracking.
    Maze is represented by a grid of 1s (walls) and 0s (paths).
    """
    maze = [[1 for _ in range(cols)] for _ in range(rows)]

    def carve_passages(cx, cy):
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 < nx < rows and 0 < ny < cols and maze[nx][ny] == 1:
                # Create a path between cells
                maze[nx][ny] = 0
                maze[cx + dx // 2][cy + dy // 2] = 0
                carve_passages(nx, ny)

    # Start the maze generation from (1, 1)
    maze[1][1] = 0
    carve_passages(1, 1)

    # Define start and end points
    maze[1][0] = 0  # Start point
    maze[rows - 2][cols - 1] = 0  # End point

    return maze

def display_maze(maze):
    """Displays the maze in text format."""
    for row in maze:
        print("".join(["#" if cell == 1 else " " for cell in row]))

def solve_maze(maze):
    """
    Solves the maze using Depth-First Search (DFS).
    Marks the solution path with '.'.
    """
    rows, cols = len(maze), len(maze[0])
    start = (1, 0)  # Start position
    end = (rows - 2, cols - 1)  # End position
    stack = [start]
    visited = set()

    while stack:
        x, y = stack.pop()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if (x, y) == end:
            break

        # Explore neighbors
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0:
                stack.append((nx, ny))

    # Mark the path in the maze
    for x, y in visited:
        if maze[x][y] == 0:
            maze[x][y] = 2  # Mark the solution path

    return maze

def display_solution(maze):
    """Displays the maze with the solution path marked as '.'."""
    for row in maze:
        print("".join(["#" if cell == 1 else "." if cell == 2 else " " for cell in row]))

# Main Execution
rows, cols = 21, 21  # Maze dimensions (odd numbers for proper walls and paths)
maze = generate_maze(rows, cols)

print("Generated Maze:")
display_maze(maze)

print("\nSolved Maze:")
solved_maze = solve_maze(maze)
display_solution(solved_maze)
