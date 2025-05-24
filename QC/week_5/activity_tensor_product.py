import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

# Step 1: Create a 2-qubit quantum circuit
qc = QuantumCircuit(2)

# Step 2: Apply gates as per your diagram
qc.x(0)          # X gate on qubit 0
qc.cx(0, 1)      # CNOT with control qubit 0, target qubit 1
qc.h(0)          # H gate on qubit 0

# Optional: Draw the circuit
print("Quantum Circuit:")
print(qc.draw())

# Step 3: Initialize simulator
simulator = AerSimulator()

# Step 4: Get final statevector
initial_state = Statevector.from_label('00')
final_state = initial_state.evolve(qc)

# Step 5: Print statevector and plot on Bloch sphere
print("\nFinal Statevector:")
print(final_state)

# Optional: Bloch sphere visualization (needs matplotlib)
fig = plot_bloch_multivector(final_state)
plt.show()




# Define basic gates
I = np.array([[1, 0], [0, 1]])
X = np.array([[0, 1], [1, 0]])
H = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]])

# Tensor product functions
def kron2(a, b):
    return np.kron(a, b)

# CNOT (control = qubit 0, target = qubit 1)
CNOT = np.array([
    [1, 0, 0, 0],  # |00⟩ → |00⟩
    [0, 1, 0, 0],  # |01⟩ → |01⟩
    [0, 0, 0, 1],  # |10⟩ → |11⟩
    [0, 0, 1, 0]   # |11⟩ → |10⟩
])

# Step 1: X ⊗ I
X_I = kron2(X, I)

# Step 2: H ⊗ I
H_I = kron2(H, I)

# Full unitary: (H ⊗ I) ⋅ CNOT ⋅ (X ⊗ I)
U = H_I @ CNOT @ X_I

# Print result
np.set_printoptions(precision=3, suppress=True)
print("Unitary matrix of the quantum circuit:\n", U)