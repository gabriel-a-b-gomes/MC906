import os
import sys
import pandas as pd
import re

dict_afd = {
  "ED_INF_CAT_1": "ED_INF_ADEQ_DOC_GRUPO1",
  "ED_INF_CAT_2": "ED_INF_ADEQ_DOC_GRUPO2",
  "ED_INF_CAT_3": "ED_INF_ADEQ_DOC_GRUPO3",
  "ED_INF_CAT_4": "ED_INF_ADEQ_DOC_GRUPO4",
  "ED_INF_CAT_5": "ED_INF_ADEQ_DOC_GRUPO5",
  "FUN_CAT_1": "FUN_ADEQ_DOC_TOTAL_GRUPO1",
  "FUN_CAT_2": "FUN_ADEQ_DOC_TOTAL_GRUPO2",
  "FUN_CAT_3": "FUN_ADEQ_DOC_TOTAL_GRUPO3",
  "FUN_CAT_4": "FUN_ADEQ_DOC_TOTAL_GRUPO4",
  "FUN_CAT_5": "FUN_ADEQ_DOC_TOTAL_GRUPO5",
  "FUN_AI_CAT_1": "FUN_ADEQ_DOC_ANOSINICIAIS_GRUPO1",
  "FUN_AI_CAT_2": "FUN_ADEQ_DOC_ANOSINICIAIS_GRUPO2",
  "FUN_AI_CAT_3": "FUN_ADEQ_DOC_ANOSINICIAIS_GRUPO3",
  "FUN_AI_CAT_4": "FUN_ADEQ_DOC_ANOSINICIAIS_GRUPO4",
  "FUN_AI_CAT_5": "FUN_ADEQ_DOC_ANOSINICIAIS_GRUPO5",
  "FUN_AF_CAT_1": "FUN_ADEQ_DOC_ANOSFINAIS_GRUPO1",
  "FUN_AF_CAT_2": "FUN_ADEQ_DOC_ANOSFINAIS_GRUPO2",
  "FUN_AF_CAT_3": "FUN_ADEQ_DOC_ANOSFINAIS_GRUPO3",
  "FUN_AF_CAT_4": "FUN_ADEQ_DOC_ANOSFINAIS_GRUPO4",
  "FUN_AF_CAT_5": "FUN_ADEQ_DOC_ANOSFINAIS_GRUPO5",
  "MED_CAT_1": "MED_ADEQ_DOC_GRUPO1",
  "MED_CAT_2": "MED_ADEQ_DOC_GRUPO2",
  "MED_CAT_3": "MED_ADEQ_DOC_GRUPO3",
  "MED_CAT_4": "MED_ADEQ_DOC_GRUPO4",
  "MED_CAT_5": "MED_ADEQ_DOC_GRUPO5",
}

dict_atu = {
  "ED_INF_CAT_0": "ED_INF_MEDIA_TOTAL_ALUNOS_SALA",
  "CRE_CAT_0": "ED_INF_MEDIA_CRECHE_ALUNOS_SALA",
  "PRE_CAT_0": "ED_INF_MEDIA_PRE_ESC_ALUNOS_SALA",
  "FUN_CAT_0": "FUN_MEDIA_TOTAL_ALUNOS_SALA",
  "FUN_AI_CAT_0": "FUN_MEDIA_ANOS_INICIAIS_ALUNOS_SALA",
  "FUN_AF_CAT_0": "FUN_MEDIA_ANOS_FINAIS_ALUNOS_SALA",
  "FUN_01_CAT_0": "FUN_MEDIA_PRIMEIRO_ALUNOS_SALA",
  "FUN_02_CAT_0": "FUN_MEDIA_SEGUNDO_ALUNOS_SALA",
  "FUN_03_CAT_0": "FUN_MEDIA_TERCEIRO_ALUNOS_SALA",
  "FUN_04_CAT_0": "FUN_MEDIA_QUARTO_ALUNOS_SALA",
  "FUN_05_CAT_0": "FUN_MEDIA_QUINTO_ALUNOS_SALA",
  "FUN_06_CAT_0": "FUN_MEDIA_SEXTO_ALUNOS_SALA",
  "FUN_07_CAT_0": "FUN_MEDIA_SETIMO_ALUNOS_SALA",
  "FUN_08_CAT_0": "FUN_MEDIA_OITAVO_ALUNOS_SALA",
  "FUN_09_CAT_0": "FUN_MEDIA_NONO_ALUNOS_SALA",
  "MULT_ETA_CAT_0": "MULT_ETAPA_MEDIA_ALUNOS_SALA",
  "MED_CAT_0": "MED_MEDIA_TOTAL_ALUNOS_SALA",
  "MED_01_CAT_0": "MED_MEDIA_PRIMEIRO_ALUNOS_SALA",
  "MED_02_CAT_0": "MED_MEDIA_SEGUNDO_ALUNOS_SALA",
  "MED_03_CAT_0": "MED_MEDIA_TERCEIRO_ALUNOS_SALA",
  "MED_NS_CAT_0": "MED_MEDIA_NAO_SERIADO_ALUNOS_SALA",
}

