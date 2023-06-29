import pandas as pd


def read_df(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Successfully read DF")
        return df 
    except FileNotFoundError as error:
        print(f"There is No file at {file_path}")
        return error
    except pd.errors.EmptyDataError as empty_data_error:
        print(f"There is No data in {file_path}")
        return empty_data_error


def drop_columns(df,drop_col):
    """removing unnecessary columns"""
    try:
        df = df.drop(columns=drop_col)
        return df
    except AssertionError as error:
        print(error)



def unique_value_df(dataframe,col,column_name):
    """Creating Df with only unique values to avoid duplication"""
    try:
        new_list=dataframe[col].unique().tolist()
        new_df = pd.DataFrame({column_name:new_list})
        return new_df
    except KeyError as error:
        print("Unique Dataframe not made")
        print(error)

def main():
    file_path = 'C:/Users\Win 10/Downloads/Projects/ETL_2/data/SampleSuperstore.csv'
    df = read_df(file_path)
    drop_col= ["Discount","Postal Code","Quantity"]
    global clean_df, df_ship_mode, df_segment, df_country, df_city, df_state, df_region, df_category, df_sub_category
    
    clean_df= drop_columns(df,drop_col)
    
    df_ship_mode = unique_value_df(df,'Ship Mode','ship_mode')
    df_segment = unique_value_df(df,'Segment','segment')
    df_country = unique_value_df(df,'Country','country')
    df_city = unique_value_df(df,'City','city')
    df_state = unique_value_df(df,'State','state')
    df_region = unique_value_df(df,'Region','region')
    df_category = unique_value_df(df,'Category','category')
    df_sub_category = unique_value_df(df,'Sub-Category','sub_category')
