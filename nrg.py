import pandas as pd
from fastapi import FastAPI, Response, Request, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
from typing import Union, List, Dict, Annotated
import json
from pydantic import BaseModel



class Measure(BaseModel):
    Index: int
    Category: str
    Measure_Group_Id: str
    MeasureGroupName: str
    Cost:str
    Cumulative_Cost: str
    SAP_following_this_Measure: float
    Individual_SAP_increase: float
    Cumulative_SAP_increase: float
    EI_following_this_Measure: float
    Individual_EI_increase: float
    Cumulative_EI_increase: float
    kgCO2_following_this_Measure: float
    Individual_kgCO2_saving: float
    Cumulative_kgCO2_saving: float
    kgCO2_following_this_Measure_1: float
    Individual_kgCO2_saving_1: float
    Cumulative_kgCO2_saving_1: float
    kgCO2_following_this_Measure_2: float
    Individual_kgCO2_saving_2: float
    Cumulative_kgCO2_saving_2: float
    kgCO2_following_this_Measure_3: float
    Individual_kgCO2_saving_3: float
    Cumulative_kgCO2_saving_3: float
    kgCO2_following_this_Measure_4: float
    Individual_kgCO2_saving_4: float
    Cumulative_kgCO2_saving_4: float
    kgCO2_following_this_Measure_5: float
    Individual_kgCO2_saving_5: float
    Cumulative_kgCO2_saving_5: float
    kgCO2_following_this_Measure_6: float
    Individual_kgCO2_saving_6: float
    Cumulative_kgCO2_saving_6: float
    Fuel_Bill_following_this_Measure: str
    Individual_Fuel_Bill_saving: str
    Cumulative_Fuel_Bill_saving: str
    Fuel_Bill_following_this_Measure_1: str
    Individual_Fuel_Bill_saving_1: str
    Cumulative_Fuel_Bill_saving_1: str
    Heating_Costs_following_this_Measure: str
    Individual_Heating_Costs_saving: str
    Cumulative_Heating_Costs_saving: str
    kWh_following_this_Measure: float
    Individual_kWh_saving: float
    Cumulative_kWh_saving: float
    kWh_m2_following_this_Measure: float
    Individual_kWh_m2_saving: float
    Cumulative_kWh__m2_saving: float
    Av_Heat_Loss_Coefficient_w_K_1: float
    Measure_Outcome_Id: str
    Measure_Outcome_Name: str

class Building(BaseModel):
    UPRN: str = None
    UDPRN:str = None
    AddressId:str = None
    Address:str = None
    SAP:float = None
    EI:float = None
    KgCO2_SAP_2012:int = None
    KgCO2_2017:int = None
    KgCO2_SAP_10_2:int = None
    KgCO2_2025:int = None
    KgCO2_2030:int = None
    KgCO2_2038:int = None
    KgCO2_2050:int = None
    Fuel_Bills:str = None
    Fuel_Bills_Realistic:str = None
    Heating_Cost:str = None
    kWh_yr:float = None
    kWh_Heating_Demand_m2_yr:float = None
    Av_Heat_Loss_Coefficient_w_K:float = None
    Total_Floor_Area:float = None
    measures:List[Measure]


df = pd.read_feather("./nrg.ft")
uprns = set(df["UPRN"].unique())
print(len(uprns), "Unique UPRNs")

#test_house = df.loc[df["UPRN"]=="10090470558"].sort_values(by=["Index (order applied)"])

