### Learnt
1. flask扩展在extend_name(app)时，进行了“初始化”
    > 对bootstrap来说，它可能修改了app设置里的tempalte的路径，
    > 使得base.html可以通过extend bootstrap/base.html来继承
    > 并且，向所有模板传入对应的类，就像把这个类通过render_template传入一样
    > 可以做一些很棒的事
2. {% block block_name %}{% endblock %}是一种占位符
    > 可以继承别的模板后继续添加
    > 如果在原有的基础上修改——模板可以设置占位，也能往占位里面预填一些东西
    > 需要来一行{{ super() }}，再在下面（上面？好像也行）添加

3. navie time（纯正时间）指不包含时区的时间戳，对应的是aware time（细致时间戳）
    > datetime.utcnow()是纯正时间

4. flask的表单在py中定义（继承Form/FlaskForm）,然后通过render_template传送
    > 有意思的是，如果在模板中用form接受Form的实例，form标签不会受到影响

5. 视图函数在修饰时，如果没有设置，methods当作GET处理

6. 表单提交使用重定向比较管用，重定向貌似只能使用GET方法

7. 用session来保存数据实在是太方便了

8. flash需要渲染才能出现，之前没有渲染，在base.html加入渲染设置后，出现了三个flash块
    > 存在消息队列？
9. get_flashed_messages()可在jinja中直接处理flash




### Question
1. extend_name(app)过程中做了哪些事？extend_name直接出现在jinja模板中是为什么？

2. url_for可以直接在jinja模板中使用，为什么？

3. 什么是CSRF攻击?

4. 看bootstrap/wtf.htm源码

5. form.validate_on_submit()验证表单的有效性（验证哪些？）

6. 以post方法传来的form是如何被视图函数接受的？

7. 提交空表单会被验证函数Required()捕捉，这个函数由谁提提供，是如何其作用的？

8. 按狗书4.5的方法构建session，但是关闭页面再打开，会出现"IOError: [Errno 32] Broken pipe"，
   什么原因？

9. session是如何实现有状态通讯的？

10. 狗书4.6中正常输入一次后关闭flask与网页（单页），接着重启并访问，仍有状态为什么？

11. get_flashed_messages()哪来的，flask中还有哪些可以直接用于jinja的函数

### wait_for_learn
1. jinja中变量的过滤函数

2. moment的更多用法

3. flask中的session
