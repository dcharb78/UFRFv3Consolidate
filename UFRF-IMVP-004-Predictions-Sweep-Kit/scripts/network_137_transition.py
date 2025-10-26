
#!/usr/bin/env python3
# Toy network sweep to look for a qualitative efficiency change near 137 connections.
# No external libs required. Builds random undirected graphs and computes a simple
# global efficiency metric (average reciprocal shortest path length).
# Usage:
#   python network_137_transition.py N max_k step artifacts/net137.json

import sys, random, json, collections

def build_graph(N, k):
    # Simple random graph where each node connects to k distinct others (cap at N-1)
    g = {i:set() for i in range(N)}
    nodes = list(range(N))
    k = min(k, N-1)
    for i in nodes:
        while len(g[i]) < k:
            j = random.randrange(N)
            if j != i:
                g[i].add(j)
                g[j].add(i)
    return g

def avg_shortest_path_efficiency(g):
    # average of 1/d(u,v) over connected pairs (u != v).
    N = len(g)
    nodes = list(g)
    total = 0.0
    count = 0
    for s in nodes:
        dist = {s:0}
        q = collections.deque([s])
        while q:
            u = q.popleft()
            for v in g[u]:
                if v not in dist:
                    dist[v] = dist[u]+1
                    q.append(v)
        for t,d in dist.items():
            if t != s and d > 0:
                total += 1.0/d
                count += 1
    return (total / count) if count else 0.0

def sweep(N=200, max_k=200, step=5):
    rows = []
    for k in range(1, max_k+1, step):
        g = build_graph(N, k)
        eff = avg_shortest_path_efficiency(g)
        rows.append({"k": k, "efficiency": eff})
        print(f"k={k:3d}  efficiency={eff:.4f}")
    return rows

def main():
    if len(sys.argv) < 5:
        print("Usage: network_137_transition.py N max_k step output.json")
        sys.exit(1)
    N = int(sys.argv[1]); max_k = int(sys.argv[2]); step = int(sys.argv[3])
    out = sys.argv[4]
    rows = sweep(N, max_k, step)
    with open(out, "w") as f:
        json.dump(rows, f, indent=2)
    print("[network] sweep saved:", out)

if __name__ == "__main__":
    main()
