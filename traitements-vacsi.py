#!/usr/bin/env python
# coding: utf-8

import pandas as pd
pd.options.display.max_columns = 1000
pd.options.display.max_rows = 4000

FILE_FRA = "vacsi-fra.csv"
FILE_REG = "vacsi-reg.csv"
FILE_DEP = "vacsi-dep.csv"
FILE_SEXE_FRA = "vacsi-s-fra.csv"
FILE_SEXE_REG = "vacsi-s-reg.csv"
FILE_SEXE_DEP = "vacsi-s-dep.csv"
FILE_AGE_FRA = "vacsi-a-fra.csv"
FILE_AGE_REG = "vacsi-a-reg.csv"
FILE_AGE_DEP = "vacsi-a-dep.csv"

INPUT_REPO = "2021-01-28/"
OUTPUT_REPO = "publish/"


# ## Synthèse

# Données nationales

spf = pd.read_csv(INPUT_REPO+FILE_FRA,dtype=str,sep=";")
spf.n_dose1 = spf.n_dose1.astype(int)
spf = spf.sort_values(by=['jour'])
spf['n_cum_dose1'] = spf[['n_dose1']].cumsum()['n_dose1']
spf.to_csv(OUTPUT_REPO+FILE_FRA,index=False,sep=";")


# Données régionales


spf = pd.read_csv(INPUT_REPO+FILE_REG,sep=";",dtype=str)
spf.n_dose1 = spf.n_dose1.astype(int)
spf = spf.sort_values(by=['jour'])
cols = ['reg','jour','n_dose1','n_cum_dose1']
spfc = pd.DataFrame(columns=cols)
for reg in spf.reg.unique():
    tmp = spf[spf['reg'] == reg]
    tmp['n_cum_dose1'] = tmp[['n_dose1']].cumsum()['n_dose1']
    spfc = spfc.append(tmp, ignore_index=True)
spfc = spfc.sort_values(by=['reg','jour'])
spfc.to_csv(OUTPUT_REPO+FILE_REG,index=False,sep=";")


# données départementales

spf = pd.read_csv(INPUT_REPO+FILE_DEP,sep=";",dtype=str)
spf.n_dose1 = spf.n_dose1.astype(int)
spf = spf.sort_values(by=['jour'])
cols = ['dep','jour','n_dose1','n_cum_dose1']
spfc = pd.DataFrame(columns=cols)
for dep in spf.dep.unique():
    tmp = spf[spf['dep'] == dep]
    tmp['n_cum_dose1'] = tmp[['n_dose1']].cumsum()['n_dose1']
    spfc = spfc.append(tmp, ignore_index=True)
spfc = spfc.sort_values(by=['dep','jour'])
spfc.to_csv(OUTPUT_REPO+FILE_DEP,index=False,sep=";")


# ## Age

# Données nationales

spf = pd.read_csv(INPUT_REPO+FILE_AGE_FRA,sep=";",dtype=str)
spf.n_dose1 = spf.n_dose1.astype(int)
cols = ['fra','clage_vacsi','jour','n_dose1','n_cum_dose1']
spfc = pd.DataFrame(columns=cols)
for el in spf.clage_vacsi.unique():
    tmp = spf[spf['clage_vacsi'] == el]
    tmp['n_cum_dose1'] = tmp[['n_dose1']].cumsum()['n_dose1']
    spfc = spfc.append(tmp, ignore_index=True)
spfc.to_csv(OUTPUT_REPO+FILE_AGE_FRA,index=False,sep=";")


# Données régionales

spf = pd.read_csv(INPUT_REPO+FILE_AGE_REG,sep=";",dtype=str)
spf.n_dose1 = spf.n_dose1.astype(int)
spf = spf.sort_values(by=['jour'])
cols = ['reg','clage_vacsi','jour','n_dose1','n_cum_dose1']
spfc = pd.DataFrame(columns=cols)
for reg in spf.reg.unique():
    for el in spf.clage_vacsi.unique():
        tmp = spf[(spf['reg'] == reg) & (spf['clage_vacsi'] == el)]
        tmp['n_cum_dose1'] = tmp[['n_dose1']].cumsum()['n_dose1']
        spfc = spfc.append(tmp, ignore_index=True)
