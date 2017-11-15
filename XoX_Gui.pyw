import tkinter as tk
from tkinter import messagebox


class XoX_Gui(object):
    """XoX oyununun grafik arabirimli versiyonu.

    2 kullanıcının oynayacağı şekilde dizayn edilmiştir. Kullanıcı geçişleri otomatiktir.
    Grafik arabirim üzerinde oynanan oyun arkaplanda bir liste çalıştırır. Kontroller bu
    liste üzerinden yapılır.

    Nitelikler:

        oyun_tahtasi : Oyunun arkaplanda oynandığı matris listedir.
        root         : Oyunun oynandığı penceredir.
        xRes         : X işaretli resimdir. Butonların üzerinde gösterilecek.
        bosRes       : Bos resimdir. Butonların üzerinde varsayılan olarak gösterilecek.
        oRes         : O işaretli resimdir. Butonların üzerinde gösterilecek.

    """
    def __init__(self):
        #arkaplanda çalışan listenin tanımı
        self.oyun_tahtasi = [["___","___","___"],
                             ["___","___","___"],
                             ["___","___","___"]]
        self.root=tk.Tk()
        self.root.resizable(False, False)
        genislik = int((self.root.winfo_screenwidth()-369)/2)
        yukseklik = int((self.root.winfo_screenheight()-369)/2)
        self.root.geometry("369x369+%d+%d"%(genislik,yukseklik))
        self.root.title("XoX")
        self.bosRes=tk.PhotoImage(file="./resimler/bos_kutu.png")
        self.xRes=tk.PhotoImage(file="./resimler/X_Kutu.png")
        self.oRes=tk.PhotoImage(file="./resimler/O_Kutu.png")
        self.sira=0 #Sıra buradan yönetilir.
    def basla(self):
        """
        Başlatma fonksiyonudur. Oluşturulan root penceresinin ekranda görünür olmasını sağlar
        ve ana döngüyü başlatır.

        Dışarıdan çağırıldığında bu metod çağırılmak zorundadır.
        """

        self.pencereCiz()
        self.root.mainloop() #Ana döngü

    def pencereCiz(self):
        """
        Pencerenin içindeki widgetleri çizen fonksiyon. Başlangıçta  tüm resimler
        boştur.
        """

        #Butonların tanımlanması
        self.but1=tk.Button(self.root,image=self.bosRes,command=lambda: self.resDegis(id(self.but1)))
        self.but2=tk.Button(self.root,image=self.bosRes,command=lambda: self.resDegis(id(self.but2)))
        self.but3=tk.Button(self.root,image=self.bosRes,command=lambda: self.resDegis(id(self.but3)))
        self.but4=tk.Button(self.root,image=self.bosRes,command=lambda: self.resDegis(id(self.but4)))
        self.but5=tk.Button(self.root,image=self.bosRes,command=lambda: self.resDegis(id(self.but5)))
        self.but6=tk.Button(self.root,image=self.bosRes,command=lambda: self.resDegis(id(self.but6)))
        self.but7=tk.Button(self.root,image=self.bosRes,command=lambda: self.resDegis(id(self.but7)))
        self.but8=tk.Button(self.root,image=self.bosRes,command=lambda: self.resDegis(id(self.but8)))
        self.but9=tk.Button(self.root,image=self.bosRes,command=lambda: self.resDegis(id(self.but9)))


        #Butonların konumlandırılması
        self.but1.grid(row=0,column=0)
        self.but2.grid(row=0,column=1)
        self.but3.grid(row=0,column=2)
        self.but4.grid(row=1,column=0)
        self.but5.grid(row=1,column=1)
        self.but6.grid(row=1,column=2)
        self.but7.grid(row=2,column=0)
        self.but8.grid(row=2,column=1)
        self.but9.grid(row=2,column=2)


        #Buton resimlerinin çizilmesi
        self.but1.img=self.bosRes
        self.but2.img=self.bosRes
        self.but3.img=self.bosRes
        self.but4.img=self.bosRes
        self.but5.img=self.bosRes
        self.but6.img=self.bosRes
        self.but7.img=self.bosRes
        self.but8.img=self.bosRes
        self.but9.img=self.bosRes



    def resDegis(self, ButId):
        """
        Tıklanan butonların resimlerinin değişmesini sağlayan fonksiyondur.
        Resim sırası otomatik olarak belirlenir. Herhangi bir kullanıcı
        müdahalesi yoktur. "sira" değişkeni 0 ise X, 1 ise O olarak değiştirilir.

        ARGS:
            ButId: Butonların bellekteki yerleri.
        """
        tiklama=self.tekrarTiklama(ButId) #Boş ya da dolu olması kontrolü
        if tiklama ==1:
            sozluk = { #IDEA : Sözlük kullanmadan direkt değişkeni parametre alarak çözülebilir mi?
                      id(self.but1) : self.but1,
                      id(self.but2) : self.but2,
                      id(self.but3) : self.but3,
                      id(self.but4) : self.but4,
                      id(self.but5) : self.but5,
                      id(self.but6) : self.but6,
                      id(self.but7) : self.but7,
                      id(self.but8) : self.but8,
                      id(self.but9) : self.but9
                      }

            self.sozluk2 = {
                      id(self.but1) : "00",
                      id(self.but2) : "01",
                      id(self.but3) : "02",
                      id(self.but4) : "10",
                      id(self.but5) : "11",
                      id(self.but6) : "12",
                      id(self.but7) : "20",
                      id(self.but8) : "21",
                      id(self.but9) : "22"
                      }

            if self.sira==0:
                sozluk[ButId].configure(image=self.xRes)
                sozluk[ButId].img=self.xRes
                self.oyun_tahtasi[int(self.sozluk2[ButId][0])][int(self.sozluk2[ButId][1])]="_O_"
                self.sira=1
                self.kontrol(0)
            elif self.sira==1:
                sozluk[ButId].configure(image=self.oRes)
                sozluk[ButId].img=self.oRes
                self.oyun_tahtasi[int(self.sozluk2[ButId][0])][int(self.sozluk2[ButId][1])]="_X_"
                self.sira=0
                self.kontrol(1)
                #burda bahsedilen _X_ GUI de O ya denk gelmektedir.Tam terside doğrudur.
        else:
            messagebox.showinfo("Yanlış Hamle", "Orası Dolu!")


    def kontrol(self,j1):
        """
        Her hamle sonunda self.oyun_tahtasi objesinden veri alarak kazananın olup olmadığını
        belirleyen metod. Kontrolü pencere üzerinden değil arkadaki liste üzerinden yapar.

        XoX_Console.py dosyasından alınmış bir metottur.

        ARGS:
            j1: Sırayı belirleyen argüman.
        """
        #Önce yerler tanımlanır.
        self.orta=self.oyun_tahtasi[1][1]
        self.sag=self.oyun_tahtasi[1][2]
        self.sol=self.oyun_tahtasi[1][0]
        self.üst=self.oyun_tahtasi[0][1]
        self.alt=self.oyun_tahtasi[2][1]
        self.sagUst=self.oyun_tahtasi[0][2]
        self.sagAlt=self.oyun_tahtasi[2][2]
        self.solUst=self.oyun_tahtasi[0][0]
        self.solAlt=self.oyun_tahtasi[2][0]

        #Bu yerlere göre tüm varyasyonlar kontrol edilir.
        if j1%2==1:
            if self.solUst=="_X_" and self.üst=="_X_" and self.sagUst=="_X_":
                messagebox.showinfo("Oyun Bitti","Kazanan 2. Oyuncu!")
                self.sifirla()
                return
            elif self.sol=="_X_" and self.orta=="_X_" and self.sag=="_X_":
                messagebox.showinfo("Oyun Bitti","Kazanan 2. Oyuncu!")
                self.sifirla()
                return
            elif self.solAlt=="_X_" and self.alt=="_X_" and self.sagAlt=="_X_":
                messagebox.showinfo("Oyun Bitti","Kazanan 2. Oyuncu!")
                self.sifirla()
                return
            elif self.solUst=="_X_" and self.sol=="_X_" and self.solAlt=="_X_":
                messagebox.showinfo("Oyun Bitti","Kazanan 2. Oyuncu!")
                self.sifirla()
                return
            elif self.üst=="_X_" and self.orta=="_X_" and self.alt=="_X_":
                messagebox.showinfo("Oyun Bitti","Kazanan 2. Oyuncu!")
                self.sifirla()
                return
            elif self.sagUst=="_X_" and self.sag=="_X_" and self.sagAlt=="_X_":
                messagebox.showinfo("Oyun Bitti","Kazanan 2. Oyuncu!")
                self.sifirla()
                return
            elif self.sagUst=="_X_" and self.orta=="_X_" and self.solAlt=="_X_":
                messagebox.showinfo("Oyun Bitti","Kazanan 2. Oyuncu!")
                self.sifirla()
                return
            elif self.solUst=="_X_" and self.orta=="_X_" and self.sagAlt=="_X_":
                messagebox.showinfo("Oyun Bitti","Kazanan 2. Oyuncu!")
                self.sifirla()
                return

        else:
            #X sırasında X için O sırasında O için kontrol yapılır.
            #Bu sayede kontrol adımları azaltılmış olur.
            if self.solUst=="_O_" and self.üst=="_O_" and self.sagUst=="_O_":
                messagebox.showinfo("Oyun Bitti","Kazanan 1. Oyuncu!")
                self.sifirla()
                return
            elif self.sol=="_O_" and self.orta=="_O_" and self.sag=="_O_":
                messagebox.showinfo("Oyun Bitti","Kazanan 1. Oyuncu!")
                self.sifirla()
                return
            elif self.solAlt=="_O_" and self.alt=="_O_" and self.sagAlt=="_O_":
                messagebox.showinfo("Oyun Bitti","Kazanan 1. Oyuncu!")
                self.sifirla()
                return
            elif self.solUst=="_O_" and self.sol=="_O_" and self.solAlt=="_O_":
                messagebox.showinfo("Oyun Bitti","Kazanan 1. Oyuncu!")
                self.sifirla()
                return
            elif self.üst=="_O_" and self.orta=="_O_" and self.alt=="_O_":
                messagebox.showinfo("Oyun Bitti","Kazanan 1. Oyuncu!")
                self.sifirla()
                return
            elif self.sagUst=="_O_" and self.sag=="_O_" and self.sagAlt=="_O_":
                messagebox.showinfo("Oyun Bitti","Kazanan 1. Oyuncu!")
                self.sifirla()
                return
            elif self.sagUst=="_O_" and self.orta=="_O_" and self.solAlt=="_O_":
                messagebox.showinfo("Oyun Bitti","Kazanan 1. Oyuncu!")
                self.sifirla()
                return
            elif self.solUst=="_O_" and self.orta=="_O_" and self.sagAlt=="_O_":
                messagebox.showinfo("Oyun Bitti","Kazanan 1. Oyuncu!")
                self.sifirla()
                return

        #Kazanandan sonra berabelik kontrolü yapılır.
        flag = 0
        for i in self.oyun_tahtasi:
            if "___" not in i:
                flag +=1
        if flag == 3:
            messagebox.showinfo("Oyun Bitti", "Berabere kaldınız")
            self.sifirla()
            return


    def tekrarTiklama(self,ButId):
        """
        Tıklanan bir butona oyun boyunca yeniden tıklanmamasını sağlamak için kullanılan
        metod.

        ARGS:
            ButId: Sinyalin hangi butondan gelldiğini belirten argüman.

        RETURNS:
            True: Butonun boş olduğunu anlatan çıktı. (Tıklanabilir)
            False: Butonun dolu olduğunu anlatan çıktı. (Tıklanamaz)
        """
        sozluk3 = {
            id(self.but1) : "00",
            id(self.but2) : "01",
            id(self.but3) : "02",
            id(self.but4) : "10",
            id(self.but5) : "11",
            id(self.but6) : "12",
            id(self.but7) : "20",
            id(self.but8) : "21",
            id(self.but9) : "22"
            }

        butonBir = self.oyun_tahtasi[int(sozluk3[ButId][0])][int(sozluk3[ButId][1])]
        butonIki = self.oyun_tahtasi[int(sozluk3[ButId][0])][int(sozluk3[ButId][1])]

        if butonBir=="_O_" or butonIki=="_X_": return False
        else: return True

    def sifirla(self):
        """
        Gerektiğinde oyunun kendini sıfırlaması için gereken metod. Buton resimlerinin
        bosResim olarak değiştirir ve arkaplandaki self.oyun_tahtasi matris listesini
        boşaltır.

        Kullanılan her değişkenin global olması değişmeyi garanti kılar.
        """
        self.but1.img=self.bosRes
        self.but2.img=self.bosRes
        self.but3.img=self.bosRes
        self.but4.img=self.bosRes
        self.but5.img=self.bosRes
        self.but6.img=self.bosRes
        self.but7.img=self.bosRes
        self.but8.img=self.bosRes
        self.but9.img=self.bosRes

        self.but1.configure(image=self.bosRes)
        self.but2.configure(image=self.bosRes)
        self.but3.configure(image=self.bosRes)
        self.but4.configure(image=self.bosRes)
        self.but5.configure(image=self.bosRes)
        self.but6.configure(image=self.bosRes)
        self.but7.configure(image=self.bosRes)
        self.but8.configure(image=self.bosRes)
        self.but9.configure(image=self.bosRes)


        self.oyun_tahtasi = [["___","___","___"],
                             ["___","___","___"],
                             ["___","___","___"]]

        self.sira = 0




if __name__ == "__main__":
    XoX_Gui().basla()
