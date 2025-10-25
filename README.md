# Grover’s Quantum Search Algorithm

This project implements **Grover’s Algorithm** using **Qiskit** to demonstrate **quantum speedup** in searching an unsorted dataset.

## Overview
- **Hackathon:** Planck’d 2025 (Quantum Computing Club, IIIT Bangalore)
- **Track:** Quantum Algorithms
- **Team Members:** Harsh Mandaliya, Prajapati Sanjay, Member 3, Member 4

## Algorithm Steps
1. Initialize qubits in superposition.
2. Apply Oracle to mark target.
3. Apply Diffuser to amplify the marked state.
4. Repeat (Oracle + Diffuser).
5. Measure and analyze results.

## Tools & Frameworks
- Python 3.12
- Qiskit
- Matplotlib
- IBM Quantum Simulator

## Results
Grover’s algorithm successfully identified the target state (e.g., `|101⟩`) with high probability.

| Classical | Quantum |
|------------|----------|
| O(N) | O(√N) |

## Files Included
- `grover_algorithm.py` – Full implementation code  
- `Planckd_Grover_Algorithm_Presentation.pptx` – Hackathon presentation  
- `Planckd_Grover_Algorithm_Report.pdf` – Full project report  

## Future Work
- Run on IBM Quantum hardware  
- Extend to cryptographic and optimization problems  

## Authors
- Harsh Mandaliya  
- Ritik Kalal  

# Grover’s Quantum Search Algorithm implemented in Qiskit for Planck’d Hackathon.


