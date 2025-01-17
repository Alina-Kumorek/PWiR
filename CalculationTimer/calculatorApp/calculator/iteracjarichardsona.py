"""Klasa realizujaca metode iteracji Richardsona"""

from calculator import uklad
# import uklad
import math
import numpy as np
from typing import List

class IteracjaRichardsona:
  
    def __init__(self, ukl):
        """Konstruktor okreslajacy problem"""
        self.n = ukl.A.shape[0]                   # wymiar macierzy
        self.u = uklad.Uklad(self.n)              # uklad do rozwiazania
        self.u.zadaj_uklad(ukl.A, ukl.B)          # zadaje uklad
        self.X = np.zeros([self.n, 1])            # biezace przyblizenie
        self.Xp = np.zeros([self.n, 1])           # poprzednie przyblizenie
        self.normy: List = []                     # lista norm
        self.kmax = 100000                        # maskymalna liczba iteracji

    def przygotuj(self):
        """Mnoży cały układ przez stałą p, tak żeby układ wylosowany
        metodą losuj_uklad_symetryczny_dodatnio_okreslony spełniał warunek zbieżności ||I-A||<1"""
        p = 1/((2*self.n)-1)
        self.u.A *= p
        self.u.B *= p
        
    def iteruj(self, iteracje, norma, wyswietlaj = 0, X0 = None):
        """Wykonuje zadana liczbe iteracji zaczynajac od wektora X0
            lub jezeli nie jest on podany od wektora [[0],[0],[0]]."""
        if X0 is None:
            X0 = np.zeros([self.n, 1])
        self.Xp = X0.copy()
        # resetujemy liste norm
        self.normy = []
        self.normy.append(self.u.norma_wektora(norma, X0))
        k = 0
        while k < iteracje:
            k += 1
            self.X = self.Xp + self.u.B - self.u.A @ self.Xp
            self.normy.append(self.u.norma_wektora(norma, self.X))
            self.Xp = self.X.copy()
            if wyswietlaj == 1:
                self.wypisz_rozwiazanie(k)               
    
    def iteruj_roznica(self, eps, norma, wyswietlaj = 0, X0 = None):
        """Wykonuje iteracje do momentu, gdy norma roznicy kolejnych
            przyblizen nie jest mniejsza niz eps, zaczynajac od wektora X0
            lub jezeli nie jest on podany od wektora [[0],[0],[0]]."""
        if X0 is None:
            X0 = np.zeros([self.n, 1])
        self.Xp = X0.copy()
        # resetujemy liste norm
        self.normy = []
        self.normy.append(self.u.norma_wektora(norma, X0))
        roznica = 1000.0
        k = 0
        while roznica > eps:
            k += 1
            self.X = self.Xp + self.u.B - self.u.A @ self.Xp
            self.normy.append(self.u.norma_wektora(norma, self.X))
            roznica = self.u.norma_roznicy_wektorow(norma, self.Xp, self.X)
            self.Xp = self.X.copy()
            if wyswietlaj == 1:
                self.wypisz_rozwiazanie(k)
            if k >self.kmax:
                print("Liczba iteracji przekroczyla ustalony limit")
                return 0
        return k
    
    def wypisz_uklad(self):
        """Metoda wyswietlajaca uklad"""
        self.u.wypisz_uklad()
    
    def wypisz_rozwiazanie(self, iteracja):
        """Metoda wyswietlajaca wektor rozwiazania"""
        print(f"X({iteracja}) = {self.X[:, 0]}")
        
    def wypisz_normy(self):
        """Metoda wypisujaca liste norm"""
        for i in range(len(self.normy)):
            print(f"||X({i})|| = {self.normy[i]}") 

    def sprawdz_rozwiazanie(self, norma):
        """Metoda sprwadzajaca niedokladnosc rozwiazania"""
        self.u.sprawdz_rozwiazanie(norma, self.X)