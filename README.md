# Yatube API

This is an API for yet another one social media - Yatube
Here you can create your own posts and comment posts of other users

## Install

```bash
python3 -m venv venv    # use 'python' instead 'python3' for Windows
source venv/bin/activate
pip3 install -r requirements.txt
```

## Run the app

```bash
python3 manage.py runserver    # use 'python' instead 'python3' for Windows
```

# REST API

The REST API to the example app is described below.

## Get list of Posts

### Request

`GET /posts/`

    http://127.0.0.1:8000/posts/

### Response

    09/May/2022 11:51:12] "GET /api/v1/posts/ HTTP/1.1" 200 863

```json
[
    {
        "id": 1,
        "author": "Alan",
        "text": "Ah, hello adventurer and welcome to the town of HoneyWood!",
        "pub_date": "2022-05-05T20:58:44.401369Z",
        "image": null,
        "group": 1
    },
    {
        "id": 2,
        "author": "Rowan",
        "text": "Nice day for fishing, ain't it? Hu ha!",
        "pub_date": "2022-05-05T21:01:41.551591Z",
        "image": null,
        "group": 1
    }
]
```

## Create a new Post

### Request

`POST /post/`

    http://127.0.0.1:8000/posts/

### Response

    [09/May/2022 11:51:23] "POST /api/v1/posts/ HTTP/1.1" 201 110

``` json
{
    "id": 9,
    "author": "Alan",
    "text": "Hello, world!",
    "pub_date": "2022-05-09T11:51:23.333972Z",
    "image": null,
    "group": null
}
```

## Get a specific Post

### Request

`GET /post/{id}/`

    http://127.0.0.1:8000/posts/5/

### Response

    [09/May/2022 12:10:07] "GET /api/v1/posts/5/ HTTP/1.1" 200 143

``` json
{
    "id": 5,
    "author": "Samuel",
    "text": "English, motherforker, do you speak it?!",
    "pub_date": "2022-05-05T21:04:25.371149Z",
    "image": null,
    "group": null
}
```

## Other endpoints

- For groups use same endpoints with post:
    
`GET /groups/`

    http://127.0.0.1:8000/groups/

- For comments use same endpoints with post, but URL should starts with ```/posts/{post_id}```

`GET /comments/`

    http://127.0.0.1:8000/posts/{id}/comments/