# machine_learning_examples.py
import numpy as np
from cyai.algorithms.machine_learning import support_vector_machine, neural_network

# Generate sample data
X = np.random.rand(100, 10)
y = np.random.randint(0, 2, 100)

# Perform Support Vector Machine
support_vector_machine(X, y)

# Perform Neural Network
neural_network(X, y)
