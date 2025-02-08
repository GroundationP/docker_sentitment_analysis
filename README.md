# docker_sentitment_analysis

In this example, a CI/CD pipeline was created to automatically test an API before deployment. The API is based on a sentiment analysis algorithm, packaged in a Docker image, which predicts whether an English sentence has a positive or negative sentiment.

API Endpoints

/status: Simply checks if the API is running.
/permissions: Allows a user, identified by a username and password, to check which model version they have access to.
/Sentiment Analysis Endpoints: These require a sentence as input, verify the user's identity, check their access rights, and return a sentiment score. A score of -1 indicates negative sentiment, while +1 indicates positive sentiment.

Authentication and Authorization Tests

Authentication Test: GET requests is sent to /permissions using two pre-registered users: alice:wonderland and bob:builder. To simulate an unregistered user behavior a third test with clementine:mandarine was sent.
Authorization Test: It ensures that bob has access to version v1 only, while Alice can access both versions. The sentences "life is beautiful" and "that sucks" will be used to test the API’s sentiment prediction capability.

Each test will be executed in separate containers and will generate a log file describing the results of each test.

