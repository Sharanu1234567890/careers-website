from re import DEBUG
from flask import Flask,render_template

app=Flask(__name__)
Jobs=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bengaluru,India',
    'slary':'Rs.10,00,000'
  },
  
    {
      'id':2,
      'title':'sde',
      'location':'Bengaluru,India',
      'slary':'Rs.13,00,000'
    },
  {
    'id':1,
    'title':'Data scientist',
    'location':'Bengaluru,India',
    'slary':'Rs.10,00,000'
  }
]
@app.route("/")
def hello_world():
  return render_template("home.html",Jobs=Jobs)
if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True)
# print("hello wolrd")
