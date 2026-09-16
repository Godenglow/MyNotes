---
tags:
  - Java
  - 面试
  - Stream
  - Java8
source: 小林coding《300道+Java面试题》
date: 2026-09-15
---

# Java Stream API

> [!question] 疑问
> Java 中 Stream 的 API 介绍一下？串行流与并行流的区别？

## 一图看懂

![[Java-Stream-API.svg]]

## Stream 是什么

Java 8 引入的**声明式数据处理管道**：把集合的操作（过滤、映射、排序、聚合）从"怎么做的循环"变成"要做什么的描述"。特点：

- **不存数据**：Stream 不是容器，只是数据源（集合、数组、IO）的一条管道
- **不改数据源**：所有操作都产生新结果，原集合不变
- **惰性求值**：中间操作只搭管道不执行，终端操作才触发整条管道（一次遍历全部做完）
- **一次性**：流只能被消费一次，再次使用抛 `IllegalStateException`

对比（PDF 案例）：筛出长度大于 3 的字符串——

```java
// 传统写法：怎么做的
List<String> filtered = new ArrayList<>();
for (String item : list) {
    if (item.length() > 3) filtered.add(item);
}

// Stream：要做什么
List<String> filtered = list.stream()
        .filter(s -> s.length() > 3)
        .collect(Collectors.toList());
```

## 三个阶段与常用 API

**1. 创建**：`collection.stream()`、`Arrays.stream()`、`Stream.of()`、`Stream.iterate()`

**2. 中间操作（返回 Stream，可链式，惰性）**

| API | 作用 |
| --- | --- |
| `filter` | 按条件过滤 |
| `map` / `mapToInt` | 一对一转换；`mapToInt` 转数值流避免装箱 |
| `flatMap` | 一对多展平（把 `List<List<T>>` 拍平） |
| `distinct` / `sorted` / `limit` / `skip` | 去重 / 排序 / 截取 |
| `peek` | 顺手看一眼（调试用），不改变元素 |

**3. 终端操作（触发执行，只能有一个）**

| API | 作用 |
| --- | --- |
| `collect` | 收集结果，配合 `Collectors.toList()/toMap()/groupingBy()/joining()` |
| `forEach` | 遍历消费 |
| `reduce` | 聚合归约（求和、求最大值） |
| `count` / `min` / `max` | 统计 |
| `anyMatch` / `allMatch` / `noneMatch` | 短路判断（找到就停） |
| `findFirst` / `findAny` | 找一个元素（也短路） |

高频代码：**分组**是笔试最常写的：

```java
Map<Integer, List<String>> byLen = list.stream()
        .collect(Collectors.groupingBy(String::length));
```

## 串行流 vs 并行流

- `parallelStream()` 或 `stream().parallel()`：数据被 Fork/Join 框架**切成多块**，丢进 `ForkJoinPool.commonPool()`（默认线程数 = CPU 核数 - 1）并行处理，最后合并
- **适合 CPU 密集型**任务：每个核一个任务，效率高
- **不适合 IO 密集型**：公共线程池只有 CPU 核数个线程，任务会排队，且会拖垮 JVM 里**其他所有用并行流的代码**（池是全局共享的）

> [!warning] 并行流两大坑
> 1. **公共线程池全局共享**：在 parallelStream 里做 IO / 阻塞调用，会饿死整个应用的并行流。需要自定义 `ForkJoinPool` 提交。
> 2. **forEach 无序、非线程安全**：并行流里往 ArrayList 里 add 会丢数据甚至抛异常，结果收集一律用 `collect`；且操作必须无状态、无副作用。

## 面试高频追问点

1. **怎么证明 Stream 是惰性的？**
   只写 `list.stream().filter(...)` 不加终端操作，程序什么都不打印——中间操作根本没执行。终端操作一加上，瞬间执行。
2. **Stream 和 InputStream 是一回事吗？**
   不是。InputStream 是 IO 字节流（传输数据），Stream 是集合数据处理管道（加工数据），只是名字像。
3. **map 和 flatMap 的区别？**
   `map` 一对一返回转换后的流；`flatMap` 把每个元素产生的集合**拍平**成一条流，常用于"拆句子成单词"。
4. **collect 和 reduce 的区别？**
   `reduce` 把流归约成**一个值**；`collect` 用收集器把流变成**容器**（List/Map/String），功能更强。
5. **流能复用吗？**
   不能，一个流只消费一次，第二次终端操作抛异常。要复用就换成重新 `stream()`，或用 `Supplier<Stream<T>>`。

> [!tip] 记忆锚点
> **Stream = 惰性的流水线**：中间操作只画图纸（惰性），终端操作才开工（一次遍历全做完）；parallelStream 是把流水线复印多份同时开工——但车间（ForkJoinPool.commonPool）只有一间，别在里面睡觉（IO 阻塞）。
