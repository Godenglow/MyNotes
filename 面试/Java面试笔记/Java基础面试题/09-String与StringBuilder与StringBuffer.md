---
tags:
  - Java
  - 面试
  - String
source: 小林coding《300道+Java面试题》
date: 2026-09-15
---

# String、StringBuilder、StringBuffer 的区别和联系

> [!question] 疑问
> String、StringBuffer、StringBuilder 的区别和联系？

## 一图看懂

![[String与StringBuilder与StringBuffer.svg]]

## 对比总结

| 特性 | String | StringBuilder | StringBuffer |
| --- | --- | --- | --- |
| 可变性 | 不可变 | 可变 | 可变 |
| 线程安全 | 是（因不可变） | 否 | 是（同步方法） |
| 性能 | 低（频繁修改时） | 高（单线程） | 中（多线程安全） |
| 适用场景 | 静态字符串 | 单线程动态字符串 | 多线程动态字符串 |

## String 为什么是不可变的

三个原因叠在一起：

1. 类本身是 `final` 的，不能被继承后重写行为
2. 内部存储字符的数组（JDK 8 是 `char[]`，JDK 9 起是 `byte[]`）是 `private final` 的，且不提供修改方法
3. 所有看似"修改"的方法（`concat`、`replace`、`+`）都返回**新对象**

**这么设计的好处**（追问"为什么设计成不可变"就答这个）：

- **常量池复用**：字面量相同就共享一个对象，省内存
- **hashCode 缓存**：内容不变，hashCode 可以缓存，适合做 `HashMap` 的 key
- **天然线程安全**：不存在被改坏的可能
- **安全性**：路径、URL、数据库连接串等敏感场景不会被中途篡改

## 面试高频追问点

1. **`new String("ab")` 创建了几个对象？**
   最多两个：常量池里一个 `"ab"`（如果之前没有），堆里一个 new 出来的 String 对象。经典陷阱题。
2. **字符串常量池在哪？**
   JDK 7 之前在方法区（永久代），JDK 7 起移到堆中。`intern()` 可以把字符串放入/返回池中的引用。
3. **循环里拼接字符串为什么慢？**
   `s += x` 每次都新建 StringBuilder 和新 String 对象，循环 N 次产生 N 个中间对象（见上面 SVG 左侧）。所以循环拼接必须把 StringBuilder 提到循环外。
4. **编译器会优化什么？**
   - 编译期常量折叠：`"a" + "b"` 直接合并成 `"ab"`
   - 普通一行拼接，javac（JDK 9 之前）会自动改写成 StringBuilder；JDK 9 起改用 `invokedynamic` + `StringConcatFactory`，性能更好
   - 但**跨循环的拼接优化不了**，这是笔试题爱挖的点
5. **StringBuilder 扩容机制？**
   默认初始容量 16，满了扩为 `2n + 2`，用 `Arrays.copyOf` 复制。能预估长度时用 `new StringBuilder(capacity)` 避免扩容。
6. **StringBuffer 现在还用吗？**
   很少。多线程场景下共享一个可变字符串本身就是坏味道，通常用局部 StringBuilder 或直接 String 处理。知道它是 `synchronized` 方法实现的即可。

> [!tip] 记忆锚点
> **不可变是 String 一切特性的根源**：因为不可变，所以能进常量池、能缓存 hashCode、天然线程安全；也因为不可变，频繁拼接才需要可变的 StringBuilder。三兄弟的答案全部从"可变与不可变"推导。
