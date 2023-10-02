from flask import Flask, flash, redirect, render_template, request, url_for
import json
import requests
from flask_bootstrap import Bootstrap

ipad_id = "ZHCbdfdMeqWdGtKNybrfyg"


def push_content(code, str):
    # /: key /: category /: title /: body
    r = requests.get(
        "https://api.day.app/"+code+"/fake-tapechat提问/"+str+"?icon=https://kyoukawa.github.io/images/icon.png&automaticallyCopy=1")
    # r = requests.get("https://api.day.app/"+code+"/"+str)
    print(r)


def create_app():
    app = Flask(
        import_name=__name__,
        static_folder='static',
        template_folder='templates'
    )
    Bootstrap(app)

    return app


app = create_app()

app.secret_key = 'random string'


@app.route('/')
def main_page():
    return render_template("index.html")
    # 主页


@app.route('/help')
def help_page():
    return render_template("help.html")
    # 帮助


@app.route('/admin')
def admin_page():
    return render_template("admin_index.html")


@app.route('/data')
def data_page():
    with open('./data/admin.json', 'r', encoding='utf8')as fp:
        admin_data = json.load(fp)
        # 获取admin信息
    with open('./data/user_data.json', 'r', encoding='utf8')as fp:
        user_data = json.load(fp)
        # 用户信息
    if admin_data == {}:
        # 无admin
        flash("无管理员请注册")
        name = request.values.get("username")
        password = request.values.get("password")
        # 获取账号密码
        if name == None:
            # 账号为空
            return render_template("data.html")
        admin_data[name] = password
        # 注册
        with open('./data/admin.json', 'w', encoding='utf8')as fp:
            json.dump(admin_data, fp, ensure_ascii=False)
            # 保存到数据
        flash("注册成功")

    # 有admin
    name = request.values.get("username")
    password = request.values.get("password")
    # 获取账号密码
    if name == None:
        # 账号为空
        return render_template("data.html")
    elif name not in admin_data:
        flash("用户不存在于管理员列表")
        return render_template("data.html")
    elif password == admin_data[name]:
        # 密码正确
        # flash("登录成功")
        print(user_data)
        print(user_data.values())
        return render_template("data.html", usr=user_data, pwd=user_data.values())

    else:
        flash("密码错误")
    return render_template("data.html")


@app.route('/clear')
def clear_page():
    with open('./data/admin.json', 'r', encoding='utf8')as fp:
        admin_data = json.load(fp)
    if admin_data == {}:
        flash("无管理员请注册")
        name = request.values.get("username")
        password = request.values.get("password")
        if name == None:
            return render_template("data.html")
        admin_data[name] = password
        with open('./data/admin.json', 'w', encoding='utf8')as fp:
            json.dump(admin_data, fp, ensure_ascii=False)
        flash("注册成功")
    name = request.values.get("username")
    password = request.values.get("password")
    if name == None:
        return render_template("clear.html")
    elif name not in admin_data:
        flash("用户不存在")
        return render_template("clear.html")
    elif password == admin_data[name]:
        flash("清空完成")
        ept = dict()
        # ept = {None: None}
        with open('./data/user_data.json', 'w', encoding='utf8')as fp:
            json.dump(ept, fp, ensure_ascii=False)
        with open('./data/data.json', 'w', encoding='utf8')as fp:
            json.dump(ept, fp, ensure_ascii=False)
    return render_template("clear.html")


@app.route('/signup')
def new_user():
    with open('./data/user_data.json', 'r', encoding='utf8')as fp:
        user_data = json.load(fp)
        # 获取已注册用户信息
    name = request.values.get("username")
    password = request.values.get("password")
    # 获取账号密码
    if name == None:
        # 账号为空
        return render_template("signup.html")
    elif password == None:
        flash("请设置密码")
        return render_template("signup.html")
    elif name not in user_data:
        flash("注册成功")
        user_data[name] = password
        # 注册
        # print(name)
    else:
        # 用户名重复
        flash("此用户名已注册")
        return render_template("signup.html")
    with open('./data/user_data.json', 'w', encoding='utf8')as fp:
        json.dump(user_data, fp, ensure_ascii=False)
        # 保存
    return render_template("signup.html")


@app.route('/ask')
def ask_question():
    with open('./data/user_data.json', 'r', encoding='utf8')as fp:
        user_data = json.load(fp)
    with open('./data/data.json', 'r', encoding='utf8')as fp:
        json_data = json.load(fp)
        # 获取问题信息
        # print(json_data)
        # print(type(json_data))

    name = request.values.get("username")
    question = request.values.get("question")
    # 获取用户名和问题

    if name == None:
        return render_template("ask.html")

    elif name not in user_data:
        flash("用户不存在")
        return render_template("ask.html")

    elif name not in json_data:
        json_data[name] = {}
        # 用户无问题,初始化字典

    json_data[name][question] = ""
    # 创建提问

    with open("./data/data.json", 'w', encoding='utf8') as fp:
        json.dump(json_data, fp, ensure_ascii=False)
        # 保存

    push_content(ipad_id, question)
    #  向被提问者发通知

    return render_template("ask.html")


@app.route('/check')
def check():
    with open('./data/data.json', 'r', encoding='utf8')as fp:
        json_data = json.load(fp)
    with open('./data/user_data.json', 'r', encoding='utf8')as fp:
        user_data = json.load(fp)
    name = request.values.get("username")

    if name == None:
        return render_template("check.html")
    elif name not in user_data:
        flash("用户不存在")
        return render_template("check.html")
    elif name not in json_data:
        flash("无问题")
        return render_template("check.html")
    else:
        print(json_data[name])
        print(json_data[name].values())
        return render_template("check.html", questions=json_data[name], answers=json_data[name].values())


@app.route('/answer')
def answer_question():
    with open('./data/data.json', 'r', encoding='utf8')as fp:
        json_data = json.load(fp)
    with open('./data/user_data.json', 'r', encoding='utf8')as fp:
        user_data = json.load(fp)
    # 加载json
    name = request.values.get("username")
    password = request.values.get("password")
    question = request.values.get("question")
    answer = request.values.get("answer")
    # 获取信息(自己看英文)
    if name == None:
        # 没输入name
        return render_template("answer.html")
    elif name not in user_data:
        flash("用户不存在")
        return render_template("answer.html")
    elif password == user_data[name] and name in json_data:
        flash("登录成功")
        if question in json_data[name]:
            flash("回答成功")
            # print(json_data[name][question])
            json_data[name][question] = answer
            # print(json_data[name][question])
            with open("./data/data.json", 'w', encoding='utf8') as fp:
                json.dump(json_data, fp, ensure_ascii=False)
            return render_template("answer.html")
        else:
            flash("此问题不存在")
            return render_template("answer.html")

    elif password != user_data[name]:
        flash("密码错误,请重试")
        return render_template("answer.html")
    else:
        return render_template("answer.html")


app.run(host="0.0.0.0", port=81)  # 运行于机器所有ip上81端口