dict_icg = {
  "EDU_BAS_CAT_1": "PERC_COMPLX_ESCOLA_NIVEL_1",
  "EDU_BAS_CAT_2": "PERC_COMPLX_ESCOLA_NIVEL_2",
  "EDU_BAS_CAT_3": "PERC_COMPLX_ESCOLA_NIVEL_3",
  "EDU_BAS_CAT_4": "PERC_COMPLX_ESCOLA_NIVEL_4",
  "EDU_BAS_CAT_5": "PERC_COMPLX_ESCOLA_NIVEL_5",
  "EDU_BAS_CAT_6": "PERC_COMPLX_ESCOLA_NIVEL_6",
}

dict_ied = {
  "FUN_CAT_1": "FUN_PERC_DOC_POR_ESFORCO_TOTAL_NIVEL_1",
  "FUN_CAT_2": "FUN_PERC_DOC_POR_ESFORCO_TOTAL_NIVEL_2",
  "FUN_CAT_3": "FUN_PERC_DOC_POR_ESFORCO_TOTAL_NIVEL_3",
  "FUN_CAT_4": "FUN_PERC_DOC_POR_ESFORCO_TOTAL_NIVEL_4",
  "FUN_CAT_5": "FUN_PERC_DOC_POR_ESFORCO_TOTAL_NIVEL_5",
  "FUN_CAT_6": "FUN_PERC_DOC_POR_ESFORCO_TOTAL_NIVEL_6",
  "FUN_AI_CAT_1": "FUN_PERC_DOC_POR_ESFORCO_ANOS_INICIAIS_NIVEL_1",
  "FUN_AI_CAT_2": "FUN_PERC_DOC_POR_ESFORCO_ANOS_INICIAIS_NIVEL_2",
  "FUN_AI_CAT_3": "FUN_PERC_DOC_POR_ESFORCO_ANOS_INICIAIS_NIVEL_3",
  "FUN_AI_CAT_4": "FUN_PERC_DOC_POR_ESFORCO_ANOS_INICIAIS_NIVEL_4",
  "FUN_AI_CAT_5": "FUN_PERC_DOC_POR_ESFORCO_ANOS_INICIAIS_NIVEL_5",
  "FUN_AI_CAT_6": "FUN_PERC_DOC_POR_ESFORCO_ANOS_INICIAIS_NIVEL_6",
  "FUN_AF_CAT_1": "FUN_PERC_DOC_POR_ESFORCO_ANOS_FINAIS_NIVEL_1",
  "FUN_AF_CAT_2": "FUN_PERC_DOC_POR_ESFORCO_ANOS_FINAIS_NIVEL_2",
  "FUN_AF_CAT_3": "FUN_PERC_DOC_POR_ESFORCO_ANOS_FINAIS_NIVEL_3",
  "FUN_AF_CAT_4": "FUN_PERC_DOC_POR_ESFORCO_ANOS_FINAIS_NIVEL_4",
  "FUN_AF_CAT_5": "FUN_PERC_DOC_POR_ESFORCO_ANOS_FINAIS_NIVEL_5",
  "FUN_AF_CAT_6": "FUN_PERC_DOC_POR_ESFORCO_ANOS_FINAIS_NIVEL_6",
  "MED_CAT_1": "MED_PERC_DOC_POR_ESFORCO_TOTAL_NIVEL_1",
  "MED_CAT_2": "MED_PERC_DOC_POR_ESFORCO_TOTAL_NIVEL_2",
  "MED_CAT_3": "MED_PERC_DOC_POR_ESFORCO_TOTAL_NIVEL_3",
  "MED_CAT_4": "MED_PERC_DOC_POR_ESFORCO_TOTAL_NIVEL_4",
  "MED_CAT_5": "MED_PERC_DOC_POR_ESFORCO_TOTAL_NIVEL_5",
  "MED_CAT_6": "MED_PERC_DOC_POR_ESFORCO_TOTAL_NIVEL_6",
}

