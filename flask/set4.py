from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)
@app.route('/upload')
def upload_file():
   return render_template('set4.html')
@app.route('/file_upload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'		
if __name__ == '__main__':
   app.run(debug = True)
