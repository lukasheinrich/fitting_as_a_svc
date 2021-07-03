from flask import jsonify
import pyhf
import json

pyhf.set_backend('pytorch')

def _regionA(patch):
    w = pyhf.Workspace(json.load(open('RegionA.json')))
    m = w.model(
        patches = [patch],
        modifier_settings={
            'normsys': {'interpcode': 'code4'},
            'histosys': {'interpcode': 'code4p'},
        },
    )
    d = w.data(m)
    o,e = pyhf.infer.hypotest(1.0,d,m, return_expected_set=True)
    return {
            'CLs_obs': float(o),
            'CLs_exp': [float(ee) for ee in e]
    }

def _regionC(patch):
    w = pyhf.Workspace(json.load(open('RegionC.json')))
    m = w.model(
        patches = [patch],
        modifier_settings={
            'normsys': {'interpcode': 'code4'},
            'histosys': {'interpcode': 'code4p'},
        },
    )
    d = w.data(m)
    o,e = pyhf.infer.hypotest(1.0,d,m, return_expected_set=True)
    return {
            'CLs_obs': float(o),
            'CLs_exp': [float(ee) for ee in e]
    }
def regionA(request):
    patch = request.get_json(silent=True)
    return jsonify(_regionA(patch))

def regionC(request):
    patch = request.get_json(silent=True)
    return jsonify(_regionC(patch))

if __name__ == '__main__':
    import sys
    import time
    p = json.load(sys.stdin)
    start = time.time()
    for i in range(10):
        print(json.dumps(_regionA(p)))
    print((time.time()-start)/10)