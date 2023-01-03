from flask import Flask, flash, redirect, render_template, request, url_for
import json

app = Flask(__name__)
app.secret_key = 'random string'

@app.route('/')
def main_page():
    return render_template("index.html")

@app.route('/admin')
def admin_page():
    password = request.values.get("password")
    if password == "12345678":
        with open('./data/user_data.json','r',encoding='utf8')as fp:
            return json.load(fp)
    return render_template("admin.html")

@app.route('/clear')
def clear_page():
    password = request.values.get("password")
    if password == "12345678":
        flash("清空成功")
        ept = dict()
        # ept = {None: None}
        with open('./data/user_data.json','w',encoding='utf8')as fp:
            json.dump(ept,fp,ensure_ascii=False)
        with open('./data/data.json','w',encoding='utf8')as fp:
            json.dump(ept,fp,ensure_ascii=False)
    return render_template("clear.html")

    

@app.route('/signup')
def new_user():
    with open('./data/user_data.json','r',encoding='utf8')as fp:
        user_data = json.load(fp)
    name = request.values.get("username")
    password = request.values.get("password")
    if name == None:
        return render_template("signup.html")
    elif name not in user_data:
        flash("注册成功")
        user_data[name] = password
        print(name)
    else:
        flash("此用户名已注册")
        return render_template("signup.html")
    with open('./data/user_data.json','w',encoding='utf8')as fp:
        json.dump(user_data,fp,ensure_ascii=False)
    return render_template("signup.html")

@app.route('/ask')
def ask_question():
    with open('./data/data.json','r',encoding='utf8')as fp:
        json_data = json.load(fp)
        # print(json_data)
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
        flash("用户不存在")
        return render_template("answer.html")
    if password == user_data[name] and name in json_data:
        flash("登录成功")
        return render_template("answer.html", questions=json_data[name])
    elif password != user_data[name]:
        flash("密码错误,请重试")
        return render_template("answer.html")
    else:
        flash('无问题')
        return render_template("answer.html")

app.run(host="0.0.0.0",port=81)