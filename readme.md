### blog_site

*   前後端完全分離，通過restapi接口通信，前端使用vue2.0 框架

*   良好的代碼組織結構以及工程实践

*   一鍵安裝所有系統依賴以及python依賴

*   uwsgi配置和nginx配置支持模板變量

*   使用nose 和 factory 寫測試用例, 覆蓋所有API

*   使用.env 文件，方便多環境部署, 屏蔽敏感配置

*   使用sphinx生成api文檔

*   使用gitflow分支管理策略

#### Configuration

* Clone this project

        git clone https://github.com/drinksober/blog.git

* Create the virtual environment by using the `VirtualEnv`.

        pip install virtualenv                   #install virtualenv
        virtualenv -p blog ENV       #create the virtualenv for project
        cd blog                               #enter the software directory
        source /blog/bin/activate    #activate the virtualenv 


*  Install `Django and the deepdency.`

    cd utility

    ./install_os_dependencies.sh

    ./install_python_dependencies.sh
