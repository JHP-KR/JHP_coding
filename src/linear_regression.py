class SimpleLinearRegression:
    """A minimal simple linear regression model for study purposes."""

    def __init__(self):
        self.slope = None
        self.intercept = None

    def fit(self, x_values, y_values):
        if len(x_values) != len(y_values):
            raise ValueError("x_values and y_values must have the same length")
        if len(x_values) == 0:
            raise ValueError("input data must not be empty")

        x_mean = sum(x_values) / len(x_values)
        y_mean = sum(y_values) / len(y_values)

        numerator = sum(
            (x - x_mean) * (y - y_mean)
            for x, y in zip(x_values, y_values)
        )
        denominator = sum((x - x_mean) ** 2 for x in x_values)

        if denominator == 0:
            raise ValueError("x_values must not all be identical")

        self.slope = numerator / denominator
        self.intercept = y_mean - self.slope * x_mean

        return self

    def predict(self, x_values):
        if self.slope is None or self.intercept is None:
            raise ValueError("model must be fitted before prediction")

        return [
            self.slope * x + self.intercept
            for x in x_values
        ]
