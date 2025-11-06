import pandas as pd


DEFAULT_CATCHMENT = "GB104026066630"

def load_data():
    df_outflow_points = pd.read_csv("C:\\Users\\Stefan.Bramer\\HOME\\PROJECTS\\PROFESSIONAL\\PROJECTS\\EYC_dashboard\\data\\WFD surface waterbody catchments list_outflow_XY.csv")
    fl_Qs = pd.read_csv("C:\\Users\\Stefan.Bramer\\HOME\\PROJECTS\\PROFESSIONAL\\PROJECTS\\EYC_dashboard\\data\\FL_flows_Qs.csv")
    ra_Qs = pd.read_csv("C:\\Users\\Stefan.Bramer\\HOME\\PROJECTS\\PROFESSIONAL\\PROJECTS\\EYC_dashboard\\data\\RA_flows_Qs.csv")
    nat_Qs = pd.read_csv("C:\\Users\\Stefan.Bramer\\HOME\\PROJECTS\\PROFESSIONAL\\PROJECTS\\EYC_dashboard\\data\\Nat_flows_Qs.csv")
    abs_impacts = pd.read_csv("C:\\Users\\Stefan.Bramer\\HOME\\PROJECTS\\PROFESSIONAL\\PROJECTS\\EYC_dashboard\\data\\Abstraction_Impacts.csv")
    scenario_results = pd.read_csv("C:\\Users\\Stefan.Bramer\\HOME\\PROJECTS\\PROFESSIONAL\\PROJECTS\\EYC_dashboard\\data\\Scenario_results.csv")
    summary_table = pd.read_csv("C:\\Users\\Stefan.Bramer\\HOME\\PROJECTS\\PROFESSIONAL\\PROJECTS\\EYC_dashboard\\data\\Summary_table.csv")
    return df_outflow_points, fl_Qs, ra_Qs, nat_Qs, abs_impacts, scenario_results, summary_table
data = load_data()


fdc_data = pd.DataFrame()
fdc_data['Percentile'] = data[2]['Percentile']
fdc_data['1.Naturalised'] = data[3]
fdc_data['2.Recent Actual'] = data[2]
fdc_data['3.Fully Licensed'] = data[1]
fdc_data = fdc_data.set_index('Percentile')


fdc_data.to_csv("fdc_data.csv")