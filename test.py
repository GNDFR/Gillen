import os
import glob
import time
from GillenCore import GillenLogic

def main():
    targets = sorted(glob.glob(os.path.join("exgraph", "*.col.txt")))

    if not targets:
        print("[!] No graph files found in 'exgraph/' directory.")
        return

    for path in targets:
        filename = os.path.basename(path)
        n, e_list = 0, []

        # Load Data
        try:
            with open(path, 'r') as f:
                for line in f:
                    if line.startswith('p'):
                        n = int(line.split()[2])
                    elif line.startswith('e'):
                        parts = line.split()
                        e_list.append((int(parts[1]), int(parts[2])))
        except Exception as e:
            print(f"[!] Error loading {filename}: {e}")
            continue

        # Launch Gillen Logic
        start_time = time.time()
        core = GillenLogic(n, e_list)
        k_found = core.get_k()
        elapsed = time.time() - start_time

        # Output
        print(f"[*] {filename:20} | N: {n:5} | E: {len(e_list):8} | K: {k_found:3} | Time: {elapsed:.4f}s")

if __name__ == "__main__":
    main()

