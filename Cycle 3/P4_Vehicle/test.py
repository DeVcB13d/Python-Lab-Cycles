from fpdf import FPDF

#Portrait,mm,Letter format
pdf = FPDF('P','mm','Letter')

#aDD a page

#To add a page to the doc
pdf.add_page()
#To set the font of the doc
pdf.set_font('times','',16)

#Add Text
#width,height,text
pdf.cell(10,10,'Hell World!')
pdf.output("pdf1.pdf")