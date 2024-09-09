from flask import Flask, render_template, request

app = Flask(__name__)

index='''
<!DOCTYPE html>
<html>
<head>
    <title>CGPA Calculator</title>
</head>
<body>
    <h1>CGPA Calculator</h1>
    <form action="/calculate" method="post">
        <div id="courses">
            <div>
                <label>Grade:</label>
                <input type="text" name="grades">
                <label>Credits:</label>
                <input type="text" name="credits">
            </div>
        </div>
        <button type="button" onclick="addCourse()">Add Course</button>
        <button type="submit">Calculate CGPA</button>
    </form>
    <script>
        function addCourse() {
            var div = document.createElement('div');
            div.innerHTML = '<label>Grade:</label><input type="text" name="grades"><label>Credits:</label><input type="text" name="credits">';
            document.getElementById('courses').appendChild(div);
        }
    </script>
</body>
</html>
'''

result='''
<!DOCTYPE html>
<html>
<head>
    <title>CGPA Result</title>
</head>
<body>
    <h1>Your CGPA is: {{ cgpa }}</h1>
    <a href="/">Calculate Again</a>
</body>
</html>

'''
@app.route('/')
def index():
    return render_template(index)

@app.route('/calculate', methods=['POST'])
def calculate():
    grades = request.form.getlist('grades')
    credits = request.form.getlist('credits')
    total_points = sum(float(grade) * float(credit) for grade, credit in zip(grades, credits))
    total_credits = sum(float(credit) for credit in credits)
    cgpa = total_points / total_credits
    return render_template(result, cgpa=cgpa)

if __name__ == '__main__':
    app.run(debug=True)
