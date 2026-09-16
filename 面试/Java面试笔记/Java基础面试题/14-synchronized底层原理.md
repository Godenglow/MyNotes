---
tags:
  - Java
  - 面试
  - 并发
  - synchronized
source: 小林coding《300道+Java面试题》并发安全篇
date: 2026-09-16
---

# synchronized 底层原理（Monitor）

> [!question] 疑问
> synchronized 的工作原理？monitor 是什么？waitSet 和 entryList 是干嘛的？

## 一图看懂 ObjectMonitor

![[synchronized底层ObjectMonitor模型.svg]]

每个 Java 对象自带一把"监视器锁"（monitor），所以 synchronized 也叫**监视器锁 / 内置锁**。HotSpot 里它就是 ObjectMonitor 结构，核心四件套：

| 字段 | 作用 |
| --- | --- |
| `_owner` | 当前持锁线程 |
| `_recursions` | 重入计数器，**可重入的来源** |
| `_EntryList` | 等锁队列（阻塞抢锁的线程） |
| `_WaitSet` | 调了 wait() 的线程，等 notify 唤醒 |

## 4 步流转（面试口径）

1. 多个线程进同步块 → 先进 `_EntryList` 排队
2. 一个线程抢到 monitor → 成为 `_owner`，计数器 +1（同线程重入再 +1）
3. 持锁线程调 `wait()` → **释放锁**（计数 -1、`_owner` 置 null），进 `_WaitSet`；被 `notify()/notifyAll()` 唤醒后回 `_EntryList` 重新竞争
4. 线程执行完 → `monitorexit` 计数 -1，减到 0 才真正释放，`_owner` 置 null

## 字节码层面

- 同步**代码块**：编译成 **1 个 `monitorenter` + 2 个 `monitorexit`** —— 第二个是异常出口，保证抛异常也能放锁
- 同步**方法**：没有这些指令，靠方法常量池的 `ACC_SYNCHRONIZED` 标志，JVM 调用前拿锁

```text
monitorenter          // 计数 +1；拿不到就进 _EntryList 阻塞
  ... 临界区 ...
monitorexit           // 正常出口：计数 -1
goto 5
monitorexit           // 异常出口：catch 后先放锁再 athrow
athrow
```

## 内存语义（为什么能保证可见性）

- **通俗版**（八股口径）：加锁时清掉工作内存里的共享变量、从主存重读；解锁时把修改写回主存
- **严谨版**（JMM）：**同一把锁的解锁 happens-before 后续加锁** —— 临界区里的写，对下一个拿锁的线程可见
- 结论：synchronized 同时解决**原子性 + 可见性 + 有序性**，不只是"加锁"

## 为什么说它"重"

synchronized 是排它锁；HotSpot 的 Java 线程与 OS 内核线程一一对应，**阻塞 / 唤醒要用户态 ↔ 内核态切换**，很贵 —— 这正是引出锁升级（偏向 → 轻量 → 重量）的原因。

> [!warning] 容易忽略的追问点
> - **wait()/notify() 为什么定义在 Object 而不是 Thread？** 因为锁属于对象（每个对象都有 monitor），wait/notify 操作的是对象的 monitor
> - wait()/notify() 必须**已持有该锁**才能调用，否则抛 `IllegalMonitorStateException`

> [!tip] 一句话速记
> **一个 _owner、一个计数器、两条队列（EntryList 抢锁、WaitSet 等唤醒）；进 +1 出 -1，归零放锁。**

> [!note] 关联
> [[13-Java常用锁]]（锁升级四级流程、synchronized vs ReentrantLock 怎么选）；ReentrantLock 的 `Condition.await()` 对应这里的 `_WaitSet` 逻辑 —— AQS 就是这套模型的显式版实现，是并发进阶的下一站。
