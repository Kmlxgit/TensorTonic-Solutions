def min_max_scaling(data: list) -> list:
    """
    Returns each data column scaled to the range from 0 through 1.
    """
    # Determine number of columns
    n_cols = len(data[0])
    n_rows = len(data)

    # Extract columns and compute min/max per column
    columns = [[data[i][j] for i in range(n_rows)] for j in range(n_cols)]
    col_mins = [min(col) for col in columns]
    col_maxs = [max(col) for col in columns]

    # Scale each element
    result = []
    for i in range(n_rows):
        row = []
        for j in range(n_cols):
            if col_maxs[j] - col_mins[j] == 0:
                row.append(0.0)
            else:
                row.append((data[i][j] - col_mins[j]) / (col_maxs[j] - col_mins[j]))
        result.append(row)

    return result   