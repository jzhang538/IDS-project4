from databricks import sql
import os
import numpy as np

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
        
        nodes = {}
        idx2zip = {}
        cnt = 0
        for row in result:
            if row["pickup_zip"] not in nodes.keys():
                nodes[row["pickup_zip"]]=cnt
                idx2zip[cnt] = row["pickup_zip"]
                cnt+=1
            if row["dropoff_zip"] not in nodes.keys():
                nodes[row["dropoff_zip"]]=cnt
                idx2zip[cnt] = row["dropoff_zip"]
                cnt+=1

        edges = np.zeros((cnt,cnt))
        for row in result:
            node_go = nodes[row["pickup_zip"]]
            node_arrive = nodes[row["dropoff_zip"]]
            edges[node_go][node_arrive]+=1
        print(edges)
        print(np.max(edges))

        edge_dict = {}
        for i in range(edges.shape[0]):
            pairs = []
            for j in range(edges.shape[1]):
                if edges[i][j]!=0:
                    pairs.append([idx2zip[j], edges[i][j]])
            edge_dict[idx2zip[i]] = pairs
    return edge_dict