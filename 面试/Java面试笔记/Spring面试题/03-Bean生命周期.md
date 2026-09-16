---
tags:
  - Spring
  - 面试
  - Bean
  - 生命周期
source: 小林coding Spring 篇
date: 2026-09-16
---

# Bean 生命周期

> [!question] 疑问
> Bean 的生命周期说一下？

## 一图走完八阶段

![[Bean生命周期流程.svg]]

原文十步可以归并为**八个阶段**，对照关系与关键点：

| 阶段 | 原文步骤 | 关键点 |
| --- | --- | --- |
| ① 实例化 | 1 | 构造器 / 工厂方法，此时属性全空 |
| ② 属性填充 | 2 | 依赖注入发生在这里（循环依赖也在这暴露/解决，见 [[02-循环依赖与三级缓存]]） |
| ③ Aware 回调 | 3-5 | 顺序固定：`BeanNameAware` → `BeanFactoryAware` → `ApplicationContextAware` |
| ④ BPP 前置 | 6 | `postProcessBeforeInitialization()` |
| ⑤ 初始化 | 7 | **顺序固定**：`@PostConstruct` → `afterPropertiesSet()` → `init-method` |
| ⑥ BPP 后置 | 8 | `postProcessAfterInitialization()` —— **AOP 代理在这里生成** |
| ⑦ 使用 | 9 | 单例驻留容器；prototype 交付后不归容器管 |
| ⑧ 销毁 | 10 | 容器关闭时：`@PreDestroy` → `destroy()` → `destroy-method` |

## 三个必考细节

**1. 初始化与销毁都是"三连"，顺序固定**

- 初始化：`@PostConstruct` → `InitializingBean#afterPropertiesSet()` → `init-method`
- 销毁：`@PreDestroy` → `DisposableBean#destroy()` → `destroy-method`
- 记法：**注解先于接口先于配置**（越靠近代码的越先执行）

**2. AOP 代理的生成时机**

在 ⑥ `postProcessAfterInitialization()` 中由 `AbstractAutoProxyCreator` 生成 —— 这就是"代理应在初始化后生成"的正常路径。**例外**：发生循环依赖时，代理提前到实例化后由三级缓存的工厂生成（见 [[02-循环依赖与三级缓存]]），两处呼应着记。

**3. 作用域决定销毁归属**

单例的销毁由容器关闭触发（`close()` / `registerShutdownHook()`）；**prototype 只负责"到手"，销毁交给使用者** —— JVM 里没有它们的销毁回调。

## 单例 vs 原型：生命周期归属 + 作用域全家桶

![[单例与原型作用域对比.svg]]

| 作用域 | 范围 | 备注 |
| --- | --- | --- |
| singleton（默认） | 每个容器一个实例 | "每容器一个"，不是 JVM 全局——多个容器各有各的 |
| prototype | 每次 getBean 新建 | 销毁回调不执行 |
| request / session / application / websocket | Web 上下文 | 靠 scoped proxy（CGLIB）实现注入 |
| 自定义 | 实现 `Scope` 接口 | 如 Spring Cloud 的 refresh 作用域 |

**经典坑：单例 Bean 注入原型 Bean** —— 注入只发生在 A 创建那一刻，之后 A 拿到的永远是同一个 B，"原型"失效。解法：`@Lookup` 方法注入 / `ObjectProvider<B>` / `ApplicationContext.getBean()`。

另一个衍生追问：**单例 Bean 的线程安全** —— 默认单例 + 可变成员变量 = 非线程安全（Controller 里写成员变量是重灾区）；要么无状态，要么并发容器 / ThreadLocal（[[16-ThreadLocal原理与内存泄漏]]）。

> [!tip] 一句话速记
> **实例化 → 填充 → 感知 → 前处理 → 初始化三连 → 后处理（AOP 在这）→ 使用 → 销毁三连；注解先于接口先于配置。**

> [!note] 关联
> [[01-IOC与AOP实现原理]]（容器怎么拿到 BeanDefinition）、[[02-循环依赖与三级缓存]]（代理提前生成的唯一例外）；初始化三连里 `@PostConstruct` 由 CommonAnnotationBeanPostProcessor 处理 —— BPP 几乎贯穿全流程，是 Spring 扩展性的核心。
