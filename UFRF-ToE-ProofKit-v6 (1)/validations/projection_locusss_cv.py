
import sys, json, math
from src.projection.cv_loader import load_splits, load_dataset, pair_deltas
from src.projection.cv_fit import fit_S_difference, predict_difference

def main(splits_json, dataset_csv):
    cfg, priors = load_splits(splits_json)
    data = load_dataset(dataset_csv)
    dM = math.log(1000.0)  # LoCuSS sample: fixed scale distance
    results = {"project": cfg["project"], "splits": []}

    # Simple LOTO splits (WL/HSE/SZ)
    for sp in cfg["splits"]:
        sid = sp["id"]
        if sid.startswith("LOTO_"):
            t_hold = sp["holdout"][0]
            t_ref  = sp["ref"]
            train = sp["train"]
            # Fit S on each available training pair against the ref
            S_hats = []
            for t in train:
                clusters = [cl for cl in data if t in data[cl] and t_ref in data[cl]]
                fit = fit_S_difference(data, clusters, t, t_ref, dM, priors[t], priors[t_ref])
                S_hats.append(fit["S"])
            S_avg = float(sum(S_hats)/len(S_hats)) if S_hats else 0.0
            # Predict holdout vs ref
            clusters_hold = [cl for cl in data if t_hold in data[cl] and t_ref in data[cl]]
            preds = []
            for cl in clusters_hold:
                y_hat = predict_difference(dM, S_avg, priors[t_hold], priors[t_ref])
                y_obs = data[cl][t_hold] - data[cl][t_ref]
                preds.append({"cluster":cl, "y_hat": y_hat, "y_obs": y_obs, "resid": y_obs - y_hat})
            results["splits"].append({"id":sid, "S_avg":S_avg, "preds":preds})

        elif sid.startswith("PAIRWISE"):
            # Train only on WL/HSE differences; predict WL/SZ and HSE/SZ
            pairs_train = sp.get("train_pairs", [])
            for (t1,t2) in pairs_train:
                clusters = [cl for cl in data if t1 in data[cl] and t2 in data[cl]]
                fit = fit_S_difference(data, clusters, t1, t2, dM, priors[t1], priors[t2])
                S_hat = fit["S"]
                preds = []
                for (hp1,hp2) in sp.get("holdout_pairs", []):
                    clusters_h = [cl for cl in data if hp1 in data[cl] and hp2 in data[cl]]
                    for cl in clusters_h:
                        y_hat = predict_difference(dM, S_hat, priors[hp1], priors[hp2])
                        y_obs = data[cl][hp1] - data[cl][hp2]
                        preds.append({"cluster":cl, "pair":[hp1,hp2], "y_hat": y_hat, "y_obs": y_obs, "resid": y_obs - y_hat})
                results["splits"].append({"id":"PAIRWISE_WL_HSE","S_hat":S_hat, "preds":preds})

    # Save artifacts
    import os
    os.makedirs("artifacts", exist_ok=True)
    with open("artifacts/projection_cv_summary.json","w") as f:
        json.dump(results, f, indent=2)
    print("Saved artifacts/projection_cv_summary.json")

if __name__ == "__main__":
    if len(sys.argv)<3:
        print("Usage: python validations/projection_locusss_cv.py <splits.json> <dataset.csv>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
