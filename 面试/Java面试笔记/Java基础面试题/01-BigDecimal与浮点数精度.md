---
tags:
  - Java
  - 面试
  - BigDecimal
source: 小林coding《300道+Java面试题》P20
date: 2026-09-15
---

# BigDecimal 与浮点数精度

> [!question] 疑问
> 浮点数为什么会丢精度？BigDecimal 是怎么工作的？

## 浮点数为什么会丢精度

Java 中的 `float`/`double` 采用 IEEE 754 二进制浮点表示，很多十进制小数（如 0.05、0.01）无法被二进制精确表示，所以 `0.05 + 0.01` 的结果不是 0.06，而是 `0.060000000000000005`。

**危害**：涉及金钱的计算会出大事。例如手上 有 0.06 元，却"买不起"一个 0.05 元加一个 0.01 元的商品。在电商高并发场景下，这类误差会导致无法下单、对账出错等严重问题。

**解决方案**：用 BigDecimal 做精确计算。

```java
import java.math.BigDecimal;

public class BigDecimalExample {
    public static void main(String[] args) {
        BigDecimal num1 = new BigDecimal("0.1");
        BigDecimal num2 = new BigDecimal("0.2");

        BigDecimal sum = num1.add(num2);
        BigDecimal product = num1.multiply(num2);

        System.out.println("Sum: " + sum);       // 0.3
        System.out.println("Product: " + product); // 0.02
    }
}
```

## BigDecimal 是怎么工作的

核心思想：**它不把数存成二进制浮点，而是存成一个"大整数 + 小数点位数"**，所有运算都在十进制整数上做，所以不会丢精度。

### 内部结构

BigDecimal 内部主要就两个字段（JDK 源码简化）：

```java
private final BigInteger intVal;  // 无标度值（unscaled value）
private final int scale;          // 标度（scale）
```

它表示的数值永远是：`intVal × 10^(-scale)`。

比如 `new BigDecimal("0.1")`，内部存的是：

- `intVal = 1`
- `scale = 1`
- 即 1 × 10⁻¹ = 0.1

因为字符串 `"0.1"` 本身就是精确的十进制描述，转成"整数 1 + 小数点后 1 位"没有任何损失。而 `double` 的 0.1 是用二进制科学计数法存的，二进制无法精确表示 1/10，从存储那一刻起就有误差——**这就是两者精度差异的根源，和 BigDecimal 的算法多"聪明"无关，纯粹是进制问题**。

### 四则运算原理

**加法/减法：先对齐 scale，再按整数相加**

计算 `0.1 + 0.01`：

1. 两个数的 scale 不同（1 和 2），先把 scale 统一成较大的 2：0.1 → intVal=10, scale=2
2. 整数相加：10 + 1 = 11
3. 结果：11 × 10⁻² = 0.11，精确

**乘法：整数相乘，scale 相加**

计算 `0.1 × 0.2`：

1. intVal 相乘：1 × 2 = 2
2. scale 相加：1 + 1 = 2
3. 结果：2 × 10⁻² = 0.02，精确

乘法永远精确，因为十进制小数乘小数，位数是有限可列的。

**除法：唯一会出问题的地方**

`0.1 ÷ 0.3` 得到 0.3333... 是无限小数，整数 + scale 的结构存不下，所以 `divide()` 必须指定精度和舍入模式：

```java
new BigDecimal("0.1").divide(new BigDecimal("0.3"), 2, RoundingMode.HALF_UP);
// 结果 0.33
```

> [!warning] 不指定精度和舍入模式时，遇到除不尽会直接抛 `ArithmeticException`——这是实际开发中最常见的 BigDecimal 报错。

### 两个必坑点

**1. scale 参与 equals 比较**

```java
new BigDecimal("1.0").equals(new BigDecimal("1.00"))  // false！
```

因为 `1.0` 存的是 (1, scale=1)，`1.00` 存的是 (1, scale=2)，equals 是逐字段比较的。判断数值相等要用 `compareTo() == 0`。这也是 `HashSet`/`HashMap` 用 BigDecimal 当 key 出 bug 的经典来源。

**2. double 构造会把误差带进来**

```java
new BigDecimal(0.1)
// 0.1000000000000000055511151231257827021181583404541015625
```

`new BigDecimal(double)` 是把 double 二进制表示的**真实值**（含误差）原样转成十进制，所以得到一长串。正确写法是用 String 构造，或 `BigDecimal.valueOf(0.1)`（它内部先走 `Double.toString()` 再走字符串构造）。

### 性能代价

这套机制是纯对象运算：每次加减乘都 new 新对象（BigDecimal 不可变），乘法可能膨胀成大整数运算。性能比原生 double 慢一到两个数量级，所以高频率交易系统里常见替代方案是**用 `long` 以"分"为单位记账**，只在展示层转成元。

## 面试高频追问点汇总

> [!tip] 结合本考点，面试官往往会继续深挖以下四点

1. **为什么用 `new BigDecimal("0.1")` 而不是 `new BigDecimal(0.1)`？**
   传 `double` 会把二进制误差原样带进来，**永远用 String 构造或 `BigDecimal.valueOf()`**。
2. **除法要传 scale 和舍入模式**
   `divide(b, 2, RoundingMode.HALF_UP)`，否则遇到除不尽会直接抛 `ArithmeticException`。
3. **比较大小用 `compareTo()` 而不是 `equals()`**
   `equals` 会连 scale 一起比，`1.0` 和 `1.00` 会判为不相等。
4. **金额计算也可以用「以分为单位的长整型 `long`」**
   这是很多大厂的实际做法，避免 BigDecimal 的性能开销。
