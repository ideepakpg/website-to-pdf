import pdfkit
import os

current_path = os.path.dirname(os.path.abspath(__file__))
print(current_path)
file_path = os.path.join( current_path, "isl.pdf" )
print(file_path)
pdfkit.from_url('http://www.indiansuperleague.com', file_path)
print("pdf file has been saved")
