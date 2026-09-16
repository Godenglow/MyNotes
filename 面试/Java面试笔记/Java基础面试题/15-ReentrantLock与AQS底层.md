---
tags:
  - Java
  - 面试
  - 并发
  - AQS
source: 小林coding《300道+Java面试题》并发安全篇
date: 2026-09-16
---

# ReentrantLock 与 AQS 底层

> [!question] 疑问
> ReentrantLock 底层怎么实现的？AQS 是什么？怎么理解可重入锁？

## 一图看懂 AQS

![[AQS核心模型.svg]]

**AQS = 一个 `volatile int state` + 一条 CLH 双向等待队列 + LockSupport 的 park/unpark**。它是个同步器框架，抢锁的通用套路：

> CAS 改 state → 抢不到就包装成 Node 入队尾 → park 挂起 → 前驱释放（state 归 0）后 unpark 队头后继 → 被唤醒者重试 CAS

AQS 用**模板方法模式**把"怎么算拿到锁"留给子类：`tryAcquire()/tryRelease()` 由实现类重写，入队、挂起、唤醒这些脏活全由框架包办。

## ReentrantLock 怎么用 AQS

内部类 `Sync` 继承 AQS，再分出 `FairSync` / `NonfairSync` 两个子类。加锁伪代码：

```text
非公平 lock():                          公平 lock():
    CAS(state 0→1) 成功 → 独占              tryAcquire():
    失败 → acquire(1):                          先看 CLH 队列有没有人排队
        tryAcquire() 再试一次                   没人排 → CAS 抢
        （公平版先查队列）                       有人排 → 排队去
        入 CLH 队尾 → park() 挂起
unlock(): state - 1 → 减到 0 时 unpark 队头后继
```

- **非公平默认的原因**：刚释放锁的线程大概率马上又要拿，插队一次少一次挂起/唤醒的切换，吞吐高
- **可中断**：`lockInterruptibly()` —— park 中的线程能被 interrupt 唤醒并返回（所以能"打断死等"）
- **超时**：`tryLockNanos()` 限时循环，拿不到就放弃
- **Condition**：`lock.newCondition()` 每个条件一条独立等待队列，`await()/signal()` 对应 Monitor 的 wait/notify 显式版 —— 14 号笔记里的 `_WaitSet` 拆成了多条队列

## 可重入锁怎么理解

**同一线程可以重复获取自己已持有的锁而不卡死**；实现就是持锁计数器：获取 +1，释放 -1，减到 0 才真正放锁。

| 实现者 | 计数器在哪 |
| --- | --- |
| synchronized | Monitor 的 `_recursions`（14 号笔记） |
| ReentrantLock | AQS 的 `state`（`getHoldCount()` 查询它） |

> [!warning] 截图纠错：字段名是 state，不是 holdCount
> AQS 里表示"重入了几次"的字段叫 **`state`**（0=无锁，>0=重入次数）；`holdCount` 只是 `getHoldCount()` 这个查询方法的名字，不是底层字段名。

为什么必须有可重入：否则同步方法 A 内部调用同类同步方法 B，线程会**等自己释放锁 → 永远等不到 → 自死锁**。Reentrant（可再进入）的名字就是从这来的。

> [!tip] 一句话速记
> **AQS = state + 队列 + park/unpark；抢锁就是 CAS state，抢不到排队挂起，释放叫醒下一个；state > 0 且线程是自己 = 重入。**

## 和 synchronized 的区别

五点对比（用法 / 释放方式 / 公平性 / 中断 / 底层实现）→ 见 [[13-Java常用锁]] 的对比表，别背两份。

> [!note] 关联 + 一通百通
> AQS 是整个 JUC 锁工具的地基：**ReentrantLock、Semaphore（state=许可数）、CountDownLatch（state=计数）、ReentrantReadWriteLock（state 高 16 位读锁 / 低 16 位写锁）全是同一个框架换了个 state 语义**。读 12 号笔记里那些工具时，脑子里都套这张图。
