

def matrix_operation(array1, array2, operation):
    if operation == "dot":
        return np.dot(array1, array2)
    elif operation == "matrix":
        return np.matmul(array1, array2)
    elif operation == "determinant":
        det1 = np.linalg.det(array1) if array1.shape[0] == array1.shape[1] else "Not a square matrix"
        det2 = np.linalg.det(array2) if array2.shape[0] == array2.shape[1] else "Not a square matrix"
        return det1, det2
    else:
        return "Invalid operation"