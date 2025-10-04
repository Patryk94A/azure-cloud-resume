import azure.functions as func
import logging
from azure.cosmos import CosmosClient
import os


enpoint = os.environ["COSMOS_DB_ENDPOINT"]
key = os.environ["COSMOS_DB_KEY"]
database_name = os.environ["COSMOS_DB_DATABASE_NAME"]
container_name = os.environ["COSMOS_DB_CONTAINER_NAME"]

cosmos_client = CosmosClient(enpoint, credential=key)
database_name = cosmos_client.get_database_client(database_name)
container = database_name.get_container_client(container_name)



app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)
@app.route(route="Http_trigger_v2")



def Http_trigger_v2(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        item= container.read_item(item="1", partition_key="1")
        count= item.get("count")

        return func.HttpResponse(f"Document found: id={item['id']}, count={count}")
    except Exception as e:
        return func.HttpResponse(f"Error reading from Cosmos DB: {str(e)}", status_code=500)
