import numpy as np

wcs: list
wgs: list
sigmas: list

def m(mt):
    ws = [wc.dot(wg).dot(wg).dot(1 / sigma) for wc, wg, sigma in zip(wcs, wgs, sigmas)]
    total = np.sum(ws, axis=None)
    return ws / total * mt
    
