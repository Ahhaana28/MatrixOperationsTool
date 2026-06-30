import numpy as np


def input_matrix():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print("Enter the matrix row by row:")

    matrix = []

    for i in range(rows):
        row = list(map(float, input(f"Row {i + 1}: ").split()))
        matrix.append(row)

    return np.array(matrix)


def display_matrix(matrix):
    print("\nResult:")
    print(matrix)


def addition():
    print("\nMatrix A")
    A = input_matrix()

    print("\nMatrix B")
    B = input_matrix()

    if A.shape == B.shape:
        display_matrix(A + B)
    else:
        print("Matrices must have the same dimensions.")


def subtraction():
    print("\nMatrix A")
    A = input_matrix()

    print("\nMatrix B")
    B = input_matrix()

    if A.shape == B.shape:
        display_matrix(A - B)
    else:
        print("Matrices must have the same dimensions.")


def multiplication():
    print("\nMatrix A")
    A = input_matrix()

    print("\nMatrix B")
    B = input_matrix()

    if A.shape[1] == B.shape[0]:
        display_matrix(np.dot(A, B))
    else:
        print("Matrix multiplication is not possible.")


def transpose():
    matrix = input_matrix()
    display_matrix(matrix.T)


def determinant():
    matrix = input_matrix()

    if matrix.shape[0] == matrix.shape[1]:
        print("\nDeterminant =", round(np.linalg.det(matrix), 2))
    else:
        print("Determinant can only be calculated for square matrices.")


def main():

    while True:

        print("\n==============================")
        print(" MATRIX OPERATIONS TOOL")
        print("==============================")
        print("1. Matrix Addition")
        print("2. Matrix Subtraction")
        print("3. Matrix Multiplication")
        print("4. Matrix Transpose")
        print("5. Determinant")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            addition()

        elif choice == "2":
            subtraction()

        elif choice == "3":
            multiplication()

        elif choice == "4":
            transpose()

        elif choice == "5":
            determinant()

        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()