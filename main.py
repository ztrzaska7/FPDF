from fpdf import FPDF

class RaportPDF(FPDF):
    def header(self):
        self.set_font("Arial",'B',12)
        self.cell(0,10,'Raport PDF',0,1,'C')
        self.ln(10)
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial','I',8)
        self.cell(0,10,"Strona %s" %self.page_no(),0,0,'C')

    def dodaj_tekst(self,tekst):
        self.set_font('Arial','',12)
        self.multi_cell(0,10,tekst)
        self.ln(10)
    def dodaj_obrazek(self,sciezka_obrazka):
        self.image(sciezka_obrazka,x=10,y=None,w=0,h=100)
raport=RaportPDF()
raport.add_page()
raport.dodaj_tekst('An Instance text')
raport.dodaj_obrazek(r'C:\Users\Zbyszek\Desktop\dino.jpg')
raport.output('raport.pdf')