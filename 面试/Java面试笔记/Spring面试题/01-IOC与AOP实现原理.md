---
tags:
  - Spring
  - 面试
  - IOC
  - AOP
source: 小林coding Spring 篇
date: 2026-09-16
---

# IOC 与 AOP 实现原理

> [!question] 疑问
> IOC 和 AOP 是通过什么机制来实现的？

## IOC：工厂模式 + 反射 + 依赖注入

![[IOC实现链路.svg]]

一句话：**IOC = 对象的创建权和依赖装配权从程序员手里交给容器**。"控制反转"反转的就是这个控制权 —— 不再 `new`，而是描述清楚要什么，容器负责造和组装。

机制拆解：

- **工厂模式**：容器本身就是个超大工厂，`BeanFactory` / `ApplicationContext` 是两个入口
- **反射**：按 BeanDefinition 里的类信息运行时 `newInstance`，代码里没有写死的 `new`
- **依赖注入**：容器创建 Bean 时把依赖"塞"进去，对象只管声明要什么

| 对比项 | BeanFactory | ApplicationContext |
| --- | --- | --- |
| 定位 | IOC 基础容器 | BeanFactory 超集 + 企业级功能 |
| 额外能力 | 无 | 国际化、事件发布、资源加载、自动注册 BeanPostProcessor |
| 单例实例化时机 | getBean 时懒加载 | 启动时**预实例化**所有单例（缺点早暴露） |

三种注入方式：**构造器注入（推荐**：依赖不可变、保证非空、早暴露问题）→ Setter 注入（可选依赖）→ 字段注入（`@Autowired` 打字段，快但难单测、字段不能 final，Spring 官方不推荐）。

## AOP：运行时动态代理

![[JDK与CGLIB动态代理.svg]]

一句话：**把日志 / 事务 / 权限这类横切逻辑，运行时通过代理对象织入方法调用前后，业务源码零改动**。

| 对比项 | JDK 动态代理 | CGLIB |
| --- | --- | --- |
| 原理 | 生成实现同一接口的 `$Proxy0`，转发给 `InvocationHandler` | 生成目标类的**子类**，`MethodInterceptor` 拦截后 `super` 调真身 |
| 前提 | 目标必须实现接口 | 无需接口；final 类 / final 方法 / private 代理不了 |
| 调用开销 | 反射调用 | 字节码直接调（FastClass 索引），更快 |

选择规则（易错点）：

- 传统 Spring：有接口 → JDK；无接口 → CGLIB
- **Spring Boot 2.x 起：默认 CGLIB**（`proxyTargetClass=true`）—— "有接口用 JDK"是过时答案

> [!warning] 最高频追问：@Transactional 为什么会失效
> 事务靠 AOP 代理实现；对象内部 `this.method()` 自调用走的是**原始对象**而不是代理 → 通知根本没机会执行。解法：拆到另一个 Bean、注入自身代理（`AopContext.currentProxy()`）、或改用 AspectJ 编译期织入。

> [!tip] 一句话速记
> **IOC 反转的是创建权：工厂 + 反射 + 注入；AOP 织入的是横切面：运行时代理 —— JDK 走接口，CGLIB 走继承，Boot 2.x 默认 CGLIB。**

> [!note] 关联
> [[06-Java反射机制]]：IOC 创建 Bean、JDK 代理转发，底层全是反射家族；[[05-Java创建对象的方式]]：反射创建不走 new（和 clone、反序列化同属"绕过构造器之外"的例外，但反射可以选构造器）。
