import numpy as np

def inp_mat(prompt):
    print(prompt)
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    print("Enter the values of the matrix row by row (space-separated):")
    
    matrix = []
    for i in range(rows):
        while True:
            row = list(map(float, input(f"Row {i+1}: ").split()))
            if len(row) != cols:
                print(f"Error: Expected {cols} values. Please try again.")
            else:
                matrix.append(row)
                break
    
    return np.array(matrix)

def operations():
    while True:
        print("\nMatrix Operations Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Exit")
        
        choice = int(input("Enter your choice (1-4): "))
        if choice == 4:
            print("Exiting program. Goodbye!")
            break
        
        mat1 = inp_mat("Matrix 1:")
        mat2 = inp_mat("Matrix 2:")
        
        if choice == 1:
            if mat1.shape == mat2.shape:
                print("Result:\n", mat1 + mat2)
            else:
                print("Error: Matrices must have the same dimensions for addition.")
        
        elif choice == 2:
            if mat1.shape == mat2.shape:
                print("Result:\n", mat1 - mat2)
            else:
                print("Error: Matrices must have the same dimensions for subtraction.")
        
        elif choice == 3:
            if mat1.shape[1] == mat2.shape[0]:
                print("Result:\n", np.dot(mat1, mat2))
            else:
                print(f"Error: The number of columns in Matrix 1 ({mat1.shape[1]}) "
                      f"must equal the number of rows in Matrix 2 ({mat2.shape[0]}) for multiplication.")
        
        else:
            print("Invalid choice. Please select a valid operation (1-4).")

if __name__ == "__main__":
    operations()
