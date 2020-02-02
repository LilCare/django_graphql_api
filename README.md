# django_graphql_api
API using Django, GraphQL, PostgreSQL


## Required Environment Dependencies

- Python 3.7.3
- Pip 20.0.2

Within the root directory of the repo:
  ```bash
  pip install -r requirements.txt
  ```
  ```bash
  cd src
  ```

Within the src directory:
  ```bash
  python manage.py runserver
  ```


## Sample GraphQL Queries

Interact with API at [http://127.0.0.1:8000/graphql/](http://127.0.0.1:8000/graphql/)

-Check if a username exists in your database:
  ```
  query user($username: String!) {
    user(username: $username) {
      id
      username
    }
  }
  ```

-Add a new user to the database:
  ```
  mutation createUser($username: String!, $password: String!) {
    createUser(username: $username, password: $password) {
      user {
        id
        username
      }
   }
  }
  ```

-Login a user (username/password must exist in the database):
  ```
  mutation loginUser($username: String!, $password: String!) {
    loginUser(username: $username, password: $password) {
      jwtToken
    }
  }
  ```

-Delete a user:
Required Headers: {"Authorization": "b'< token >'"}
  ```
  mutation {
    deleteUser {
      ok
    }
  }
  ```