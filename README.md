# Social Media API

## Overview

This project implements a RESTful API for a social media platform using Django REST Framework (DRF). The API allows users to perform actions such as creating and managing posts, likes, comments, and follows. Each endpoint is secured with appropriate permissions and provides detailed responses for various actions.

## Features

- **User Authentication**: Only authenticated users can perform actions like creating posts, likes, comments, and follows.
- **CRUD Operations**: Full support for creating, reading, updating, and deleting posts, likes, comments, and follow relationships.
- **Efficient Querysets**: Optimized database queries to minimize load and improve performance.
- **Filtering**: Ability to filter posts by hashtags.
- **Detailed API Documentation**: OpenAPI schema extensions for detailed API documentation and support for query parameters.

## API Endpoints

### Post Endpoints

- **`/posts/`**: List and create posts.
  - `GET`: Retrieve a list of all posts. Supports filtering by `hashtag`.
  - `POST`: Create a new post.
- **`/posts/{id}/`**: Retrieve, update, or delete a specific post.
  - `GET`: Retrieve a post by its ID.
  - `PUT`/`PATCH`: Update a post.
  - `DELETE`: Delete a post.

### My Posts Endpoints

- **`/myposts/`**: List and create posts by the authenticated user.
  - `GET`: Retrieve a list of posts created by the authenticated user.
  - `POST`: Create a new post by the authenticated user.

### Like Endpoints

- **`/likes/`**: List and create likes.
  - `GET`: Retrieve a list of likes by the authenticated user.
  - `POST`: Like a post.
- **`/likes/{id}/`**: Retrieve or delete a specific like.
  - `GET`: Retrieve a like by its ID.
  - `DELETE`: Remove a like.

### Comment Endpoints

- **`/comments/`**: List and create comments.
  - `GET`: Retrieve a list of comments by the authenticated user.
  - `POST`: Comment on a post.
- **`/comments/{id}/`**: Retrieve, update, or delete a specific comment.
  - `GET`: Retrieve a comment by its ID.
  - `PUT`/`PATCH`: Update a comment.
  - `DELETE`: Delete a comment.

### Follow Endpoints

- **`/follows/`**: List and create follow relationships.
  - `GET`: Retrieve a list of users followed by the authenticated user.
  - `POST`: Follow a user.
- **`/follows/{id}/`**: Retrieve or delete a specific follow relationship.
  - `GET`: Retrieve a follow relationship by its ID.
  - `DELETE`: Unfollow a user.

### My Followers Endpoints

- **`/myfollowers/`**: List and delete followers of the authenticated user.
  - `GET`: Retrieve a list of users following the authenticated user.
  - `DELETE`: Remove a follower.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/social-media-api.git
    ```
2. Install the required packages:
    ```bash
    docker-compose build
    ```
3. Apply migrations:
    ```bash
    docker-compose up

## Usage

### Authentication

- Obtain a token by posting your credentials to the `/api/token/` endpoint.
- Include the token in the `Authorization` header of your requests.

### Example Request

To retrieve all posts with the hashtag `#example`, use the following curl command:

```bash
curl -X GET "http://localhost:8000/posts/?hashtag=example" -H "Authorization: Bearer <your_token>"
