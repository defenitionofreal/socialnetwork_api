# starnavi_test
Social Network API

`import requests as r

# signup new user
register = r.post('http://127.0.0.1:8000/api/v1/register/', json={'email': 'test@email.com', 'username': 'testuser', 'password': 'testpass', 'password2': 'testpass'})
print('Signup status: ', register.status_code)

# receive authorization token / login
res = r.post('http://127.0.0.1:8000/api/v1/token/', json={'username': 'testuser', 'password': 'testpass'})
token = res.json()['access']
h = {'Authorization': f'Bearer {token}'}
print('Login token status: ', res.status_code)
print('Headers: ', h)

# update user data without auth (check pk in path)
update = r.patch('http://127.0.0.1:8000/api/v1/users/2/', json={'first_name': 'erik'})
print('Update without auth status: ', update.status_code)


# update user data with auth (check pk in path)
update = r.patch('http://127.0.0.1:8000/api/v1/users/2/', json={'first_name': 'erik'}, headers=h)
print('Update with auth status: ', update.status_code)

# create new post
post = r.post('http://127.0.0.1:8000/api/v1/posts/', json={'title': 'Test title', 'body': 'Some test content...'}, headers=h)
post.json()
print('Create post status: ', post.status_code)
print(post.json())

# like post
like = r.post('http://127.0.0.1:8000/api/v1/posts/1/like/', headers=h)
print('Like status: ', like.status_code)

# unlike post
like = r.post('http://127.0.0.1:8000/api/v1/posts/1/unlike/', headers=h)
print('UnLike status: ', like.status_code)


# users analytics
i = r.get('http://127.0.0.1:8000/api/v1/users/analytics/', headers=h)
print('Users analytics:\n', i.json())

# posts likes analytics
i = r.get('http://127.0.0.1:8000/api/v1/posts/analytics/date_from=2021-05-26&date_to=2021-05-27', headers=h)
print('Posts likes analytics:\n', i.json())``
```
