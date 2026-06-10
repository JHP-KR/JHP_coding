from src.linear_regression import SimpleLinearRegression


X = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

model = SimpleLinearRegression()
model.fit(X, y)

predictions = model.predict(X)

print("slope:", model.slope)
print("intercept:", model.intercept)
print("predictions:", predictions)
