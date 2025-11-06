import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    ls = np.array(list)
    float_ls = ls.astype(float)
    print(float_ls)

    mean_rows = [
        float(float_ls[[0, 1, 2]].mean().item()),
        float(float_ls[[3, 4, 5]].mean().item()),
        float(float_ls[[6, 7, 8]].mean().item())
    ]
    mean_columns = [
        float(float_ls[[0, 3, 6]].mean().item()),
        float(float_ls[[1, 4, 7]].mean().item()),
        float(float_ls[[2, 5, 8]].mean().item())
    ]

    var_rows = [
        float(float_ls[[0, 1, 2]].var().item()),
        float(float_ls[[3, 4, 5]].var().item()),
        float(float_ls[[6, 7, 8]].var().item())
    ]
    var_columns = [
        float(float_ls[[0, 3, 6]].var().item()),
        float(float_ls[[1, 4, 7]].var().item()),
        float(float_ls[[2, 5, 8]].var().item())
    ]

    std_rows = [
        float(float_ls[[0, 1, 2]].std().item()),
        float(float_ls[[3, 4, 5]].std().item()),
        float(float_ls[[6, 7, 8]].std().item())
    ]
    stds_columns = [
        float(float_ls[[0, 3, 6]].std().item()),
        float(float_ls[[1, 4, 7]].std().item()),
        float(float_ls[[2, 5, 8]].std().item())
    ]

    max_rows = [
        float(float_ls[[0, 1, 2]].max().item()),
        float(float_ls[[3, 4, 5]].max().item()),
        float(float_ls[[6, 7, 8]].max().item())
    ]
    max_columns = [
        float(float_ls[[0, 3, 6]].max().item()),
        float(float_ls[[1, 4, 7]].max().item()),
        float(float_ls[[2, 5, 8]].max().item())
    ]

    min_rows = [
        float(float_ls[[0, 1, 2]].min().item()),
        float(float_ls[[3, 4, 5]].min().item()),
        float(float_ls[[6, 7, 8]].min().item())
    ]
    min_columns = [
        float(float_ls[[0, 3, 6]].min().item()),
        float(float_ls[[1, 4, 7]].min().item()),
        float(float_ls[[2, 5, 8]].min().item())
    ]

    sum_rows = [
        float(float_ls[[0, 1, 2]].sum().item()),
        float(float_ls[[3, 4, 5]].sum().item()),
        float(float_ls[[6, 7, 8]].sum().item())
    ]
    sum_columns = [
        float(float_ls[[0, 3, 6]].sum().item()),
        float(float_ls[[1, 4, 7]].sum().item()),
        float(float_ls[[2, 5, 8]].sum().item())
    ]

    return {
        "mean": [mean_columns, mean_rows, float(float_ls.mean().item())],
        "variance": [var_columns, var_rows, float(float_ls.var().item())],
        "standard deviation": [stds_columns, std_rows, float(float_ls.std().item())],
        "max": [max_columns, max_rows, float(float_ls.max().item())],
        "min": [min_columns, min_rows, float(float_ls.min().item())],
        "sum": [sum_columns, sum_rows, float(float_ls.sum().item())],
    }
