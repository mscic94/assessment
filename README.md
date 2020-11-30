# Interview Assessment
Flask API service that searches public hosting platform repositories. 

### How to run the service
In order to start testing the service, first we have to start the application by running the following command in terminal.

```bash
docker-compose -f <path-to-project>/OfficeApp/docker-compose.yml up -d --build
```

### How to test the service
After executing the docker-compose file, now we can test the endpoint by running the following command.
```bash
curl --request POST \
  --url http://localhost:5000/search/repo \
  --header 'content-type: application/json' \
  --data '{
	"provider": "gitlab",
	"keyword": "python",
	"page_no": 1
}'
```

For the simplicity of this assignment, `Gitlab` is the only provider accepted in the payload. Since Gitlab Search API uses pagination, I also added `page_no` in the payload to get the next page of repositories.
However to make the call efficient from our end, I specified the total repositories returned per page in the application configurations which is set to 10.

### How to run the tests suite
After executing the docker-compose file, we can run the tests suite inside `office-app-search-repos` container.
1. Enter inside the container from the terminal using the following command:
    ```bash
    docker exec -it office-app-search-repos bash
    ```
2. Execute the command to run all the unit tests inside the container:
    ```bash
    python -m unittest
    ```

### Improvements
To simplify this API service I had to eliminate several functionalities that could be useful for this project if time and resources weren't an issue.

1. Implement `Logs`
 
    Logs are important to know exactly what is happening when something bad/weird occurs. This also could be used for security purposes and API calls count.
    
2. Write more `tests`

    Since I had limited time to implement this API, a lot of tests are missing (unit and functional tests) and this could cause bugs when modifying code or implementing new features/integrations.

3. `Flask config` file improvement
    
    As you might notice, in order to make use of the Gitlab Search API, an access token was required. Access token are time based and will be expired after certain time (in my case 2 months).
    Such properties could be stored in the application config settings and the access token could be read from environmental variables. This would be helpful if this service will have lots of integrations.

4. API `documentation`
    
   If the future vision of this API service gets bigger over time, it is important to document all the endpoints and this could be achieved by an API documentation platform such as Swagger.
   
5. `Error tracking`
    
   If the future vision of this API service gets bigger over time, it is important to track and monitor all the errors for faster debugging and crash reports. This could be achieved by an Application monitoring such as Sentry.