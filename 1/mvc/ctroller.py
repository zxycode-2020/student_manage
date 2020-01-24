#coding:utf8
import jinja2

def index():
    with open('views/index.html','r') as f:
        html = f.read()  # 获取模板内容
        tpl = jinja2.Template(html) # 传入jinja2模板引擎 返回模板对象

        articles = [
            ('文章1标题','文章1内容'),
            ('文章2标题','文章2内容')

        ]
        html = tpl.render(user='苏格拉底',articles=articles) # 渲染完的html内容
        return html.encode('utf-8')

def article():
    with open('views/article.html','r') as f:
        html = f.read()
        tpl = jinja2.Template(html)
        html = tpl.render(title='文章标题',content='文章内容')
        return html.encode('utf-8')

def article_list():
    return 'article list page ok'