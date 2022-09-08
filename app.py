from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
  'ID:1,
  'Title':'Data Analyst',
  'Location':'Bengaluru'
  'Salary':'Rs.10,00,000'
},
  {
  'ID:2,
  'Title':'Data Scientist',
  'Location':'Pune'
  'Salary':'Rs.15,00,000'
},
  {
  'ID:3,
  'Title':'ML Engineer',
  'Location':'Remote'
  'Salary':'Rs.18,00,000'
},
  {
  'ID:4,
  'Title':'Front-End Engineer',
  'Location':'Remote'
  'Salary':'Rs.25,00,000'
}
]



@app.route("/")
def hello_world():
  return render_template('home.html',openings = JOBS)



if __name__ == "__main__":
    
  app.run(host='0.0.0.0',debug = True)

