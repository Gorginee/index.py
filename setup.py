# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['indexpy',
 'indexpy.http',
 'indexpy.http.view',
 'indexpy.openapi',
 'indexpy.routing',
 'indexpy.websocket']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0',
 'pydantic>=1.6,<2.0',
 'python-multipart>=0.0.5,<0.0.6',
 'starlette>=0.13.6,<0.14.0']

extras_require = \
{':python_version < "3.8"': ['typing-extensions>=3.7.4,<4.0.0'],
 'full': ['gunicorn', 'requests>=2.24.0,<3.0.0', 'uvicorn'],
 'serve': ['gunicorn', 'uvicorn'],
 'test': ['requests>=2.24.0,<3.0.0']}

entry_points = \
{'console_scripts': ['index-cli = indexpy.cli:index_cli']}

setup_kwargs = {
    'name': 'index.py',
    'version': '0.16.1',
    'description': 'An easy-to-use high-performance asynchronous web framework.',
    'long_description': '<div align="center">\n\n<img style="max-width:60%;" src="https://raw.githubusercontent.com/abersheeran/index.py/master/docs/img/index-py.png" />\n\n<p>\n中文\n|\n<a href="https://github.com/abersheeran/index.py/tree/master/README-en.md">English</a>\n</p>\n\n<p>\n<a href="https://github.com/abersheeran/index.py/actions?query=workflow%3ATest">\n<img src="https://github.com/abersheeran/index.py/workflows/Test/badge.svg" alt="Github Action Test" />\n</a>\n\n<a href="https://app.codecov.io/gh/abersheeran/index.py/">\n<img alt="Codecov" src="https://img.shields.io/codecov/c/github/abersheeran/index.py">\n</a>\n</p>\n\n<p>\n<a href="https://github.com/abersheeran/index.py/actions?query=workflow%3A%22Publish+PyPi%22">\n<img src="https://github.com/abersheeran/index.py/workflows/Publish%20PyPi/badge.svg" alt="Publish PyPi" />\n</a>\n\n<a href="https://pypi.org/project/index.py/">\n<img src="https://img.shields.io/pypi/v/index.py" alt="PyPI" />\n</a>\n\n<a href="https://pepy.tech/project/index-py">\n<img src="https://static.pepy.tech/personalized-badge/index-py?period=total&units=international_system&left_color=black&right_color=blue&left_text=PyPi%20Downloads" alt="Downloads">\n</a>\n</p>\n\n<p>\n<img src="https://img.shields.io/pypi/pyversions/index.py" alt="PyPI - Python Version" />\n</p>\n\n一个易用的高性能异步 web 框架。\n\n<a href="https://index-py.abersheeran.com">Index.py 文档</a>\n\n</div>\n\n---\n\nIndex.py 实现了 [ASGI3](http://asgi.readthedocs.io/en/latest/) 接口，并使用 Radix Tree 进行路由查找。是[最快的 Python web 框架之一](https://github.com/the-benchmarker/web-frameworks)。一切特性都服务于快速开发高性能的 Web 服务。\n\n- 灵活且高效的路由系统 (基于 Radix Tree)\n- 自动解析请求 & 生成文档 (基于 [pydantic](https://pydantic-docs.helpmanual.io/))\n- 可视化 API 接口 (基于 ReDoc, 针对中文字体优化)\n- 自带一键部署命令 (基于 uvicorn 与 gunicorn)\n- 挂载 ASGI/WSGI 应用\n- 进程内后台任务 (基于 [asyncio](https://docs.python.org/3/library/asyncio.html))\n- 可使用任何可用的 ASGI 生态\n\n## Install\n\n```bash\npip install -U index.py\n```\n\n或者直接从 Github 上安装最新版本（不稳定）\n\n```bash\npip install -U git+https://github.com/abersheeran/index.py@setup.py\n```\n\n中国大陆内的用户可从 Coding 上的镜像仓库拉取\n\n```bash\npip install -U git+https://e.coding.net/aber/github/index.py.git@setup.py\n```\n\n## Quick start\n\n向 `main.py` 文件写入如下代码，使用 `pip install index.py uvicorn` 安装 `uvicorn` 和 `index.py`，接下来执行 `index-cli uvicorn main:app` 就可以启动一个高效的 Web 服务了。\n\n```python\nfrom indexpy import Index\nfrom indexpy.routing import HttpRoute\n\n\nasync def homepage(request):\n    return "hello, index.py"\n\n\napp = Index(\n    routes=[\n        HttpRoute("/", homepage, method="get"),\n    ]\n)\n```\n',
    'author': 'abersheeran',
    'author_email': 'me@abersheeran.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/abersheeran/index.py',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

