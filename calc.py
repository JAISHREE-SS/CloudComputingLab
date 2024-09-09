from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template embedded within the Python file
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Calculator</title>
</head>
<body>
    <h1>Simple Calculator</h1>
    <form method="post">
        <input type="number" name="num1" placeholder="Number 1" required>
        <input type="number" name="num2" placeholder="Number 2" required>
        <select name="operation">
            <option value="add">Add</option>
            <option value="subtract">Subtract</option>
            <option value="multiply">Multiply</option>
            <option value="divide">Divide</option>
        </select>
        <button type="submit">Calculate</button>
    </form>
    {% if result is not none %}
        <h2>Result: {{ result }}</h2>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.form.get('num1'))
            num2 = float(request.form.get('num2'))
            operation = request.form.get('operation')

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 == 0:
                    result = 'Error: Division by zero'
                else:
                    result = num1 / num2
        except ValueError:
            result = 'Invalid input'

    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == '__main__':
    app.run(debug=True)
