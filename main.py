class LinearRegression:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def _sum(self, arr):
    sum = 0

    for element in arr:
      sum += element

    return sum

  def _calc_fit_accuracy(self):
    accuracy_numerator = 0
    accuracy_denominator = 0

    for i in range(len(self.x)):
      accuracy_numerator += (self.predict(self.x[i]) - self.y_mean) ** 2
      accuracy_denominator += (self.y[i] - self.y_mean) ** 2

    self.accuracy =  accuracy_numerator / accuracy_denominator

  def fit(self):
    self.x_mean = self._sum(self.x) / len(x)
    self.y_mean = self._sum(self.y) / len(y)

    slope_numerator = 0;
    slope_denominator = 0;

    for i in range(len(self.x)):
      slope_numerator += (self.y[i] - self.y_mean) ** 2
      slope_denominator +=  (self.x[i] - self.x_mean) ** 2

    self.slope = slope_numerator / slope_denominator
    self.b = -self.slope * self.x_mean + self.y_mean

    self._calc_fit_accuracy()

    return self

  def predict(self, x):
    return self.slope * x + self.b

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

linearRegression = LinearRegression(x, y)
model = linearRegression.fit()

number_to_predict = 7
prediction = model.predict(number_to_predict)

print('predicted_value: {predicted_value}, fit_accuracy: {fit_accuracy}'.format(predicted_value = prediction, fit_accuracy = model.accuracy))