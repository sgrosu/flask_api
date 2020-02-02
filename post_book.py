import requests
content = {
    "name":"Free Will 1 ",
    "price": 8.2,
    "isbn": 21324355723,
    'author': 'Sam Harris'
}

#request = requests.post("http://127.0.0.1:5000/books", json=content)
#print(request.text)

# payload = {
#     #'name': 'Meditation step by step',
#     'price': 15.56
# }
#
# request = requests.patch('http://127.0.0.1:5000/books/998877665544',json=payload)
# print(request.text)

req = requests.delete('http://127.0.0.1:5000/books/998877665544')
print(req.text)