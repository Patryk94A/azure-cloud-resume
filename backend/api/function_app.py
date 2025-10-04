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
        # Step 1: Read item from Cosmos DB
        item= container.read_item(item="1", partition_key="1")

        # Step 2: Increment the count, if 'count' does not exist. Give it a default value of 0
        count = item.get('count', 0) + 1

        # Step 3: Update the item in Cosmos DB
        item['count'] = count

        # Step 4: Find document with (item["id"] == "1") and replace it with (body=item(new version of document and save it back in container))
        container.replace_item(item=item["id"], body=item)


        return func.HttpResponse(f"Document found: id={item['id']}, count={count}")
    except Exception as e:
        return func.HttpResponse(f"Error reading from Cosmos DB: {str(e)}", status_code=500)
