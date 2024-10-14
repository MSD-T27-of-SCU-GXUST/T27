from flask import Flask, render_template, request

app = Flask(__name__)

# Sample dormitory data
dorms = {
    "Dorm A": [],
    "Dorm B": [],
    "Dorm C": [],
    "Dorm D": []
}

# Home route to render the form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle dorm allocation
@app.route('/allocate', methods=['POST'])
def allocate():
    name = request.form['name']
    preferred_dorm = request.form['dorm']
    
    if preferred_dorm in dorms:
        dorms[preferred_dorm].append(name)
        message = f"{name} has been allocated to {preferred_dorm}."
    else:
        message = "Invalid dorm selection."

    # Show the allocation result
    return render_template('index.html', message=message, dorms=dorms)

if __name__ == '__main__':
    app.run(debug=True)