spfc = spfc.sort_values(by=['reg','clage_vacsi','jour'])
spfc.to_csv(OUTPUT_REPO+FILE_AGE_REG,index=False,sep=";")


# Données départementales

spf = pd.read_csv(INPUT_REPO+FILE_AGE_DEP,sep=";",dtype=str)
spf.n_dose1 = spf.n_dose1.astype(int)
spf = spf.sort_values(by=['jour'])
cols = ['dep','clage_vacsi','jour','n_dose1','n_cum_dose1']
spfc = pd.DataFrame(columns=cols)
for dep in spf.dep.unique():
    for el in spf.clage_vacsi.unique():
        tmp = spf[(spf['dep'] == dep) & (spf['clage_vacsi'] == el)]
        tmp['n_cum_dose1'] = tmp[['n_dose1']].cumsum()['n_dose1']
        spfc = spfc.append(tmp, ignore_index=True)
spfc = spfc.sort_values(by=['dep','clage_vacsi','jour'])
spfc.to_csv(OUTPUT_REPO+FILE_AGE_DEP,index=False,sep=";")


# ## Sexe

# Données nationales

spf = pd.read_csv(INPUT_REPO+FILE_SEXE_FRA,sep=";",dtype=str)
spf.n_dose1 = spf.n_dose1.astype(int)
cols = ['fra','sexe','jour','n_dose1','n_cum_dose1']
spfc = pd.DataFrame(columns=cols)
for el in spf.sexe.unique():
    tmp = spf[spf['sexe'] == el]
    tmp['n_cum_dose1'] = tmp[['n_dose1']].cumsum()['n_dose1']
    spfc = spfc.append(tmp, ignore_index=True)
spfc.to_csv(OUTPUT_REPO+FILE_SEXE_FRA,index=False,sep=";")


# Données régionales

spf = pd.read_csv(INPUT_REPO+FILE_SEXE_REG,sep=";",dtype=str)
spf.n_dose1 = spf.n_dose1.astype(int)
spf = spf.sort_values(by=['jour'])
cols = ['reg','sexe','jour','n_dose1','n_cum_dose1']
spfc = pd.DataFrame(columns=cols)
for reg in spf.reg.unique():
    for el in spf.sexe.unique():
        tmp = spf[(spf['reg'] == reg) & (spf['sexe'] == el)]
        tmp['n_cum_dose1'] = tmp[['n_dose1']].cumsum()['n_dose1']
        spfc = spfc.append(tmp, ignore_index=True)
spfc = spfc.sort_values(by=['reg','sexe','jour'])
spfc.to_csv(OUTPUT_REPO+FILE_SEXE_REG,index=False,sep=";")


# Données départementales

spf = pd.read_csv(INPUT_REPO+FILE_SEXE_DEP,sep=";",dtype=str)
spf.n_dose1 = spf.n_dose1.astype(int)
spf = spf.sort_values(by=['jour'])
cols = ['dep','sexe','jour','n_dose1','n_cum_dose1']
spfc = pd.DataFrame(columns=cols)
for dep in spf.dep.unique():
    for el in spf.sexe.unique():
        tmp = spf[(spf['dep'] == dep) & (spf['sexe'] == el)]
        tmp['n_cum_dose1'] = tmp[['n_dose1']].cumsum()['n_dose1']
        spfc = spfc.append(tmp, ignore_index=True)
spfc = spfc.sort_values(by=['dep','sexe','jour'])
spfc.to_csv(OUTPUT_REPO+FILE_SEXE_DEP,index=False,sep=";")

