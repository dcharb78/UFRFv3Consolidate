
import json, csv, math
from collections import defaultdict

def load_splits(json_path):
    with open(json_path) as f:
        cfg = json.load(f)
    priors = {k: v.get("alpha_total", None) for k,v in cfg["alpha_priors"].items()}
    return cfg, priors

def load_dataset(csv_path):
    data = defaultdict(dict)
    with open(csv_path) as f:
        r = csv.DictReader(f)
        for row in r:
            cl = row["cluster"]; tech = row["tech"]
            data[cl][tech] = float(row["ln_mass"])
    return data

def pair_deltas(data, t1, t2):
    X=[]; Y=[]
    for cl, rec in data.items():
        if t1 in rec and t2 in rec:
            Y.append(rec[t1] - rec[t2])
            X.append(cl)
    return X, Y  # X are ids here (we map to design values later)
