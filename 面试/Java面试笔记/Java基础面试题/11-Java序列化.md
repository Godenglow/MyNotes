---
tags:
  - Java
  - 面试
  - 序列化
  - 分布式
source: 小林coding《300道+Java面试题》
date: 2026-09-15
---

# Java 序列化

> [!question] 疑问
> 序列化和反序列化是什么？怎么把一个对象从一个 JVM 转移到另一个 JVM？让你自己实现序列化怎么办？

## 一图看懂

![[Java序列化.svg]]

## 一句话定义

**序列化**：把内存中的对象转换成一串可以存储或传输的**字节流**的过程；**反序列化**：逆过程——从字节流把对象**重新构造**回内存。

```
内存对象 --序列化--> 字节流 --> 文件 / 网络 / 缓存 / 数据库
内存对象 <--反序列化-- 字节流 <--（从上面某处读回）
```

> [!important] 关键认知
> 序列化解决的是**"进程边界"和"时间边界"**的问题。对象只活在某个 JVM 堆里、只活在这次进程运行期间；一旦要跨出这两个边界（发给别的机器、存到磁盘），就必须先变成字节。

比喻：对象是宅家的人，序列化是**打包**，传输是**快递**，反序列化是**拆包复原**。包里必须写清"这是什么类"（元信息）和"里面各是什么值"，对方才能原样复原。

## 为什么需要：四个真实场景

| 场景 | 说明 |
| --- | --- |
| 持久化 | 对象存到文件/磁盘，下次启动读回来 |
| 网络传输 / RPC | 分布式调用要把参数和返回值发到另一台机器（RMI、Dubbo/Hessian）；HTTP 请求体里的 JSON 也是序列化的一种 |
| 缓存 / Session | 对象塞进 Redis、Memcached，或 Web 容器的 session 共享，必须先变成字节 |
| 深拷贝 | 序列化再反序列化，能得到完全独立的新对象（见 [[04-深拷贝与浅拷贝]]） |

## Java 原生实现（三步）

```java
public class Person implements Serializable {          // 1. 实现标记接口
    private static final long serialVersionUID = 1L;   // 2. 显式版本号
    private transient String password;                 // 3. 敏感字段不打包
    private String name;
    private int age;
}

// 序列化
ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("p.bin"));
oos.writeObject(person);

// 反序列化
ObjectInputStream ois = new ObjectInputStream(new FileInputStream("p.bin"));
Person p = (Person) ois.readObject();
```

只有实现了 `Serializable` 或 `Externalizable` 接口的类才能被序列化，否则抛 `NotSerializableException`。

### 三个必须懂的细节

1. **`Serializable` 是空接口（标记接口）**，没有任何方法，纯粹是给 JVM 的"允许打包"标记，检查逻辑在 `writeObject` 内部。
2. **`serialVersionUID` 是版本号**：反序列化时校验字节流里的版本和当前类是否一致，不一致抛 `InvalidClassException`。不写则 JVM 根据类结构自动生成——**类一改（哪怕加个字段）旧字节流就作废**，所以必须显式声明。
3. **`transient` 字段不参与序列化**，反序列化后是默认值（null/0）；**`static` 字段也不序列化**（属于类不属于对象）。父子类继承时，父类也要实现 `Serializable`，否则父类字段不会被序列化。

## Java 原生序列化的三大缺陷（为什么不建议生产使用）

1. **无法跨语言**：字节流格式是 Java 私有协议，Go/Python 等其他语言解析不了
2. **性能差、体积大**：流里携带大量类元信息
3. **安全漏洞**：`readObject()` 反序列化时执行类逻辑，历史上有大量**反序列化攻击**（构造恶意字节流实现远程代码执行）

主流替代方案：

| 方案 | 特点 | 典型使用 |
| --- | --- | --- |
| JSON（Jackson / Fastjson） | 文本格式、人类可读、跨语言 | HTTP 接口 |
| Protobuf | 二进制、体积小、跨语言、需写 IDL | gRPC |
| Hessian | 二进制、比原生小 | Dubbo |
| Kryo | 高性能但仅 Java | 内部框架 |

## 怎么把对象从一个 JVM 转移到另一个 JVM（四种方式）

1. **序列化 + 网络传输**：对象变成字节流，通过网络套接字发送，对端反序列化恢复
2. **消息队列**（RabbitMQ / Kafka）：把传输托管给中间件，附带削峰、解耦、异步
3. **RPC 框架**（gRPC / Dubbo）：把"调用远程方法"封装得像本地调用，序列化藏在框架里
4. **共享存储**（MySQL / Redis）：不直接传对象，双方读写同一份数据——适合共享数据而非直接传输的场景

## 让你自己实现序列化会怎么做？（开放设计题）

思路和 class 文件一致——**先定义协议，再做编解码**：

1. 定义字节流格式：`魔数 + 版本 + 类元信息（类名/字段名/字段类型）+ 各字段值`
2. 编码器：反射读出对象的结构和值，按协议写出字节
3. 解码器：按协议读回元信息和字段值，反射重建对象
4. 优化方向：压缩、字段编号代替字段名（Protobuf 的核心思想）、变长整数编码

> [!tip] 记忆锚点
> **对象出堆，先变成字节。** 序列化 = 打包（按协议把类和字段值写成字节流），反序列化 = 拆包（校验版本号后按协议重建）。Java 原生那套只适合演示，生产上 JSON 走接口、Protobuf 走 RPC。

> [!note] 关联
> 与 [[05-Java创建对象的方式]] 的"反序列化创建对象"呼应——反序列化**不调用构造器**，因此能破坏单例（防御手段 `readResolve()`）；与 [[04-深拷贝与浅拷贝]] 的"序列化实现深拷贝"呼应。
