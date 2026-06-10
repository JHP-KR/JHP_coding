def mean_squared_error(y_true, y_pred):
    if len(y_true) != len(y_pred):
        raise ValueError("y_true and y_pred must have the same length")
    if len(y_true) == 0:
        raise ValueError("input data must not be empty")

    return sum(
        (actual - predicted) ** 2
        for actual, predicted in zip(y_true, y_pred)
    ) / len(y_true)


def mean_absolute_error(y_true, y_pred):
    if len(y_true) != len(y_pred):
        raise ValueError("y_true and y_pred must have the same length")
    if len(y_true) == 0:
        raise ValueError("input data must not be empty")

    return sum(
        abs(actual - predicted)
        for actual, predicted in zip(y_true, y_pred)
    ) / len(y_true)


def r2_score(y_true, y_pred):
    if len(y_true) != len(y_pred):
        raise ValueError("y_true and y_pred must have the same length")
    if len(y_true) == 0:
        raise ValueError("input data must not be empty")

    y_mean = sum(y_true) / len(y_true)
    total_sum_of_squares = sum((actual - y_mean) ** 2 for actual in y_true)
    residual_sum_of_squares = sum(
        (actual - predicted) ** 2
        for actual, predicted in zip(y_true, y_pred)
    )

    if total_sum_of_squares == 0:
        raise ValueError("r2_score is undefined when all y_true values are identical")

    return 1 - residual_sum_of_squares / total_sum_of_squares
