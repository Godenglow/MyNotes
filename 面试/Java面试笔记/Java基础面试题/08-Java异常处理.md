---
tags:
  - Java
  - 面试
  - 异常
source: 小林coding《300道+Java面试题》P43-44
date: 2026-09-15
---

# Java 异常处理

> [!question] 疑问
> Java 异常处理有哪些方式？抛出异常为什么不用 throws？try-catch 中的语句运行情况？

## 一图看懂异常体系

![[Java异常体系.svg]]

## 三种处理方式

**1. try-catch-finally** —— 捕获并处理异常，可以有多个 catch 块处理不同类型：

```java
try {
    // 可能抛出异常的代码
} catch (IOException e) {
    // 处理该类型异常
} catch (Exception e) {
    // 兜底处理
} finally {
    // 无论是否发生异常都会执行（释放资源）
}
```

**2. throw** —— 在方法内**手动抛出**一个具体的异常对象：

```java
throw new IllegalArgumentException("参数不能为空");
```

**3. throws** —— 在**方法签名**上声明该方法可能抛出的异常，交给调用者处理：

```java
public void readFile() throws IOException {
    // ...
}
```

> [!tip] throw 与 throws 的经典对比
> | 对比项 | throw | throws |
> | --- | --- | --- |
> | 位置 | 方法体内 | 方法签名上 |
> | 后面跟什么 | 一个异常**对象** | 一到多个异常**类名** |
> | 作用 | 实际抛出异常 | 声明可能抛出的异常 |
> | 数量 | 一次只能抛一个 | 可以声明多个 |

## 抛出异常为什么不用 throws？

两种情况不需要 `throws` 声明：

1. **异常是 Unchecked Exception**：继承自 `RuntimeException` 或 `Error`，编译器不强制处理（如 `NullPointerException`、`ArrayIndexOutOfBoundsException`）
2. **方法内部已经 catch 处理了**：异常没有向上传递，自然不用声明

根源就在异常体系的分类（见上面 SVG）：**只有 checked 异常（受检异常）才被编译器强制要求 try-catch 或 throws**。

## try-catch 的执行流程

- try 块代码**顺序执行**；一旦抛出异常，从抛出点**立刻跳转**，后面的代码不执行
- 按顺序匹配 catch 块（**子类异常要写在父类前面**，否则编译报错），匹配到就执行，然后继续执行 catch 之后的代码
- 没有匹配的 catch，异常沿调用栈**传递给上一层方法**，直到 JVM 默认处理器（打印堆栈、终止线程）

## 面试高频追问点

1. **finally 一定执行吗？**
   几乎一定，除了 `System.exit()`、JVM 崩溃、线程被杀等极端情况。
2. **finally 里写 return 会怎样？**
   会**覆盖** try/catch 里的返回值，并且**吞掉异常**——绝对不要这么写。执行顺序：try 的 return 先计算但暂不返回，finally 执行，若 finally 也有 return 则以其为准。
3. **try-with-resources（JDK 7+）**
   `try (Resource r = ...) {}` 自动调用 `close()`，替代 finally 里手动关资源，资源类需实现 `AutoCloseable`。实际开发中关资源的首选。
4. **Error 和 Exception 的区别？**
   Error 是程序无法处理的严重错误（OOM、StackOverflowError），不该去 catch；Exception 是程序可以捕获处理的。
5. **自定义异常继承谁？**
   需要调用方强制处理的业务异常继承 `Exception`（checked）；一般业务异常继承 `RuntimeException`（unchecked），是目前的主流做法（Spring 的事务回滚默认也只针对 RuntimeException）。
6. **异常的性能代价在哪？**
   填充**栈跟踪**（`fillInStackTrace`）很贵。高频路径上可用重写 `fillInStackTrace()` 返回自身的异常做流程控制，但**不要用异常做正常业务流程**。
