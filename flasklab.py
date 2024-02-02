from flask import Flask, render_template, request,json,jsonify

app = Flask(__name__)

def get_user_data(user_id):
    with open('users.txt', 'r') as file:
        for line in file:
            user_data = json.loads(line)
            if user_data.get('user_id') == user_id:
                return user_data
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        user_data = {
            'name': name,
            'email': email,
            'password': password
        }
        with open('users.txt', 'a') as file:
            json.dump(user_data, file)
            file.write('\n')
            return "Registration successful!"
@app.route('/user/<int:user_id>')
def get_user(user_id):
        user_data = get_user_data(user_id)

        if user_data:
            return jsonify(user_data)
        else:
            return "User not found", 404

if __name__ == '__main__':
    app.run(debug=True)
