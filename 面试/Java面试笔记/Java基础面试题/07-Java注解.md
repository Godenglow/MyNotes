---
tags:
  - Java
  - 面试
  - 注解
  - 反射
source: 小林coding《300道+Java面试题》P41-42
date: 2026-09-15
---

# Java 注解

> [!question] 疑问
> 对注解解析的底层实现了解吗？Java 注解的作用域有哪些？

## 一图看懂注解的生命周期

![[Java注解的生命周期.svg]]

## 注解的本质

注解本质上是一种**特殊接口**：定义 `@interface` 后，编译器会把它转换成一个继承 `java.lang.annotation.Annotation` 的接口，所以注解也叫**声明式接口**。

```java
public @interface MyAnnotation {
    String value();
}
```

**底层解析流程**（面试回答版本）：

1. 通过反射获取注解时，返回的不是接口实例，而是 **JVM 运行时生成的动态代理对象**
2. 通过代理对象调用注解的属性方法（如 `value()`），最终走到 `AnnotationInvocationHandler.invoke()`
3. 该方法从 `memberValues` 这个 **Map** 中索引出对应的值
4. `memberValues` 的来源是 **Java 常量池**（编译期就把属性值写进了字节码）

> [!note] 关联
> 动态代理 + 反射，正是 [[06-Java反射机制]] 里讲的两大能力——注解解析就是它们的组合应用。

## 两个容易混为一谈的维度（PDF 没点破，面试要分清）

PDF 把两个概念都叫"作用范围"，但它们是**正交的两个维度**，由两个元注解分别控制：

| 元注解 | 控制什么 | 取值 |
| --- | --- | --- |
| `@Retention` | 注解**活到什么时候**（保留策略） | SOURCE / CLASS / RUNTIME |
| `@Target` | 注解**能用在哪**（作用目标） | TYPE / METHOD / FIELD / PARAMETER / CONSTRUCTOR / LOCAL_VARIABLE 等 |

三种保留策略：

- **SOURCE**：仅存在于源码，编译后丢弃——如 `@Override`、`@SuppressWarnings`、**Lombok 全家桶**（编译期生成代码）
- **CLASS**：保留在 `.class` 文件中，但运行时不可见——默认值，供字节码工具（ASM、AspectJ 编译期织入）使用
- **RUNTIME**：保留到运行时，可被反射读取——**只有它才能配合反射 API 解析**，Spring 的 `@Component`、自定义业务注解都是这个

> [!warning] 常见追问
> "为什么自定义注解反射拿不到值？"——九成是忘了 `@Retention(RetentionPolicy.RUNTIME)`，默认是 CLASS，运行时不可见。

## 完整的自定义注解 + 解析（面试常让手写）

```java
@Retention(RetentionPolicy.RUNTIME)   // 必须是 RUNTIME 才能反射读取
@Target(ElementType.METHOD)           // 只能标在方法上
public @interface MyLog {
    String value() default "";
}

// 解析：扫描方法上的注解
for (Method m : obj.getClass().getDeclaredMethods()) {
    MyLog log = m.getAnnotation(MyLog.class);
    if (log != null) {
        System.out.println("方法 " + m.getName() + " 的日志描述：" + log.value());
    }
}
```

## 应用场景

1. **框架配置与扫描**：Spring 的 `@Component`、`@Autowired`——容器启动时反射扫描注解完成装配
2. **编译期代码生成**：Lombok（SOURCE 级）、MapStruct
3. **AOP 日志 / 权限校验**：自定义注解 + 切面，拦截带注解的方法（项目经验高频考点）
4. **测试**：JUnit 的 `@Test`、`@BeforeEach`
5. **替代配置文件**：注解 + 反射让"约定优于配置"成为可能

> [!tip] 记忆锚点
> **注解 = 会写字的标记 + 会读字的读者。** 注解本身只是标记（继承 Annotation 的接口），真正干活的是"读者"——RUNTIME 注解靠反射读，SOURCE 注解靠编译器/APT 读。没有读者，注解什么也不会发生。
