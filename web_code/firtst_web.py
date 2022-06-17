from flask import Flask ,render_template
app=Flask(__name__,template_folder='templates')#template_folder设置浏览的文件夹路径


#创建网址/show/info 和函数Index的对应关系
#访问网址/show/info，网站自动执行Index
@app.route("/show/info")
def index():
    # return "中国联通"#返回显示内容，由网页解析。
    #Flask内部会自动打开这个文件夹，并读取内容，将用户内容返回。
    #默认：去当前项目目录的templates文件夹中找
    return render_template("index.html")

@app.route("/get/news")
def get_news():
    return render_template("news.html")





if __name__=='__main__':
    app.run()
    # app.run(host="",post="")