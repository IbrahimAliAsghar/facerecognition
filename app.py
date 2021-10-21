from flask import Flask,request
from deepface import DeepFace

app = Flask(__name__)





@app.route("/verify",methods=['POST'])
def hello():
    
   # print(request.form.get('base1'))
    base1 = request.form.get('base1')
    base2 = request.form.get('base2')

    return DeepFace.verify(base1, base2,model_name='Facenet')


if __name__ == "__main__":
  app.run()