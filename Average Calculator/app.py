from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def fibonacci(n):
    a, b = 0, 1
    fibs = []
    while b <= n:
        fibs.append(b)
        a, b = b, a + b
    return fibs

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/e', methods=['POST'])
def even_average():
    numbers = request.json.get('numbers', [])
    evens = [num for num in numbers if num % 2 == 0]
    avg = sum(evens) / len(evens) if evens else 0
    return jsonify(average=avg)

@app.route('/o', methods=['POST'])
def odd_average():
    numbers = request.json.get('numbers', [])
    odds = [num for num in numbers if num % 2 != 0]
    avg = sum(odds) / len(odds) if odds else 0
    return jsonify(average=avg)

@app.route('/f', methods=['POST'])
def fibonacci_average():
    numbers = request.json.get('numbers', [])
    max_num = max(numbers) if numbers else 0
    fibs = fibonacci(max_num)
    avg = sum(fibs) / len(fibs) if fibs else 0
    return jsonify(average=avg)

@app.route('/p', methods=['POST'])
def prime_average():
    numbers = request.json.get('numbers', [])
    primes = [num for num in numbers if is_prime(num)]
    avg = sum(primes) / len(primes) if primes else 0
    return jsonify(average=avg)

@app.route('/r', methods=['POST'])
def random_average():
    numbers = request.json.get('numbers', [])
    if numbers:
        random_numbers = random.sample(numbers, min(len(numbers), 5))
        avg = sum(random_numbers) / len(random_numbers)
    else:
        avg = 0
    return jsonify(average=avg)

if __name__ == '__main__':
    app.run(debug=True)
