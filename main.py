inputs = [1, 2, 3, 2.5]
weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]
biases = [2, 3, 0.5]

outputs = []
for row in weights:
  output = 0
  for wght in row:
    output += inputs[row.index(wght)] * wght
  output += biases[weights.index(row)]
  outputs.insert(weights.index(row), output)
  
print(outputs)

