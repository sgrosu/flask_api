from flask import Flask, jsonify, request, Response
import json
from settings import *

books = [

    {
        'name': 'The Beginning of Infinity',
        'price': 17,
        'isbn': 998877665544
    },
    {

        'name': 'The Fabric of Reality',
        'price': 22,
        'isbn': 887799004422
    }
]


def validBookObject(bookObject):
    if ('name' in bookObject) and ('price' in bookObject) and ('isbn' in bookObject):
        return True
    else:
        return False

@app.route('/')
def hello_world():
    return 'Hello Flask!'

#GET books

@app.route('/books')
def return_books():
    return jsonify({'books': books})

#POST books

@app.route('/books', methods=['POST'])
def add_book():
    #test
    #return jsonify(request.get_json())
    request_data = request.get_json()
    if validBookObject(request_data):
        new_book = {
            'name': request_data['name'],
            'price': request_data['price'],
            'isbn': request_data['isbn']
        }
        books.insert(0,new_book)
        response = Response('bagat',201, mimetype='application/json')
        response.headers['Location'] = '/books/' + str(new_book['isbn'])
        return response
    else:
        invalidBookErrorMsg ={
            'error': 'invalid book object was passed in the request',
            'helpStr': 'baga formatu calumea neamule!'
        }
        response = Response(json.dumps(invalidBookErrorMsg),400, mimetype='application/json')
        return response



#GET books/isbn

@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    return_val = {}
    for book in books:
        if book['isbn']  == isbn:
            return_val = {
                'name': book['name'],
                'price': book['price']
            }
    return jsonify(return_val)



# PUT book

@app.route('/books/<int:isbn>', methods=['PUT'])
def replace_book(isbn):
    request_data = request.get_json()
    new_book = {
        'name': request_data['name'],
        'price': request_data['price'],
        'isbn': isbn
    }
    i = 0
    for book in books:
        if book['isbn'] == isbn:
            books[i] = new_book
        i+=1
    response = Response('modificat', status=204, mimetype='application/json')
    return response

@app.route('/books/<int:isbn>', methods=['PATCH'])
def update_book(isbn):
    request_data = request.get_json()
    updated_book = {}
    if 'name' in request_data:
        updated_book['name'] = request_data['name']
    if 'price' in request_data:
        updated_book['price'] = request_data['price']
    for book in books:
        if book['isbn'] == isbn:
            book.update(updated_book)
    response = Response('updatat',status=204)
    response.headers['Location'] = '/books/' + str(isbn)
    return response

@app.route('/books/<int:isbn>',methods=['DELETE'])
def delete_book(isbn):
    i = 0
    for book in books:
        if book['isbn'] == isbn:
            books.pop(i)
            response = Response("", 204)
            return response
        i+=1
    invalidBookObjectErrMess = {
        'error': 'A book with the ISBN provided has bot been found'
    }
    response = Response(json.dumps(invalidBookObjectErrMess), status=404, mimetype='application/json')
    return response
app.run(port=5000)