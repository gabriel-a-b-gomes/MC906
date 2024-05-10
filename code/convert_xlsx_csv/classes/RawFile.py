import os
import pandas as pd

from .ColumnName import ColumnName

class RawFile:
  def __init__(self, path) -> None:
    self.path = path
    self.file = None
    
    self.columns_master = ColumnName()
    
    self.ext = self.__get_ext()
    
    self.read()
    
  def __get_ext(self):
    _, ext = os.path.splitext(self.path)
    
    return ext[1:]
  
  def read(self):
    if self.ext == "csv":
      return self.__read_csv()
    if self.ext in ["xls", "xlsx", "xslx", "xlsm", "xlsb", "odf", "ods", "odt"]:
      return self.__read_excel()
    
    raise FileNotFoundError("Extensão do arquivo não é válida")
  
  def __read_excel(self):
    self.file = pd.read_excel(self.path)
    
  def __read_csv(self):
    self.file = pd.read_csv(self.path)
    
  def prune_lines(self):
    first_index = self.file[self.file.iloc[:, 0].fillna('').astype(str).str.contains('ANO_CENSO')].index[0]
    
        # Find the index of the last row
    last_index = len(self.file) - 1

    # Initialize index for iteration
    index = last_index

    # Search for NaN values from the bottom
    while index >= 0:
      if pd.isna(self.file.iloc[index, 0]):
          break
      index -= 1

    index = index if index > 0 else last_index

    columns = self.file.iloc[first_index]
    
    self.file = self.file.iloc[first_index+1:index]
    self.file.columns = columns
    
  def replace_columns(self):
    newColumns = []
    for column in self.file.columns:
      newColumns.append(self.columns_master.get_column_name(column))
      
    self.file.columns = newColumns
  
  def save_as_csv(self, output_path):
    self.file.to_csv(output_path, index=False, sep=";")