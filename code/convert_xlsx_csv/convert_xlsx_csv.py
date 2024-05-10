from classes.RawFile import RawFile

def main():
  raw = RawFile("./data/raw/AFD_MUNICIPIOS_2021.xlsx")
  
  raw.prune_lines()
  
  raw.replace_columns()
  
  raw.save_as_csv("./data/interim/teste.csv")

if __name__ == "__main__":
  main()