dict_ird = {
  "EDU_BAS_CAT_1": "PERC_REG_DOC_BAIXA",
  "EDU_BAS_CAT_2": "PERC_REG_DOC_MEDIA_BAIXA",
  "EDU_BAS_CAT_3": "PERC_REG_DOC_MEDIA_ALTA",
  "EDU_BAS_CAT_4": "PERC_REG_DOC_ALTA",
}

dict_tdi = {
  "FUN_CAT_0": "FUN_TX_DIST_IDADE_SERIE_TOTAL",
  "FUN_AI_CAT_0": "FUN_TX_DIST_IDADE_SERIE_ANOS_INICIAIS",
  "FUN_AF_CAT_0": "FUN_TX_DIST_IDADE_SERIE_ANOS_FINAIS",
  "FUN_01_CAT_0": "FUN_TX_DIST_IDADE_SERIE_PRIMEIRO",
  "FUN_02_CAT_0": "FUN_TX_DIST_IDADE_SERIE_SEGUNDO",
  "FUN_03_CAT_0": "FUN_TX_DIST_IDADE_SERIE_TERCEIRO",
  "FUN_04_CAT_0": "FUN_TX_DIST_IDADE_SERIE_QUARTO",
  "FUN_05_CAT_0": "FUN_TX_DIST_IDADE_SERIE_QUINTO",
  "FUN_06_CAT_0": "FUN_TX_DIST_IDADE_SERIE_SEXTO",
  "FUN_07_CAT_0": "FUN_TX_DIST_IDADE_SERIE_SETIMO",
  "FUN_08_CAT_0": "FUN_TX_DIST_IDADE_SERIE_OITAVO",
  "FUN_09_CAT_0": "FUN_TX_DIST_IDADE_SERIE_NONO",
  "MED_CAT_0": "MED_TX_DIST_IDADE_SERIE_TOTAL",
  "MED_01_CAT_0": "MED_TX_DIST_IDADE_SERIE_PRIMEIRO",
  "MED_02_CAT_0": "MED_TX_DIST_IDADE_SERIE_SEGUNDO",
  "MED_03_CAT_0": "MED_TX_DIST_IDADE_SERIE_TERCEIRO",
}

dict_tnr = {
  "4_CAT_FUN": "FUN_TX_N_RESP_TOTAL",
  "4_CAT_FUN_AI": "FUN_TX_N_RESP_ANOS_INICIAIS",
  "4_CAT_FUN_AF": "FUN_TX_N_RESP_ANOS_FINAIS",
  "4_CAT_FUN_01": "FUN_TX_N_RESP_PRIMEIRO",
  "4_CAT_FUN_02": "FUN_TX_N_RESP_SEGUNDO",
  "4_CAT_FUN_03": "FUN_TX_N_RESP_TERCEIRO",
  "4_CAT_FUN_04": "FUN_TX_N_RESP_QUARTO",
  "4_CAT_FUN_05": "FUN_TX_N_RESP_QUINTO",
  "4_CAT_FUN_06": "FUN_TX_N_RESP_SEXTO",
  "4_CAT_FUN_07": "FUN_TX_N_RESP_SETIMO",
  "4_CAT_FUN_08": "FUN_TX_N_RESP_OITAVO",
  "4_CAT_FUN_09": "FUN_TX_N_RESP_NONO",
  "4_CAT_MED": "MED_TX_N_RESP_TOTAL",
  "4_CAT_MED_01": "MED_TX_N_RESP_PRIMEIRO",
  "4_CAT_MED_02": "MED_TX_N_RESP_SEGUNDO",
  "4_CAT_MED_03": "MED_TX_N_RESP_TERCEIRO",
  "4_CAT_MED_NS": "MED_TX_N_RESP_NAO_SERIADO",
}

