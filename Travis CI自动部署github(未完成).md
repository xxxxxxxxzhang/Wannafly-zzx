# Travis CI自动部署github



# 基础概念

## 什么是Travis CI

Travis CI是用Ruby语言开发的一个开源的分布式持续集成服务 （Continuous Integration，简称 CI） ，用于自动构建和测试在GitHub托管的项目。支持包括Javascript、Node.js、Ruby等20多种程序语言。对于开源项目免费提供CI服务。你也可以买他的收费版，享受更多的服务。

他绑定Github上面的项目，只要有了新的代码，就会自动抓取。然后，提供一个运行环境，测试执行测试、完成构建，还能部署到服务器。

持续集成指的是只要代码有变更，就自动运行构建和测试，反馈运行结果。确保符合预期以后，再将新代码"集成"到主干。

持续集成的好处在于，每次代码的小幅变更，就能看到运行结果，从而不断累积小的变更，而不是在开发周期结束时，一下子合并一大块代码。

#### 需要拥有一下条件，才能使用Travis CI

* 拥有 GitHub 帐号
* 该帐号下面有一个项目
* 该项目里面有可运行的代码
* 该项目还包含构建或测试脚本

## 步骤

首先，访问官方网站 [travis-ci.org](https://travis-ci.org/)，点击右上角的个人头像，使用 Github 账户登入 Travis CI。

Travis 会列出 Github 上面你的所有仓库，以及你所属于的组织。此时，选择你需要 Travis 帮你构建的仓库，打开仓库旁边的开关。一旦激活了一个仓库，Travis 会监听这个仓库的所有变化。



# 参考链接

[持续集成服务 Travis CI 教程]( http://www.ruanyifeng.com/blog/2017/12/travis_ci_tutorial.html )

[利用Travis CI+GitHub实现持续集成和自动部署]( https://juejin.im/post/5d95bfa3e51d4578034d2d8a#heading-6 )