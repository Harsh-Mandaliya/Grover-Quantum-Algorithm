# Grover's Algorithm Implementation using Qiskit 1.x
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Step 1️ - Create the Oracle (mark the target state)
def grover_oracle(n, target):
    qc = QuantumCircuit(n)
    target_bin = format(target, f'0{n}b')
    
    # Flip qubits where target bit is 0
    for qubit, bit in enumerate(target_bin):
        if bit == '0':
            qc.x(qubit)
    
    # Multi-controlled Z gate (oracle marking)
    qc.h(n-1)
    if n > 2:
        qc.mcx(list(range(n-1)), n-1)  # mcx instead of mct
    else:
        qc.cx(0, 1)
    qc.h(n-1)
    
    # Flip back
    for qubit, bit in enumerate(target_bin):
        if bit == '0':
            qc.x(qubit)
    
    return qc

# Step 2️ - Create the Diffuser (inversion about mean)
def diffuser(n):
    qc = QuantumCircuit(n)
    
    # Apply H gates
    qc.h(range(n))
    
    # Apply X gates
    qc.x(range(n))
    
    # Multi-controlled Z gate
    qc.h(n-1)
    if n > 2:
        qc.mcx(list(range(n-1)), n-1)  # mcx instead of mct
    else:
        qc.cx(0, 1)
    qc.h(n-1)
    
    # Apply X gates
    qc.x(range(n))
    
    # Apply H gates
    qc.h(range(n))
    
    return qc

# Step 3️ - Build Grover's Circuit
def build_grover_circuit(n, target, iterations=1):
    """Build complete Grover's circuit"""
    grover = QuantumCircuit(n, n)
    
    # Initialize in superposition
    grover.h(range(n))
    
    # Create oracle and diffuser
    oracle = grover_oracle(n, target)
    diff = diffuser(n)
    
    # Apply Grover iterations
    for _ in range(iterations):
        grover.append(oracle, range(n))
        grover.append(diff, range(n))
    
    # Measure
    grover.measure(range(n), range(n))
    
    return grover

# Step 4️ - Main Execution
def main():
    # Configuration
    n = 3  # number of qubits (search space = 2^n = 8 elements)
    target = 5  # target element (binary 101)
    iterations = 1  # optimal for n=3
    
    print(f"Searching for target: {target} (binary: {format(target, f'0{n}b')})")
    print(f"Search space size: {2**n} elements")
    print(f"Grover iterations: {iterations}")
    print("-" * 50)
    
    # Build circuit
    print("\n Building quantum circuit...")
    grover_circuit = build_grover_circuit(n, target, iterations)
    print("Circuit built successfully!")
    
    # Visualize circuit
    print("\n Drawing quantum circuit...")
    try:
        fig = grover_circuit.draw('mpl', scale=0.8, fold=20)
        plt.savefig('grover_circuit.png', dpi=300, bbox_inches='tight')
        print("Circuit saved as 'grover_circuit.png'")
        plt.close()
    except Exception as e:
        print(f"Circuit drawing failed: {e}")
        print("Showing text representation instead...")
        print(grover_circuit.draw('text'))
    
    # Run simulation
    print("\nRunning quantum simulation...")
    simulator = AerSimulator()
    compiled_circuit = transpile(grover_circuit, simulator)
    result = simulator.run(compiled_circuit, shots=1024).result()
    counts = result.get_counts()
    print("Simulation completed!")
    
    # Display results
    print("\nMeasurement Results:")
    print("-" * 50)
    for state, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        percentage = (count / 1024) * 100
        bar = " " * int(percentage / 2)
        print(f"  |{state}⟩: {count:4d}/1024 ({percentage:5.2f}%) {bar}")
    
    # Check if target was found
    target_binary = format(target, f'0{n}b')
    print("\n" + "=" * 50)
    if target_binary in counts:
        success_rate = (counts[target_binary] / 1024) * 100
        print(f"SUCCESS! Target |{target_binary}⟩ found with {success_rate:.2f}% probability")
    else:
        print(f"Target |{target_binary}⟩ not found in measurements")
    print("=" * 50)
    
    # Visualize histogram
    print("\nCreating histogram...")
    try:
        plt.figure(figsize=(12, 6))
        plot_histogram(counts, title=f"Grover's Algorithm Results (Target: |{target_binary}⟩)")
        plt.savefig('grover_histogram.png', dpi=300, bbox_inches='tight')
        print("Histogram saved as 'grover_histogram.png'")
        plt.close()
    except Exception as e:
        print(f"Histogram creation failed: {e}")
    
    print("\nGrover's Algorithm execution completed!")
    print("\nGenerated files:")
    print("grover_circuit.png (quantum circuit diagram)")
    print("grover_histogram.png (measurement results)")
    print("\n Use these images for your hackathon submission!")

if __name__ == "__main__":
    main()