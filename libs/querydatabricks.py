from databricks import sql
import os

DATABRICKS_HOSTNAME = 'https://adb-3886069633353933.13.azuredatabricks.net'
DATABRICKS_SERVER_HOSTNAME = 'adb-3886069633353933.13.azuredatabricks.net' 
DATABRICKS_HTTP_PATH = 'sql/protocolv1/o/3886069633353933/0326-204742-af1fo56f' 
DATABRICKS_TOKEN = 'dapi336a1f512f4ad37295d9d859227a8ebb-3'

def querymydb(k):
    query="SELECT * FROM samples.nyctaxi.trips LIMIT {}".format(k)
    with sql.connect(
        server_hostname=DATABRICKS_SERVER_HOSTNAME,
        http_path=DATABRICKS_HTTP_PATH,
        access_token=DATABRICKS_TOKEN,
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        for row in result:
            print(row)

    return result
