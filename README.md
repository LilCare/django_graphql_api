# django_graphql_api
API using Django, GraphQL, PostgreSQL


##Getting Started

Within the root directory of the repo:
  ```bash
  pip install -r requirements.txt
  ```

Within the home directory:
  ```bash
  python manage.py runserver
  ```


##Sample GraphQL Queries

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
Required Headers: {"Authorization": "b'<token>'"}
  ```
  mutation {
    deleteUser {
      ok
    }
  }
  ```