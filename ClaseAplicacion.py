from tkinter import *
from tkinter import ttk,font,messagebox

class Aplicacion:
    __ventana=None
    __cantidad=None
    __precio_Abase=None
    __precio_Aactual=None

    def __init__(self):
        self.__ventana= Tk()
        self.__ventana.resizable(0,0)
        
        self.marco=ttk.Frame(self.__ventana,padding=(10,10))
        self.__IPC=StringVar()
        ttk.Label(self.__ventana,textvariable=self.__IPC).grid(column=1,row=5,sticky=(W))
        ttk.Label(self.__ventana,text="IPC %").grid(column=0,row=5,sticky=(W))
        self.__ventana.title("Indice de Precios al Consumidor (IPC)")
        self.__itemLbl=ttk.Label(self.__ventana,text="Item",padding=(5,5))
        self.__vestimentaLbl=ttk.Label(self.__ventana,text="Vestimenta",padding=(5,5))
        self.__alimentosLbl=ttk.Label(self.__ventana,text="Alimentos",padding=(5,5))
        self.__educacionLbl=ttk.Label(self.__ventana,text="Educacion",padding=(5,5))
        self.__cantidadLbl=ttk.Label(self.__ventana,text="Cantidad",padding=(5,5))
        self.__precio_AbaseLbl=ttk.Label(self.__ventana,text="Precio Año Base",padding=(5,5))
        self.__precio_AactualLbl=ttk.Label(self.__ventana,text="Precio Año Actual",padding=(5,5))
        self.ctext1=ttk.Entry(self.__ventana,textvariable=self.__cantidad,width=10)
        self.ctext2=ttk.Entry(self.__ventana,textvariable=self.__cantidad,width=10)
        self.ctext3=ttk.Entry(self.__ventana,textvariable=self.__cantidad,width=10)
        self.ctext4=ttk.Entry(self.__ventana,textvariable=self.__precio_Abase,width=10)
        self.ctext5=ttk.Entry(self.__ventana,textvariable=self.__precio_Abase,width=10)
        self.ctext6=ttk.Entry(self.__ventana,textvariable=self.__precio_Abase,width=10)
        self.ctext7=ttk.Entry(self.__ventana,textvariable=self.__precio_Aactual,width=10)
        self.ctext8=ttk.Entry(self.__ventana,textvariable=self.__precio_Aactual,width=10)
        self.ctext9=ttk.Entry(self.__ventana,textvariable=self.__precio_Aactual,width=10)
        self.boton1=ttk.Button(self.__ventana,text="Calcular IPC",command=self.calcular)
        self.boton2=ttk.Button(self.__ventana,text="Salir",command=quit)
        
        self.__itemLbl.grid(column=0,row=0)
        self.__cantidadLbl.grid(column=1,row=0)
        self.__precio_AbaseLbl.grid(column=2,row=0)
        self.__precio_AactualLbl.grid(column=3,row=0)
        self.__vestimentaLbl.grid(column=0,row=1)
        self.ctext1.grid(column=1,row=1)
        self.ctext2.grid(column=2 ,row=1)
        self.ctext3.grid(column=3 ,row=1)
        self.__alimentosLbl.grid(column=0 ,row=2)
        self.ctext4.grid(column=1 ,row=2)
        self.ctext5.grid(column=2 ,row=2)
        self.ctext6.grid(column=3 ,row=2)
        self.__educacionLbl.grid(column=0,row=3)
        self.ctext7.grid(column=1,row=3)
        self.ctext8.grid(column=2,row=3)
        self.ctext9.grid(column=3,row=3)
        self.boton1.grid(column=2,row=4)
        self.boton2.grid(column=3,row=4)

        self.__ventana.mainloop()

    def calcular (self):
        costo_Base=(int(self.ctext1.get())*int(self.ctext4.get()))+(int(self.ctext2.get())*int(self.ctext5.get()))+(int(self.ctext3.get())*int(self.ctext6.get()))
        costo_Actual=(int(self.ctext1.get())*int(self.ctext7.get()))+(int(self.ctext2.get())*int(self.ctext8.get()))+(int(self.ctext3.get())*int(self.ctext9.get()))
        ipc=int(costo_Actual)/int(costo_Base)
        total=float(ipc)*int(100)
        #print("total",total)
        self.__IPC.set(total)