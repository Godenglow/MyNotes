---
tags:
  - Java
  - 面试
  - 对象创建
  - 反射
source: 小林coding《300道+Java面试题》P35-38
date: 2026-09-15
---

# Java 创建对象的方式

> [!question] 疑问
> Java 创建对象有哪些方式？哪些会调用构造器？

## 一图看懂

![[Java创建对象的方式.svg]]

## 五种方式

**1. new 关键字** —— 最常见、最基础的方式，编译期就确定类，通过调用构造器实例化：

```java
Person p = new Person("大山");
```

**2. 反射：`Class.newInstance()`** —— 运行时动态创建，不需要在编译时知道具体的类：

```java
MyClass obj = (MyClass) Class.forName("com.example.MyClass").newInstance();
```

> [!warning] `Class.newInstance()` 在 JDK 9 后被标记为过时
> 因为它只能调用无参公有构造器，且会把受检异常原样抛出。推荐用 `Constructor.newInstance()`，更强大、更灵活。
>
> ```java
> Constructor<MyClass> constructor = MyClass.class.getConstructor();
> MyClass obj = constructor.newInstance();
> ```

**3. `clone()`** —— 实现 `Cloneable` 接口并重写 `Object.clone()`，基于一个现有对象（原型）创建副本，详见 [[04-深拷贝与浅拷贝]]。

**4. 反序列化** —— 通过 `ObjectInputStream` 从字节流（文件或网络）中重建对象，类必须实现 `Serializable`：

```java
ObjectInputStream ois = new ObjectInputStream(new FileInputStream("person.txt"));
Person p = (Person) ois.readObject();
```

**5. 工厂模式** —— 不直接 `new`，通过一个方法返回对象实例，`getInstance()`、`valueOf()` 都是常见的静态工厂方法。构造器可以设为 `private`，方法内部可以加缓存、日志、返回子类实例等额外逻辑（Spring 的 BeanFactory 就是这一思想）。

## 面试关键：哪些方式不调用构造器

| 方式 | 是否调用构造器 |
| --- | --- |
| new 关键字 | 调用 |
| 反射（`Constructor.newInstance()`） | 调用 |
| 工厂方法 | 调用（只是藏在方法内部） |
| `clone()` | **不调用** |
| 反序列化 | **不调用** |

> [!tip] 由此引出的经典追问
> `clone()` 和反序列化**绕过构造器**，所以它们能破坏单例模式：
>
> - 防克隆：单例类重写 `clone()` 直接抛异常
> - 防反序列化破坏：在单例类里加 `readResolve()` 方法，返回已有实例
> - 静态内部类单例、枚举单例天然免疫（枚举的反序列化由 JVM 特殊处理），见 [[03-static关键字与内部类]]
