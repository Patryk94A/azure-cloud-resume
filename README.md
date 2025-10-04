# azure-cloud-resume
My own azure resume challenge, following ACG project video.

# First steps
- Frontend folder contains the website
- main.js contains code for counter
- index.html contains my resume in html format

# After a lot of time finding solution for "ERROR: unhandled error in functions worker: '_SixMetaPathImporter' object has no attribute '_path'". 
- Solution was to downgrade python to 3.11.9 

# Connection with CosmosDB
- Added and tested connection with CosmosDB. Firstly i wanted to do it using bindings, but was not getting it ready. So switched it to SDK and it works perfectly after some tests
- Added functionality to retrive data (id and count from CosmosDB) and each time someone enters HTTP trigger it adds 1 to it and replace it in CosmosDB