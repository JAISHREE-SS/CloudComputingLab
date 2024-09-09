from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = '''
<!doctype html>
<html>
<head>
    <title>Temperature Converter</title>
</head>
<body>
    <h1>Temperature Converter</h1>
    <form method="post">
        <input type="text" name="temperature" placeholder="Enter temperature">
        <select name="unit">
            <option value="CtoF">Celsius to Fahrenheit</option>
            <option value="FtoC">Fahrenheit to Celsius</option>
        </select>
        <button type="submit">Convert</button>
    </form>
    {% if result is not none %}
        <h2>Result: {{ result }}</h2>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        temp = float(request.form['temperature'])
        unit = request.form['unit']
        if unit == 'CtoF':
            result = temp * 9/5 + 32
        elif unit == 'FtoC':
            result = (temp - 32) * 5/9
        result = round(result, 2)
    return render_template_string(HTML, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
