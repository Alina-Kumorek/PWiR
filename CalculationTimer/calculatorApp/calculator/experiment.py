import time
from calculator import uklad, iteracjaprosta, iteracjarichardsona
# import uklad, iteracjaprosta, iteracjarichardsona

class Experiment:
    def __init__(self, n = 100, M = 10, N = 10):
        self.n = n                          # maksymalny rozmiar
        self.M = M                          # liczba pomiarow
        self.N = N                          # liczba rozmiarow
        self.wyniki = {
            "prosta": [],
            "richardson": [],
            "timer": 0.0
        }

    def _time(self, k, method=0):
        iteracje = 50
        eps = 0.0000000001

        czas = 0.0
        
        u = uklad.Uklad(k)

        for i in range(self.M):
            u.losuj_uklad_symetryczny_dodatnio_okreslony()

            stoper = time.time()

            if method == 0:
                test = iteracjaprosta.IteracjaProsta(u)
            else:
                test = iteracjarichardsona.IteracjaRichardsona(u)
            
            test.przygotuj()
            # test.iteruj(iteracje, 0)
            test.iteruj_roznica(eps, 0)
            stoper = time.time() - stoper

            czas = czas + stoper
        
        return czas/self.M

    def run(self):
        krok = self.n / self.N
        self.wyniki = {
            "prosta": [],
            "richardson": [],
            "timer": 0.0
        }

        timer = time.time()

        for i in range(self.N):
            k = int((i+1)*krok)
            t0 = self._time(k, 0)
            self.wyniki["prosta"].append({"x": k,
                                "y": t0})
            t1 = self._time(k, 1)
            self.wyniki["richardson"].append({"x": k,
                                "y": t1})
            
        timer = time.time() - timer
        self.wyniki["timer"]=round(timer, 2)

        return self.wyniki
    
if __name__ == '__main__':
    print(Experiment().run())