import time
import os
import glob
from GillenCore import GillenLogic

def main():
    # Scanning DIMACS graph files
    targets = sorted(glob.glob(os.path.join("exgraph", "*.col.txt")))

    for path in targets:
        filename = os.path.basename(path)
        n, e_list = 0, []

        # Data Loading
        with open(path, 'r') as f:
            for line in f:
                if line.startswith('p'):
                    n = int(line.split()[2])
                elif line.startswith('e'):
                    p = line.split()
                    e_list.append((int(p[1]), int(p[2])))

        # Singular Field Extraction
        core = GillenLogic(n, e_list)
        k_target = core.get_k()

        print(f"[*] {filename:20} | N: {n:4} | E: {len(e_list):7} | K_FOUND: {k_target}")

if __name__ == "__main__":
    main()
