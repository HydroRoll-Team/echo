# ES 1.0

## Term

> [!IMPORTANT]
> 
> Echo 标准只作用于多人聊天窗口(Window)。


### Window

窗口(Window)，一个能呼出水系骰子并能与之交互且能提供消息显示与聊天输入功能的窗体被称为聊天窗口，简称窗口。


### World

广义上，一个包含多个(至少两个)用户的聊天窗口即为一个 World(世界)。你可以将此类比为 QQ 平台的群聊(Group)或者 KOOK/Discord 平台的频道(Channel)——但是在(水系)这里，它们都统一被称为 World。

> [!WARNING]
>
> 单人群聊不能算作一个世界，即使此群聊有一个骰子且一个用户，也不能成为一个世界，只有用户量 >= 2 且能够与水系骰子交互时才算是一个世界。


### Sub-world/Main-world

狭义上讲，一个 World 应该在一段时间内只保持(也必须保持)一个规则包的绑定，因此类似于秘密团那样临时创建的分群或分频道并不能说是一个标准的 World，这类窗口我们称为 Sub-world(子世界)，因此当涉及到 Sub-world 时，我们不能说主群/主频道是一个 World，而应该说是 Main-world(主世界)。


### Nodes

Nodes(节点) 描述 ES 的实现端，这是它们的统一称谓。同时，通过 ES 所规定的 Events 传递的方向，可以扩展称为 1号节点(Node-1)、2号节点(Node-2) 甚至 3号节点(Node-3)、四号节点(Node4)...但是一般来说，两个节点已经足够使用了，Events 的传递方向总是由数字小的节点传递到数字大的节点再传回原数字较小的节点，这被成为一套完整的 pipeline。


### Pipeline

管线(Pipeline)，或称“流水线”。这个概念可能比较抽象，因此在这里给出一个生动的形容——Pipeline，你土味一点，可翻译成“一条龙服务”；专业一点，叫它“综合解决方案”。

总之，一个 pipeline，一定是完整的，但不一定是闭合的。


### Events

Events(事件)作用于从 World 侧转发端(例如 HydroRoll)传过来的一切以及将要从 ES 实现端(例如 HydroRol 或 Infini)发出(必须有响应)的一切。事件划分为 Specific-events(具体事件，例如消息事件、世界人数增减事件等) 与 Abstract-events(抽象事件，例如工作流事件、回调事件等)。具体可翻阅事件一览表[Events.md](./Events.md) 查看所有 ES 1.0 所支持的事件。


### Elements

Elements(元素)尤其指代包含在 Events 中的各类可以被抽象出来的概念，比如文本(Text)、图片(Image)、富文本(RichText)、音频(Audio)、视频(Vedio)等。具体可翻阅元素列表 [Elements.md](./Elements.md) 查看所有 ES 1.0 所定义的元素。


### API

是指节点(尤其是 Node-2)需要实现的一些网络接口规范。具体参阅 ES 1.0 API列表 [API.md](./API.md)。


### Without bells and whistles

没有花里胡哨的方法（不添加不必要，冗余的东西）。


### Off-the-shelf

已有的，现成的。

### end to end

端到端(e2e)，给定一个输入，再给出一个输出，不管其中的过程多么复杂，但只要给了一个输入，那么对应一个输出。

### Priority

优先级(priority)，作用在 Events 中，尤其是 [Workflow Events]()。