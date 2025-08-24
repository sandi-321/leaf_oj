<h1>Leaf oj</h1>
<p>leaf oj是一个基于Django和Python的oj模板</p>
<p>你可以将leaf oj文件下载下来后，打开cmd窗口，并用cd指令切到leaf oj文件夹，然后输入命令</p>
<p><code>pip install --user virtualenv</code></p>
<p>这个指令可以安装virtualenv(ll_env)，然后输入指令</p>
<p><code>python -m venv ll_env</code></p>
<p>用来建立虚拟环境</p>
<p>建立虚拟环境后，我们需要激活它，输入指令</p>
<p><code>source ll_env/bin/activate</code></p>
<p>注意，如果你用的是Windows系统，需用指令</p>
<p><code>ll_env\Scripts\activate</code></p>
<p>然后我们就可以安装Django了，输入指令</p>
<p><code>pip install Django</code></p>
<p>我们要为leaf oj建立数据库，输入指令</p>
<p><code>python manage.py migrate</code></p>
<p>接下来创建管理员账户，输入指令</p>
<p><code>python manage.py createsuperuser</code></p>
<p>然后你就可以输入你想要的用户名，比如admin、sandi之类的</p>
<p>当你输入到密码的时候，你输入的密码会自动隐藏，不是因为显示问题或输不进去</p>
<p>最后输入指令</p>
<p><code>python manage.py runserver</code></p>
<p>这样就启动了你的网站，在浏览器里输入<a>http://127.0.0.1:8000</a>就可以访问你的网站</p>
<p>浏览器里输入<a>http://127.0.0.1:8000/admin</a>，然后登录你刚才输的管理员账户，就可以修改题目或添加题目了</p>
<h3><a href="https://www.bilibili.com/video/BV1he4y1w7wB">愿者上钩</a></h3>
