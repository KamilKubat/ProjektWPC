import os, boto3
from flask import Flask, render_template, jsonify,request
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/")
def index():
  return render_template('upload_form.html', uploadButtonName="send")

@app.route("/upload", methods=['POST'])
def upload():
  files = request.files
  for f in files.getlist('file'):
    filename = f.filename
    bucket_name = '167244-kubat'
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    updir = '/home/ec2-user/s3-2/upload'
    f.save(os.path.join(updir, filename)) 
    bucket.put_object(Key='another.jpg', Body=open('/home/ec2-user/s3-2/upload/'+filename, 'rb'))
    #updir = 'album'
    #key = bucket.new_key(os.path.join(updir, filename))
    #key.set_contents_from_filename(filename)
    #key.set_acl('public-read') 
  return jsonify()

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

