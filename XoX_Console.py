class XoXMain():
    def __init__(self):
        self.oyun_tahtasi = [["___","___","___"],
                             ["___","___","___"],
                             ["___","___","___"]]

        baslangicYazi="""
        XoX oyununa hoşgeldiniz.
        Oyun 2 kişiliktir.
        1.Oyuncu "X"
        2. Oyuncu "O" olucaktır.
        Hamlenizi yapmak istediğiniz yeri kordinat siteminde giriniz.
        Örnek girdi :
        1
        2
        Örnek Çıktı :
        ___ ___ ___
        _X_ ___ ___
        ___ ___ ___
        Çıkmak için iki değere de 9 giriniz.\n
        \t\t\t\t Oyun Tahtası
        """

        print(baslangicYazi)
        if __name__ == "__main__":
            while True:
                self.tahtaYazdir()
                self.oynamaSırası()

    def tahtaYazdir(self):
        for i in self.oyun_tahtasi:
            print("\t\t\t\t",*i)

    def kapat(self):
        input()
        quit()

    def kontrol(self,j1):
        orta=self.oyun_tahtasi[1][1]
        sag=self.oyun_tahtasi[1][2]
        sol=self.oyun_tahtasi[1][0]
        üst=self.oyun_tahtasi[0][1]
        alt=self.oyun_tahtasi[2][1]
        sagUst=self.oyun_tahtasi[0][2]
        sagAlt=self.oyun_tahtasi[2][2]
        solUst=self.oyun_tahtasi[0][0]
        solAlt=self.oyun_tahtasi[2][0]
        if j1%2==1:
            if solUst=="_X_" and üst=="_X_" and sagUst=="_X_":
                print("1. Oyuncu kazandı")
                self.kapat()
            elif sol=="_X_" and orta=="_X_" and sag=="_X_":
                print("1. Oyuncu kazandı")
                self.kapat()
            elif solAlt=="_X_" and alt=="_X_" and sagAlt=="_X_":
                print("1. Oyuncu kazandı")
                self.kapat()
            elif solUst=="_X_" and sol=="_X_" and solAlt=="_X_":
                print("1. Oyuncu kazandı")
                self.kapat()
            elif üst=="_X_" and orta=="_X_" and alt=="_X_":
                print("1. Oyuncu kazandı")
                self.kapat()
            elif sagUst=="_X_" and sag=="_X_" and sagAlt=="_X_":
                print("1. Oyuncu kazandı")
                self.kapat()
            elif sagUst=="_X_" and orta=="_X_" and solAlt=="_X_":
                print("1. Oyuncu kazandı")
                self.kapat()
            elif solUst=="_X_" and orta=="_X_" and sagAlt=="_X_":
                print("1. Oyuncu kazandı")
                self.kapat()
            else:
                j1=j1+1
                self.oynamaSırası(j1)
        else:
            if solUst=="_O_" and üst=="_O_" and sagUst=="_O_":
                print("2. Oyuncu kazandı")
                self.kapat()
            elif sol=="_O_" and orta=="_O_" and sag=="_O_":
                print("2. Oyuncu kazandı")
                self.kapat()
            elif solAlt=="_O_" and alt=="_O_" and sagAlt=="_O_":
                print("2. Oyuncu kazandı")
                self.kapat()
            elif solUst=="_O_" and sol=="_O_" and solAlt=="_O_":
                print("2. Oyuncu kazandı")
                self.kapat()
            elif üst=="_O_" and orta=="_O_" and alt=="_O_":
                print("2. Oyuncu kazandı")
                self.kapat()
            elif sagUst=="_O_" and sag=="_O_" and sagAlt=="_O_":
                print("2. Oyuncu kazandı")
                self.kapat()
            elif sagUst=="_O_" and orta=="_O_" and solAlt=="_O_":
                print("2. Oyuncu kazandı")
                self.kapat()
            elif solUst=="_O_" and orta=="_O_" and sagAlt=="_O_":
                print("2. Oyuncu kazandı")
                self.kapat()
            else:
                j1=j1+1
                self.oynamaSırası(j1)

    def oynamaSırası(self, q=1):
            if q%2==1:
                print("1.Oyuncu")
            else:
                print("2.Oyuncu")
            x=int(input("x Kordinatını Giriniz: "))
            y=int(input("y Kordinatını Giriniz: "))
            x=x-1
            y=y-1
            if x==8 and y==8:
                self.kapat()
            self.yerlestirme(x,y,q)

    def yerlestirme(self,k,l,j):
        try:
            t=self.oyun_tahtasi[l][k]
            if t=="_X_"or t=="_O_":
                print("Girdiğiniz yer dolu")
                self.oynamaSırası(j)
            elif j%2==1:
                self.oyun_tahtasi[l][k]="_X_"
                self.tahtaYazdir()
            else:
                self.oyun_tahtasi[l][k]="_O_"
                self.tahtaYazdir()          
        except:
                print("1 ve 3 arasında değer giriniz.")
                self.oynamaSırası(j)
        self.kontrol(j)
        j=j+1
XoXMain()
            