dict_tx_aprov = {
  "1_CAT_FUN": "FUN_TX_APROVACAO_TOTAL",
  "1_CAT_FUN_AI": "FUN_TX_APROVACAO_ANOS_INICIAIS",
  "1_CAT_FUN_AF": "FUN_TX_APROVACAO_ANOS_FINAIS",
  "1_CAT_FUN_01": "FUN_TX_APROVACAO_PRIMEIRO",
  "1_CAT_FUN_02": "FUN_TX_APROVACAO_SEGUNDO",
  "1_CAT_FUN_03": "FUN_TX_APROVACAO_TERCEIRO",
  "1_CAT_FUN_04": "FUN_TX_APROVACAO_QUARTO",
  "1_CAT_FUN_05": "FUN_TX_APROVACAO_QUINTO",
  "1_CAT_FUN_06": "FUN_TX_APROVACAO_SEXTO",
  "1_CAT_FUN_07": "FUN_TX_APROVACAO_SETIMO",
  "1_CAT_FUN_08": "FUN_TX_APROVACAO_OITAVO",
  "1_CAT_FUN_09": "FUN_TX_APROVACAO_NONO",
  "1_CAT_MED": "MED_TX_APROVACAO_TOTAL",
  "1_CAT_MED_01": "MED_TX_APROVACAO_PRIMEIRO",
  "1_CAT_MED_02": "MED_TX_APROVACAO_SEGUNDO",
  "1_CAT_MED_03": "MED_TX_APROVACAO_TERCEIRO",
  "1_CAT_MED_NS": "MED_TX_APROVACAO_NAO_SERIADO",
}

dict_tx_reprov = {
  "2_CAT_FUN": "FUN_TX_REPROVACAO_TOTAL",
  "2_CAT_FUN_AI": "FUN_TX_REPROVACAO_ANOS_INICIAIS",
  "2_CAT_FUN_AF": "FUN_TX_REPROVACAO_ANOS_FINAIS",
  "2_CAT_FUN_01": "FUN_TX_REPROVACAO_PRIMEIRO",
  "2_CAT_FUN_02": "FUN_TX_REPROVACAO_SEGUNDO",
  "2_CAT_FUN_03": "FUN_TX_REPROVACAO_TERCEIRO",
  "2_CAT_FUN_04": "FUN_TX_REPROVACAO_QUARTO",
  "2_CAT_FUN_05": "FUN_TX_REPROVACAO_QUINTO",
  "2_CAT_FUN_06": "FUN_TX_REPROVACAO_SEXTO",
  "2_CAT_FUN_07": "FUN_TX_REPROVACAO_SETIMO",
  "2_CAT_FUN_08": "FUN_TX_REPROVACAO_OITAVO",
  "2_CAT_FUN_09": "FUN_TX_REPROVACAO_NONO",
  "2_CAT_MED": "MED_TX_REPROVACAO_TOTAL",
  "2_CAT_MED_01": "MED_TX_REPROVACAO_PRIMEIRO",
  "2_CAT_MED_02": "MED_TX_REPROVACAO_SEGUNDO",
  "2_CAT_MED_03": "MED_TX_REPROVACAO_TERCEIRO",
  "2_CAT_MED_NS": "MED_TX_REPROVACAO_NAO_SERIADO",
}

