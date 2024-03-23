from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl.utils.cell import get_column_interval, column_index_from_string

# salvando á base de dados do excel  e colocando o diretorio 
def save_wb(wb, filename):
    wb.save(filename)
    
    
def create_sheet(wb, sheet_name_list):
    # adicionando a planilha no excel
    """
        fazendo uma iteração com o sheet_name_list ,
        para criar uma nova planilha 
    """
    for sheet_name in sheet_name_list:
        wb.create_sheet(sheet_name)
        
        
if __name__ == '__main__':
    # criando um woorkbook 
    wb = Workbook()
    filename = 'estudo001.xlsx'
    create_sheet(wb, ["Python", "Javascript", "Mysql"])