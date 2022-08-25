from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template("index.html")

@app.route('/signup')
def new_user():
    with open('./data/user_data.json','r',encoding='utf8')as fp:
        user_data = json.load(fp)
    name = request.values.get("username")
    password = request.values.get("password")
    if name not in user_data:
        user_data[name] = password
    else:
        return render_template("error.html")
    with open('./data/user_data.json','w',encoding='utf8')as fp:
        json.dump(user_data,fp,ensure_ascii=False)
    return render_template("signup.html")

@app.route('/ask')
def ask_question():
    with open('./data/data.json','r',encoding='utf8')as fp:
        json_data = json.load(fp)
        print(json_data)
        # print(type(json_data))
    name = request.values.get("username")
    question = request.values.get("question")
    if name not in json_data:
        json_data[name]=[]
    json_data[name].append(question)
    with open("./data/data.json",'w',encoding='utf8') as fp:
        json.dump(json_data,fp,ensure_ascii=False)
    return render_template("ask.html")

@app.route('/answer')
def answer_question():
    with open('./data/data.json','r',encoding='utf8')as fp:
        json_data = json.load(fp)
    with open('./data/user_data.json','r',encoding='utf8')as fp:
        user_data = json.load(fp)
    name = request.values.get("username")
    password = request.values.get("password")
    if name == None:
        return render_template("answer.html")
    if name not in user_data:
        return render_template("error.html")
    if password == user_data[name]:
        return render_template("answer.html", questions=json_data[name])
    else:
        return render_template("password_error.html")

app.run(host="0.0.0.0",port=80)
