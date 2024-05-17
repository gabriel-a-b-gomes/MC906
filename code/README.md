# convert_xlsx_csv.py USAGE

```.sh
 python convert_xlsx_csv.py <arquivo_entrada> <arquivo_saida> <flag_drop_correlacao>
```

## Exemplos

- Com correlação

```.sh
 python .\convert_xlsx_csv.py ..\data\raw\2020\AFD_MUNICIPIOS_2020.xlsx ..\data\interim\2020\AFD_CLEAN_2020.csv
```

- Sem correlação

```.sh
 python .\convert_xlsx_csv.py ..\data\raw\2020\AFD_MUNICIPIOS_2020.xlsx ..\data\interim\2020\AFD_CLEAN_2020.csv drop
```

Ah flag de drop pode ser qualquer coisa, um "drop" um "d" ou até mesmo 1. O código apenas verifica a condição de existência dela.