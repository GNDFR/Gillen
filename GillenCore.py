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

        self.delta = max(degrees)
        self.avg_deg = (2 * self.e) / n
        self.p = (2 * self.e) / (n * (n - 1)) if n > 1 else 0
        self.tau = self.delta / self.avg_deg if self.avg_deg > 0 else 0

    def get_k(self):
        if self.n <= 0: return 0
        if self.e == 0: return 1
        if self.p >= 1.0: return self.n

        q_inv_ln = -math.log(max(1e-10, 1 - self.p))
        freedom = 2 * math.log(self.n / (math.log(self.n + 1) + 1) + 1)
        k_gillen = (self.n * q_inv_ln) / freedom
        l_max = self.avg_deg + (self.delta / self.n)
        l_min = -1.5 * math.sqrt(self.avg_deg * (1 - self.p))
        k_hoffman = 1 - (l_max / min(-0.1, l_min))
        ln_b = -math.log(max(1e-10, 1 - self.p))
        alpha_est = 2 * (math.log(self.n) / ln_b) if ln_b > 0 else self.n
        k_lovasz = self.n / max(1.0, alpha_est)
        k_local = 0

        if self.tau > 2:
            density_correction = (2 * self.e) / (self.delta**2) if self.delta > 0 else 0
            k_local = (self.delta + 1) * min(1, density_correction)

        k_twist = 3 if (self.avg_deg >= 2 and self.tau < 1.5) else 0
        k_final = max(k_gillen, k_hoffman, k_lovasz, k_local, k_twist)

        result = math.ceil(k_final)

        return max(2, min(self.n, result, self.delta + 1))

