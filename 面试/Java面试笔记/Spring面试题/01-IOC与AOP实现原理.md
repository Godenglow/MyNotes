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

## 动态代理 vs 静态代理

![[静态代理与动态代理对比.svg]]

| 对比项 | 静态代理 | 动态代理 |
| --- | --- | --- |
| 生成时机 | 编译期（手写 / 工具生成） | 运行时（反射 + 字节码生成） |
| 复用性 | 一个代理类对一个目标，横切逻辑重复写 | 一份 `InvocationHandler` 服务所有目标 |
| 改动成本 | 接口改动，代理和实现两头改 | 逻辑集中在 handler，改一处生效 |

`invoke()` 转发链（AOP 增强的落点就在这段代码里）：

```java
UserService proxy = (UserService) Proxy.newProxyInstance(
    target.getClass().getClassLoader(),
    new Class[]{UserService.class},
    (p, method, args) -> {
        doBefore();                               // 前置增强（如开事务）
        try {
            return method.invoke(target, args);   // 反射调真身
        } finally {
            doAfter();                            // 后置增强（如提交 / 记日志）
        }
    });
```

> [!note] 纠正原文一处表述
> "动态代理代理的是一个接口下的多个实现类"不准确 —— 准确说：**同一份代理逻辑（handler）可以在运行时套用到任意接口 / 任意目标类上**。静态代理也可以代理多个实现类（多写几个类），核心区别是**编译期 vs 运行期**、**逻辑写 N 遍 vs 写 1 遍**。

## AOP 在 Spring 中的应用场景

| 场景 | 实现要点 |
| --- | --- |
| **声明式事务** | `@Transactional`：AOP 在方法前开事务，异常按规则回滚（底层 = 动态代理 + **ThreadLocal 绑定 Connection**，同线程同一事务） |
| **日志记录** | `@Before` 拿入参、`@AfterReturning` 拿返回值、`@Around` 统计耗时 |
| **权限校验** | 自定义注解 + 切面，方法执行前校验登录态 / 角色 |
| **接口限流** | `@Around` + Semaphore / Redis 计数，超限直接拒绝 |
| **缓存** | `@Cacheable` 本质也是 AOP（CacheInterceptor 先查缓存再执行方法） |
| **统一异常 / 审计** | `@AfterThrowing` 上报监控、埋点 |

`@Around` 统计耗时的典型写法：

```java
@Around("@within(org.springframework.stereotype.Service)")
public Object timing(ProceedingJoinPoint pjp) throws Throwable {
    long start = System.currentTimeMillis();
    try {
        return pjp.proceed();               // 目标方法在这执行
    } finally {
        log.info("{} 耗时 {} ms", pjp.getSignature(), System.currentTimeMillis() - start);
    }
}
```

### 五种通知的执行顺序（高频追问）

![[AOP通知执行顺序.svg]]

- 正常返回：`@Around` 前半 → `@Before` → 目标方法 → `@Around` 后半 → `@After` → `@AfterReturning`
- 抛异常：Around 后半不执行（除非 try 包住 proceed）→ `@AfterThrowing` → `@After`（finally 语义）
- 跨切面顺序由 `@Order` 决定，**值越小优先级越高**

> [!warning] @Around 的能力与危险
> 环绕通知能改参数、改返回值、吞异常 —— 最强大也最容易出 bug：在 proceed() 外不 re-throw 异常，事务的回滚判断会失效。

> [!note] 关联
> 声明式事务 = 动态代理 + ThreadLocal（连接绑定当前线程），与 [[16-ThreadLocal原理与内存泄漏]] 的"线程隔离"思路同源；代理原理与自调用失效见上文。
> 底层机制回链：[[06-Java反射机制]]（IOC 创建 Bean、JDK 代理转发全是反射家族）、[[05-Java创建对象的方式]]（反射创建不走 new）。

> [!tip] 一句话速记
> **IOC 反转的是创建权：工厂 + 反射 + 注入；AOP 织入的是横切面：运行时代理 —— JDK 走接口，CGLIB 走继承，Boot 2.x 默认 CGLIB。**