dict_tx_abandono = {
  "3_CAT_FUN": "FUN_TX_ABANDONO_TOTAL",
  "3_CAT_FUN_AI": "FUN_TX_ABANDONO_ANOS_INICIAIS",
  "3_CAT_FUN_AF": "FUN_TX_ABANDONO_ANOS_FINAIS",
  "3_CAT_FUN_01": "FUN_TX_ABANDONO_PRIMEIRO",
  "3_CAT_FUN_02": "FUN_TX_ABANDONO_SEGUNDO",
  "3_CAT_FUN_03": "FUN_TX_ABANDONO_TERCEIRO",
  "3_CAT_FUN_04": "FUN_TX_ABANDONO_QUARTO",
  "3_CAT_FUN_05": "FUN_TX_ABANDONO_QUINTO",
  "3_CAT_FUN_06": "FUN_TX_ABANDONO_SEXTO",
  "3_CAT_FUN_07": "FUN_TX_ABANDONO_SETIMO",
  "3_CAT_FUN_08": "FUN_TX_ABANDONO_OITAVO",
  "3_CAT_FUN_09": "FUN_TX_ABANDONO_NONO",
  "3_CAT_MED": "MED_TX_ABANDONO_TOTAL",
  "3_CAT_MED_01": "MED_TX_ABANDONO_PRIMEIRO",
  "3_CAT_MED_02": "MED_TX_ABANDONO_SEGUNDO",
  "3_CAT_MED_03": "MED_TX_ABANDONO_TERCEIRO",
  "3_CAT_MED_NS": "MED_TX_ABANDONO_NAO_SERIADO",
}

dict_tx_promo = {
  "1_CAT1_CATFUN": "FUN_TX_PROMOCAO_TOTAL",
  "1_CAT1_CATFUN_AI": "FUN_TX_PROMOCAO_ANOS_INICIAIS",
  "1_CAT1_CATFUN_AF": "FUN_TX_PROMOCAO_ANOS_FINAIS",
  "1_CAT1_CATFUN_01": "FUN_TX_PROMOCAO_PRIMEIRO",
  "1_CAT1_CATFUN_02": "FUN_TX_PROMOCAO_SEGUNDO",
  "1_CAT1_CATFUN_03": "FUN_TX_PROMOCAO_TERCEIRO",
  "1_CAT1_CATFUN_04": "FUN_TX_PROMOCAO_QUARTO",
  "1_CAT1_CATFUN_05": "FUN_TX_PROMOCAO_QUINTO",
  "1_CAT1_CATFUN_06": "FUN_TX_PROMOCAO_SEXTO",
  "1_CAT1_CATFUN_07": "FUN_TX_PROMOCAO_SETIMO",
  "1_CAT1_CATFUN_08": "FUN_TX_PROMOCAO_OITAVO",
  "1_CAT1_CATFUN_09": "FUN_TX_PROMOCAO_NONO",
  "1_CAT1_CATMED": "MED_TX_PROMOCAO_TOTAL",
  "1_CAT1_CATMED_01": "MED_TX_PROMOCAO_PRIMEIRO",
  "1_CAT1_CATMED_02": "MED_TX_PROMOCAO_SEGUNDO",
  "1_CAT1_CATMED_03": "MED_TX_PROMOCAO_TERCEIRO",
}

dict_tx_repet = {
  "1_CAT2_CATFUN": "FUN_TX_REPETENCIA_TOTAL",
  "1_CAT2_CATFUN_AI": "FUN_TX_REPETENCIA_ANOS_INICIAIS",
  "1_CAT2_CATFUN_AF": "FUN_TX_REPETENCIA_ANOS_FINAIS",
  "1_CAT2_CATFUN_01": "FUN_TX_REPETENCIA_PRIMEIRO",
  "1_CAT2_CATFUN_02": "FUN_TX_REPETENCIA_SEGUNDO",
  "1_CAT2_CATFUN_03": "FUN_TX_REPETENCIA_TERCEIRO",
  "1_CAT2_CATFUN_04": "FUN_TX_REPETENCIA_QUARTO",
  "1_CAT2_CATFUN_05": "FUN_TX_REPETENCIA_QUINTO",
  "1_CAT2_CATFUN_06": "FUN_TX_REPETENCIA_SEXTO",
  "1_CAT2_CATFUN_07": "FUN_TX_REPETENCIA_SETIMO",
  "1_CAT2_CATFUN_08": "FUN_TX_REPETENCIA_OITAVO",
  "1_CAT2_CATFUN_09": "FUN_TX_REPETENCIA_NONO",
  "1_CAT2_CATMED": "MED_TX_REPETENCIA_TOTAL",
  "1_CAT2_CATMED_01": "MED_TX_REPETENCIA_PRIMEIRO",
  "1_CAT2_CATMED_02": "MED_TX_REPETENCIA_SEGUNDO",
  "1_CAT2_CATMED_03": "MED_TX_REPETENCIA_TERCEIRO",
}

