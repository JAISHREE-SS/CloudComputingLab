from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template as a string
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CGPA Calculator</title>
</head>
<body>
    <h1>CGPA Calculator</h1>
    <form method="post">
        <div id="courses">
            <div class="course">
                <input type="number" name="credits[]" step="any" required placeholder="Credits" min="0">
                <input type="number" name="grade_points[]" step="any" required placeholder="Grade Points" min="0" max="4">
                <br><br>
            </div>
        </div>
        <button type="button" onclick="addCourse()">Add Another Course</button>
        <br><br>
        <button type="submit">Calculate CGPA</button>
    </form>

    {% if cgpa is not none %}
        <h2>CGPA: {{ cgpa }}</h2>
    {% endif %}

    <script>
        function addCourse() {
            var container = document.getElementById('courses');
            var courseDiv = document.createElement('div');
            courseDiv.classList.add('course');
            courseDiv.innerHTML = `
                <input type="number" name="credits[]" step="any" required placeholder="Credits" min="0">
                <input type="number" name="grade_points[]" step="any" required placeholder="Grade Points" min="0" max="10">
                <br><br>
            `;
            container.appendChild(courseDiv);
        }
    </script>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    cgpa = None
    if request.method == 'POST':
        try:
            credits = list(map(float, request.form.getlist('credits[]')))
            grade_points = list(map(float, request.form.getlist('grade_points[]')))
            
            if len(credits) != len(grade_points) or not credits:
                cgpa = "Invalid input"
            else:
                total_credits = sum(credits)
                weighted_sum = sum(c * g for c, g in zip(credits, grade_points))
                if total_credits > 0:
                    cgpa = weighted_sum / total_credits
                else:
                    cgpa = "Total credits cannot be zero"
        except ValueError:
            cgpa = "Invalid input"

    return render_template_string(html_template, cgpa=cgpa)

if __name__ == '__main__':
    app.run(debug=True)
