---
tags:
  - Java
  - 面试
  - 并发
  - 锁
source: 小林coding《300道+Java面试题》并发安全篇
date: 2026-09-16
---

# Java 常用锁

> [!question] 疑问
> Java 中有哪些常用的锁，在什么场景下使用？实践中怎么用锁？

## 一图看懂锁的分类

![[Java锁的分类全景.svg]]

四个维度是**独立**的，别背成一串：synchronized / ReentrantLock 是**实现**，悲观 / 乐观是**思想**，公平 / 非公平是**策略**，阻塞 / 自旋是**等锁的方式**。逐个一句话：

| 锁 | 一句话 | 典型场景 |
| --- | --- | --- |
| synchronized | 内置锁，JVM 层，用完自动释放 | 绝大多数简单互斥场景，默认首选 |
| ReentrantLock | 显式锁：可中断、可限时、可选公平、多 Condition | 需要上述高级控制时才用 |
| ReadWriteLock | 读共享、写独占 | 读多写少（配置、缓存） |
| 悲观锁 | 假设最坏情况，先锁再操作 | 写多冲突重；synchronized / ReentrantLock 都是 |
| 乐观锁 | 不锁，更新时校验（CAS / 版本号） | 读多写少、计数；AtomicXxx、DB 的 version 字段 |
| 自旋锁 | 拿不到锁就循环重试，不挂起 | 锁持有时间极短；过度自旋白烧 CPU |

## synchronized 的锁升级

![[synchronized锁升级流程.svg]]

> [!warning] 偏向锁已经是"历史知识"
> JDK 15 起偏向锁默认禁用并废弃（JEP 374），原因是维护成本高于收益、在现代硬件上收益不明显。答题正确姿势：**先按 JDK 8 讲完四级流程（面试官考的就是这个），再补一句"偏向锁新版本已废弃"**，是加分项。

## synchronized vs ReentrantLock

| 对比项 | synchronized | ReentrantLock |
| --- | --- | --- |
| 层面 | JVM 关键字（对象头 Mark Word） | JDK API，基于 AQS |
| 释放 | 代码块结束**自动**释放 | 必须手动 `unlock()`，必须放 finally |
| 公平锁 | 不支持（只有非公平） | 构造参数可选 |
| 可中断 | 不可 | `lockInterruptibly()` |
| 限时获取 | 不可 | `tryLock(time, unit)` |
| 条件队列 | 一把锁一套 wait/notify | 一把锁可建多个 `Condition` |
| 怎么选 | **默认用它**（简单、不会忘释放） | 需要上面那些高级功能才用 |

## 实践写法

**synchronized（截图示例的规范版）** —— 优先用私有锁对象缩小粒度，而不是锁 `this`：

```java
public class Counter {
    private int count = 0;
    private final Object lock = new Object();   // 私有锁对象，final 防替换

    public void increment() {
        synchronized (lock) {       // 代码块：只串行化真正冲突的部分
            count++;
        }
    }
    // 方法上直接加 synchronized = 锁 this，粒度大，慎用
}
```

**ReentrantLock 模板** —— lock/unlock 必须成对，unlock 必须在 finally：

```java
Lock lock = new ReentrantLock();   // 默认非公平，吞吐高
lock.lock();
try {
    // 临界区
} finally {
    lock.unlock();                 // 忘了这句 = 死锁炸弹
}
```

> [!warning] 用锁的四个坑
> 1. **别锁 String 字面量、Integer 缓存对象** —— 它们被 JVM 全局共享（如 `"abc"`、`Integer.valueOf(127)`），会跟不相干的代码互锁
> 2. **`synchronized(this)` 粒度大** —— 把不冲突的操作也串行化了，用私有 final 锁对象
> 3. **ReentrantLock 忘 finally unlock()** —— 异常路径漏释放，直接死锁
> 4. **锁对象别暴露** —— 加 `private final`，防止外部代码拿到同一把锁捣乱

## 场景 → 锁速查

| 场景 | 用什么 |
| --- | --- |
| 简单互斥（默认选择） | synchronized |
| 需要超时、中断、公平、多条件队列 | ReentrantLock |
| 读多写少 | ReentrantReadWriteLock（JDK 8+ 可看 StampedLock 乐观读） |
| 单变量的原子更新（计数、累加） | AtomicInteger / LongAdder（乐观锁 = CAS） |
| 数据库层面防并发更新 | 乐观锁 version 字段（`update ... where version = ?`） |

> [!tip] 一句话速记
> **默认 synchronized，进阶 ReentrantLock，读多用读写锁，单值更新用 CAS。**

> [!note] 关联
> [[12-JUC并发工具]]：AtomicInteger 就是乐观锁（CAS）的落地实现；ReentrantLock 基于 AQS（后续进阶主线）。锁升级看的是对象头 Mark Word，想挖深属于 JVM 专题。