dict_tx_evasao = {
  "1_CAT3_CATFUN": "FUN_TX_EVASAO_TOTAL",
  "1_CAT3_CATFUN_AI": "FUN_TX_EVASAO_ANOS_INICIAIS",
  "1_CAT3_CATFUN_AF": "FUN_TX_EVASAO_ANOS_FINAIS",
  "1_CAT3_CATFUN_01": "FUN_TX_EVASAO_PRIMEIRO",
  "1_CAT3_CATFUN_02": "FUN_TX_EVASAO_SEGUNDO",
  "1_CAT3_CATFUN_03": "FUN_TX_EVASAO_TERCEIRO",
  "1_CAT3_CATFUN_04": "FUN_TX_EVASAO_QUARTO",
  "1_CAT3_CATFUN_05": "FUN_TX_EVASAO_QUINTO",
  "1_CAT3_CATFUN_06": "FUN_TX_EVASAO_SEXTO",
  "1_CAT3_CATFUN_07": "FUN_TX_EVASAO_SETIMO",
  "1_CAT3_CATFUN_08": "FUN_TX_EVASAO_OITAVO",
  "1_CAT3_CATFUN_09": "FUN_TX_EVASAO_NONO",
  "1_CAT3_CATMED": "MED_TX_EVASAO_TOTAL",
  "1_CAT3_CATMED_01": "MED_TX_EVASAO_PRIMEIRO",
  "1_CAT3_CATMED_02": "MED_TX_EVASAO_SEGUNDO",
  "1_CAT3_CATMED_03": "MED_TX_EVASAO_TERCEIRO",
}

dict_dsu = {
  "ED_INF_CAT_0": "ED_INF_PERC_DOC_SUPERIOR_TOTAL",
  "CRE_CAT_0": "ED_INF_PERC_DOC_SUPERIOR_CRECHE",
  "PRE_CAT_0": "ED_INF_PERC_DOC_SUPERIOR_PRE_ESC",
  "FUN_CAT_0": "FUN_PERC_DOC_SUPERIOR_TOTAL",
  "FUN_AI_CAT_0": "FUN_PERC_DOC_SUPERIOR_ANOS_INICIAIS",
  "FUN_AF_CAT_0": "FUN_PERC_DOC_SUPERIOR_ANOS_FINAIS",
  "MED_CAT_0": "MED_PERC_DOC_SUPERIOR_TOTAL",
}

dict_had = {
  "ED_INF_CAT_0": "ED_INF_MEDIA_TOTAL_HORAS_AULA",
  "CRE_CAT_0": "ED_INF_MEDIA_CRECHE_HORAS_AULA",
  "PRE_CAT_0": "ED_INF_MEDIA_PRE_ESC_HORAS_AULA",
  "FUN_CAT_0": "FUN_MEDIA_TOTAL_HORAS_AULA",
  "FUN_AI_CAT_0": "FUN_MEDIA_ANOS_INICIAIS_HORAS_AULA",
  "FUN_AF_CAT_0": "FUN_MEDIA_ANOS_FINAIS_HORAS_AULA",
  "FUN_01_CAT_0": "FUN_MEDIA_PRIMEIRO_HORAS_AULA",
  "FUN_02_CAT_0": "FUN_MEDIA_SEGUNDO_HORAS_AULA",
  "FUN_03_CAT_0": "FUN_MEDIA_TERCEIRO_HORAS_AULA",
  "FUN_04_CAT_0": "FUN_MEDIA_QUARTO_HORAS_AULA",
  "FUN_05_CAT_0": "FUN_MEDIA_QUINTO_HORAS_AULA",
  "FUN_06_CAT_0": "FUN_MEDIA_SEXTO_HORAS_AULA",
  "FUN_07_CAT_0": "FUN_MEDIA_SETIMO_HORAS_AULA",
  "FUN_08_CAT_0": "FUN_MEDIA_OITAVO_HORAS_AULA",
  "FUN_09_CAT_0": "FUN_MEDIA_NONO_HORAS_AULA",
  "MULT_ETA_CAT_0": "MULT_ETAPA_MEDIA_HORAS_AULA",
  "MED_CAT_0": "MED_MEDIA_TOTAL_HORAS_AULA",
  "MED_01_CAT_0": "MED_MEDIA_PRIMEIRO_HORAS_AULA",
  "MED_02_CAT_0": "MED_MEDIA_SEGUNDO_HORAS_AULA",
  "MED_03_CAT_0": "MED_MEDIA_TERCEIRO_HORAS_AULA",
  "MED_04_CAT_0": "MED_MEDIA_QUARTO_HORAS_AULA",
  "MED_NS_CAT_01": "MED_MEDIA_NAO_SERIADO_HORAS_AULA",
}

