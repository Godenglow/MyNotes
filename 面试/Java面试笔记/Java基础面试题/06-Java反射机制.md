---
tags:
  - Java
  - 面试
  - 反射
  - Class对象
source: 小林coding《300道+Java面试题》P39-40
date: 2026-09-15
---

# Java 反射机制

> [!question] 疑问
> 什么是反射？反射在你平时写代码或框架中的应用场景有哪些？

## 一图看懂反射的原理

![[Java反射机制.svg]]

**关键认知：类加载后，JVM 会在堆里为每个类生成一个唯一的 `Class` 对象**（它和该类的实例对象是两回事）。反射的一切能力都来自拿到这个 `Class` 对象——它就像一张类的"说明书"，拿着说明书就能查看类里有什么、并反向操控实例。

## 什么是反射

Java 反射机制是在**运行状态**中：

- 对任意一个类，都能知道这个类的所有属性和方法
- 对任意一个对象，都能调用它的任意方法和属性

这种**动态获取信息**以及**动态调用对象方法**的功能称为 Java 语言的反射机制。

## 四个特性

1. **运行时类信息访问**：获取类的完整结构——类名、包名、父类、实现的接口、构造函数、方法和字段等
2. **动态对象创建**：编译时不知道类名也能创建实例（`Class.newInstance()` / `Constructor.newInstance()`），见 [[05-Java创建对象的方式]]
3. **动态方法调用**：通过 `Method.invoke(对象, 参数)` 运行时调用方法，包括私有方法
4. **访问和修改字段值**：通过 `Field.get()` / `set()` 读写对象字段，包括私有字段

## 基本用法

```java
// 获取 Class 对象的三种方式
Class<Person> c1 = Person.class;                    // 1. 类字面量
Class<?> c2 = Class.forName("com.example.Person");  // 2. 全类名（最常用）
Class<?> c3 = person.getClass();                    // 3. 实例的 getClass()

// 暴力访问私有成员
Field nameField = c1.getDeclaredField("name");
nameField.setAccessible(true);   // 突破 private 限制
nameField.set(person, "大山");

// 反射调用方法
Method m = c1.getDeclaredMethod("sayHello");
m.setAccessible(true);
m.invoke(person);
```

## 应用场景（面试重点）

1. **Spring IOC 容器**：根据配置的全类名字符串，反射创建 Bean 并依赖注入——反射最典型的应用
2. **加载数据库驱动**：底层用 MySQL 还是 Oracle，根据配置动态加载驱动类 `Class.forName("com.mysql.cj.jdbc.Driver")`
3. **动态代理**：`Proxy.newProxyInstance()` + `InvocationHandler`，AOP 切面的底层就是动态代理 + 反射调用
4. **序列化/反序列化框架**：Jackson、Fastjson 通过反射读写对象的字段
5. **MyBatis**：把数据库列名映射到实体类字段、动态调用 Mapper 接口
6. **JUnit**：扫描 `@Test` 注解的方法并反射调用

## 反射的缺点（说了应用最好能说出代价）

- **性能开销**：方法查找、参数装箱、安全检查，比直接调用慢一个数量级
- **破坏封装**：`setAccessible(true)` 可以绕过 `private`，滥用会让代码不可控
- **失去编译期检查**：类名、方法名都是字符串，写错了运行时才报错
- **JDK 9+ 模块化限制**：跨模块反射未 `opens` 的包会被拒绝

> [!tip] 记忆锚点
> **反射 = 运行时拿着 Class 对象这张"说明书"，看类的结构、调类的方法。** 类加载时每个类在堆里的 Class 对象唯一，这是所有反射能力的源头。
