from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/ninja')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:vari>')
def multi(vari):
    return f'Hi {vari}'

@app.route('/repeat/<int:num>/<string:vari>')
def repeat(vari, num):
    if(vari and num):
      return f'{vari * num}'
    else:
      return 'Sorry! No response. Try again.'

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.