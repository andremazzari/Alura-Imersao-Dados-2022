import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

def AddIBGEdata(df):
    #Read data from enderecos.csv
    df_address = pd.read_csv('../data/interim/Data_Day4_Address.csv', sep = ',', encoding = 'utf_8')

    #Extract address data from collumn 'Rua', and create column 'Rua_Compare' to make merge with df_address
    df["Rua_Compare"] = df["Rua"].str.extract(r'(^[\w ]+)')
    df["Rua_Compare"] = df["Rua_Compare"].str.lower().str.strip()

    #Merge df and df_address
    df_merged = df.merge(df_address[['cep','latitude','longitude','Rua_Compare']], how = 'left', left_on = 'Rua_Compare', right_on = "Rua_Compare")

    #Drop duplicates
    df_merged.drop_duplicates(subset=df.columns, inplace = True)

    #Get data from censo sectors  in Sao Paulo using geopandas
    setor_censo = gpd.read_file('../data/external/Data_Geopandas/35SEE250GC_SIR.shp')
    setor_censo_sp = setor_censo[setor_censo.NM_MUNICIP == "SÃO PAULO"]

    df_merged["Point"] = ""
    for i in df_merged.index:
        df_merged["Point"][i] = Point(df_merged["longitude"][i], df_merged["latitude"][i])
    df_merged['setor_censo'] = df_merged["Point"].map(lambda x: setor_censo_sp.loc[setor_censo_sp.contains(x), 'CD_GEOCODI'].values).str[0]

    df_merged['setor_censo'] = pd.to_numeric(df_merged['setor_censo'])
    
    #Drop rows with NaN value in 'setor_censo'
    df_merged.drop(df_merged[df_merged['setor_censo'].isnull()].index.tolist(), axis = 0, inplace = True)
    
    #Get data from IBGE (already clenaed)
    df_ibge = pd.read_csv('../data/interim/IBGE_cleaned.csv')

    #Merge the original dataframe with IBGE dataframe
    df_prices_ibge = pd.merge(left = df_merged, right = df_ibge, how = "left", left_on = "setor_censo", right_on = "Cod_setor")

    return df_prices_ibge[['Metragem', 'Quartos', 'Banheiros', 'Vagas', 'Valor', 'V005', 'V007', 'V009', 'V011']]
