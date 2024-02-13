from flask import Flask, request, render_template

# Flask constructor
app = Flask(__name__)

# Decorator that tells which url associated with this function
@app.route('/', methods=['GET', 'POST'])
def home():
    """ Home function"""
    if request.method == 'POST':
        name = request.form.get('name')
        place = request.form.get('place')
        
        return f'{name.capitalize()}, Welcome to {place}'
    return render_template('data.html')     

#Testing to check if it works
@app.route('/test')
def test():
    return "Works!"    

# Start the apllication
if __name__ == '__main__':
    app.run(host='localhost',port=5300,debug=True)


