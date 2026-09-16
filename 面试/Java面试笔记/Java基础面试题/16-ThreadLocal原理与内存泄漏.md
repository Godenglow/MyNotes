---
tags:
  - Java
  - 面试
  - 并发
  - ThreadLocal
source: 小林coding《300道+Java面试题》并发安全篇
date: 2026-09-16
---

# ThreadLocal 原理与内存泄漏

> [!question] 疑问
> ThreadLocal 作用、原理？里面存的 key、value 是啥？会有什么问题，如何解决？

## 一图看懂内存结构

![[ThreadLocal内存结构.svg]]

**反直觉的第一点：map 不在 ThreadLocal 里，在 Thread 身上**（Thread 类的 `threadLocals` 成员变量）。所以每个线程各有一份，互不可见 —— 它是"线程隔离"思路，和锁的"线程同步"是两个方向，**不加锁也线程安全，本质是空间换时间**。

| 问题 | 答案 |
| --- | --- |
| key 存的啥 | **ThreadLocal 对象本身**，且是**弱引用**（Entry 继承 WeakReference） |
| value 存的啥 | 你 `set()` 进去的值，**强引用** |
| 一把还是多把 | 一个线程的 map 里可以挂多个 ThreadLocal（"Thread 是包，ThreadLocal 是钥匙"） |
| 冲突怎么解 | **开放地址法（线性探测）**，不是 HashMap 的链地址法 —— 源码细节考点 |

## 典型使用场景

| 场景 | 为什么需要 |
| --- | --- |
| `SimpleDateFormat`（非线程安全） | 每线程 new 一份副本，避免加锁 |
| Spring 事务（Connection 绑定线程） | 同一线程内多处拿到同一个连接 |
| 链路追踪 traceId / MDC 日志 | 全链路随时取当前请求的上下文 |
| 当前登录用户上下文 | 拦截器 set，业务代码随处 get |

## 内存泄漏：链路 + 解决

**泄漏链条**：key 是弱引用，外部不再持有 ThreadLocal 时 key 被 GC → Entry 变成 `(null, value)`；但 value 仍被 `Thread → map → Entry` 强引用着，**线程池的线程基本不死 → value 永远回收不掉**。

**解决**：

```java
static final ThreadLocal<User> CONTEXT = new ThreadLocal<>();   // static 防止被回收
try {
    CONTEXT.set(user);
    // 业务逻辑
} finally {
    CONTEXT.remove();   // 正解：用完必须删
}
```

- 弱引用只是"防泄漏的一半"：保住 ThreadLocal 对象本身能被回收，**保不住 value**
- 框架有兜底：set/get/rehash 时探测式清理 key=null 的过期 Entry —— 是补救，不是依赖的理由
- ThreadLocal 建议修饰为 `private static final`：防止被回收产生 `(null, value)` 垃圾

## 线程池专属坑：数据串号

线程复用，上一个任务 set 了没 remove，下一个任务 `get()` 到的是**上个请求的旧值** —— 用户 A 看到用户 B 的数据，比内存泄漏更严重。答案同样是 **finally 里 remove()**。

> [!warning] 进阶追问
> - `InheritableThreadLocal` 能让子线程继承父线程的值，但**线程池里失效**（线程是提前建好的，不新建）；要用阿里的 TransmittableThreadLocal（TTL）
> - key 为什么弱引用：保 ThreadLocal 对象本身可回收（否则 map 强引用它永不释放）；value 强引用无法避免（业务要用），只能靠 remove

> [!tip] 一句话速记
> **map 挂在 Thread 身上，key 是弱引用的钥匙，value 是强引用的包袱；线程池不死人，用完必须 remove。**

> [!note] 关联
> [[12-JUC并发工具]]：ThreadLocal 与锁是并发两大流派 —— 隔离（无锁）vs 同步（[[13-Java常用锁]]）；线程池复用问题回到 [[12-JUC并发工具]] 的 ThreadPoolExecutor。
