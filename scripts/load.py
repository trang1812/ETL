import psycopg2
import transform
import queries


# connecting to database 
conn = psycopg2.connect(host="localhost", database="superstore", user="postgres", password="xxx")
print("connected to Database")

# Function which runs postgres querries 
def run_query(conn, query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        print(f"Successfully ran query")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Following query failed {query}")
        print(error)

# function which loads values to dimension tables 
def insert_values_in_table(cursor, df, table_name):
    cols = ", ".join(df.columns)
    asterisk = ", ".join(["%s"] * len(df.columns))
    query = (
        f"INSERT INTO {table_name}({cols}) VALUES ({asterisk}) "
    )
    for index, row in df.iterrows():
        values = tuple(row)
        cursor.execute(query, values)
    conn.commit()
    return

#function loads data to the fact table 
def load_sales_to_db(cursor, df,insert_query):
    # create connection
    tuples = [tuple(x) for x in df.to_numpy()]

    try:
        cursor.executemany(
            insert_query,
            tuples
        )
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        return
    
# main function which runs the whole ETL process 
def main():

    run_query(conn,queries.shipping_table)
    run_query(conn,queries.region_table)
    run_query(conn,queries.segment_table)
    run_query(conn,queries.city_table)
    run_query(conn,queries.category_table)
    run_query(conn,queries.sub_category_table)
    run_query(conn,queries.country_table)
    run_query(conn,queries.state_table)
    run_query(conn,queries.sales_fact)
    print("all queries have been run successfully")
    cursor = conn.cursor()
    print("Cursor is made")
    insert_values_in_table(cursor,transform.df_ship_mode,'ship_mode')
    insert_values_in_table(cursor,transform.df_region,'regions')
    insert_values_in_table(cursor,transform.df_segment,'segments')
    insert_values_in_table(cursor,transform.df_city,'citys')
    insert_values_in_table(cursor,transform.df_category,'category')
    insert_values_in_table(cursor,transform.df_sub_category,'sub_category')
    insert_values_in_table(cursor,transform.df_country,'country')
    insert_values_in_table(cursor,transform.df_state,'states')

    load_sales_to_db(cursor,transform.clean_df,queries.insert_fact_table)
    print("all data has been ingested")
    conn.close()
