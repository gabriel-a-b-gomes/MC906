from constants.dict_afd import dict_afd

class ColumnName:
  def __init__(self) -> None:
    self.main_dict = self.__get_final_dict(dict_afd)
    
  def __get_final_dict(*dicts):
    concatenated_dict = {}
    for d in dicts:
        concatenated_dict = {**concatenated_dict, **d}
    return concatenated_dict
  
  def get_column_name(self, raw_column):
    if raw_column in self.main_dict:
      return self.main_dict[raw_column]
    
    return raw_column