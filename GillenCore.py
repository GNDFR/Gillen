import math

class GillenLogic:
    def __init__(self, n, e_list):
        self.n = n
        self.e = len(e_list)
        if n <= 1: return

        degrees = [0] * (n + 1)
        for u, v in e_list:
            degrees[u] += 1
            degrees[v] += 1

        self.delta = max(degrees) if n > 0 else 0
        self.avg_deg = (2 * self.e) / n if n > 0 else 0
        self.p = (2 * self.e) / (n * (n - 1)) if n > 1 else 0
        self.tau = self.delta / (self.avg_deg + 1e-9)

    def get_k(self):
        if self.n <= 0: return 0
        if self.e == 0: return 1

        q_inv_ln = -math.log(max(1e-10, 1 - self.p))
        denom = 2 * math.log(self.n / (math.log(self.n + 1) + 1) + 1)
        k_global = (self.n * q_inv_ln) / (denom + 1e-9)
        k_local = 0
        if self.tau > 2:
            density_correction = (2 * self.e) / (self.delta**2) if self.delta > 0 else 0
            k_local = (self.delta + 1) * min(1.0, density_correction)

        k_twist = 3 if (self.avg_deg >= 2 and self.tau < 1.5) else 0
        k_raw = max(k_global, k_local, k_twist)

        result = math.ceil(k_raw)
        return max(2, min(self.n, result))
