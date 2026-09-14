"""Recompute Table 1 indicators for all 62 networks on the frozen dataset."""
import sys, math, csv, json
from pathlib import Path
import numpy as np
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT/'reproduction_kit'/'pipeline'))
sys.path.insert(0, str(ROOT/'dataset_v2'))
from data_loader import load_city
from compute_curves import generalised_D
import importlib.util
spec = importlib.util.spec_from_file_location('rt', ROOT/'dataset_v2'/'reproduce_table1.py')
rt = importlib.util.module_from_spec(spec); spec.loader.exec_module(rt)

F = ROOT/'August - revision'/'dataset_frozen_2026-09-12'
NAME_FIX = {"Xi'an": "Xian"}

def ind(ldir, pdir, city):
    P = load_city(ldir, pdir, city)
    D = generalised_D(P, transfer_penalty=5.0, wait_weight=2.0)
    tMc = math.ceil(float(np.nanmax(D[np.isfinite(D)])))
    b = np.arange(0, tMc+1, 1.0)
    d = rt.degree_curve(D, b); tau = b/tMc
    g, th, r2 = rt.fit_eq2(tau, d)
    return dict(n=D.shape[0], t_M=tMc, gamma=round(g,2), theta=round(th,3), R2=round(r2,4),
                d30=round(float(d[min(30,len(d)-1)]),3),
                tau5=round(rt.tau_at(0.05,g,th),3), tau50=round(rt.tau_at(0.50,g,th),3),
                tau95=round(rt.tau_at(0.95,g,th),3))

cities = sorted(p.name[:-7] for p in (F/'L2').glob('*-L.json'))
tex = rt.parse_table1(ROOT/'August - revision'/'submitted_version'/'main.tex')
tex_by_stem = {NAME_FIX.get(k, k): v for k, v in tex.items()}

out = []
for i, c in enumerate(cities, 1):
    try:
        r = ind(F/'L2', F/'P2', c)
        old = tex_by_stem.get(c, {})
        row = dict(city=c, **{f'new_{k}': v for k, v in r.items()},
                   **{f'old_{k}': old.get(k) for k in ['n','t_M','gamma','theta','R2','d30','tau5','tau50','tau95']})
        out.append(row)
        print(f'[{i}/62] {c:12s} n={r["n"]:4d} t_M={r["t_M"]:4d} g={r["gamma"]:6.2f} th={r["theta"]:.3f} R2={r["R2"]:.4f}', flush=True)
    except Exception as e:
        print(f'[{i}/62] {c:12s} ERROR {type(e).__name__}: {e}', flush=True)

with open(F/'table1_frozen.csv','w',newline='',encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)

def mean(key):
    v=[r[key] for r in out if r[key] is not None]
    return round(float(np.mean(v)),3), round(float(np.std(v,ddof=1)),3)
summ={k:mean(f'new_{k}') for k in ['n','t_M','gamma','theta','d30','tau5','tau50','tau95']}
summ_old={k:mean(f'old_{k}') for k in ['n','t_M','gamma','theta','d30','tau5','tau50','tau95']}
json.dump(dict(new=summ, old_from_tex=summ_old, n_cities=len(out)), open(F/'ea_summary_frozen.json','w'), indent=1)
print('\nEA MEANS (new) :', summ)
print('EA MEANS (tex) :', summ_old)
