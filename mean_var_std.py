import numpy as np


def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    m = np.array(list).reshape(3, 3)

    return {
        'mean':               [m.mean(axis=0).tolist(), m.mean(axis=1).tolist(), m.mean().tolist()],
        'variance':           [m.var(axis=0).tolist(),  m.var(axis=1).tolist(),  m.var().tolist()],
        'standard deviation': [m.std(axis=0).tolist(),  m.std(axis=1).tolist(),  m.std().tolist()],
        'max':                [m.max(axis=0).tolist(),  m.max(axis=1).tolist(),  m.max().tolist()],
        'min':                [m.min(axis=0).tolist(),  m.min(axis=1).tolist(),  m.min().tolist()],
        'sum':                [m.sum(axis=0).tolist(),  m.sum(axis=1).tolist(),  m.sum().tolist()],
    }
