from flask import jsonify
import pyhf
import json

def regionA(request):
    patch = request.get_json(silent=True)
    w = pyhf.Workspace(json.load(open('RegionA.json')))
    m = w.model(
        patches = [patch],
        modifier_settings={
            'normsys': {'interpcode': 'code4'},
            'histosys': {'interpcode': 'code4p'},
        },
    )
    d = w.data(m)
    o,e = pyhf.utils.hypotest(1.0,d,m, return_expected_set=True)

    return jsonify(
        {
            'CLs_obs': o.tolist()[0],
            'CLs_exp': [ee.tolist()[0] for ee in e]
        }
    )

def regionC(request):
    patch = request.get_json(silent=True)
    w = pyhf.Workspace(json.load(open('RegionC.json')))
    m = w.model(
        patches = [patch],
        modifier_settings={
            'normsys': {'interpcode': 'code4'},
            'histosys': {'interpcode': 'code4p'},
        },
    )
    d = w.data(m)
    o,e = pyhf.utils.hypotest(1.0,d,m, return_expected_set=True)

    return jsonify(
        {
            'CLs_obs': o.tolist()[0],
            'CLs_exp': [ee.tolist()[0] for ee in e]
        }
    )
