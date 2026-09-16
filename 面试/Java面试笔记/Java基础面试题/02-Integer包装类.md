---
tags:
  - Java
  - 面试
  - Integer
source: 小林coding《300道+Java面试题》
date: 2026-09-15
---

# Integer 包装类

> [!question] 疑问
> Java 为什么要有 Integer？既然有 int 了，为什么还要一个包装类？

## 两个核心原因

**1. 面向对象的需要：数据 + 方法封装在一起**

`int` 是基本类型，只是一个裸的数值，身上没有任何方法。而 Integer 把 int 包装成 Object 对象，可以把数据和处理数据的方法结合在一起，比如 `parseInt()`（字符串转 int）、`compareTo()`（比较大小）、`toBinaryString()`（转二进制字符串）等。基本类型做不到这些。

**2. 集合和泛型只接受引用类型**

Java 中绝大部分类和方法都是为"对象"设计的：

- `ArrayList` 内部只能存类类型，没法写 `ArrayList<int>`，想存 int 必须先包装成 Integer
- 泛型同样只能使用引用类型
- `Collections.sort()` 操作的是对象列表，配合 Integer 才能直接使用

## 深一层：为什么 Java 不干脆取消基本类型

理解了这道题的正反两面，面试回答会更完整：

- **int 等基本类型存在的意义是性能**：直接在栈上存值，没有对象头、没有 GC 压力、没有指针间接寻址。Integer 一个对象光对象头就要多占十几字节，还有装箱开销。
- **Integer 存在的意义是"融入对象世界"**：能放进集合、能当泛型参数、能为 null（可以表达"没有值"，而 int 默认是 0，无法区分"没填"和 0）、能参与反射和框架的通用处理。

所以 Java 的设计是两者并存，用**自动装箱/拆箱**（`Integer x = 5;` ↔ `int y = x;`）在两个世界之间无缝转换。

> [!note] 关联
> 本题与 [[01-BigDecimal与浮点数精度]] 属于同一类考点模式：**"为什么有了 X 还要有 Y" + 引用类型比较的坑**，可以放在一起记。

## 面试必然追问：Integer 缓存

最常见的后续问题是这段代码输出什么：

```java
Integer a = 127, b = 127;
Integer c = 128, d = 128;
System.out.println(a == b);  // true
System.out.println(c == d);  // false
```

原因：

- 自动装箱走的是 `Integer.valueOf()`，它对 **-128 ~ 127** 范围内的数用了缓存池（`IntegerCache`），同一范围内的装箱返回同一个对象，`a == b` 为 true
- 超出范围就 new 新对象了，`c == d` 比较的是不同对象地址，为 false
- 缓存上界可以通过 JVM 参数 `-XX:AutoBoxCacheMax` 调整

> [!warning] 结论
> **包装类之间的比较永远用 `equals()`，不要用双等号做地址比较。**
