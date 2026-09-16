---
tags:
  - Java
  - 面试
  - 并发
source: 小林coding《300道+Java面试题》并发安全篇
date: 2026-09-16
---

# JUC 并发工具（java.util.concurrent）

> [!question] 疑问
> juc 包下你常用的类有哪些？

## 一图看懂 JUC 四大类

![[JUC并发工具箱四大类.svg]]

JUC 是 JDK 5 加入的并发工具箱（Doug Lea 主导）。学校课程一般只讲到 `new Thread` + `synchronized` 就停了，这块恰好是面试八股的重灾区。四大类一句话定位：

| 类别 | 解决什么问题 |
| --- | --- |
| 线程池 | 线程创建销毁太贵，复用 + 管控并发数量 |
| 并发集合 | 普通集合并发下会坏（HashMap 死循环、丢数据） |
| 同步工具 | 多线程之间"等"与"放行"的协调 |
| 原子类 | `i++` 不是原子的，用 CAS 无锁解决 |

## 线程池：ThreadPoolExecutor

一句话结论：**提前造好线程复用；任务提交后走"核心线程 → 塞队列 → 扩到最大线程 → 拒绝"四步，这条链是必考题**。

7 个构造参数记 4 个就够：`corePoolSize`（核心线程数）、`maximumPoolSize`（最大线程数）、`workQueue`（任务队列）、`RejectedExecutionHandler`（拒绝策略，默认 AbortPolicy 抛异常）。

> [!warning] 面试纠错：别背"推荐用 Executors"
> - `newFixedThreadPool`：队列**无界**，任务堆积到 OOM
> - `newCachedThreadPool`：线程数无上限（Integer.MAX_VALUE），线程爆炸 OOM
> - 阿里 Java 开发手册**禁止**直接用 Executors，生产上手动 `new ThreadPoolExecutor(...)` —— 面试主动提这句是加分项

## 并发集合

**ConcurrentHashMap** —— 线程安全的 HashMap，比 Hashtable 快的本质是**锁粒度细**：

- JDK 7：分段锁（Segment 继承 ReentrantLock，一段一段锁）
- JDK 8：**CAS + synchronized 锁单个桶的头节点**（桶为空时直接 CAS 插入，根本不加锁）

> [!warning] 很多资料（包括截图版八股）写"ConcurrentHashMap 采用分段锁"
> 那只对 JDK 7 成立。答题时按版本演进说，反而显得你懂底层。

**CopyOnWriteArrayList** —— 写时复制：修改时复制一份**新数组**，改完把引用换过去；读操作不加锁，读的还是旧数组。读写分离，适合**读多写少**（如监听器列表、配置缓存）。代价：写慢、内存翻倍、读到的可能是旧值（最终一致）。

## 同步三兄弟

![[JUC同步三兄弟对比.svg]]

| 对比项 | CountDownLatch | CyclicBarrier | Semaphore |
| --- | --- | --- | --- |
| 模型 | 倒计时门闩 | 屏障集合 | 许可池 |
| 谁等谁 | 等待方等 N 件事**完成** | N 个线程**互相**等齐 | 线程抢许可，抢不到就等 |
| 可复用 | 否（一次性，计数到 0 就废） | 是（到齐后自动重置，可多轮） | 持续（release() 归还许可） |
| 典型场景 | 主线程等所有子任务跑完再汇总 | 分阶段任务，全员到齐再进下一阶段 | 限流、数据库连接池 |

## 原子类与 CAS

`i++` 看着是一行，实际是"读 → 加 1 → 写回"**三步**，多线程下互相覆盖导致少加。`AtomicInteger` 用 **CAS**（Compare-And-Swap，CPU 硬件级原子指令）：更新前先比较"内存里的值还是不是我预期的旧值"，是才写入，不是就自旋重试 —— 全程不加锁。

- `AtomicInteger` / `AtomicLong`：无锁计数
- `AtomicReference`：CAS 更新整个对象引用
- `LongAdder`：高并发计数把值分散到多个 Cell 再汇总，比 AtomicLong 快（JDK 8+）

## 场景 → 工具速查

| 场景 | 用什么 |
| --- | --- |
| 主线程等 N 个子任务全部完成再汇总 | CountDownLatch |
| 一组线程分阶段推进，每阶段互相等齐 | CyclicBarrier |
| 限制同时访问某资源的线程数（限流） | Semaphore |
| 并发计数 / 简单扣减（无锁） | AtomicInteger / LongAdder |
| 读多写少的并发 List | CopyOnWriteArrayList |
| 并发 Map（替代 Hashtable） | ConcurrentHashMap |

> [!tip] 一句话速记
> **哈希表（或集合）保"找得到"，同步工具保"等得到"，原子类保"算得对"。**

> [!note] 关联
> [[10-Java-Stream-API]] 的并行流用的也是线程池（公共 ForkJoinPool），"并行流不等于随便用"和线程池参数管控是同一套思想。落到 seckill 项目：Tomcat 扛请求靠线程池；库存防超卖本质是原子操作（CAS 语义）；接口限流对应 Semaphore / 令牌桶 —— 学一个概念就往项目里套一个场景。
