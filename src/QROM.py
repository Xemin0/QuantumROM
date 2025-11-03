from qiskit.circuit import QuantumCircuit, QuantumRegister

def processing_pattern_str(qc: QuantumCircuit, x: QuantumRegister,
                           pat_str: str, target):
    '''
    Processing the indicator pattern string by negating the corresponding NOTs
    Args:
        - qc (QuantumCircuit)   :
        - x  (QuantumRegister)  :
        - pat_str (List[str])   : indicator string representing logical expression
    Return:
        None
    '''
    assert len(pat_str) == len(x)
    ctrls = []
    negated = []
    # Flip the nageted literals
    for j, b in enumerate(pat_str):
        if '1' == b:
            ctrls.append(x[j])
        elif '0' == b:
            qc.x(x[j]) # Flip
            negated.append(x[j])
            ctrls.append(x[j])
        # '-' or other placeholding chars ignored.

    # Apply the multi-controlled X into target.
    if 0 == len(ctrls):
        qc.x(target)            # adding a constant TRUE / 1 into target bit = nagation
    elif 1 == len(ctrls):
        qc.cx(ctrls[0], target) # target + ctrl
    elif 2 == len(ctrls):
        qc.ccx(ctrls[0], ctrls[1], target)
    else:
        qc.mcx(ctrls, target)

    # Unflip negated controls
    for q in reversed(negated):
        qc.x(q)


def U_from_list_pattern_str(n: int, lst_pat_str):
    '''
    Uf with d-bit output represented by a list of pattern strings as the sum of logical products
    Args:
        - n (int)               : number of control bits
        - lst (List[List[str]]) : list of pattern strings / sum of products
    '''
    x = QuantumRegister(n, 'x')
    d = len(lst_pat_str)
    y = QuantumRegister(d, 'y')
    qc = QuantumCircuit(x, y, name = 'U_f')

    for i, terms in enumerate(lst_pat_str):
        for pat in terms:
            processing_pattern_str(qc, x, pat, y[i])

    return qc, x, y
