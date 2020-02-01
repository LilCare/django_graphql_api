# django_graphql_api
API using Django, GraphQL, PostgreSQL

##Sample GraphQL Queries

-Check if a username exists in your database:

  query {
    user(username: "testyUN") {
      id
    }
  }

-Add a new user to the database:

  mutation {
    createUser(username: "testyUN", password: "testyPW") {
      user {
        id
      }
    }
  }