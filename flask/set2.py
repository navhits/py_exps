from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
   return render_template(‘set2.html’)
if __name__ == '__main__':
   app.run()
