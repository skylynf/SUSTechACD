# CS304 SUSTech_ACD 经费管理系统 Final Report





## 1.	Metrics



## 2.	Documentation

Documentation分为用户端文档和开发者文档两个部分。

### User-end document

#### SUSTech ACD 经费管理系统 - 用户端使用文档

URL: https://github.com/skylynf/SUSTechACD/blob/main/%E7%94%A8%E6%88%B7%E7%AB%AF%E6%96%87%E6%A1%A3.pdf

上述文档是一个用户端使用文档的示例，它旨在帮助用户理解和操作系统的各个功能模块。该文档提供了以下内容：

1. **简介**：介绍了系统的基本概念，如课题组、经费和支出之间的关系，以及一些限制条件。
2. **操作列表**：列出了用户可以执行的各种操作，包括查询、审批、增加/删除、修改等。
3. **用户使用内容**：描述了用户在系统中的角色和相关操作，包括登录、注册、导航栏功能和各个模块的具体功能。
4. **导出功能**：说明了用户可以使用导出功能将生成的Excel表格导出的方法。

整个文档结构清晰，按照不同功能模块分别进行介绍，并提供了具体的操作步骤和注意事项。文档旨在帮助用户快速上手系统，了解每个功能的用途和操作方法，以提高用户的使用体验。

##### 目录

1. 登录和注册
2. 导航栏功能说明
3. 展示模块
4. 支出模块
5. 经费模块
6. 审批模块
7. 导出功能



#### Screenshot

>![image-20230530133720531](D:\CS304\final\SUSTechACD\FinalReport-Pictures\image-20230530133720531.png)



### Developer-end document

URL: https://github.com/skylynf/SUSTechACD/blob/main/Project%20API%20Document.pdf

这份文档是SUSTech_ACD API开发者文档，用于介绍SUSTech_ACD财务管理系统的API接口及其使用方法。该系统用于管理课题组的经费和支出情况。

以下是文档的目录：

1. 简介
2. 操作列表
   - 总览
     - 查询某课题组名下的全部经费的完成情况（支出情况）
     - 查询一笔支出的申请情况
     - 可视化查看一笔经费的使用情况和支出项目
     - 查询若干个fundID的使用情况和执行率
   - 审批
     - 查询待审批的所有支出列表
     - 审批支出
   - 增加/删除
     - 增加或删除一个经费
     - 增加或删除一个支出
   - 修改
     - 修改一个支出并重新送审
     - 修改一个经费
3. Json对象内容示例
   - 经费（fund）
   - 支出（expense）
   - 课题组（user）
4. 后端API
   - 获取课题组全部经费完成情况（支出情况）
   - 查询若干个fundID的使用情况和执行率，或是所有fundID的使用情况和执行率
   - 查询一笔支出的申请情况
   - 查询待审批的所有支出列表
   - 增加或删除一个经费
   - 增加或删除一个支出
   - 送审一个支出
   - 修改一个支出并重新送审
   - 修改一个经费
   - 用户操作
     - 增加用户
     - 修改用户
     - 删除用户
     - 用户登录
5. 注意事项

该文档提供了系统中各种操作的API接口说明，包括请求方式、路径、参数和响应等信息。开发者可以根据文档中的接口定义和示例，进行后端API的实现和功能完善。此外，文档还提供了一些注意事项，如占位符替换和后端实现建议等。



#### ScreenShot

> ![image-20230530135415322](D:\CS304\final\SUSTechACD\FinalReport-Pictures\image-20230530135415322.png)





## 3.	Tests



## 4.	Build



### Front-end Build (Vue.js):

1. Technology/Tools/Frameworks:

   - Node.js: JavaScript runtime used to execute build scripts and manage dependencies.
   - npm (Node Package Manager): Used to install and manage project dependencies.
   - Vue CLI (Command-Line Interface): A development tool for scaffolding and managing Vue.js projects.

2. Tasks executed in the build and final artifacts produced:

   - Installation of project dependencies: This includes Vue.js itself and any additional libraries or packages required by your project.

   - Compilation and bundling of front-end assets: The build process compiles Vue.js components, CSS styles, and other static assets into optimized and minified files.

   - Generation of production-ready artifacts: The final output typically includes HTML, CSS, and JavaScript files that can be served by a web server.

   - ```shell
     npm install
     npm run dev
     ```

3. Buildfile or related artifacts/scripts:

   - Vue CLI generates a configuration file called `vue.config.js` in project's root directory. This file can be customized to modify the build process, configure webpack, and handle other build-related tasks. 

   - Find more information about `vue.config.js` in the Vue CLI documentation: [Vue CLI Configuration Reference](https://cli.vuejs.org/config/).

   - URL of  `vue.config.js` :https://github.com/skylynf/SUSTechACD/blob/main/vue.config.js

   - Part of Snapshot:

     >  ![image-20230530141327691](D:\CS304\final\SUSTechACD\FinalReport-Pictures\image-20230530141327691.png)

   - The `package.json` file is a manifest file that contains metadata about your project and its dependencies. It is also used to define various scripts that can be executed using npm.

   - URL of `package.json` : https://github.com/skylynf/SUSTechACD/blob/main/vue.config.js

   - Part of Snapshot:

     >![image-20230530141136952](D:\CS304\final\SUSTechACD\FinalReport-Pictures\image-20230530141136952.png)



### Back-end Build (Python Flask):

1. Technology/Tools/Frameworks:

   - Python: Programming language used for back-end development.
   - pip: Package installer for Python used to manage project dependencies.
   - Flask: Micro web framework for Python used to build the back-end server.

2. Tasks executed in the build and final artifacts produced:

   - Dependency installation: Installation of required Python packages, including Flask and any additional libraries.

   - Configuration and setup: The build process might involve setting up environment variables, configuring the database connection, and other initialization steps.

   - ```shell
     pip install
     python -m flask run
     ```

3. Buildfile or related artifacts/scripts:

   - In Python Flask projects, build scripts are typically not as standardized as in front-end frameworks. 





## 5.	Deployment


