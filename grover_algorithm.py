# Grover's Algorithm Implementation using Qiskit

from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Step 1 - Create the Oracle (mark the target state)
def grover_oracle(n, target):
    qc = QuantumCircuit(n)
    target_bin = format(target, f'0{n}b')
    for qubit, bit in enumerate(target_bin):
        if bit == '0':
            qc.x(qubit)
    qc.h(range(n))
    qc.mct(list(range(n-1)), n-1)  # multi-controlled Toffoli (oracle mark)
    qc.h(range(n))
    for qubit, bit in enumerate(target_bin):
        if bit == '0':
            qc.x(qubit)
    return qc

# Step 2️ - Create the Diffuser (inversion about mean)
def diffuser(n):
    qc = QuantumCircuit(n)
    qc.h(range(n))
    qc.x(range(n))
    qc.h(n-1)
    qc.mct(list(range(n-1)), n-1)
    qc.h(n-1)
    qc.x(range(n))
    qc.h(range(n))
    return qc

# Step 3️ - Combine Oracle + Diffuser
n = 3  # number of qubits
target = 5  # number we want to search (binary 101)

grover = QuantumCircuit(n, n)
grover.h(range(n))  # superposition

oracle = grover_oracle(n, target)
diff = diffuser(n)

# Grover iterations
iterations = 1  # For small n, 1 iteration is enough
for _ in range(iterations):
    grover.append(oracle, range(n))
    grover.append(diff, range(n))

# Step 4️ - Measure
grover.measure(range(n), range(n))

# Step 5️ - Run the circuit
simulator = Aer.get_backend('qasm_simulator')
result = execute(grover, simulator, shots=1024).result()
counts = result.get_counts()

# Step 6️ - Visualize results
print("Measurement Results:", counts)
plot_histogram(counts)
plt.show()