nrg_port = os.getenv("NRG_PORT", "5008")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_measures(df):
    measures = df.drop(["UPRN", "UDPRN", "Address Id (used by website)", "Address", "SAP", "EI",
       "KgCO2 (SAP 2012)", "KgCO2 2017", "KgCO2 (SAP 10.2)", "KgCO2 2025",
       "KgCO2 2030", "KgCO2 2038", "KgCO2 2050", "Fuel Bills",
       "Fuel Bills 'Realistic'", "Heating Cost", "kWh/yr",
       "kWh(Heating Demand) /m2/yr", "Av. Heat Loss Coefficient (w/K)",
       "Total Floor Area"], axis=1)
    measures.columns = [
        "Index",
        "Category",
        "Measure_Group_Id",
        "MeasureGroupName",
        "Cost",
        "Cumulative_Cost",
        "SAP_following_this_Measure",
        "Individual_SAP_increase",
        "Cumulative_SAP_increase",
        "EI_following_this_Measure",
        "Individual_EI_increase",
        "Cumulative_EI_increase",
        "kgCO2_following_this_Measure",
        "Individual_kgCO2_saving",
        "Cumulative_kgCO2_saving",
        "kgCO2_following_this_Measure_1",
        "Individual_kgCO2_saving_1",
        "Cumulative_kgCO2_saving_1",
        "kgCO2_following_this_Measure_2",
        "Individual_kgCO2_saving_2",
        "Cumulative_kgCO2_saving_2",
        "kgCO2_following_this_Measure_3",
        "Individual_kgCO2_saving_3",
        "Cumulative_kgCO2_saving_3",
        "kgCO2_following_this_Measure_4",
        "Individual_kgCO2_saving_4",
        "Cumulative_kgCO2_saving_4",
        "kgCO2_following_this_Measure_5",
        "Individual_kgCO2_saving_5",
        "Cumulative_kgCO2_saving_5",
        "kgCO2_following_this_Measure_6",
        "Individual_kgCO2_saving_6",
        "Cumulative_kgCO2_saving_6",
        "Fuel_Bill_following_this_Measure",
        "Individual_Fuel_Bill_saving",
        "Cumulative_Fuel_Bill_saving",
        "Fuel_Bill_following_this_Measure_1",
        "Individual_Fuel_Bill_saving_1",
        "Cumulative_Fuel_Bill_saving_1",
        "Heating_Costs_following_this_Measure",
        "Individual_Heating_Costs_saving",
        "Cumulative_Heating_Costs_saving",
        "kWh_following_this_Measure",
        "Individual_kWh_saving",
        "Cumulative_kWh_saving",
        "kWh_m2_following_this_Measure",
        "Individual_kWh_m2_saving",
        "Cumulative_kWh__m2_saving",
        "Av_Heat_Loss_Coefficient_w_K_1",
        "Measure_Outcome_Id",
        "Measure_Outcome_Name",
    ]
    return json.loads(measures.to_json(orient="records"))


@app.get('/building')
def get_buildings(uprn: Annotated[list[str] | None, Query()]) -> list[Building]:
    '''
    Returns buildings, each with possible energy saving measures. Pass uprns in as query parameters
    '''
    buildings = []
    for u in uprn:
        if u not in uprns:
            raise HTTPException(status_code=404, detail="UPRN:" + str(u) + " not found")
        parity_mess = df.loc[df["UPRN"] == u].sort_values(by=["Index (order applied)"])
        out_building = {
            "UPRN": parity_mess.iloc[0]["UPRN"],
            "UDPRN":parity_mess.iloc[0]["UDPRN"],
            "AddressId":parity_mess.iloc[0]["Address Id (used by website)"],
            "Address":parity_mess.iloc[0]["Address"],
            "SAP":parity_mess.iloc[0]["SAP"],
            "EI":parity_mess.iloc[0]["EI"],
            "KgCO2_SAP_2012":parity_mess.iloc[0]["KgCO2 (SAP 2012)"],
            "KgCO2_2017":parity_mess.iloc[0]["KgCO2 2017"],
            "KgCO2_SAP_10_2":parity_mess.iloc[0]["KgCO2 (SAP 10.2)"],
            "KgCO2_2025":parity_mess.iloc[0]["KgCO2 2025"],
            "KgCO2_2030":parity_mess.iloc[0]["KgCO2 2030"],
            "KgCO2_2038":parity_mess.iloc[0]["KgCO2 2038"],
            "KgCO2_2050":parity_mess.iloc[0]["KgCO2 2050"],
            "Fuel_Bills":parity_mess.iloc[0]["Fuel Bills"],
            "Fuel_Bills_Realistic":parity_mess.iloc[0]["Fuel Bills 'Realistic'"],
            "Heating_Cost":parity_mess.iloc[0]["Heating Cost"],
            "kWh_yr":parity_mess.iloc[0]["kWh/yr"],
            "kWh_Heating_Demand_m2_yr":parity_mess.iloc[0]["kWh(Heating Demand) /m2/yr"],
            "Av_Heat_Loss_Coefficient_w_K":parity_mess.iloc[0]["Av. Heat Loss Coefficient (w/K)"],
            "Total_Floor_Area":parity_mess.iloc[0]["Total Floor Area"],
            "measures":[]
        }   

        out_building["measures"] = get_measures(parity_mess)
        buildings.append(out_building)   
    return buildings        

@app.get('/building_denormalised')
def get_buildings(uprn: Annotated[list[str] | None, Query()]) -> list:
    '''
    Returns all measures denormalised and using original Parity field names...which may not play nicely with REST client...be careful out there !
    '''
    for u in uprn:
        if u not in uprns:
            raise HTTPException(status_code=404, detail="UPRN:" + str(u) + " not found")

    buildings = df.loc[df["UPRN"].isin(uprn)].sort_values(by=["UPRN","Index (order applied)"])
    obj = json.loads(buildings.to_json(orient="records"))
    return obj



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=nrg_port)
