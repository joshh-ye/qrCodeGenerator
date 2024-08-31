import pandas as pd
import openpyxl;
from fpdf import FPDF
import qrcode

df = pd.read_excel('list_names.xlsx')


pdf_w=210
pdf_h=297

class PDF(FPDF):

    def addImage(self,img,x,y,w,h):
        img.save('temp.png')
        self.image('temp.png', x,y,w,h)


for code in df['Names']:


    #qr code generation
    data = code
    img = qrcode.make(data)


    pdf = PDF()
    pdf.add_page()
    pdf.addImage(img, 10,10,pdf_w/2,pdf_h/3)


    pdf.output(f'{code}.pdf','F')