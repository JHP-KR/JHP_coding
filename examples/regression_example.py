from src.linear_regression import SimpleLinearRegression
from src.metrics import mean_squared_error, mean_absolute_error, r2_score


X = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

model = SimpleLinearRegression()
model.fit(X, y)

predictions = model.predict(X)

print("slope:", model.slope)
print("intercept:", model.intercept)
print("predictions:", predictions)
print("MSE:", mean_squared_error(y, predictions))
print("MAE:", mean_absolute_error(y, predictions))
print("R2:", r2_score(y, predictions))
