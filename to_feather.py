import pandas as pd

p = lambda s: float(s.replace('£', '').replace(',',''))

df = pd.read_csv("./Parity Pathways Reduced CO2_ImprovementScenario_14-02-2023_0927.csv",dtype={
        "UPRN":str,
        "UDPRN":str,
        "Address Id (used by website)":str,
        "SAP":float,
        "EI":float,
        "KgCO2 (SAP 2012)":int,
        "KgCO2 2017":int,
        "KgCO2 (SAP 10.2)":int,
        "KgCO2 2025":int,
        "KgCO2 2030":int,
        "KgCO2 2038":int,
        "KgCO2 2050":int,
        "Fuel Bills":str,
        "Fuel Bills 'Realistic'":str,
        "Heating Cost":str,
        "kWh/yr":float,
        "kWh(Heating Demand) /m2/yr":float,
        "Av. Heat Loss Coefficient (w/K)":float,
        "Total Floor Area":float
    },thousands=r',')#, converters={'Fuel Bills': p,"Fuel Bills 'Realistic'": p,'Heating Cost': p})
print(df.head())
print(df.dtypes)
df.to_feather("./nrg.ft",compression='zstd')