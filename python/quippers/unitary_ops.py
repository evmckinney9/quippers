import qutip
import numpy as np
import sympy

def main1():
    # prettier printing
    def pprint(matrix):
        return '\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix])

    # get pauli matrices
    sx = qutip.sigmax()
    sy = qutip.sigmay()
    sz = qutip.sigmaz()

    # for each pauli, print it's eigenvalues and eigenvectors
    for op in [sx, sy, sz]:
        print("Operator:\n {}".format(pprint(op)))
        
        # qutip built-in method
        eigvals, eigvecs = op.eigenstates()
    
        print("Eigenvalues:\n {}".format(eigvals))
        print("Eigenvectors:\n {}".format(pprint(eigvecs)))

        # qutip built-in method for diagonalization
        # eigvals_diag = np.diag(eigvals)

        # calculate diagonal matrix explicitly using eigenvector matrix
        eigvec_matrix = np.array([vec.full().T[0] for vec in eigvecs]).T
        eigvals_diag = np.linalg.inv(eigvec_matrix) @ op.full() @ eigvec_matrix
        print("Diagonal matrix of eigenvalues:\n {}\n".format(pprint(eigvals_diag)))


def check_unitary_hermitian(op):
    # qutip built-in methods
    print("Is unitary: {}".format(op.isunitary))
    print("Is hermitian: {}\n".format(op.isherm))

    # calculate unitary and hermitian explicitly
    # check if unitary by checking if self * self^dagger = identity
    print("Is unitary: {}".format(np.allclose(op.full() @ op.dag().full(), np.eye(2))))
    # check if hermitian by checking if self^dagger = self
    print("Is hermitian: {}\n".format(np.allclose(op.dag().full(), op.full())))

def main2():
    #a
    print("a")
    op_list = [qutip.sigmax(), qutip.sigmay(), qutip.sigmaz()]
    list(map(check_unitary_hermitian, op_list))
    #b
    print("b")
    check_unitary_hermitian(1/np.sqrt(2) * qutip.Qobj([[1, 1], [1, -1]]))
    #c
    print("c")
    check_unitary_hermitian(qutip.Qobj([[1, 0], [0, 1j]]))
    #d
    print("d")
    check_unitary_hermitian(qutip.Qobj([[1, 0], [0, np.exp(1j * np.pi / 4)]]))
    #e
    print("e")
    theta = np.random.uniform(0, 2 * np.pi) #rest of proof in doc
    check_unitary_hermitian(qutip.Qobj([[1, np.exp(1j * theta)], [np.exp(-1j* theta), 1]]))
    #f
    print("f")
    check_unitary_hermitian(qutip.Qobj([[1, 1+1j], [1+1j, 0]]))


def main3():
    # setup
    u1 = qutip.Qobj([[1, 0], [0, 1j]])
    check_unitary_hermitian(u1)
    u2 =qutip.Qobj([[1, 1j], [-1j, 1]])
    check_unitary_hermitian(u2)
    u3 = qutip.Qobj([[1, 1], [1, -1]])
    check_unitary_hermitian(u3)

    # calc u3u2u1
    u = u3 * u2 * u1
    print(u)
    check_unitary_hermitian(u)

    # calc u1u2u3
    u = u1 * u2 * u3
    print(u)
    check_unitary_hermitian(u)

def main4():
    from qiskit.circuit.library import RXGate
    print(RXGate(np.pi/2).to_matrix())

def main5():
    # calculate the pauli products
    # xx, yy, zz, xy, yz, zx
    pauli_products = [
        qutip.sigmax() * qutip.sigmax(),
        qutip.sigmay() * qutip.sigmay(),
        qutip.sigmaz() * qutip.sigmaz(),
        qutip.sigmax() * qutip.sigmay(),
        qutip.sigmay() * qutip.sigmaz(),
        qutip.sigmaz() * qutip.sigmax()
    ]

    # print the pauli products
    for op in pauli_products:
        print(op)

if __name__ == "__main__":
    main5()