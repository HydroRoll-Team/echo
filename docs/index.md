# 一、Echo 规范

ES 1.0.0 是 Echo 规范的第一个投入生产环境的版本，而 Echo 是水系规定 HydroRoll 与 infini 之间事件传参类型的一个内部标准，全称 Event Communication and Harmonization across Online platforms。

## 1.1 版本 1.0.0

文档里的关键词 "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" 都遵循 [BCP 14]、[RFC2119]、[RFC8174] 里的解释说明。

[BCP 14]: https://www.rfc-editor.org/info/bcp14
[RFC2119]: https://datatracker.ietf.org/doc/html/rfc2119
[RFC8174]: https://datatracker.ietf.org/doc/html/rfc8174


# 二、介绍

Echo 规范（ES），是定义一个标准的、与具体编程语言无关的 RESTful API 与 Event Defined 规范。文字跑团(TRPG)游戏是一种基于文字描述和角色扮演的桌上游戏，通常由一个游戏主持人(KP)和多个玩家(PC)组成，通过网络平台进行交流和互动。不同的平台可能有不同的功能和限制，比如群聊、频道、图片、音频甚至视频等，这些都会影响到游戏的体验和效果。为了让水系的文字跑团游戏能够跨平台运行，ES 规定了游戏的数据结构、接口定义、错误处理等。这样，水系用户的 TRPG 游戏就可以在不同的平台上实现相同或相似的功能，同时也可以方便模型或规则包或插件开发者进行扩展和定制。


# 三、术语定义

## 3.1 ES 文档

一（或多）份用来定义或描述一个 Event 以及 API 的文档。

## 3.2 Media Types

媒体类型定义分散于多处。 媒体类型定义应当符合RFC6838。

以下是一些媒体类型定义的示例：

```
text/plain; charset=utf-8
  application/json
  application/vnd.github+json
  application/vnd.github.v3+json
  application/vnd.github.v3.raw+json
  application/vnd.github.v3.text+json
  application/vnd.github.v3.html+json
  application/vnd.github.v3.full+json
  application/vnd.github.v3.diff
  application/vnd.github.v3.patch
```

## 3.3 HTTP状态码

HTTP状态码被用来表示一次请求的被执行状态。[RFC7231] 定义了有效的状态码，可以在 [IANA Status Code Registry] 找到已经被注册的状态码的列表。

[RFC7231]: http://tools.ietf.org/html/rfc7231#section-6
[IANA Status Code Registry]: http://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml

## 3.4 其他术语

包含 Window、World、Event、Element等词条，详见 [Term.md](./Term.md)。


# 四、规范

## 版本

开放 API 规范使用符合[语义化版本 2.0.0](http://semver.org/spec/v2.0.0.html)(semver)规范的版本号。版本号由三部分组成：主版本号.次版本号.修订号。每次更新文档时，根据以下规则递增版本号：
* 主版本号：当 API 有不兼容的修改时，递增主版本号，例如从 1.0.0 变为 2.0.0。
* 次版本号：当 API 有向下兼容的功能新增时，递增次版本号，例如从 1.0.0 变为 1.1.0。
* 修订号：当 API 有向下兼容的问题修正时，递增修订号，例如从 1.0.0 变为 1.0.1。
支持开放API规范 1.0 的工具应该兼容所有 1.0.* 的版本，工具不应当关注修订版本号，比如 1.0.0 和 1.0.1 对它来说应该没有任何区别。

此后开放 API 规范的相同主版本号下更高次要版本的发布不应当对面向低于此次要版本号开发的工具的造成干扰。因此 1.1.0 版本的规范应当可以在面向 1.0.0 版本规范开发的工具内使用。

任何兼容开放 API 规范 1.*.* 的文档应当包含一个 echo 字段用来表明它使用的规范的语义化版本。
