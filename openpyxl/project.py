from ast import Pass
from openpyxl import load_workbook # para manipular 
from openpyxl import Workbook # para criar

# diretorio para salvar nosso excel 
def save_wb(wb, filename):
    wb.save(filename)

#abrir nossa tabela do excel 
def open_wb(wb, filename):
    return load_workbook(filename)


# criação de planilhas 
def create_sheet(wb, create_sheet_list):
    for x in create_sheet_list:
        wb.create_sheet(x)


# apar planilhas 
def delete_sheet_by_name(wb, sheet_name):
    wb.remove(wb[sheet_name])

# copiar planilhas 
def copy_sheet(wb, source_sheet_name, new_sheet_name= ""):
    new_sheet_name = "Copiando" + source_sheet_name if new_sheet_name == '' else new_sheet_name

    source = wb[source_sheet_name]
    new_sheet = wb.copy_worksheet(source)
    new_sheet.title =  new_sheet_name

# requisição get name 
def get_sheet_name_index(wb):
    # retornamos um dict
    sheet_name_index_dict = {} # passamos o dicionario 
    for index, sheet in enumerate(wb): # fazendo a iteração 
        sheet_name_index_dict[index] =  sheet.title  # atribuindo e fazendo o index 
    return sheet_name_index_dict # retornando o proprio dict



# requisição pelo o get sheet 

def get_sheet_by(wb, index):
    try:
        return wb.worksheets[index]
    except IndexError:
        print("Não tem folhas e nem index", index)
        



if __name__ == "__main__":
    wb = Workbook()
    open_wb("Frist project.xlsx")
    create_sheet(wb, ["Python", "Escala", "Machine-learning", "Universo-dota"])
    delete_sheet_by_name(wb, "Universo-dota",)
    delete_sheet_by_name(wb, "Escala")
    copy_sheet(wb, "Python")
    copy_sheet(wb, "Python", "Python copiado")
    copy_sheet(wb, "Python copiado", "Java")
    print(get_sheet_by(wb, 1).title)
    print("-"*100)
    print(get_sheet_name_index(wb))
    save_wb(wb, "Frist project.xlsx")