class ColumnName:
  def __init__(self, input_path: str) -> None:
    self.path = input_path.lower()
    self.main_dict = {}
    if "afd" in self.path:
      self.main_dict = self.__get_final_dict(dict_afd)
    elif "atu" in self.path:
      self.main_dict = self.__get_final_dict(dict_atu)
    elif "icg" in self.path:
      self.main_dict = self.__get_final_dict(dict_icg)
    elif "ied" in self.path:
      self.main_dict = self.__get_final_dict(dict_ied)   
    elif "ird" in self.path:
      self.main_dict = self.__get_final_dict(dict_ird) 
    elif "tdi" in self.path:
      self.main_dict = self.__get_final_dict(dict_tdi)
    elif "tnr" in self.path:
      self.main_dict = self.__get_final_dict(dict_tnr)
    elif "rend" in self.path:
      self.main_dict = self.__get_final_dict(dict_tx_aprov, dict_tx_reprov, dict_tx_abandono)
    elif "transicao" in self.path:
      self.main_dict = self.__get_final_dict(dict_tx_promo, dict_tx_repet, dict_tx_evasao)
    elif "had" in self.path:
      self.main_dict = self.__get_final_dict(dict_had)
    elif "dsu" in self.path:
      self.main_dict = self.__get_final_dict(dict_dsu)
    
  def __get_final_dict(self, *dicts):
    concatenated_dict = {}
    for d in dicts:
      if isinstance(d, dict):
        concatenated_dict = {**concatenated_dict, **d}
    return concatenated_dict
  
  def get_column_name(self, raw_column):
    if raw_column in self.main_dict:
      return self.main_dict[raw_column]
    
    return raw_column

