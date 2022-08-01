import numpy as np


test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def calculate(list1):
    array1 = np.array(list1)
    if type(list1) is list and len(list1) == 9:
        matrix1 = array1.reshape(3, 3)
        mean = [
            np.mean(matrix1, axis=0).tolist(),
            np.mean(matrix1, axis=1).tolist(),
            np.mean(array1),
        ]
        var = [
            np.var(matrix1, axis=0).tolist(),
            np.var(matrix1, axis=1).tolist(),
            np.var(array1),
        ]
        std = [
            np.std(matrix1, axis=0).tolist(),
            np.std(matrix1, axis=1).tolist(),
            np.std(array1),
        ]

        max = [
            np.amax(matrix1, axis=0).tolist(),
            np.amax(matrix1, axis=1).tolist(),
            np.amax(array1),
        ]
        min = [
            np.amin(matrix1, axis=0).tolist(),
            np.amin(matrix1, axis=1).tolist(),
            np.amin(array1),
        ]
        sum = [
            np.sum(matrix1, axis=0).tolist(),
            np.sum(matrix1, axis=1).tolist(),
            np.sum(array1),
        ]
        calculations = {
            "mean": mean,
            "variance": var,
            "standard deviation": std,
            "max": max,
            "min": min,
            "sum": sum,
        }
        return calculations
    else:
        raise ValueError("List must contain nine numbers.")


print(calculate(test_list))
