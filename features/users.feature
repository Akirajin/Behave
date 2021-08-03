Feature: Testing behave

  Scenario: run a simple test with FastAPI
    Given we have the application running on "http://localhost:8000/docs"
    And we have postgreSQL running on "http://locahost:5432"
    And we have the following user in the database
      | name    | surname |
      | Glauber | Rocha   |
      | Jessica | Rocha   |
    When we request "GET" to "http://localhost:8000/users"
    Then we will get http status "200" with payload:
    """
    [{
      "name":"Jessica",
      "surname":"Rocha"
    },
    {
      "name":"Glauber",
      "surname":"Rocha"
    }]
    """