class RawFile:
  def __init__(self, path) -> None:
    self.path = path
    self.file = None
    
    self.columns_master = ColumnName(path)
    
    self.ext = self.__get_ext()
    
    self.read()
    
  def __get_ext(self):
    _, ext = os.path.splitext(self.path)
    
    return ext[1:]
  
  def read(self):
    print("Iniciando leitura do arquivo...", end=" ")
    
    if self.ext == "csv":
      return self.__read_csv()
    if self.ext in ["xls", "xlsx", "xslx", "xlsm", "xlsb", "odf", "ods", "odt"]:
      return self.__read_excel()
    
    raise FileNotFoundError("Extensão do arquivo não é válida")
  
  def __read_excel(self):
    self.file = pd.read_excel(self.path)
    print("COMPLETE")
    
  def __read_csv(self):
    self.file = pd.read_csv(self.path)
    print("COMPLETE")
    
  def prune_lines(self):
    print("Iniciando corte de linhas...", end=" ")
    
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
    
    print("COMPLETE")
  
  def __prune_by_file(self):
    input_path = self.path.lower()
    
    if "afd" in input_path:
      return lambda col: col.startswith("EJA_")
    elif "atu" in input_path:
      return lambda col: col == "MED_04_CAT_0" or col == "MED_NS_CAT_0"
    elif "tdi" in input_path:
      return lambda col: col == "MED_04_CAT_0" or col == "MED_NS_CAT_0"
    elif "tnr" in input_path:
      return lambda col: col.endswith("_MED_NS") or col.endswith("_MED_04")
    elif "rend" in input_path:
      return lambda col: col.endswith("_MED_NS") or col.endswith("_MED_04")
    elif "transicao" in input_path:
      return lambda col: col.startswith("1_CAT4_") or col == "MED_NS_CAT_01"
    elif "had" in input_path:
      return lambda col: col == "MED_04_CAT_0" or col == "MED_NS_CAT_01"
    elif "dsu" in input_path:
      return lambda col: col == "PROF_CAT_0" or col == "EJA_CAT_0" or col == "EDU_BAS_CAT_0"

  def prune_columns(self):
    prunning = self.__prune_by_file()
    
    if not prunning: return

    # Get the columns to drop based on the prunning
    columns_to_drop = [col for col in self.file.columns if prunning(col)]

    # Drop the columns
    self.file = self.file.drop(columns=columns_to_drop)
  
  def __define_criterion(self):
    input_path = self.path.lower()
    
    if "afd" in input_path:
      return lambda col: "_AI_" in col or "_AF_" in col
    elif "atu" in input_path:
      return lambda col: col == "CRE_CAT_0" or col == "PRE_CAT_0" or col == "MULT_ETA_CAT_0" or re.match('^MED_\d{2}_CAT_0$', col) or re.match('^FUN_\d{2}_CAT_0$', col)
    elif "tdi" in input_path:
      return lambda col: re.match('^MED_\d{2}_CAT_0$', col) or re.match('^FUN_\d{2}_CAT_0$', col)
    elif "tnr" in input_path:
      return lambda col: col.startswith('4_CAT_FUN_') or col.startswith('4_CAT_MED_')
    elif "rend" in input_path:
      return lambda col: col.startswith('1_CAT_FUN_') or col.startswith('1_CAT_MED_') or col.startswith('2_CAT_FUN_') or col.startswith('2_CAT_MED_') or col.startswith('3_CAT_FUN_') or col.startswith('3_CAT_MED_')
    elif "transicao" in input_path:
      return lambda col: col.startswith('1_CAT1_CATFUN_') or col.startswith('1_CAT1_CATMED_') or col.startswith('1_CAT2_CATFUN_') or col.startswith('1_CAT2_CATMED_') or col.startswith('1_CAT3_CATFUN_') or col.startswith('1_CAT3_CATMED_')
    elif "had" in input_path:
      return lambda col: col == "CRE_CAT_0" or col == "PRE_CAT_0" or re.match('^MED_\d{2}_CAT_0$', col) or re.match('^FUN_\d{2}_CAT_0$', col)
    elif "dsu" in input_path:
      return lambda col: col == "CRE_CAT_0" or col == "PRE_CAT_0" or re.match('^MED_\d{2}_CAT_0$', col) or re.match('^FUN_\d{2}_CAT_0$', col) or col == "MED_NS_CAT_01"

  def drop_correlation(self):
    criterion = self.__define_criterion()
    
    if not criterion: return

    # Get the columns to drop based on the criterion
    columns_to_drop = [col for col in self.file.columns if criterion(col)]

    # Drop the columns
    self.file = self.file.drop(columns=columns_to_drop)
  
  def replace_columns(self):
    print("Iniciando alteração e correcoes de colunas...", end=" ")
    newColumns = []
    for column in self.file.columns:
      newColumns.append(self.columns_master.get_column_name(column))
      
    self.file.columns = newColumns
    
    self.file[self.file.columns[0]] = self.file[self.file.columns[0]].apply(extract_second_year)
    
    print("COMPLETE")
  
  def save_as_csv(self, output_path):
    self.file.to_csv(output_path, index=False, sep=";")
    
    print(f"Arquivo {output_path} salvo com sucesso!")

def extract_second_year(year):
  parts = year.split('/')
  if len(parts) > 1:
      return parts[1]
  else:
      return year

def main():
  try:
    if len(sys.argv) < 3:
        print("Usage: python convert_xlsx_csv.py <arquivo_entrada> <arquivo_saida.csv> <flag_drop_correlation>")
    else:
      input_path = sys.argv[1]
      output_path = sys.argv[2]
      
      drop_correlation = None
      
      if len(sys.argv) == 4:
        drop_correlation = sys.argv[3]
      
      raw = RawFile(input_path)
      
      raw.prune_lines()
      
      raw.prune_columns()
      
      if drop_correlation:
        raw.drop_correlation()
      
      raw.replace_columns()
      
      raw.save_as_csv(output_path)
  except Exception as e:
    print("ERROR! Algo de errado ocorreu na execução - Mensagem: " + str(e))

if __name__ == "__main__":
  main()