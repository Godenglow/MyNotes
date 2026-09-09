# JavaSE 基础问答笔记

> 来源：动力节点 JavaSE 教程 · 课堂答疑整理
> 整理日期：2026-08-31
> 适用：Obsidian 阅读
> 范围：基本数据类型、类型转换、Scanner、运算符、包机制、对象与内存、构造方法、this 关键字、继承、方法覆盖、多态、抽象类、接口、访问控制权限、内部类、main 参数与可变长参数、单元测试、异常体系、自定义异常

---

> 配套：[[JavaSE]]

## 目录

1. [[#一、八种基本数据类型总览|八种基本数据类型总览]]
2. [[#二、局部变量与成员变量的默认值|局部变量与成员变量的默认值]]
3. [[#三、为什么 long z = 2147483648 会报错|为什么 long z = 2147483648 会报错]]
4. [[#四、为什么 float f = 3.0 会报错|为什么 float f = 3.0 会报错]]
5. [[#五、浮点数为什么不能用 == 比较|浮点数为什么不能用 == 比较]]
6. [[#六、char 字符型要点|char 字符型要点]]
7. [[#七、转义字符有什么用|转义字符有什么用]]
8. [[#八、byte / short / char 运算为什么会报错|byte / short / char 运算为什么会报错]]
9. [[#九、Scanner 的 nextXxx 怎么选|Scanner 的 nextXxx 怎么选]]
10. [[#十、&& 与 & 有什么区别|&& 与 & 有什么区别]]
11. [[#十一、package 与 import 怎么用|package 与 import 怎么用]]
12. [[#十二、对象的创建与 JVM 内存分析|对象的创建与 JVM 内存分析]]
13. [[#十三、构造方法|构造方法]]
14. [[#十四、this 关键字|this 关键字]]
15. [[#十五、继承（extends）基本概念|继承（extends）基本概念]]
16. [[#十六、方法覆盖（Override）|方法覆盖（Override）]]
17. [[#十七、多态（Polymorphism）|多态（Polymorphism）]]
18. [[#十八、抽象类（abstract）|抽象类（abstract）]]
19. [[#十九、接口（interface）基础|接口（interface）基础]]
20. [[#二十、接口 vs 抽象类（终极对比）|接口 vs 抽象类（终极对比）]]
21. [[#二十一、访问控制权限（4 个修饰符）|访问控制权限（4 个修饰符）]]
22. [[#二十二、内部类（4 种）|内部类（4 种）]]
23. [[#二十三、main 方法 args 与可变长参数|main 方法 args 与可变长参数]]
24. [[#二十四、单元测试（JUnit 5）|单元测试（JUnit 5）]]
25. [[#二十五、异常继承结构（Throwable 体系）|异常继承结构（Throwable 体系）]]
26. [[#二十六、自定义异常|自定义异常]]
27. [[#二十七、正则表达式常用符号|正则表达式常用符号]]
28. [[#二十八、泛型（Generics）|泛型（Generics）]]
29. [[#二十九、泛型的使用：类 / 静态方法 / 接口|泛型的使用：类 / 静态方法 / 接口]]
30. [[#三十、泛型通配符与 PECS|泛型通配符与 PECS]]
31. [[#三十一、迭代时删除元素与 fail-fast 机制|迭代时删除元素与 fail-fast 机制]]
32. [[#三十二、Map 继承结构与三大家族|Map 继承结构与三大家族]]
33. [[#三十三、Set 的底层真相（Set 就是 Map 的 key）|Set 的底层真相（Set 就是 Map 的 key）]]
34. [[#三十四、HashMap：key 去重机制与自定义 key 陷阱|HashMap：key 去重机制与自定义 key 陷阱]]
35. [[#三十五、HashMap 底层：哈希表与源码|HashMap 底层：哈希表与源码]]
36. [[#三十六、进程与线程概述|进程与线程概述]]
37. [[#三十七、JVM 与 Java 程序运行原理|JVM 与 Java 程序运行原理]]

---

## 一、八种基本数据类型总览

> **一句话**：8 种 primitive 类型，整数默认用 int，小数默认用 double。

### 总览表

| 类型 | 字节 | 取值范围 | 默认值 |
|------|------|----------|--------|
| byte | 1 | -128 ~ 127 | 0 |
| short | 2 | -32768 ~ 32767 | 0 |
| int | 4 | -2147483648 ~ 2147483647 | 0 |
| long | 8 | -2⁶³ ~ 2⁶³-1 | 0L |
| float | 4 | 约 ±3.4E38（6~7 位有效数字） | 0.0F |
| double | 8 | 约 ±1.8E308（15~16 位有效数字） | 0.0 |
| boolean | 1 | true / false | false |
| char | 2 | 0 ~ 65535（无符号） | '\u0000' |

### 要点

- 整数范围公式：n 位有符号 → `-2ⁿ⁻¹ ~ 2ⁿ⁻¹-1`
- 日常整数用 `int`，小数用 `double`
- boolean 在 Java 里**不能**和 0/1 互换（与 C 不同）
- char 是无符号 16 位，和 short 字节数相同但范围不同

### 速记

> 整数 4 兄弟：byte < short < int < long
> 小数 2 兄弟：float < double
> 外加 boolean（真假）与 char（字符）

---

## 二、局部变量与成员变量的默认值

> **一句话**：局部变量没有默认值，成员变量有默认值。

### 规则

| 变量位置 | 是否有默认值 | 未赋值就用 |
|----------|--------------|------------|
| 局部变量（方法内、代码块内） | ❌ 没有 | **编译报错** |
| 成员变量（类的属性） | ✅ 有 | 按类型默认值 |

### 示例

```java
public class Test {
    int a;                // 成员变量

    void method() {
        int b;            // 局部变量
        System.out.println(a);  // ✅ 输出 0（自动默认值）
        System.out.println(b);  // ❌ 编译错误：可能尚未初始化变量 b
    }
}
```

### 原因

- 成员变量随对象在**堆**中创建，JVM 会整体清零初始化
- 局部变量在**栈**上，JVM 为性能不做清理
- 「使用前必须赋值」是**编译器**的强制安全检查，不是运行时检查

### 速记

> 方法里的变量，先赋值再用；不确定的话一律显式写 `int b = 0;`

---

## 三、为什么 long z = 2147483648 会报错

> **一句话**：报错在「字面量合法性」阶段，不在赋值转换阶段。

### 规则

**整数类型字面量默认当做 int 类型处理。**

处理顺序：

1. 编译器看到 `2147483648`，**还没有任何赋值动作**
2. 按规则把它当 int 处理
3. 检查：int 最大值是 2147483647，`2147483648` 超范围
4. 还没轮到赋值给 `z`，编译就失败了

### 对比

| 代码 | 结果 | 原因 |
|------|------|------|
| `long a = 10;` | ✅ | 合法的 int 字面量，int → long 自动拓宽 |
| `long b = 2147483648;` | ❌ | 字面量本身超 int 范围 |
| `long c = 2147483648L;` | ✅ | `L` 让字面量直接成为 long 类型 |

### 要点

- `L` 的作用是告诉编译器「别按 int 处理，直接按 long 处理」
- 习惯用**大写 `L`**，小写 `l` 容易被看成数字 `1`

### 速记

> 超过 int 范围的整数，字面量必须带 `L`

---

## 四、为什么 float f = 3.0 会报错

> **一句话**：浮点字面量默认是 double，double → float 是大转小，不允许自动收窄。

### 规则

**浮点类型字面量默认当做 double 类型处理。**

### 与 long 案例的区别（重点）

| 代码 | 字面量默认类型 | 报错原因 |
|------|----------------|----------|
| `long z = 2147483648;` | int | 字面量**超 int 范围**，int 自己装不下 |
| `float f = 3.0;` | double | `3.0` 作为 double 合法，但 **double → float 大转小** |

两个报错「病因」不同，但解法一致：**加后缀让字面量出生就正确**。

### 示例

```java
float f = 3.0F;    // ✅ 字面量直接是 float 类型
double d = 3.0;    // ✅ 或干脆用 double，什么都不用加
double d2 = 1.5656856894;   // 输出 1.5656856894（原样）
float  f2 = 1.5656856894F;  // 输出 1.5656857（被舍入）
```

### 精度对比

- float：4 字节，约 **6~7 位**有效数字
- double：8 字节，约 **15~16 位**有效数字

超出精度的位数会被舍入 → 实际开发**小数优先用 double**。

### 速记

> 整数默认 int（超范围加 `L`），小数默认 double（转 float 加 `F`）

---

## 五、浮点数为什么不能用 == 比较

> **一句话**：浮点是近似值，用 `==` 比较会翻车，改用误差范围（epsilon）。

### 规则

float / double 按 IEEE 754 标准存储，**本质都是近似值**，大部分十进制小数无法用二进制精确表示。

### 示例

```java
double x = 6.9;
double y = 3.0;
double z = x / y;      // 数学上应为 2.3，实际是 2.3000000000000003

if (z == 2.3) {        // ❌ false，逐位比较被误差击穿
}
```

### 正确写法

```java
if (Math.abs(z - 2.3) < 0.000001) {   // ✅ 差值在容差内就算相等
    System.out.println("相等");
}
```

注意：只写 `z - 2.3 < 0.000001` 没取绝对值，**比目标小很多的值也会通过**——差值恒为负、必然 < 0.000001，如 `1.0/3.0` ≈ 0.333 也会被判「相等」，必须加 `Math.abs()`。

### 其他常见坑

```java
double sum = 0.1 + 0.2;
sum == 0.3;                     // false，实际 0.30000000000000004

double d = 5 / 2;               // 2.0，不是 2.5（整数除法先算完再转）
double d2 = 5.0 / 2;            // 2.5 ✅

new BigDecimal("1.0").equals(new BigDecimal("1.00"));  // false！scale 不同
// BigDecimal 比较用 compareTo() == 0
```

### 速记

| 场景                | 做法                          |
| ----------------- | --------------------------- |
| float / double 比较 | `Math.abs(a - b) < epsilon` |
| 金钱、精确小数           | `BigDecimal`                |
| 想用 `==` 比浮点       | 默认不写                        |

---

## 六、char 字符型要点

> **一句话**：Java 的 char 是 2 字节 Unicode 字符，本质是 0~65535 的无符号整数。

### 规则

- 占用 **2 字节**，范围 **0 ~ 65535**（无符号）
- 与 short 字节数相同，但 short 是 -32768 ~ 32767（有符号）
- 用**单引号**，且**只能一个字符**
- 可以保存一个汉字（中文也占一个 Unicode 字符）
- 默认值是空字符 `'\u0000'`

### 示例

```java
char c1 = 'A';        // ✅
char c2 = "A";        // ❌ 双引号是 String
char c3 = 'AB';       // ❌ char 只能存一个字符
char c4 = '中';       // ✅ 可以存汉字
char c5 = '';         // ❌ 单引号内必须有一个字符
char c6 = '\u0000';   // ✅ 空字符，也是默认值

int i = 'A';          // ✅ char → int 自动提升，i = 65
char c = 20013;       // ✅ 20013 是 '中' 的 Unicode 码点
```

### 空字符 vs 空格字符

| 名称 | 写法 | 含义 |
|------|------|------|
| 空字符 | `'\u0000'` | 无内容，占位置不可见 |
| 空格字符 | `' '` | 真实空白，显示为空格 |

### 速记

> char = 2 字节 Unicode，单引号包一个字符，默认 `\u0000`

---

## 七、转义字符有什么用

> **一句话**：`\n`、`\\`、`\"` 是高频三件套，写字符串、路径、正则时天天见。

### 常用对照表

| 转义 | 含义 | 典型场景 |
|------|------|----------|
| `\n` | 换行 | 多行输出、日志拼接 |
| `\t` | 制表符 | 表格式对齐输出 |
| `\"` | 双引号 | 字符串里嵌套引号 |
| `\'` | 单引号 | char / 字符串里的单引号 |
| `\\` | 反斜杠 | Windows 路径、正则表达式 |

### 示例

```java
System.out.println("第一行\n第二行");
// 第一行
// 第二行

System.out.println("姓名\t年龄\nAlice\t20");
// 姓名  年龄
// Alice 20

String s = "他说：\"你好\"";              // 输出：他说："你好"
String path = "C:\\Users\\29074\\Desktop"; // 实际是一个 \
```

### 要点

- `"` 是字符串边界，字符串内写 `"` 必须用 `\"` 转义
- Windows 路径本来用 `\`，但 `\` 又是转义符，所以写一个真反斜杠要写 `\\`

### 速记

> 字符串里想写「特殊符号」，前面加 `\`

---

## 八、byte / short / char 运算为什么会报错

> **一句话**：字面量默认是 int，且小类型一参与运算就变 int，双重保险 → 结果必然是 int。

### 两条核心规则

| 规则 | 内容 |
|------|------|
| ① | **整数字面量默认是 int**，`1`、`99`、`100` 全是 int |
| ② | **byte / short / char 参与算术运算时，一律先提升成 int** |

Java 里**没有 byte 字面量、没有 short 字面量**，也没有对应后缀，压根不存在。

### 示例

```java
short s = 100;
s = s - 99;          // ❌ 结果是 int

byte b = 100;
b = b + 1;           // ❌ 结果是 int

byte a1 = 1;
byte a2 = 2;
byte c = a1 + a2;    // ❌ 没有字面量参与，照样报错！

// 正确写法
s = (short)(s - 99);
b = (byte)(b + 1);
b++;                 // ✅ 自增运算符底层帮你强转
b += 1;              // ✅ 复合赋值运算符自动强转
```

### 混合类型运算

```java
char c = 'a';
int i = 20;
float f = .3F;

double d = c + i + f;   // ✅
// 提升链：char → int → float → double
// 等价：double d = (double)((float)((int)c + i) + f);

byte b = 100;
short s = 100;

short x = b + s;              // ❌ byte + short 结果仍是 int
x = (short)(b + s);           // ✅ 强转后再赋值
```

### 常量赋值的例外

```java
short s = 100;   // ✅ 常量直接赋值，值在范围内 → 自动窄化
byte  b = 100;   // ✅ 同上
```

### 为什么这样设计

byte / short 运算极易溢出（`100 + 100 = 200` 已超 byte 最大值 127）。
JVM 规定小整数运算统一在 int 层面进行，避免中间结果溢出 —— 代价是必须手动强转。

### 速记

> 常量直接赋值 → 范围内自动过
> 变量参与运算 → 结果至少是 int，塞回小类型必须强转

---

## 九、Scanner 的 nextXxx 怎么选

> **一句话**：要什么类型就叫什么方法名，但 `nextInt()` 后接 `nextLine()` 要清换行符。

### 方法对照表

| 方法 | 返回类型 | 读取内容 |
|------|----------|----------|
| `next()` | String | 一个「单词」，以空格 / Tab / 换行为分隔 |
| `nextLine()` | String | 一整行，包含空格，直到换行符 |
| `nextInt()` | int | 一个整数 |
| `nextLong()` | long | 一个长整数 |
| `nextDouble()` | double | 一个小数 |
| `nextFloat()` | float | 一个单精度小数 |
| `nextByte()` | byte | 一个 byte |
| `nextShort()` | short | 一个 short |
| `nextBoolean()` | boolean | true / false |

### 没有 nextChar()

```java
char c = scanner.next().charAt(0);   // 先读字符串，再取第一个字符
```

### 大坑：nextInt() 吞不掉换行符

```java
scanner.nextInt();     // 输入 18 后按回车
scanner.nextLine();    // ❌ 读到空字符串，不是下一行输入
```

**原因**：`nextInt()` 只读数字，没读走末尾的换行符；`nextLine()` 一看到换行符就认为「一行读完了」。

**解决**：中间插一个 `nextLine()` 吃掉残留换行符。

### 完整示例

```java
import java.util.Scanner;

public class Demo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("请输入年龄：");
        int age = scanner.nextInt();
        scanner.nextLine();              // 清理换行符

        System.out.print("请输入姓名：");
        String name = scanner.nextLine();

        System.out.println(name + " 今年 " + age + " 岁");
        scanner.close();
    }
}
```

### 速记

> `nextInt()` 后要接 `nextLine()`，中间补一句 `nextLine()` 清空换行

---

## 十、&& 与 & 有什么区别

> **一句话**：`&&` 短路更高效，但 `&` 在「右边必须执行」和位运算场景下不可替代。

### 对照表

| 运算符 | 是否短路 | 行为 |
|--------|----------|------|
| `&&` | ✅ 是 | 左边 false → 右边**不执行** |
| `&` | ❌ 否 | 不管左边，右边**一定执行** |
| `\|\|` | ✅ 是 | 左边 true → 右边**不执行** |
| `\|` | ❌ 否 | 不管左边，右边**一定执行** |
| `^` | — | 异或（两边不同才为 true） |

### 什么时候必须用 &

**右边有副作用、必须执行时**（如参数校验希望把所有错误都报出来）：

```java
if (checkA(x) && checkB(x)) { }   // A 失败 → B 不执行
if (checkA(x) &  checkB(x)) { }   // A 失败 → B 仍然执行
```

### 位运算只能用 & | ^

`&&` 没有位运算功能：

```java
int a = 5;   // 二进制 101
int b = 3;   // 二进制 011

int c = a & b;   // 001 → 1  按位与
int d = a | b;   // 111 → 7  按位或
int e = a ^ b;   // 110 → 6  按位异或
```

### 选择建议

| 场景 | 用哪个 |
|------|--------|
| 普通逻辑判断，只求结果 | `&&` / `\|\|`（效率高） |
| 右边有必须执行的副作用 | `&` / `\|` |
| 二进制位运算 | 只能 `&` / `\|` / `^` |

### 速记

> 效率不是唯一标准，需求决定用哪个 —— 别无脑把 `&` 全换成 `&&`

---

## 十一、package 与 import 怎么用

> **一句话**：`package` 是给类贴「地址标签」，`import` 是根据地址去「找人」。

### package：类的文件夹地址

```java
package com.powernode.javase.chapter02;

public class PackageTest {
    // ...
}
```

**规则**

- `package` 必须是 Java 文件的**第一行**
- 一个文件只能有一个 package
- 包名**全小写**：`公司域名倒序 + 项目名 + 模块名 + 功能名`
  - 动力节点域名 `powernode.com` → 倒序 `com.powernode`
  - 例：`com.powernode.oa.empgt.service`

**目录结构**

```
项目/
└── com/
    └── powernode/
        ├── javase/
        │   └── chapter02/
        │       └── PackageTest.java
        └── oa/
            └── empgt/
                └── service/
                    └── EmployeeService.java
```

物理路径必须与 package 声明**一一对应**，编译器靠这个路径找类。

### 带 package 的编译与运行

```bash
javac -d . PackageTest.java                              # -d 指定 class 文件输出目录
java com.powernode.javase.chapter02.PackageTest          # 运行要写完整类名
```

> **完整类名 = 包名 + 类名**

### import：引入其他包的类

```java
package com.example.service;

import com.example.dao.UserDao;   // 引入另一个包里的类

public class UserService {
    UserDao userDao = new UserDao();
}
```

**规则**

- import 写在 **package 之后、class 之前**
- 可以写多个 import
- `java.lang` 包下的类**默认自动导入**，不用写（`String`、`System` 等）
- 模糊导入 `import java.util.*;` 只导当前这一层，**不递归子包**

### 静态导入（少见，知道即可）

```java
import static java.lang.System.*;

public class Test {
    public static void main(String[] args) {
        out.println("hello");   // 不用写 System.out
    }
}
```

可读性差，日常不建议使用。

### 速记

| 关键字 | 作用 | 位置 |
|--------|------|------|
| `package` | 声明这个类属于哪个包 | 文件第一行 |
| `import` | 引入其他包里的类 | package 之后、class 之前 |

| 情况 | 是否需要 import |
|------|----------------|
| 同包下的类 | ❌ 不需要 |
| 不同包下的类 | ✅ 需要 |
| `java.lang` 下的类 | ❌ 不需要 |

---

## 十二、对象的创建与 JVM 内存分析

> **一句话**：引用在栈里，对象在堆里，类的元数据在元空间；方法结束栈帧销毁，对象靠 GC 回收。

### 6 条核心结论

| # | 结论 | 说明 |
|---|------|------|
| ① | `new` 在**堆**中分配空间 | 这块空间 + 里面的实例变量 = Java 对象 |
| ② | 对象有内存地址，保存地址的变量叫**引用** | 引用不是对象，只是「门牌号」 |
| ③ | GC 主要针对**堆内存** | 清理没有任何引用指向的对象 |
| ④ | **空指针异常** | 引用为 `null` 却去访问对象的属性 / 方法 |
| ⑤ | 方法传参 = **复制一份值** | 基本类型复制数据，引用类型复制地址 |
| ⑥ | `this` 代表**当前对象** | 在实例方法中，通常可省略；存于栈帧局部变量表 0 号槽位 |

### 图示 1：方法调用时引用被复制传参

![[jvm-mem-01-ref-passing.svg]]

### 图示 2：方法结束，栈帧销毁但对象还在

```java
public static void add(User u) {   // u 是 main 中 u 的副本，地址都是 0x12
    u.age++;                       // 改的是堆里同一个对象，main 看得到
}
// add 结束 → add 栈帧销毁 → 但堆里的 User 对象仍在（main 的 u 还指着它）
```

![[jvm-mem-02-frame-destroyed.svg]]

**注意**：在 `add` 内部写 `u = null`，**不会影响** main 的 `u` —— 改的只是副本。

### 图示 3：Java 8 之后的三块内存区域

![[jvm-mem-03-java8-memory.svg]]

> 类对象（`.class` 的运行时表示）也在堆中，类的**元数据**在元空间 Metaspace（使用本地内存）。

### 图示 4：引用断开 → 对象变垃圾 → GC 回收

```java
Pet dog = new Pet("小黑", "2012-10-11", '雄');
dog = null;               // 引用断开
System.out.println(dog.name);   // ❌ NullPointerException
```

![[jvm-mem-04-null-gc.svg]]

### 参数传递的本质

| 参数类型 | 传递的内容 | 方法内修改的影响 |
|----------|------------|------------------|
| 基本类型 | 数据值的副本 | 不影响原变量 |
| 引用类型 | 地址的副本 | 改**对象内容**会影响；改**引用本身**（如 `u = null`）不影响 |

### this 关键字

```java
public class Student {
    String name;
    public void setName(String name) {
        this.name = name;      // this.name = 当前对象的 name
    }
}
```

- `this` 是引用，指向**当前正在调用该方法的对象**
- 编译后存放在**实例方法栈帧局部变量表的 0 号槽位**
- 大部分情况下 `this.` 可以省略，仅当**局部变量与成员变量同名**时必须写

### 速记

> 对象在堆，引用在栈，类信息在元空间
> 方法结束栈帧销毁，对象没人指就 GC
> 传参一律传副本，改内容生效、改引用不生效

---

## 十三、构造方法

> **一句话**：`new` 对象时自动调用、专门用来初始化对象的特殊方法。

### 作用

对象创建分两个阶段，**不能颠倒、不可分割**：

1. **创建阶段**：`new` 在堆里开辟空间，给属性赋**默认值**
2. **初始化阶段**：执行构造方法，把属性改成**你想要的值**

```java
Student s = new Student("张三", 20);
// ① new 在堆中创建对象
// ② 调用 Student("张三", 20) 初始化对象
```

### 定义三要素

```java
public class Student {
    String name;
    int age;

    // 构造方法：没有返回值，方法名必须和类名一样
    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }
}
```

| 要点 | 说明 |
|------|------|
| 没有返回值 | 连 `void` 都不能写 |
| 方法名 = 类名 | 大小写必须完全一致 |
| 可重载 | 参数列表不同即可 |

### 调用方式

构造方法不是用 `.方法名()` 调用，而是跟在 `new` 后面：

```java
Student s = new Student("张三", 20);
```

### 无参构造的坑（重点）

**如果一个构造方法都没写，Java 会自动送你一个无参构造；一旦你写了任意构造方法，系统就不再送了。**

```java
public class Student {
    String name;
    int age;

    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }
}

Student s1 = new Student("张三", 20);   // ✅
Student s2 = new Student();              // ❌ 编译报错！无参构造已消失
```

**建议**：不管需不需要，都显式把无参构造写出来。

```java
public Student() {}   // 手动加上，避免后续踩坑
```

### 重载示例

```java
public class Student {
    String name;
    int age;

    public Student() {}                              // 无参
    public Student(String name) { this.name = name; } // 一个参数
    public Student(String name, int age) {            // 两个参数
        this.name = name;
        this.age = age;
    }
}
```

### 构造代码块

类里用 `{}` 包起来的代码，**每次创建对象时都会执行**，而且在构造方法之前执行。

```java
public class Student {
    String name;

    // 构造代码块
    {
        System.out.println("构造代码块执行");
    }

    public Student(String name) {
        System.out.println("构造方法执行");
        this.name = name;
    }
}

new Student("张三");
// 输出：
// 构造代码块执行
// 构造方法执行
```

### 对象初始化全过程

![[java-obj-init-order.svg]]

1. `new` 在堆中开辟空间，属性赋默认值
2. 执行**构造代码块**
3. 执行**构造方法体**
4. 构造方法结束，对象初始化完成

### 速记

> 构造方法 = 没有返回值 + 方法名同类名 + new 时自动调用
> 建议无参构造显式写，否则写了有参构造后默认无参会消失

---

## 十四、this 关键字

> **一句话**：`this` 是指向当前对象的引用。

### this 是什么

`this` 本质上是一个**引用变量**，保存着**当前正在调用方法的那个对象**的内存地址。

```java
public class Student {
    String name;

    public void show() {
        System.out.println(this);     // 打印当前对象的地址
        System.out.println(this.name);
    }
}
```

### this 能干嘛

通过 `this.` 可以访问实例变量、调用实例方法：

```java
public class Student {
    String name;

    public void setName(String name) {
        this.name = name;            // this.name = 当前对象的 name
    }

    public void sayHello() {
        this.study();                // 调用当前对象的 study 方法
    }

    public void study() {
        System.out.println(name + " 在学习");
    }
}
```

### this. 什么时候可以省略

大部分情况下，`this.` 可以省略：

```java
public void study() {
    System.out.println(this.name);   // ✅ 完整写法
    System.out.println(name);        // ✅ 省略写法，效果一样
}
```

**不能省略**的情况：**局部变量和实例变量同名**。

```java
public void setName(String name) {
    name = name;      // ❌ 两个都是参数 name，没意义
    this.name = name; // ✅ 左边是当前对象的 name，右边是参数 name
}
```

### this 不能出现在静态方法中

```java
public class Student {
    String name;

    public static void test() {
        // System.out.println(this.name);   // ❌ 编译报错
    }
}
```

**原因**：静态方法属于类，不属于某个对象；调用时可能根本不存在对象，`this` 就没有指向。

### this(实参) 调用其他构造方法

`this(实参)` 只能出现在**构造方法的第一行**，用来调用本类中另一个构造方法，避免重复写代码。

```java
public class Student {
    String name;
    int age;

    // 无参构造调用有参构造
    public Student() {
        this("张三", 20);   // ✅ 必须是第一行
    }

    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }
}
```

**注意**：
- `this(...)` 和 `super(...)` 都必须放在构造方法**第一行**
- 所以一个构造方法里**不能同时出现** `this(...)` 和 `super(...)`

### this 存储在哪

编译后，`this` 被放在**实例方法栈帧局部变量表的 0 号槽位**。每个实例方法被调用时，JVM 都会悄悄把当前对象的引用塞进去。

### 速记

> `this` = 指向当前对象的引用；同名时必须写，静态方法里不能用，`this(实参)` 调别的构造方法且必须放第一行

---

## 十五、继承（extends）基本概念

> **一句话**：`extends` 让子类直接拥有父类的属性和方法，**Java 只支持单继承**，没写 `extends` 就默认继承 `java.lang.Object`。

### 继承的作用

| 层次 | 作用 | 说明 |
|------|------|------|
| 基本作用 | **代码复用** | 不用把父类的属性、方法再抄一遍 |
| 重要作用 | **铺垫方法覆盖和多态** | 没有继承 → 没有方法覆盖 → 没有多态 |

### 语法

```java
[修饰符列表] class 子类名 extends 父类名 {
    // 类体
}
```

`extends` 翻译为**扩展**：子类继承父类后，是对父类的**扩展**，不是简单复制。

### 术语对照

以「猫继承动物」为例：

| 角色 | 类名 | 别名 |
|------|------|------|
| 被继承的 | `Animal` | 父类 / 超类 / 基类 / **superclass** |
| 去继承的 | `Cat` | 子类 / 派生类 / **subclass** |

### 三条硬性限制

| # | 限制 | 说明 |
|---|------|------|
| ① | **只支持单继承** | 一个类只能 `extends` 一个直接父类 |
| ② | **不支持多继承** | `class C extends A, B` → ❌ 编译报错 |
| ③ | **支持多层继承** | `A → B → C` 逐级往下 ✅ 合法 |

```java
class A {}
class B {}

class C extends A, B { }        // ❌ 多继承，编译报错
class D extends A { }            // ✅ 单继承
class E extends D { }            // ✅ 多层继承（E 的父类是 D，祖宗是 A）
```

### 哪些成员被继承

| 成员类型 | 是否被继承 | 说明 |
|----------|------------|------|
| public / protected 属性、方法 | ✅ 继承 | 子类可直接访问 |
| **private** 属性、方法 | ⚠️ **继承下来但不可直接访问** | 内存里存在，被 `private` 锁住 |
| **构造方法** | ❌ **不继承** | 每个类有自己独立的构造方法列表 |
| 默认（包）访问权限 | 看是否同包 | 跨包访问不到 |

> ⚠️ 常见误解：「private 的不被继承」——**不准确**。private 成员确实存在于子类对象中（占内存），
> 只是子类代码**没有权限直接访问**，需要靠父类提供的 `getter / setter` 间接操作。

```java
class Father {
    private int money = 100;      // 私有
    public String name = "老王";
}

class Son extends Father {
    void test() {
        System.out.println(name);    // ✅ 老王（public 继承可用）
        System.out.println(money);   // ❌ 编译报错：money 在 Father 中是 private
    }
}
```

### 默认继承 Object

一个类**没有显式继承任何类**时，编译器自动补上 `extends java.lang.Object`：

```java
class Animal { }                                  // 等价 → class Animal extends Object { }
class Animal extends Object { }                   // 手写也行，但没人这么写
```

`Object` 是 Java 类体系的**根**，所有类（数组、字符串、自定义类）都是它的后代。

### 图示：继承层级

![[inheritance-hierarchy.svg]]

### 示例

```java
class Animal {                      // 父类（没写 extends → 默认继承 Object）
    public String name;
    public void eat() {
        System.out.println("吃");
    }
}

class Cat extends Animal {          // 子类，extends = 扩展
    public void catchMouse() {      // 子类自己的新方法
        System.out.println("抓老鼠");
    }
}

public class Test {
    public static void main(String[] args) {
        Cat c = new Cat();
        c.name = "Tom";             // ✅ 继承自父类的属性
        c.eat();                    // ✅ 继承自父类的方法（代码复用）
        c.catchMouse();             // ✅ 子类扩展的方法
    }
}
```

### 速记

> `extends` 是扩展不是复制；一个类只能认一个爹，但可以一代传一代
> private 继承下来但用不了，构造方法压根不继承
> 没写 `extends` 就默认继承 `Object`

---

## 十六、方法覆盖（Override）

> **一句话**：父子类之间、方法签名完全相同、权限不变低、异常不变多 —— 满足这四条才是方法覆盖，作用是用子类实现**替换**父类实现。

### 什么时候用方法覆盖

只有一种情况：**从父类继承过来的方法，满足不了子类的业务需求**时。

- 想"用"父类方法 → 直接继承，不用覆盖
- 想"改"父类方法 → 覆盖，换掉实现

### 方法覆盖的 5 个条件

| # | 条件 | 说明 |
|---|------|------|
| ① | **有继承关系的父子类之间** | 没有继承就只是普通新方法 |
| ② | **方法签名完全相同** | 方法名相同 + 形式参数列表相同（个数、类型、顺序） |
| ③ | **访问权限不能变低，可以变高** | 父类 `protected` → 子类可 `public`，**不能**变 `private` |
| ④ | **抛出的异常不能变多，可以变少** | 子类异常必须是父类异常的子类或子集 |
| ⑤ | **返回值类型相同或协变** | 返回值可以是父类方法返回值的**子类**（Java 5+ 协变返回） |

```java
class Animal {
    protected Animal eat() throws Exception {    // 父类：protected + 抛 Exception
        return this;
    }
}

class Cat extends Animal {
    @Override
    public Cat eat() throws IOException {        // ✅ 权限变高 + 异常变少 + 返回值协变
        return this;
    }
}
```

### 5 个易踩坑的细节

| # | 细节 | 原因 |
|---|------|------|
| ① | `@Override` 让编译器**检查是否真的重写** | 写错方法名会编译报错，建议永远加 |
| ② | **private 方法不能覆盖** | private 不继承 → 子类看不见 → 同名只是新方法 |
| ③ | **构造方法不能覆盖** | 构造方法压根不继承 |
| ④ | **静态方法不存在覆盖** | 静态方法属于类，不存在多态，同名叫「隐藏」 |
| ⑤ | **实例变量无关覆盖** | 变量是静态绑定，看引用类型，不是运行时对象 |

### 细节 ①：@Override 注解

```java
class Cat extends Animal {
    @Override
    public void eat() { }        // 如果父类没有 eat()，编译直接报错
}
```

不加 `@Override` 也能重写，但**失去编译期检查**。写错方法名（如 `eats()`）会变成"新增方法"，逻辑静默失效，很难查。

### 细节 ②③④：private / 构造方法 / 静态

```java
// ② private：不是覆盖
class Father { private void show() { } }
class Son extends Father { private void show() { } }   // Son 自己的新方法

// ④ static：不是覆盖，是隐藏
class Father { public static void m() { } }
class Son extends Father { public static void m() { } } // 隐藏，看引用类型调用
```

### 细节 ⑤：实例变量不存在覆盖 ⭐ 高频坑

```java
class Father {
    int count = 10;
    public void method() { System.out.println("父类方法"); }
}

class Son extends Father {
    int count = 20;
    public void method() { System.out.println("子类方法"); }
}

Father obj = new Son();              // 父类型引用 → 子类对象

System.out.println(obj.count);       // 10   ← 静态分派：看引用类型 Father
obj.method();                        // 子类方法  ← 动态分派：看实际对象 Son
```

**同名变量和方法同时存在，结果可能不一致** —— 这是面试高频坑。

![[override-dispatch.svg]]

### 覆盖 vs 隐藏 vs 重载（三个概念别混）

| 现象 | 叫法 | 分派方式 | 决定因素 |
|------|------|----------|----------|
| 父子类同名**实例方法** | **Override 覆盖** | 动态分派（运行期） | 实际对象类型 |
| 父子类同名**静态方法** | Hide 隐藏 | 静态分派（编译期） | 引用类型 |
| 父子类同名**成员变量** | Hide 隐藏 | 静态分派（编译期） | 引用类型 |
| 同类中同名不同参 | **Overload 重载** | 静态分派（编译期） | 参数列表 |

覆盖（Override）与重载（Overload）对比：

| 维度 | 覆盖 Override | 重载 Overload |
|------|---------------|---------------|
| 发生位置 | 父子类之间 | **同一个类**中 |
| 方法名 | 必须相同 | 必须相同 |
| 参数列表 | 必须**相同** | 必须**不同** |
| 返回类型 | 相同或协变 | 无关 |
| 访问权限 | 不能变低 | 无关 |
| 绑定时机 | 运行期 | 编译期 |

```java
// 重载：同一个类，参数不同
class Calculator {
    int add(int a, int b)       { return a + b; }
    double add(double a, double b) { return a + b; }   // ✅ 重载
}

// 覆盖：父子类，签名完全相同
class Animal { void cry() { System.out.println("叫"); } }
class Cat extends Animal { @Override void cry() { System.out.println("喵"); } }
```

### 完整示例

```java
class Animal {
    public Animal eat() {
        System.out.println("动物在吃");
        return this;
    }
}

class Cat extends Animal {
    @Override
    public Cat eat() {                 // 协变返回：Cat 是 Animal 的子类
        System.out.println("猫在吃鱼");
        return this;
    }
}

public class Test {
    public static void main(String[] args) {
        Animal a = new Cat();          // 多态：父类型引用指向子类对象
        Animal r = a.eat();            // 输出「猫在吃鱼」—— 动态分派到 Cat.eat()
    }
}
```

### 速记

> 覆盖四要素：父子之间 + 签名相同 + 权限不变低 + 异常不变多（返回值可协变）
> private / 构造方法 / 静态方法 都不能覆盖，**实例变量也不存在覆盖**
> 变量看左边（引用类型），方法看右边（实际对象）
> 永远加 `@Override`，防拼写错

---

## 十七、多态（Polymorphism）

> **一句话**：父类型引用指向子类对象（`Animal a = new Cat()`），**编译期看左边类型、运行期看右边对象**，同一个调用呈现两种形态 —— 这就是多态。

### 多态的三个前提（缺一不可）

| 前提 | 缺了会怎样 |
|------|------------|
| ① 有**继承**关系 | 转型编译不通过 |
| ② 有**方法覆盖** | 调到的是父类方法，多态没意义 |
| ③ **父类型引用指向子类对象** | 这是多态的语法形态 |

> 关系链：**继承 → 方法覆盖 → 多态**。覆盖是多态的语法基础，多态是覆盖的应用。

### 向上转型 / 向下转型

| 转型 | 方向 | 语法 | 是否强转 | 安全性 |
|------|------|------|----------|--------|
| **向上转型** upcasting | 子 → 父 | `Animal a = new Cat();` | ❌ 自动 | ✅ 永远安全 |
| **向下转型** downcasting | 父 → 子 | `Cat c = (Cat) a;` | ✅ 必须加 `(Cat)` | ⚠️ 有 ClassCastException 风险 |

**前提**：两种类型之间必须存在**继承关系**，否则编译器直接报错。

- **向上安全**：猫一定是动物（`Cat is-a Animal`），小范围转大范围不会丢信息
- **向下危险**：动物不一定是猫，大范围转小范围可能"认错对象"

### 多态的两阶段 ⭐ 核心机制

```java
Animal a = new Cat();   // 父类型引用 → 子类对象
a.move();               // 编译期看 Animal，运行期看 Cat
```

| 阶段 | 看什么 | 绑定方式 | 别名 |
|------|--------|----------|------|
| **编译阶段** | 引用**左边**的静态类型（`Animal`） | 静态绑定 | early binding |
| **运行阶段** | 堆中**右边**的实际对象（`Cat`） | 动态绑定 | late binding |

![[polymorphism-two-phase.svg]]

**为什么叫"多态"**：编译期一种形态（`Animal.move()`），运行期另一种形态（`Cat.move()`），**两种形态 → 多态**。

> 承接上一条：变量看左、静态方法看左、**实例方法看右**。
> 多态特指**实例方法的动态绑定**。

### 向下转型的坑：ClassCastException

```java
Animal a = new Cat();
Dog d = (Dog) a;        // 编译通过 ✅，运行抛 ClassCastException ❌
```

**原因**：编译期只检查 `Animal` 和 `Dog` 有没有继承关系（有 → 放行）；运行期才发现真实对象是 `Cat`，不是 `Dog`。

> **编译能过 ≠ 运行能过**，这是向下转型的核心警钟。

### instanceof 运算符

| 项 | 内容 |
|----|------|
| 语法 | `(引用 instanceof 类型)` |
| 返回值 | `true` / `false` |
| `true` | 引用指向的对象**是**该类型（或其子类） |
| `false` | 引用指向的对象**不是**该类型 |

**标准用法：向下转型前先判断**

```java
public void feed(Animal a) {              // 多态：参数用父类型
    if (a instanceof Cat) {
        Cat c = (Cat) a;                  // 先判断，再强转
        c.catchMouse();                   // 猫才有的方法
    } else if (a instanceof Dog) {
        Dog d = (Dog) a;
        d.guardHouse();
    }
    a.eat();                              // 多态：自动调子类实现
}
```

**Java 16+ 模式匹配（推荐新代码用）**

```java
if (a instanceof Cat c) {                 // 判断 + 转型一步到位
    c.catchMouse();                       // c 直接就是 Cat 类型
}
```

少一行强转、少一个临时变量，可读性更好。

### 多态在开发中的作用

**反例：不用多态**

```java
class Master {
    void feed(Cat c) { c.eat(); }     // 养猫
    void feed(Dog d) { d.eat(); }     // 养狗
    void feed(Pig p) { p.eat(); }     // 养猪
    // 养 100 种动物 → 写 100 个方法，Master 被绑死在具体类上
}
```

**正例：使用多态**

```java
class Master {
    void feed(Animal a) { a.eat(); }   // 一个方法搞定所有动物
}
// 新增 Rabbit 类 → Master 一行都不用改
```

| 收益 | 体现 |
|------|------|
| **降低耦合度** | Master 只依赖 `Animal` 抽象，不依赖具体子类 |
| **提高扩展力** | 新增子类不改调用方代码（对修改关闭、对扩展开放） |

> **面向抽象编程，不要面向具体编程** —— 参数、返回值、字段类型，能用父类型就别写死子类型。

### 速记

> 多态 = 继承 + 覆盖 + 父引用指子对象，三者缺一不可
> 编译期看左（静态绑定），运行期看右（动态绑定），只有实例方法才动态绑定
> 向下转型前先 `instanceof`，ClassCastException 是懒人的回报
> 多态的价值：降耦合、提扩展；能写父类型就别写子类型

---

## 十八、抽象类（abstract）

> **一句话**：抽象方法是「只有声明、没有实现」的方法，有抽象方法的类必须声明为 `abstract`；**抽象类不能被 `new`，但有构造方法**，作用是当半成品模板逼子类实现细节。

### 什么时候定义抽象类

父类**知道有这么个方法，但不知道怎么实现** → 只声明、不实现 → 强制子类给出自己的实现。

| 例子 | 为什么父类实现不了 |
|------|--------------------|
| `Person.greet()` | 中国人说「你好」、英国人说「Hello」，实现取决于子类 |
| `Pet.eat()` | 不知道养的是什么宠物，`eat()` 方法体没意义 |

> **抽象类的本质：半成品模板** —— 父类规定「子类必须长这样」，不管「具体长什么样」。

### 定义语法

```java
public abstract class Animal {              // 抽象类
    protected String name;                  // ✅ 可以有成员变量

    public Animal(String name) {            // ✅ 可以有构造方法
        this.name = name;
    }

    public void sleep() {                   // ✅ 可以有普通方法（有方法体）
        System.out.println(name + " 睡觉");
    }

    public abstract void eat();             // ✅ 抽象方法：只有声明，没有方法体
}
```

| 元素 | 语法 | 注意 |
|------|------|------|
| 抽象类 | `abstract class 类名 {}` | `abstract` 在 `class` 前 |
| 抽象方法 | `abstract 返回值类型 方法名(形参);` | **末尾是分号，不是 `{}`** |

### ③ 不能实例化，但有构造方法

```java
public abstract class Animal {
    public Animal() { }              // ✅ 可以有构造方法
}

Animal a = new Animal();             // ❌ 编译报错：Animal 是抽象的，无法实例化
```

> **抽象类的构造方法给子类用**：`new Cat()` 时子类构造方法第一行默认 `super()`，用来初始化从父类继承下来的属性。

### ⑤ 抽象类与抽象方法的关系

| 方向 | 是否成立 | 说明 |
|------|----------|------|
| 有抽象方法 → 类**必须**是抽象类 | ✅ 强制 | 编译器要求 |
| 抽象类 → **不一定**有抽象方法 | ✅ 可以没有 | 但没抽象方法还声明 abstract，逻辑上没意义 |

```java
abstract class A { }                       // ✅ 合法（但没什么用）
class B { abstract void m(); }              // ❌ 编译报错：含抽象方法的类必须声明为 abstract
```

### ⑥ 非抽象子类必须重写全部抽象方法

```java
abstract class Animal {
    public abstract void eat();
}

class Cat extends Animal {                  // Cat 是非抽象类
    @Override
    public void eat() {                     // ✅ 必须实现，否则编译报错
        System.out.println("猫吃鱼");
    }
}

abstract class Dog extends Animal {         // ✅ 自己也声明 abstract，可以暂不实现
    // 不实现 eat() 也合法，把"债"继续往下传
}
```

> **二选一**：子类要么**实现**所有抽象方法，要么**自己也声明 abstract**。

### ⑦ abstract 不能和这些关键字共存

| 搭配 | 为什么冲突 |
|------|------------|
| `abstract + private` | private 不继承 → 子类看不见 → 重写无从谈起 |
| `abstract + final` | final 禁止重写 → 与「抽象方法必须被重写」直接矛盾 |
| `abstract + static` | static 属于类、没有多态 → 「重写」无意义 |
| `abstract + native` | native 方法体在外部 → 与「强制子类重写」矛盾 |
| `abstract + synchronized` | abstract 没有方法体 → 没有可加锁的代码 |

```java
abstract class A {
    private abstract void m1();      // ❌
    final abstract void m2();        // ❌
    static abstract void m3();       // ❌
    public abstract void m4();       // ✅
}
```

### 抽象类 vs 普通类

| 维度 | 普通类 | 抽象类 |
|------|--------|--------|
| `new` 实例化 | ✅ 可以 | ❌ 不可以 |
| 抽象方法 | ❌ 不能有 | ✅ 可以有（也可以没有） |
| 构造方法 | ✅ | ✅（只能给子类用） |
| 普通方法 | ✅ | ✅ |
| 成员变量 | ✅ | ✅ |
| 静态方法 | ✅ | ✅ |
| 子类继承 | 直接可用 | 必须重写全部抽象方法（除非自己也 abstract） |

> 抽象类的代价只有一个：**不能 new**。换来的是逼着子类干活。

### 图示：父类模板 + 子类实现

![[abstract-class-template.svg]]

### 完整示例

```java
public abstract class Animal {
    protected String name;

    public Animal(String name) {          // 构造方法
        this.name = name;
    }

    public void sleep() {                  // 普通方法
        System.out.println(name + " 睡觉");
    }

    public abstract void eat();            // 抽象方法，子类必须实现
}

class Cat extends Animal {
    public Cat(String name) {
        super(name);                       // 调用父类构造，必须第一行
    }

    @Override
    public void eat() {
        System.out.println(name + " 吃鱼");
    }
}

class Dog extends Animal {
    public Dog(String name) {
        super(name);
    }

    @Override
    public void eat() {
        System.out.println(name + " 啃骨头");
    }
}

public class Test {
    public static void main(String[] args) {
        // Animal a = new Animal("x");     // ❌ 抽象类不能 new

        Animal a1 = new Cat("Tom");        // ✅ 多态：父引用指子对象
        Animal a2 = new Dog("旺财");
        a1.eat();                          // "Tom 吃鱼"    动态分派
        a2.eat();                          // "旺财 啃骨头"  动态分派
    }
}
```

### 速记

> 抽象类 = 半成品模板，方法没意义就声明 abstract，让子类实现
> 有抽象方法 → 类必 abstract；abstract 类 → 不一定有抽象方法
> 抽象类不能 new，但有构造方法（给子类 `super()` 用）
> 子类必须重写全部抽象方法，否则自己也 abstract
> abstract 和 private / final / static 是死敌（语义互相打架）

---

## 十九、接口（interface）基础

> **一句话**：接口是**完全抽象**的规范（合约），只能定义常量和抽象方法（Java 8+ 允许 default / static，Java 9+ 允许 private），**没有构造方法、不能 new**，用来描述"实现类应该有什么行为"。

### 概念

接口定义一组**抽象方法 + 常量**，描述实现这个接口的类应该具有哪些行为和属性。**接口和类一样，也是一种引用数据类型**。

### 定义语法

```java
[修饰符列表] interface 接口名 {
    // 接口体
}
```

### 接口是完全抽象的

| 维度 | 抽象类 | 接口 |
|------|--------|------|
| 抽象程度 | **半**抽象 | **完全**抽象 |
| 构造方法 | ✅ 有（给子类用） | ❌ 没有 |
| 实例化 | ❌ | ❌ |

### 接口中能定义什么

| 成员 | 完整写法 | 可省略 | 编译器自动补 |
|------|----------|--------|--------------|
| 常量 | `public static final` | **三个都能省** | `public static final` |
| 抽象方法 | `public abstract` | **两个都能省** | `public abstract` |
| 默认方法（Java 8+） | `public default` | `default` **不能省** | `public` |
| 静态方法（Java 8+） | `public static` | `static` **不能省** | `public` |
| 私有方法（Java 9+） | `private` / `private static` | 都不能省 | — |

> **核心规则**：接口里**所有**方法和变量**默认都是 public**。

```java
public interface Usb {
    int VERSION = 3;                 // 等价 public static final int VERSION = 3;

    void read();                      // 等价 public abstract void read();
    void write();                     // 等价 public abstract void write();

    default void log(String s) {      // Java 8+ 默认方法
        System.out.println("log: " + s);
    }

    static void info() {              // Java 8+ 静态方法
        System.out.println("Usb v" + VERSION);
    }

    private void helper() {           // Java 9+ 私有方法，为 default 服务
        System.out.println("internal");
    }
}
```

### 接口的继承与实现（四种关系）

| 关系 | 关键字 | 方向 | 数量 |
|------|--------|------|------|
| 类继承类 | `extends` | 子类 → 父类 | **单**继承 |
| **接口继承接口** | `extends` | 子接口 → 父接口 | **多**继承 |
| **类实现接口** | `implements` | 实现类 → 接口 | **多**实现 |
| 接口继承类 | — | — | ❌ 不允许 |

```java
interface A { void ma(); }
interface B { void mb(); }
interface C extends A, B { void mc(); }     // ✅ 接口多继承

class X implements A, B {                    // ✅ 类多实现
    public void ma() { }
    public void mb() { }
}
```

### 实现类必须重写全部抽象方法

与抽象类规则一致：非抽象实现类必须**全部实现**，否则自己也声明为 `abstract`。

```java
class Printer implements Usb {                // 非抽象类
    @Override public void read()  { System.out.println("读数据"); }
    @Override public void write() { System.out.println("写数据"); }
}
```

### Java 8 默认方法：解决「接口演变」问题

**问题**：`Usb` 已被 Printer、HardDrive 实现。某天要给 `Usb` 加一个 `format()` 方法 → **所有实现类都得改**，否则编译报错。这就是**接口演变问题**。

**解决**：用 `default` 提供默认实现，实现类**可选择**是否重写。

```java
public interface Usb {
    void read();
    void write();

    default void format() {                  // 默认实现
        System.out.println("默认格式化");
    }
}

class Printer implements Usb {
    public void read()  { }
    public void write() { }
    // 不重写 format() 也合法 → 走 Usb 的默认实现
}
```

### Java 8 接口静态方法（反直觉规则）

> **接口的静态方法只能通过接口名调用，实现类不会继承它。**

```java
Usb.info();               // ✅ 通过接口名调用
Printer.info();           // ❌ 编译报错：实现类不继承接口静态方法
new Printer().info();     // ❌ 编译报错
```

**这和类的静态方法完全不同**（类的静态方法可被子类继承、通过子类名调用）。这是 Java 8 的防御性设计。

### Java 9 私有方法

```java
public interface Usb {
    default void start() { helper(); System.out.println("start"); }
    default void stop()  { helper(); System.out.println("stop");  }

    private void helper() {                     // 只为 default 服务
        System.out.println("公共初始化");
    }
}
```

**目的**：避免 `helper()` 这类辅助代码在多个 `default` 方法里重复。

### 接口隐式继承 Object

接口虽然"完全抽象"，但默认可以调用 `Object` 的方法（`toString()` / `equals()` / `hashCode()`）。

### 接口的作用：解耦合

| 角色 | 比喻 | 行为 |
|------|------|------|
| **接口调用者** | 顾客 | 拿着接口（菜单）去用 |
| **接口实现者** | 厨师 | 按接口（菜单）做菜 |
| **接口本身** | 菜单 | 双方遵守的规范 |

**两个收益**：

- **降低耦合度**：调用者不关心实现者，双方都遵循接口
- **提高扩展力**：新增实现者不改调用者代码

![[interface-usb-decoupling.svg]]

### 完整示例：USB 接口

```java
public interface Usb {
    void read();
    void write();
}

public class Computer {                       // 调用者
    public void conn(Usb usb) {               // 形参是接口类型
        usb.read();                            // 多态：实际对象是哪个就调哪个
        usb.write();
    }
}

public class Printer implements Usb {         // 实现者 1
    public void read()  { System.out.println("打印机读"); }
    public void write() { System.out.println("打印机写"); }
}

public class HardDrive implements Usb {       // 实现者 2
    public void read()  { System.out.println("硬盘读"); }
    public void write() { System.out.println("硬盘写"); }
}

Computer c = new Computer();
c.conn(new Printer());        // 打印机工作
c.conn(new HardDrive());      // 硬盘工作
// Computer 不用改，新增任何 Usb 实现都能接入
```

### 速记

> 接口 = 完全抽象的规范：常量 + 抽象方法 +（default / static / private）
> 全部 public：常量默认 `public static final`，方法默认 `public abstract`
> 类单继承、类多实现、接口多继承，接口不能继承类
> Java 8 `default` 解决接口演变，静态方法只能接口名调用（实现类不继承）
> 接口的价值：解耦合、提扩展；面向接口编程，不面向实现编程

---

## 二十、接口 vs 抽象类（终极对比）

> **一句话**：抽象类是 `is-a`（是什么，复用代码骨架），接口是 `can-do`（能做什么，只定规范）；**一个类只能有一个身份，但可以有多种能力**。

### 逐维度对照表

| 维度 | 抽象类 | 接口 |
|------|--------|------|
| 抽象程度 | 半抽象 | **完全抽象** |
| 关键字 | `abstract class` | `interface` |
| 使用方式 | `extends`（**单**继承） | `implements`（**多**实现） |
| 构造方法 | ✅ 有 | ❌ **没有** |
| 实例化 | ❌ 不能 new | ❌ 不能 new |
| 普通成员方法 | ✅ 可以有 | Java 8+ 用 `default` 实现 |
| 成员变量 | 普通字段 | **只能是 `public static final` 常量** |
| 抽象方法 | ✅ | ✅（默认 `public abstract`） |
| 静态方法 | ✅（子类可继承） | ✅（**实现类不继承**，只能接口名调用） |
| 私有方法 | ✅ | Java 9+ `private`（为 default / static 服务） |
| 多继承 | ❌ | ✅（接口之间多继承，类多实现） |
| 设计意图 | **模板复用**（共享代码骨架） | **规范抽象**（约定能力，不复用代码） |

### 设计意图：is-a vs can-do

![[interface-vs-abstract.svg]]

| 用法 | 语义 | 例子 |
|------|------|------|
| **抽象类** | `is-a`：**是什么** | `Duck is-a Animal`（鸭子**是**动物） |
| **接口** | `can-do`：**能做什么** | `Duck can fly` / `Duck can swim`（鸭子**会**飞、会游） |

> **一个类只能继承一个抽象类（血缘唯一），但可以实现多个接口（能力叠加）。**

### 组合使用：一个身份 + 多种能力

```java
interface Flyable   { void fly(); }          // 能力 1
interface Swimmable { void swim(); }         // 能力 2

abstract class Animal {                       // 身份（模板）
    protected String name;
    public Animal(String name) { this.name = name; }
    public abstract void eat();
}

class Duck extends Animal                     // extends 只能一个（血缘）
        implements Flyable, Swimmable {       // implements 可以多个（能力）
    public Duck(String name) { super(name); }

    @Override public void eat()  { System.out.println(name + " 吃"); }
    @Override public void fly()  { System.out.println(name + " 飞"); }
    @Override public void swim() { System.out.println(name + " 游"); }
}
```

### 什么时候用哪个

| 场景 | 选择 | 理由 |
|------|------|------|
| 需要**复用代码**（多个子类共享一堆方法实现） | 抽象类 | 接口不能提供可复用的实例方法（只有 default，能力有限） |
| 只是**定规范**，不关心实现细节 | 接口 | 更灵活，不占用继承名额 |
| 需要类具备**多种能力** | 接口 | 单继承限制，只能靠多实现 |
| 需要**定义状态**（实例字段） | 抽象类 | 接口只能有常量 |
| 两者都要 | **抽象类 + 接口组合** | `extends` 一个抽象类 + `implements` 多个接口 |

### 速记

> 抽象类 = `is-a` 是什么（模板复用），接口 = `can-do` 能做什么（规范抽象）
> 类单继承、类多实现、接口多继承
> 需要共享代码用抽象类，只需要定规范用接口
> 关键差异：接口没构造方法、字段只能是常量、静态方法不被实现类继承

---

## 二十一、访问控制权限（4 个修饰符）

> **一句话**：4 个修饰符（`private` / 缺省 / `protected` / `public`）控制**类内成员**在不同目录位置的可见性，**范围从小到大依次累加** —— 越往后的修饰符能访问的位置越多。

### 4 个修饰符的含义

| 修饰符 | 关键字 | 含义 | 典型场景 |
|--------|--------|------|----------|
| **private** | 私有的 | **只能在本类中**访问 | 类的内部实现细节、敏感字段 |
| **缺省** | 默认 | **同一个包下**可以访问 | 包级别的工具方法、同包内共享数据 |
| **protected** | 受保护的 | **同包 + 子类**可以访问 | 给"子孙"用的"家产" |
| **public** | 公共的 | **任何位置**都可以访问 | 对外暴露的 API、常量 |

### 访问范围对照表 ⭐ 必背

| 修饰符 | 同一个类 | 同一个包 | 子类 | 所有类 |
|--------|----------|----------|------|--------|
| `private` | ✅ | ❌ | ❌ | ❌ |
| 缺省 | ✅ | ✅ | ❌ | ❌ |
| `protected` | ✅ | ✅ | ✅ | ❌ |
| `public` | ✅ | ✅ | ✅ | ✅ |

> **口诀**：`private` ⊂ 缺省 ⊂ `protected` ⊂ `public`，**每一级在前一级基础上多开放一个场景**。

![[access-control-package-tree.svg]]

### 4 种调用方位置（目录结构图已展示）

| 位置 | 说明 | 例子 |
|------|------|------|
| **同一个类内** | Animal 类自己的方法体 | `Animal.this.method()` |
| **同包** | 与 Animal 在同一个 `package` 下 | `com.powernode.SamePackage` |
| **子类** | 跨包继承 Animal 的类 | `com.powernode.sub.SubClass` |
| **他包** | 完全无关的其他包 | `com.other.OtherClass` |

### 3 条附加限制

| # | 限制 | 说明 |
|---|------|------|
| ① | **类的访问权限只有 2 种**：`public` 和缺省 | 顶层类**不能**用 `private` / `protected`（内部类除外） |
| ② | 访问权限控制符**不能修饰局部变量** | 局部变量只在方法内有效，谈不上跨类访问 |
| ③ | `protected` 主要给"子孙"用，**跨包子类访问**的是从父类**继承**下来的成员 | 在子类里访问自己的字段不算 protected 生效 |

### 示例

```java
package com.powernode;

public class Animal {
    private    int    money = 100;        // 仅本类
              String name  = "Tom";       // 同包
    protected int    age   = 5;           // 同包 + 子类
    public    String info  = "OK";        // 所有位置
}
```

```java
package com.powernode.sub;
import com.powernode.Animal;

public class Cat extends Animal {
    void test() {
        // System.out.println(money);    // ❌ private 不可见
        // System.out.println(name);     // ❌ 缺省，跨包不可见
        System.out.println(age);         // ✅ protected，子类可见
        System.out.println(info);        // ✅ public，所有位置可见
    }
}
```

### 速记

> `private` ⊂ 缺省 ⊂ `protected` ⊂ `public`，**累加**关系
> 同类能看全部，**只有 `public` 全程 √**
> 类的访问权限**只有 `public` / 缺省 两种**，**不能修饰局部变量**
> `protected` 是"给子孙的"，主要场景是**跨包子类继承**

---

## 二十二、内部类（4 种）

> **一句话**：内部类是**定义在类内部的类**，共 4 种 —— 静态内部类（成员区）、实例内部类（成员区）、局部内部类（方法里）、匿名内部类（一次性）；**修饰符、位置、实例化语法都不同**。

### 什么是内部类

**定义在一个类内部的类**。Java 允许把类作为成员嵌套在另一个类里，共 4 种形式。

### 什么时候用内部类

| # | 理由 | 直白讲 |
|---|------|--------|
| ① | 两个类联系密切，独立定义会**增加类数量** | 内部类**就近**写在用它的类旁边 |
| ② | 内部类能**直接访问外部类私有成员**，提高封装性 | 把"配套"类藏起来 |
| ③ | 匿名内部类**只用一次**的场景 | 不想起名字时用 |

### 4 种内部类位置示意

![[inner-class-positions.svg]]

### 4 种内部类对照表 ⭐ 必背

| 类型 | 修饰符 | 类体位置 | 实例化方式 | 能否定义静态成员 |
|------|--------|----------|------------|------------------|
| **静态内部类** | `static class` | 外部类的**成员区** | `new Outer.StaticInner()` | ✅ 可以 |
| **实例内部类** | `class` | 外部类的**成员区** | `new Outer().new Inner()` | ❌ 不能（`static final` 常量除外） |
| **局部内部类** | `class` | **方法体 / 代码块**内 | 在其作用域内 `new` | ❌ 不能 |
| **匿名内部类** | 无类名，`new 父类(){}` | 通常在**方法参数**位置 | 定义即实例化 | ❌ 不能 |

### 4 种内部类访问外部类的能力

| 类型 | 访问外部**实例**成员 | 访问外部**静态**成员 | 访问**局部**变量 |
|------|----------------------|----------------------|------------------|
| 静态内部类 | ❌ | ✅ | — |
| 实例内部类 | ✅（含 private） | ✅ | — |
| 局部内部类 | ✅ | ✅ | ✅ 只能访问**有效 final** |
| 匿名内部类 | ✅ | ✅ | ✅ 只能访问**有效 final** |

### ① 静态内部类

```java
public class Outer {
    private static int y = 20;

    static class StaticInner {            // 静态内部类
        void test() {
            System.out.println(y);        // ✅ 访问外部静态
            // System.out.println(x);     // ❌ 不能访问外部实例
        }
    }
}

// 实例化（不用先有 Outer 实例）
Outer.StaticInner s = new Outer.StaticInner();
```

> 相当于外部类的一个"静态成员"，**可以**有自己的静态成员。

### ② 实例内部类 ⭐ 高频考点

```java
public class Outer {
    private int x = 10;
    private static int y = 20;

    class Inner {                          // 实例内部类
        void test() {
            System.out.println(x);              // ✅ 直接访问
            System.out.println(Outer.this.x);   // 显式访问外部的 x
            System.out.println(y);              // ✅ 静态也行
        }
    }
}

// 实例化（必须先有 Outer 实例）
Outer outer = new Outer();
Outer.Inner i = outer.new Inner();         // ⚠️ 链式 new 语法
```

> **不能有静态成员**（`static final` 常量除外）。
> `this` 指向内部类自身，`外部类.this` 指向外部类实例（同名变量时必须写）。

**同名变量问题**：

```java
class Outer {
    int x = 10;
    class Inner {
        int x = 20;                         // 内外同名
        void test() {
            System.out.println(x);              // 20  ← Inner 的
            System.out.println(Outer.this.x);   // 10  ← Outer 的
        }
    }
}
```

### ③ 局部内部类

```java
public void method() {
    int localVar = 30;                      // 局部变量

    class LocalInner {                      // 写在方法里
        void test() {
            System.out.println(localVar);   // ✅ JDK 8+ 自动 final
        }
    }

    new LocalInner().test();
}
```

> **JDK 8+**：不用显式 `final`，**自动判定**"有效 final"（变量没被改过）。
> **但**：**只要内部类用了这个局部变量，它就被"冻结"了**，不能再赋值。
> **实际中**：局部内部类几乎不用，要用也用**匿名内部类**代替。

### ④ 匿名内部类 ⭐ 最常用

```java
// 1. 继承一个类
new Animal() {                              // 没名字，直接继承
    @Override
    public void eat() {
        System.out.println("猫吃鱼");
    }
}.eat();

// 2. 实现一个接口
Runnable r = new Runnable() {
    @Override
    public void run() {
        System.out.println("跑起来");
    }
};
r.run();
```

**4 个硬性限制**：

| # | 限制 |
|---|------|
| ① | **没有类名**，不能重复使用 |
| ② | **必须继承一个类 或 实现一个接口**（二选一） |
| ③ | **不能定义构造方法**（没有类名） |
| ④ | 访问外部**局部**变量时同样受**有效 final** 约束 |

**Lambda 替代**（Java 8+ 函数式接口）：

```java
// 匿名内部类
Runnable r = new Runnable() {
    @Override
    public void run() { System.out.println("跑"); }
};

// Lambda 写法
Runnable r = () -> System.out.println("跑");
```

> **函数式接口**（只有一个抽象方法的接口）的匿名内部类能用 Lambda 替代，**更简洁**。

### 实例化语法速记

| 类型 | 语法 |
|------|------|
| 静态内部类 | `new Outer.StaticInner()` |
| 实例内部类 | `outer.new Inner()` |
| 局部内部类 | `new LocalInner()` |
| 匿名内部类 | `new 父类() { ... }` 或 `new 接口() { ... }` |

### 速记

> 4 种内部类：静态（成员区·可静态）+ 实例（成员区·必须 `outer.new`）+ 局部（方法里·几乎不用）+ 匿名（一次性·函数式接口用 Lambda 替）
> 实例内部类**不能**有静态成员、**不能**直接 new
> 后 3 种访问外部局部变量 → 必须「有效 final」，**用了就被冻结**
> 匿名内部类只能继承一个类或实现一个接口

---

## 二十三、main 方法 args 与可变长参数

> **一句话**：`main(String[] args)` 的 `args` 接收**命令行参数**；可变长参数 `int...` 是 `int[]` 的**语法糖**，只能放形参列表最后且一个方法最多一个。

### main 方法的 args

```java
public static void main(String[] args) { }
```

`args` 就是一个普通的 `String[]`，**用来接收命令行参数**。

### 怎么传参

| 方式 | 操作 |
|------|------|
| **DOS 命令行** | `java Demo Tom Jerry 25` |
| **IDEA** | `Run` → `Edit Configurations` → 选类 → `Program arguments` 填 `Tom Jerry 25` |

```bash
javac Demo.java
java Demo Tom Jerry 25
# 此时 args = {"Tom", "Jerry", "25"}
```

```java
public static void main(String[] args) {
    if (args.length == 0) {                     // 没传参时长度是 0
        System.out.println("没传参");
        return;
    }
    System.out.println("第一个参数：" + args[0]);
    System.out.println("参数个数：" + args.length);
}
```

| 元素 | 值 |
|------|-----|
| `args[0]` | `"Tom"` |
| `args[1]` | `"Jerry"` |
| `args[2]` | `"25"` |
| `args.length` | `3` |

> **细节**：多个参数用**空格**分隔；参数本身带空格时用**双引号**包起来：`java Demo "hello world" foo`。
> **没传参时** `args` 是**空数组**（`length == 0`），**不是 `null`** —— 可以直接 `args.length` 不用判空。

### 可变长参数（varargs）

```java
public static int sum(int... nums) {       // int... 语法糖
    int total = 0;
    for (int n : nums) {                    // 当数组用
        total += n;
    }
    return total;
}

sum(1, 2, 3, 4);                            // ✅ 任意多个
sum(1, 2);                                 // ✅
sum();                                     // ✅ 空参（nums 是空数组，不是 null）
sum(new int[]{1, 2, 3});                   // ✅ 也可直接传数组
```

### 两条硬规则

| # | 规则 |
|---|------|
| ① | **只能放在形参列表最后**，一个方法最多**一个** |
| ② | 编译器**当数组处理**（`int...` ≡ `int[]`） |

```java
// ❌ 错误
public void m(int... a, String b) { }      // 不能放前面
public void m(int... a, int... b) { }      // 一个方法最多一个

// ✅ 正确
public void m(String a, int... nums) { }   // 放最后
```

### ⚠️ 与数组重载冲突（高频坑）

```java
public static void m(int[] a) { }           // ①
public static void m(int... a) { }         // ②

m(new int[]{1, 2});                        // ❌ 编译报错：重复方法
```

**原因**：`int...` 编译后**就是 `int[]`**，两个签名对编译器来说**完全相同**，所以报"重复方法"。

> **结论**：写代码时**二选一**，不要同时写 `int[]` 和 `int...` 两种重载。

### 图示

![[main-args-and-varargs.svg]]

### 速记

> `main(String[] args)` 收命令行参数，**空格分隔**，IDEA 在 Run Configurations 里填
> 没传参时 `args` 是**空数组不是 null**
> 可变长参数 `int...` ≡ `int[]`，**只能放最后**、**最多一个**
> `int[]` 和 `int...` **不能重载共存**（编译器视为同一签名）

---

## 二十四、单元测试（JUnit 5）

> **一句话**：JUnit 5 是 Java 主流的单元测试框架（**JDK 不自带**，需引入 3 个 jar），写测试 = **测试类 + `@Test` 注解方法 + 断言**；4 个生命周期注解负责 setup / teardown。

### 什么是单元测试

**项目 = 很多代码块拼起来的**，每块代码（一个方法 / 一个类）要保证正确，整个项目才正常。**单元 = 一块代码**，**单元测试 = 对这块代码写专门的"验货脚本"**。

### 引入 JUnit 5

**JDK 不自带**，需要额外引入 3 个 jar（Maven/Gradle 用户通过依赖自动管理）：

| jar 包 | 作用 |
|--------|------|
| `junit-jupiter-api-5.8.0.jar` | 写测试用的 API（`@Test`、断言方法等） |
| `junit-platform-commons-1.9.2.jar` | 公共支持（执行器、扩展点） |
| `junit-platform-engine-1.9.2.jar` | **测试引擎**（IDEA 跑测试要靠它） |

> JUnit 5 把 JUnit 4 的"一个 jar"拆成 3 个，**模块化设计**。Maven 用户引入 `junit-jupiter` 一个依赖自动拉 3 个。

### 测试类（测试用例）怎么写

**命名规范**：`XxxTest`（被测类 `Calculator` → 测试类 `CalculatorTest`），普通 Java 类。

### 测试方法 4 个硬性要求 ⭐

| # | 要求 | 原因 |
|---|------|------|
| ① | **必须加 `@Test` 注解** | JUnit 靠注解识别"这是测试方法" |
| ② | **返回值必须是 `void`** | 测试结果靠"是否抛异常"判定，不需要返回 |
| ③ | **形参个数为 0** | JUnit 不会传参数给你 |
| ④ | **建议命名 `testXxx()`** | 一眼能看出是测试方法 |

```java
@Test
public void testAdd() {
    Calculator c = new Calculator();
    int result = c.add(1, 2);
    assertEquals(3, result);
}
```

### 期望值 vs 实际值 + 断言三件套

| 名称 | 含义 | 例子 |
|------|------|------|
| **期望值** | 程序执行**前**你**希望**得到的结果 | 期望 `1 + 2 == 3` |
| **实际值** | 程序执行**后**实际得到的结果 | 实际 `c.add(1, 2) == 3` |
| **断言** | 用 `assertXxx` 方法**自动比较**两者 | `assertEquals(3, result)` |

**常用断言方法**：

| 方法 | 作用 |
|------|------|
| `assertEquals(expected, actual)` | 期望 == 实际 |
| `assertNotEquals(expected, actual)` | 期望 != 实际 |
| `assertTrue(condition)` | 条件为真 |
| `assertFalse(condition)` | 条件为假 |
| `assertNull(obj)` | 对象为 null |
| `assertNotNull(obj)` | 对象不为 null |
| `assertThrows(异常类.class, () -> {...})` | 期望抛异常 |
| `assertAll(...)` | 多个断言一起跑（一个挂不终止其他） |

### 完整示例

```java
import org.junit.jupiter.api.*;

public class Calculator {
    public int add(int a, int b) { return a + b; }
    public int divide(int a, int b) { return a / b; }
}

public class CalculatorTest {

    @Test
    public void testAdd() {
        assertEquals(3, new Calculator().add(1, 2));
    }

    @Test
    public void testDivideByZero() {
        assertThrows(ArithmeticException.class, () -> {
            new Calculator().divide(6, 0);
        });
    }
}
```

### 4 个生命周期注解 ⭐ 高频

| 注解 | 何时执行 | 执行次数 | 标注方法 |
|------|----------|----------|----------|
| `@BeforeAll` | **所有测试方法前** | 整个类跑 **1 次** | 必须是 `static` |
| `@AfterAll` | **所有测试方法后** | 整个类跑 **1 次** | 必须是 `static` |
| `@BeforeEach` | **每个测试方法前** | 每个 `@Test` 各跑 1 次 | 实例方法 |
| `@AfterEach` | **每个测试方法后** | 每个 `@Test` 各跑 1 次 | 实例方法 |

![[junit-lifecycle.svg]]

**完整示例**：

```java
public class CalculatorTest {

    @BeforeAll
    static void setupAll() {                // 整个类跑前执行 1 次
        System.out.println("--- 测试开始 ---");
    }

    @BeforeEach
    void setup() {                          // 每个测试方法前
        System.out.println("准备测试数据");
    }

    @Test
    void testAdd() {
        assertEquals(3, new Calculator().add(1, 2));
    }

    @Test
    void testSubtract() {
        assertEquals(-1, new Calculator().subtract(1, 2));
    }

    @AfterEach
    void teardown() {                       // 每个测试方法后
        System.out.println("清理测试数据");
    }

    @AfterAll
    static void teardownAll() {             // 整个类跑后执行 1 次
        System.out.println("--- 测试结束 ---");
    }
}
```

**典型场景**：

| 注解 | 用途 |
|------|------|
| `@BeforeAll` / `@AfterAll` | 打开/关闭数据库连接、加载全局配置 |
| `@BeforeEach` / `@AfterEach` | 每个测试前 `new` 一个新对象、清理临时文件 |

### Scanner 在测试中失效的解决

**原因**：IDEA 默认把单元测试的输入输出**重定向到非交互模式**，`Scanner.nextLine()` 等就会"卡住"或读不到东西。

**修复**：

1. IDEA 顶部菜单 → `Help` → `Edit Custom VM Options...`
2. 在打开的 `IDEA64.exe.vmoptions` 文件**末尾**加一行：
   ```
   -Ddeditable.java.test.console=true
   ```
3. **重启 IDEA**

> Maven/Gradle 用户更简单：在 `pom.xml` 加 `systemPropertyVariables` 配置，或用 JUnit 5 的 `ConsoleLauncher`。

### 速记

> JUnit 5 = 3 个 jar（api + commons + engine），JDK 不自带
> 测试类 `XxxTest`，测试方法 **`@Test` + `void` + 无参 + `testXxx`**
> 断言三件套：`assertEquals(期望, 实际)` / `assertTrue` / `assertThrows`
> **All** 整个类跑 1 次·static，**Each** 每个 Test 跑·实例方法
> IDEA 跑测试时 Scanner 失效 → `Help → Edit Custom VM Options` 加 `-Ddeditable.java.test.console=true`

---

## 二十五、异常继承结构（Throwable 体系）

> **一句话**：所有异常和错误都继承 `Throwable`，往下分 **`Error`**（JVM 层面，**无法处理**）和 **`Exception`**（程序层面，**可处理**）；`Exception` 再分**受检（Checked，编译器强制处理）**和**非受检（`RuntimeException` 派，编译器不强制）**。

### ① 一切的根：Throwable

`Throwable` 是 Java 异常体系的**根**，**只有 `Throwable` 及其子类才能被 `throw` / `throws`**。

| 派系 | 含义 | 能否处理 | 出现后 |
|------|------|----------|--------|
| **`Error`（错误）** | JVM 层面的问题 | ❌ **不能** | 程序**只能终止** |
| **`Exception`（异常）** | 程序层面的问题 | ✅ 能 | try-catch 或 throws 抛出 |

### ② Error：无法处理，让程序挂掉

| 常见 Error | 含义 |
|------------|------|
| `OutOfMemoryError` | 堆内存耗尽（JVM 给新对象分配空间失败） |
| `StackOverflowError` | 栈溢出（递归太深、循环方法调用） |
| `NoClassDefFoundError` | 类定义找不到（jar 包缺失） |
| `ExceptionInInitializerError` | 静态初始化块抛异常 |

> **特点**：Error 一旦发生，**JVM 直接终止**，**别 try-catch**（接不住，没意义）。

### ③④ Exception 的两大派系

| 派系 | 别名 | 编译器要求 |
|------|------|------------|
| **`RuntimeException` 及其子类** | 运行时异常 / 未检查异常 / 非受控异常 / **Unchecked** | **不强制**（可处理可不处理） |
| **`Exception` 其他子类**（除 `RuntimeException`） | 编译时异常 / 检查异常 / 受控异常 / **Checked** | **必须** try-catch 或 throws |

### ⑤ 编译时异常 vs 运行时异常

| 维度 | 编译时异常（Checked） | 运行时异常（Unchecked） |
|------|----------------------|------------------------|
| **包含** | 除 `RuntimeException` 外的 `Exception` 子类 | `RuntimeException` 及其子类 |
| **编译器要求** | **必须**处理（不写编译报错） | 可处理可不处理（不写不报错） |
| **处理方式** | try-catch / throws 二选一 | 不写也行（出了再补救或让程序挂） |
| **来源** | **外部环境**（IO、SQL、文件、线程） | **程序员代码错误**（空指针、下标越界、类型转换） |
| **能否预防** | 难以预防（环境不可控） | 理论上可预防（写代码时判断） |

```java
// 编译时异常：必须处理
public void readFile() throws IOException {        // throws 抛给调用方
    FileReader fr = new FileReader("a.txt");        // ❌ 不抛就编译报错
}

// 运行时异常：可以不处理
public String safeToString(Object o) {
    return o.toString();                            // 可能 NPE，但编译器不强制
}
```

### 5 大常见运行时异常（Unchecked）

| 异常 | 典型场景 |
|------|----------|
| `NullPointerException` | 引用为 null 却调用方法或访问属性 |
| `ArrayIndexOutOfBoundsException` | 数组下标越界（负数、≥ length） |
| `ClassCastException` | 强制类型转换类型不匹配 |
| `ArithmeticException` | 算术异常（如 `1 / 0`） |
| `NumberFormatException` | 数字格式错（如 `Integer.parseInt("abc")`） |

> 由**程序员代码错误**引起，**理论上可以避免**。

### 5 大常见编译时异常（Checked）

| 异常 | 典型场景 |
|------|----------|
| `IOException` | I/O 操作失败（读写文件、网络流） |
| `FileNotFoundException` | 找不到文件（`new FileInputStream("不存在的文件")`） |
| `SQLException` | 数据库访问出错 |
| `ClassNotFoundException` | 反射加载类时找不到（`Class.forName("xxx")`） |
| `InterruptedException` | 线程被中断（`Thread.sleep()`、`wait()`） |

> 由**外部环境**引起，**程序员无法预判**，所以编译器强制要求处理。

### 图示

![[exception-hierarchy.svg]]

### ⚠️ 关键澄清：所有异常都是运行期发生的

> **"编译时异常"并不是在编译阶段发生的异常** —— **所有异常都是运行期发生的**，因为每个异常发生都要 `new` 异常对象，而 `new` 只能在运行期完成。
>
> 之所以叫"编译时异常"，是因为编译器**强制**让你在**编译期**就把处理代码写好（try-catch 或 throws），**不写就报错**。
>
> 所以更准确的叫法是 **"受检异常（Checked Exception）"** —— 它的本意是"**被编译器检查**"。

**类比**：

- **受检异常** = 出门前必须带伞（不带不让出机场，**编译期检查**）
- **非受检异常** = 路上可能踩坑（自己小心，**运行期看命**）

### 处理方式速查

| 方式 | 语法 | 何时用 |
|------|------|--------|
| **try-catch** | `try { ... } catch (异常 e) { ... }` | 自己能处理 |
| **throws** | `void m() throws 异常 { ... }` | 自己处理不了，抛给调用方 |
| **不处理** | — | 只有运行时异常（Unchecked）才能这么干 |

### 速记

> 所有异常 / 错误都继承 **`Throwable`**，往下分 **`Error`**（不能处理，JVM 终止）和 **`Exception`**（能处理）
> `Exception` 分两派：**`RuntimeException` 派**（Unchecked，编译器不强制）vs **其它**（Checked，编译器强制）
> 5 大运行时异常：NPE、AIOOBE、CCE、AE、NFE —— **程序员代码错误**
> 5 大编译时异常：IOE、FNF、SQL、CNF、IE —— **外部环境引起**
> **所有异常都是运行期发生的**，"编译时异常"只是被**编译器检查**而已

---

## 二十六、自定义异常

> **一句话**：JDK 内置异常覆盖不了业务错误（名字长度、年龄、余额不足），**自定义异常 = 继承 `Exception` / `RuntimeException` + 两个构造方法**，业务代码里用 `throw new` 手动抛出。

### 为什么要自定义异常

| 场景 | JDK 有没有现成异常 |
|------|--------------------|
| 空指针、下标越界、类型转换 | ✅ 有（NPE、AIOOBE、CCE） |
| **用户名长度不在 6-12 位** | ❌ 没有 |
| **年龄小于 18 岁 / 余额不足** | ❌ 没有 |

> **业务规则违反** → JDK 不可能预知你的业务 → **自己定义**。

### 定义两步走 ⭐

| 步骤 | 内容 |
|------|------|
| **第一步** | 编写异常类，**继承 `Exception`（编译时）或 `RuntimeException`（运行时）** |
| **第二步** | 提供**两个构造方法**：无参 + `String message` 有参，有参里 `super(message)` |

```java
/** 编译时异常：继承 Exception */
public class IllegalAgeException extends Exception {
    public IllegalAgeException() { }

    public IllegalAgeException(String message) {
        super(message);          // 错误信息传给父类，getMessage() 能取到
    }
}

/** 运行时异常：继承 RuntimeException */
public class IllegalNameException extends RuntimeException {
    public IllegalNameException() { }

    public IllegalNameException(String message) {
        super(message);
    }
}
```

> **为什么必须有 String 构造方法**：`throw new IllegalAgeException("年龄必须大于18")` 把信息存进父类 message 字段，异常被 catch 后 `e.getMessage()` 才能拿到。没有它，异常**只有类型没有信息**，排查全靠猜。

### 继承 Exception 还是 RuntimeException？

| 选择 | 异常性质 | 调用方 |
|------|----------|--------|
| `extends Exception` | 编译时异常（受检） | **必须** try-catch 或 throws |
| `extends RuntimeException` | 运行时异常（非受检） | 可处理可不处理 |

> **实际开发多用 `RuntimeException`**（Spring 的业务异常基本都是 Runtime 派），避免调用方到处写 try-catch。

### 完整实战：用户注册

```java
// ① 自定义两个编译时异常
public class IllegalNameException extends Exception {
    public IllegalNameException() { }
    public IllegalNameException(String message) { super(message); }
}

public class IllegalAgeException extends Exception {
    public IllegalAgeException() { }
    public IllegalAgeException(String message) { super(message); }
}

// ② 业务方法：抛出异常
public class UserService {
    public void register(String name, int age)
            throws IllegalNameException, IllegalAgeException {   // 编译时异常要 throws 声明

        if (name.length() < 6 || name.length() > 12) {
            throw new IllegalNameException("名字长度必须在 6-12 位");
        }
        if (age < 18) {
            throw new IllegalAgeException("年龄必须大于 18");
        }
        System.out.println("恭喜" + name + "注册成功！");
    }
}

// ③ 调用方：必须处理
public class Test {
    public static void main(String[] args) {
        UserService service = new UserService();
        try {
            service.register("tom", 20);          // ✅ 注册成功
            service.register("tom", 15);          // ❌ 抛 IllegalAgeException
        } catch (IllegalNameException | IllegalAgeException e) {
            System.out.println("注册失败：" + e.getMessage());
        }
    }
}
```

**运行效果**：

```
恭喜tom注册成功！
注册失败：年龄必须大于 18
```

### 图示：抛出与捕获流转

![[custom-exception-flow.svg]]

### ⭐ throw vs throws（面试高频）

| 维度 | `throw` | `throws` |
|------|---------|----------|
| **位置** | 方法**体内** | 方法**签名**上 |
| **作用** | **动作**：抛出一个异常对象 | **声明**：本方法可能抛出的异常类型 |
| **后跟** | 一个**异常对象**（`new` 的） | **异常类名**（可多个，逗号隔开） |
| **执行后** | 方法**立即终止** | 只是声明，不终止 |
| **数量** | 一次抛一个 | 可声明多个 |

```java
public void register(String name, int age)                     // 方法签名
        throws IllegalNameException, IllegalAgeException {     // ← throws：声明
    throw new IllegalNameException("...");                     // ← throw：动作
}
```

> **口诀**：**throws 是预告片（可能出事），throw 是案发现场（真出事了）**。

### 速记

> 自定义异常两步：**继承 Exception / RuntimeException + 两个构造方法（无参 + String）**
> `super(message)` 把错误信息传给父类，catch 后 `getMessage()` 能取到
> `extends Exception` → 编译时（调用方必须处理）；`extends RuntimeException` → 运行时（看着办）
> 实际开发**多用 RuntimeException**（Spring 业务异常都是 Runtime 派）
> **throws 预告片、throw 案发现场** —— 前者声明可能出事，后者真的出事

---

## 二十七、正则表达式常用符号

> **一句话**：正则表达式是用符号描述"文本长什么样"的语言，掌握 5 类符号（元字符、量词、字符类、分组分支、反义）就能读懂 90% 的正则。

![[regex-syntax-map.svg]]

### 五类符号对照

**① 元字符**（一个符号配一类字符）

| 符号 | 含义 | 等价写法 |
|------|------|----------|
| `.` | 任意字符（除换行） | — |
| `\w` | 单词字符 | `[a-zA-Z0-9_]` |
| `\s` | 空白符（空格、Tab） | — |
| `\d` | 数字 | `[0-9]` |
| `\b` | 单词边界（是"位置"，不消耗字符） | — |
| `^` / `$` | 字符串开始 / 结束 | — |

**② 量词**（重复次数）

| 符号 | 次数 | 符号 | 次数 |
|------|------|------|------|
| `*` | 0~n | `{n}` | 恰好 n |
| `+` | 1~n | `{n,}` | ≥ n |
| `?` | 0 或 1 | `{n,m}` | n~m |

**③ 字符类与转义**

- `[abc]` 任选其一；`[0-9]`、`[a-zA-Z0-9]` 范围叠加
- `[^?!]` —— **`[]` 内的 `^` 是取反**（除 ? ! 外），和行首 `^` 完全两回事
- 想匹配符号本身要转义：`\.` 匹配 `.`、`\\` 匹配 `\`
- **Java 双转义坑**：Java 字符串里 `\` 也要转义，所以写正则 `"\\d"` 才是正则的 `\d` —— 初学 90% 的"正则不生效"都栽在这

**④ 分组 `()` 与分支 `|`**

```text
座机两种格式：0\d{2}-\d{8} | 0\d{3}-\d{7}
              （3位区号）     （4位区号）
IP 地址：     (\d{1,3}\.){3}\d{1,3}
              （1~3位数字+点）重复3次，再来一段
```

`()` 的价值：让量词作用于**一整段**而不是单个字符。

**⑤ 反义**（大写 = 取反）

| 小写 | 大写 | 小写 | 大写 |
|------|------|------|------|
| `\w` 单词 | `\W` 非单词 | `\s` 空白 | `\S` 非空白 |
| `\d` 数字 | `\D` 非数字 | `\b` 边界 | `\B` 非边界 |

`[^x]` 除 x 外任意；`[^aeiou]` 除元音外任意。

### 示例

```java
// 手机号：1 开头，第二位 3-9，共 11 位
String phone = "^1[3-9]\\d{9}$";
System.out.println("13812345678".matches(phone));   // true

// 分支：两种座机格式
String tel = "0\\d{2}-\\d{8}|0\\d{3}-\\d{7}";
System.out.println("010-12345678".matches(tel));    // true
System.out.println("0376-2233445".matches(tel));    // true

// 分组：简化版 IP
String ip = "(\\d{1,3}\\.){3}\\d{1,3}";
System.out.println("192.168.1.3".matches(ip));      // true
```

### 速记

> 点任意、w 单词、s 空白、d 数字，b 是边界不是字符
> 星加问 = 0+/1+/0或1；花括号精确到次数
> `[]` 选一个，`[^]` 取反，`()` 打包，`|` 二选一
> 大写四对反义：W S D B
> Java 里反斜杠永远写两道

---

## 二十八、泛型（Generics）

> **一句话**：泛型是写在集合后面的 `<类型>` 标签，本质是**编译阶段的类型检查** —— 把"放错类型"从运行时爆炸提前到编译期报错，顺便省掉所有强转。

![[generics-compile-check.svg]]

### 为什么需要泛型（没有泛型的世界）

Java 5 之前，集合只能装 `Object` —— 什么都进得去：

```java
List list = new ArrayList();
list.add("abc");
list.add(123);          // int 也能混进去，编译不报错
String s = (String) list.get(1);   // 运行时爆炸：ClassCastException
```

两个痛点：**错误发现太晚**（放进去不报错，取出来用才炸）、**强转写到手酸**（每次 get 都要手动转）。

### 泛型怎么解决

`<String>` 相当于和编译器签了**合同**：这个集合只放 String。

| 对比 | 没泛型（Object） | 有泛型 |
|------|------------------|--------|
| 放错类型 | 编译不报错，**运行时** ClassCastException | **编译期**直接报错，运行不了 |
| 取元素 | 每次手动强转 `(String) list.get(0)` | 直接 `String s = list.get(0)` |
| 检查时机 | 运行期 | 编译期 |

```java
Collection<String> strs = new ArrayList<String>();   // Java 5 写法
strs.add("abc");
strs.add(123);       // 编译报错，当场拦下
String s = strs.get(0);   // 无需强转，直接当 String 用，能调 String 特有方法
```

### 两个补充点

**① "泛型是编译阶段的功能" = 类型擦除**
编译生成的字节码里**没有** `<String>` —— 运行时的 ArrayList 并不知道自己存过什么。泛型检查全部发生在编译期，编译通过后标签就被"擦掉"，不付出运行时代价。

**② Java 7 钻石表达式 `<>`**
右边的类型编译器能从左边推出来，不用重写一遍：

```java
Collection<String> strs = new ArrayList<>();   // <> 留空，编译器自己推
```

### 速记

> 泛型 = 合同，签给编译器看；放错类型**编译就报错**
> 两大好处：类型安全（错误提前）+ 代码简洁（免强转）
> 类型擦除：编译后 `<T>` 就没了，只活在编译期
> Java 7 钻石 `<>`：右边类型让编译器推

---

## 二十九、泛型的使用：类 / 静态方法 / 接口

> **一句话**：泛型能定义在类、静态方法、接口三个位置 —— 类上的 T 跟着对象走（new 时确定），静态方法没有对象所以必须自己声明 `<T>`，接口泛型由实现类决定写死还是继续传。

![[generics-declaration-positions.svg]]

### ① 在类上定义泛型

语法 `class 类名<泛型1, 泛型2...>`，泛型参数名随便起（惯例 T、E、K、V）：

```java
public class MyClass<NameType, AgeType> {
    private NameType name;
    private AgeType age;

    public MyClass(NameType name, AgeType age) {
        this.name = name;
        this.age = age;
    }
    // getter/setter 同理，全用 NameType/AgeType
}

// 使用：new 的那一刻确定类型
MyClass<String, Integer> myClass = new MyClass<>("jack", 40);
String name = myClass.getName();     // 直接当 String 用
Integer age = myClass.getAge();      // 直接当 Integer 用
```

关键理解：**类上的 T 跟着对象走** —— 每个 `new` 确定一次自己的类型。

### ② 静态方法：类上的泛型用不了，要自己声明

**为什么？** 类上的 T 在 `new` 时才确定，而静态方法**不依赖对象** —— 类加载时就存在了，那时类型还没定，编译器不让用。

解决：静态方法自己声明泛型，写在**返回值类型前面**：

```java
// <T> 在 static 和返回值之间，这是"方法自己的泛型"
public static <T> T first(List<T> list) {
    return list.get(0);
}
// 调用时编译器自动推断 T
String s = first(List.of("a", "b"));   // T = String
```

### ③ 在接口上定义泛型

```java
public interface Flyable<T> {
    void fly(T t);
}
```

实现时分两种情况：

```java
// 知道具体类型：直接写死
public class MyClass implements Flyable<Bird> {
    public void fly(Bird b) { ... }
}

// 不知道具体类型：继续把 T 往下传
public class MyClass<T> implements Flyable<T> {
    public void fly(T t) { ... }
}
```

第二种就是 `Comparable<E>`、`Comparator<E>` 的用法 —— 写类的人不知道用户要比较什么，把类型决定权留给使用者。

### 速记

> 类上的 T 跟对象走，new 时确定
> 静态方法没对象 → 自己声明 `<T> T m(...)`，写在返回值前
> 接口泛型：知道类型写死，不知道 `class C<T> implements I<T>` 继续传
> `Comparable<E>` 就是"接口泛型 + 继续传"的典型

---

## 三十、泛型通配符与 PECS

> **一句话**：泛型没有继承性（`List<String>` 不是 `List<Object>` 的子类），所以方法参数想收"某类范围的类型"就得用通配符 `?` —— `<?>` 任意、`extends` 上限读、`super` 下限写。

![[generics-wildcards.svg]]

### 先踩坑：泛型没有继承性

```java
public static void print(List<Object> list) { ... }

print(new ArrayList<String>());   // 编译报错！
```

`String` 是 `Object` 的子类，但 **`List<String>` 不是 `List<Object>` 的子类**。如果允许，就能往里 `add(new Object())`，把"只装 String"的合同撕了。

### 三种通配符

| 写法 | 含义 | 典型场景 |
|------|------|----------|
| `<?>` | 任意类型 | 只关心个数不关心元素 |
| `<? extends Number>` | Number **及子类**（上限） | 读取元素当 Number 用（只读） |
| `<? super Number>` | Number **及父类**（下限） | 往里写 Number 及子类（只写） |

```java
public static double sum(List<? extends Number> list) {   // Integer/Double 都能传
    double total = 0;
    for (Number n : list) total += n.doubleValue();
    return total;
}
```

### PECS 口诀

**P**roducer **E**xtends, **C**onsumer **S**uper：

- **生产者用 extends**：数据源只往外读 → `<? extends T>`，读出来一定是 T
- **消费者用 super**：数据汇只往里写 → `<? super T>`，写的元素一定兼容 T

### 速记

> 泛型无继承性：`List<String>` ≠ `List<Object>` 的子类
> `?` 三式：任意 `<?>` / 上限 `extends` / 下限 `super`
> PECS：读 extends，写 super

---

## 三十一、迭代时删除元素与 fail-fast 机制

> **一句话**：遍历集合时要删元素，**只能用 `迭代器对象.remove()`，不能用 `集合对象.remove(元素)`** —— 后者会触发 fail-fast，在下一次 `next()` 时抛 `ConcurrentModificationException`。

![[fail-fast-compare.svg]]

### 三种删除方式对比

| 方式 | 结果 | 原因 |
|------|------|------|
| 边遍历边 `集合.remove(元素)` | ❌ 抛异常 | 只改了集合的 `modCount`，迭代器的 `expectedModCount` 没同步 |
| 边遍历边 `迭代器.remove()` | ✅ 正常 | 两个计数**同时 +1** |
| 遍历结束后再删 / fori 倒序 / `removeIf` | ✅ 正常 | 遍历过程中没有结构修改 |

### fail-fast 的源码原理

集合体系里有两个计数器，它们的"一致"就是安全线：

```text
集合对象:   int modCount;          // 结构修改次数，增/删都 +1
迭代器对象: int expectedModCount;  // 创建迭代器那一刻 = modCount
```

`next()` 每次执行都先检查 `modCount != expectedModCount`，不等就立刻抛异常 —— **宁可失败，不带错运行**，这就是"快速失败"（fail-fast）。

时序还原：迭代器创建时 `expectedModCount = modCount = 0`；`list.remove("B")` → `modCount=1` 但 `expectedModCount` 仍为 0；下一次 `it.next()` 发现 `1 != 0` → 抛异常。而 `it.remove()` 会把两个计数**同步 +1**，检查永远通过。

### 两个红线（易错点）

1. **单线程也算"并发修改"**：哪怕没有多线程，"迭代器遍历 + 集合删除"这个组合就被认定为并发修改 —— 迭代器无法预知是不是真有另一个线程，干脆一律防御。
2. **`it.remove()` 删的是"上一次 `next()` 返回的元素"**，所以必须**先 `next()` 再 `remove()`**，否则 `IllegalStateException`：

```java
Iterator<String> it = list.iterator();
// it.remove();          // ❌ IllegalStateException，还没 next 过
it.next();
it.remove();             // ✅ 先 next 再 remove
```

### 正确代码 + 不用迭代器的替代方案

```java
List<String> list = new ArrayList<>(Arrays.asList("A", "B", "C"));

// ✅ 标准写法：迭代器删
Iterator<String> it = list.iterator();
while (it.hasNext()) {
    String s = it.next();
    if (s.equals("B")) it.remove();
}

// 替代 1：fori 倒序（从后往前删，不受结构变化影响）
for (int i = list.size() - 1; i >= 0; i--) {
    if (list.get(i).equals("B")) list.remove(i);
}

// 替代 2：JDK8+ 一行搞定，实际开发最常用
list.removeIf(s -> s.equals("B"));
```

### 速记

> 遍历中删元素：用**迭代器** remove，不用集合 remove
> 异常名：`ConcurrentModificationException`（fail-fast 快速失败）
> 本质：`modCount ≠ expectedModCount` → `next()` 当场抛
> `it.remove()` 删的是**上一个 next() 返回的**，先 next 再 remove
> 实战首选 `removeIf`，一行搞定

---

## 三十二、Map 继承结构与三大家族

> **一句话**：Map 是 key/value 键值对集合，**key 主导一切**（不可重复、决定取值，value 只是附属）；整个家族分三派 —— HashMap 系、Hashtable 系、TreeMap 系。

![[map-inheritance.svg]]

### 核心概念

1. Map 以 key/value 键值对存储，**key 和 value 存的都是引用**
2. **key 起主导作用**，value 是挂在 key 上的附属 —— 取值靠 key，去重也看 key
3. key 不可重复，**key 重复时 value 覆盖**（相当于修改）
4. `SequencedMap` 是 Java 21 新增的接口；Map 和 Collection **没有继承关系**（两套独立体系）

### 三大家族对照

| 实现 | 底层数据结构 | key 特点 | 备注 |
|------|--------------|----------|------|
| **HashMap** | 哈希表（数组+链表+红黑树） | 无序 · 不可重复 | 使用最多，线程不安全 |
| **LinkedHashMap** | 双向链表 + 哈希表 | **有序** · 不可重复 | HashMap 子类，效率略低 |
| **Hashtable** | 哈希表 | 无序 · 不可重复 | 方法全线程安全 → 效率低，已少用 |
| **Properties** | 哈希表 | key/value **都必须是 String** | 属性类，配置文件专用 |
| **TreeMap** | 红黑树 | **可排序** · 不可重复 | 实现 SortedMap → NavigableMap |

接口侧：`SortedMap` → `NavigableMap` → 由 TreeMap 实现；`SequencedMap`（Java21）由 LinkedHashMap 实现。

### 速记

> Map：key 主导，value 附属；key 重复 → value 覆盖
> 三大家族：HashMap（哈希无序）/ TreeMap（红黑树可排序）/ Hashtable（线程安全但慢）
> Properties：KV 都是 String 的属性类
> Map 和 Collection 没有继承关系，两套独立体系

---

## 三十三、Set 的底层真相（Set 就是 Map 的 key）

> **一句话**：HashSet 底层 new 了一个 HashMap，TreeSet new 的是 TreeMap，LinkedHashSet new 的是 LinkedHashMap —— **元素全存在 Map 的 key 位，value 位放固定常量 PRESENT 纯占位**，Set 的一切特性都继承自 Map 的 key。

![[set-underlying-map.svg]]

### 对应关系

| Set | 底层 new 的 Map | 特性来源 |
|-----|-----------------|----------|
| HashSet | **HashMap**（哈希表） | 哈希表 → 无序、不可重复 |
| TreeSet | **TreeMap**（红黑树） | 可排序、不可重复 |
| LinkedHashSet | **LinkedHashMap**（双向链表+哈希表） | 有序、不可重复 |

### add 的真实实现

```java
// 向 Set 集合 add 时，底层实际是 Map.put：
set.add(e);   // 等价于 ↓
map.put(e, PRESENT);   // PRESENT 是固定不变的常量，value 纯占位，主要看 key
```

### 为什么这个视角有价值

之前单独背的"Set 三兄弟特点"（无序/有序、可排序、不可重复、底层结构）在这一刻**全部有了出处**——它们不是 Set 自己的特性，而是 Map 的 key 的特性顺着底层实现"漏"上来的。理解了这一点，Set 和 Map 两大家族不用分开背。

### 速记

> **HashSet = HashMap 的 key，TreeSet = TreeMap 的 key，LinkedHashSet = LinkedHashMap 的 key**
> `set.add(e)` 就是 `map.put(e, PRESENT)`，value 是占位常量
> Set 的特性 = Map 的 key 的特性（无序/有序/可排序/不可重复 全部对上）

---

## 三十四、HashMap：key 去重机制与自定义 key 陷阱

> **一句话**：HashMap 的 key 无序、不可重复，**重复的判断分两步走 —— 先比 hashCode 再比 equals**；把自定义类当 key 用时，必须同时重写 `hashCode()` 和 `equals()`，否则去重失效。

![[hashmap-key-dedup.svg]]

### HashMap 的 key 特点

| 特点 | 说明 |
|------|------|
| 无序 | 存进去的顺序和取出来的顺序没有关系（LinkedHashMap 才有序） |
| 不可重复 | 相同的 key 只保留一个 |
| value 可重复 | key 判重只看 key，value 随便重复 |
| key 重复 | **value 覆盖**（新值换旧值，相当于修改） |

### 去重两步走

```java
// 判断 key 是否相同，先 hashCode 后 equals：
// 第 1 步：比 hashCode() —— 不同直接判定不是同一个 key（快筛）
// 第 2 步：hashCode 相同再比 equals() —— 相同才算"重复 key"
map.put(k1, v1);
map.put(k2, v2);   // 若 k2 与 k1 判定为同一 key → v1 被 v2 覆盖
```

### 自定义 key 陷阱（重点）

```java
// 没重写 hashCode/equals 的类当 key —— 去重失效
Student s1 = new Student("张三");
Student s2 = new Student("张三");   // 内容相同，但是两个对象
map.put(s1, 100);
map.put(s2, 200);
// 没重写时 s1、s2 的 hashCode 来自 Object（按地址算）→ 两步都判"不同"
// → map 里出现两个"张三"，去重失效

// 正确做法：重写类里必须同时重写两个方法
@Override public int hashCode() { ... }
@Override public boolean equals(Object o) { ... }
```

规范约定：**equals 相等 → hashCode 必须相等**；只重写一个会出现"明明 equals 相等却散到不同桶里"的诡异 bug。

### 速记

> HashMap key：无序、不可重复，重复 → value 覆盖
> 判重两步走：先 hashCode（快筛），再 equals（精判）
> 自定义类当 key：hashCode 和 equals **必须同时重写**
> 规范：equals 相等 ⇒ hashCode 相等

---

## 三十五、HashMap 底层：哈希表与源码

> **一句话**：HashMap 底层是**哈希表 = 位桶数组 + 链表 + 红黑树**，靠 hash 定位数组下标做到接近 O(1) 的存取；链表长度 ≥ 8 且数组长度 ≥ 64 时链表树化为红黑树。

![[hashmap-hash-table.svg]]

### 底层结构

| 结构 | 作用 |
|------|------|
| 位桶数组 `Node<K,V>[] table` | 哈希表主体，每个格子叫一个"桶"（bucket） |
| 链表 | hash 冲突的 key 挂在同一个桶里，拉链法 |
| 红黑树 | 链表太长时的优化，查询从 O(n) 提到 O(log n) |

### Node 源码（JDK 8）

```java
static class Node<K,V> implements Map.Entry<K,V> {
    final int hash;      // key 的 hash 值，算一次缓存住
    final K key;         // final：key 存进去之后引用不再变
    V value;             // value 可以被覆盖换新
    Node<K,V> next;      // 单向链表，指向冲突的下一个节点
}
```

### 关键机制

1. **首次 put 才初始化数组** —— new HashMap() 时 table 是 null，懒加载
2. **容量永远是 2 的幂** —— 16 → 32 → 64…，为了 `hash & (capacity-1)` 位运算代替取模，算下标快且散列均匀
3. **树化条件（两个都要满足）**：链表长度 ≥ 8 **且** 数组长度 ≥ 64；数组不够 64 时优先扩容而不是树化
4. put 流程：算 key 的 hash → 定位桶 → 桶空直接放 → 不空则两步判重（hashCode/equals）→ 重复覆盖 value，不重复尾插

### 容量 2 的幂的原理（位运算视角）

![[hashmap-capacity-power2.svg]]

**为什么等式成立**：只有 length 是 2 的幂时，`length - 1` 的二进制才是全 1（如 16-1 = `1111`），此时 `hash & (length-1)` 才等价于 `hash % length`。位运算是二进制里最快的运算，所以容量坚持 2 的幂。

**为什么奇数不行**：奇数 length - 1 一定是偶数，二进制末位是 0，与任何数做与运算结果末位必为 0 → **所有奇数下标的桶永远空着，白白浪费一半空间**，哈希冲突反而暴增。

### 扩容与负载因子

| 项 | 值 / 规则 |
|----|-----------|
| 负载因子 loadFactor | 默认 **0.75**，空间利用率与冲突率的折中 |
| 扩容阈值 threshold | 容量 × loadFactor，如 16 × 0.75 = **12** |
| 触发时机 | HashMap 中元素数 **超过阈值**（数组长度 × loadFactor）时，执行 put 就会扩容 |
| 扩容动作 | 容量翻倍 16 → 32，**遍历全部元素 rehash** 重新散到新哈希表中 |
| 代价 | rehash 非常消耗性能 → 能避免就避免 |

**预估容量实践**：要存 1000 个元素，设 1024 仍会扩容（1024 × 0.75 = 768 < 1000），直接设 **2048**（2048 × 0.75 = 1536 ≥ 1000）一步到位 —— 既考虑了 `&` 运算，也避免了扩容。

**思考题答案**：`new HashMap(15)` 对象创建成功，实际容量是 **16** —— 构造参数只是"建议值"，内部 `tableSizeFor()` 会向上取最近的 2 的幂（15→16，31→32）。

### 为什么快

存取都先由 hash 直接算出数组下标，不用一个个遍历 —— 定位是 O(1)；即使冲突也只是遍历一小段链表/红黑树。这就是哈希表集合（HashMap / HashSet / Hashtable）效率高的根本原因。

### 速记

> 哈希表 = 数组 + 链表 + 红黑树（JDK 8 起）
> Node 四件套：hash（缓存）· key（final）· value（可覆盖）· next（拉链）
> 首次 put 才建数组，容量恒为 2 的幂
> 2 的幂原理：hash & (length-1) == hash % length 才成立；奇数长度 → 末位恒 0，浪费一半桶
> 扩容阈值 = 容量 × 0.75（16→12），超了就翻倍 + 全量 rehash（耗性能）
> 存 1000 个元素直接设 2048；new HashMap(15) 实际容量 16（tableSizeFor 向上取整）
> 树化两条件：链表 ≥ 8 且数组 ≥ 64，否则先扩容
> 哈希表快的本质：hash 直接定位下标，O(1)

---

## 三十六、进程与线程概述

> **一句话**：进程是操作系统中**正在执行的程序实例**，有独立内存和系统资源；线程是进程里**负责执行一段代码**的单元，共享进程资源、各有私有栈 —— 多线程的目的就是榨干 CPU。

![[thread-process-vs.svg]]

### 进程 vs 线程对照

| | 进程 | 线程 |
|---|------|------|
| 是什么 | 正在执行的程序实例 | 进程中负责执行一段代码的单元 |
| 内存 | 有**独立的**内存空间和系统资源（文件、网络端口等） | 没有独立内存，**共享进程的资源** |
| 私有物 | —— | 每个线程有自己的**栈**和**程序计数器** |
| 创建顺序 | 先创建进程 | 再在进程中创建线程 |

### 两种并发

1. **多进程并发**：现代操作系统支持同时启动多个软件，一个软件也可以启动多个进程
2. **多线程并发**：一个进程内启动多个线程，同一时刻执行不同的操作，提高程序执行效率

### 多线程的作用

CPU 处理一个任务的同时还能处理多个线程 → 充分利用 CPU 资源 → 提高处理效率和利用率。

### 速记

> 进程 = 独立厂房（独立内存+资源），线程 = 厂房里的工人（共享资源、私有栈）
> 先建进程，再建线程；线程执行的就是进程中的一段代码
> 多线程的目的：榨干 CPU，提高利用率

---

## 三十七、JVM 与 Java 程序运行原理

> **一句话**：JVM 内存按"共享 / 私有"划分 —— **堆和方法区所有线程共享，虚拟机栈、本地方法栈、程序计数器每线程私有**；`java HelloWorld` 一回车，JVM 这个进程至少启动 main 主线程和垃圾回收线程两个线程。

![[thread-jvm-memory.svg]]

### 共享 vs 私有（重点）

| 归属 | 区域 | 为什么 |
|------|------|--------|
| **线程共享**（一份） | 堆 Heap、方法区 | 线程间通信、数据共享的地方 → 也是线程安全问题的来源 |
| **每线程私有**（各一份） | 虚拟机栈、本地方法栈、程序计数器 | 互不干扰，线程切换时能恢复现场 |

和条目十二的内存分析对照记：堆/方法区 = 公共车间，栈 = 私人工位。

### java HelloWorld 回车之后

1. JVM 启动 —— **JVM 的启动就是一个进程的启动**
2. JVM 会先启动一个**主线程（main-thread）**，由主线程负责调用 main 方法 → **main 方法是在主线程里运行的**
3. 除此之外还启动了一个**垃圾回收线程** → JVM 启动**至少两个线程**
4. main 方法执行过程中，程序员可以手动创建其他线程对象并启动

### 速记

> 堆 + 方法区 = 线程共享；两个栈 + 程序计数器 = 线程私有
> 共享区是通信的地方，也是冲突的来源；私有区保证互不干扰
> 启动 JVM = 启动一个进程 = 至少 main 主线程 + GC 线程
> main 方法跑在主线程里

---

## 附录：速查总表

### 字面量后缀规则

| 写法 | 默认类型 | 说明 |
|------|----------|------|
| `100` | int | 整数字面量默认 int |
| `100L` | long | 超 int 范围必须加 `L` |
| `3.0` | double | 浮点字面量默认 double |
| `3.0F` | float | 赋给 float 必须加 `F` |

### 类型提升链

```
byte / short / char  →  int  →  long  →  float  →  double
    （一运算就变 int）        （自动拓宽，无需强转）
```

### 内存区域速查

| 区域 | 存储内容 | 生命周期 |
|------|----------|----------|
| 虚拟机栈 | 局部变量、方法栈帧 | 方法结束即销毁栈帧 |
| 堆 Heap | 对象、实例变量、类对象 | 由 GC 回收 |
| 元空间 Metaspace | 类的元数据（.class 信息） | 使用本地内存 |

### 常见概念速查

| 概念 | 一句话 |
|------|--------|
| 对象 | 堆里的数据块 |
| 引用 | 保存对象地址的变量 |
| 空指针 | 引用为 null 却去访问对象 |
| 参数传递 | 复制一份值再传 |
| this | 指向当前对象的引用 |
| 构造方法 | 没有返回值、方法名同类名、new 时自动调用 |
| 构造代码块 | 类中 `{}` 包起来的代码，每次 new 对象时执行，且在构造方法之前 |
| 继承 | 子类直接拥有父类的属性和方法，作用是代码复用、铺垫多态 |
| `extends` | 扩展，子类继承父类后是对父类的扩展 |
| 父类 / 子类 | 被继承的叫父类（superclass），去继承的叫子类（subclass） |
| `Object` | Java 类体系的根，没写 extends 的类默认继承它 |
| 方法覆盖 | 父子类之间用子类实现替换父类实现，是多态的前提 |
| `@Override` | 注解，编译期检查是否真的重写了父类方法 |
| 协变返回 | 子类覆盖方法的返回值可以是父类返回值的子类（Java 5+） |
| 动态分派 | 实例方法运行期按实际对象类型决定，静态方法/变量是编译期按引用类型 |
| 多态 | 编译期一种形态、运行期另一种形态，父类型引用指向子类对象 |
| 向上转型 | 子 → 父，自动转换，永远安全 |
| 向下转型 | 父 → 子，必须强转，有 ClassCastException 风险 |
| `instanceof` | 判断引用指向的对象是否属于某类型，返回 boolean，转型前必用 |
| 抽象类 | 半成品模板，不能 new 但有构造方法，作用是逼子类实现细节 |
| 抽象方法 | 只有声明没有方法体（`;` 结尾），非抽象子类必须重写 |
| `abstract` | 修饰类 → 不能实例化；修饰方法 → 无方法体，强制子类重写 |
| 接口 | 完全抽象的规范，描述实现类该有什么行为，不能 new、无构造方法 |
| `implements` | 类实现接口，可以多实现 |
| 默认方法 | Java 8+ `default`，接口提供默认实现，解决接口演变问题 |
| is-a / can-do | 抽象类表达"是什么"（单继承），接口表达"能做什么"（多实现） |
| 访问控制权限 | 4 个修饰符 `private` / 缺省 / `protected` / `public`，控制成员在不同目录位置的可见性 |
| `private` | 只能本类访问，范围最小 |
| `public` | 任何位置都能访问，范围最大 |
| `protected` | 同包 + 子类可访问，给"子孙"用 |
| 内部类 | 定义在类内部的类，共 4 种（静态·实例·局部·匿名） |
| `static class` | 静态内部类，成员区，可有静态成员，`new Outer.Inner()` |
| `outer.new Inner()` | 实例内部类，成员区，**必须**先有 outer 实例 |
| 匿名内部类 | 没有类名，定义即实例化，函数式接口可用 Lambda 替代 |
| 有效 final | JDK 8+，局部变量没被改过就视为 final，被内部类用过后就"冻结" |
| `args` | main 方法的 String[] 形参，接收命令行参数，空格分隔 |
| 可变长参数 | `int...` 是 `int[]` 的语法糖，只能放形参最后、一个方法最多一个 |
| JUnit 5 | Java 主流单元测试框架，JDK 不自带，需引入 3 个 jar |
| `@Test` | 标注方法是测试方法，必须 void + 无参 + 命名 testXxx |
| 断言 | `assertEquals(期望, 实际)` 等方法自动比较，期望==实际才通过 |
| `@BeforeAll` / `@AfterAll` | 整个测试类前后各跑 1 次，方法必须是 static |
| `@BeforeEach` / `@AfterEach` | 每个 @Test 前后各跑 1 次，方法是实例方法 |
| `Throwable` | 异常体系的根，所有异常和错误都继承它，只有它和子类能 throw/throws |
| `Error` | JVM 层面错误（OOM、StackOverflow），无法处理，出现即终止 |
| `Exception` | 程序层面异常，可处理，分 Checked（受检）和 RuntimeException（非受检） |
| Checked 异常 | 受检异常，编译器强制 try-catch 或 throws（如 IOException） |
| Unchecked 异常 | 非受检异常（RuntimeException 派），编译器不强制处理（如 NPE） |
| 自定义异常 | 继承 Exception/RuntimeException + 两个构造方法（无参 + String），表示业务错误 |
| `throw` | 方法体内手动抛出异常对象，抛出后方法立即终止 |
| `throws` | 方法签名上声明可能抛出的异常类型，只是声明不终止 |
| 正则元字符 | `.` 任意、`\w` 单词、`\s` 空白、`\d` 数字、`^$` 开始结束 |
| 正则量词 | `*` 0+、`+` 1+、`?` 0或1、`{n}` 恰好、`{n,m}` 范围 |
| 正则字符类 | `[]` 任选其一，`[^]` 取反；符号本身要转义 `\.` |
| 正则分组分支 | `()` 打包整体，`|` 二选一；`(\d{1,3}\.){3}` 整段重复 |
| 正则反义 | 大写取反：`\W` `\S` `\D` `\B` |
| Java 正则双转义 | 字符串里 `\` 也要转义，`"\\d"` 才是正则的 `\d` |
| 泛型 | `<类型>` 标签，编译期检查集合元素类型，把放错类型提前到编译期报错 |
| 类型擦除 | 泛型只活在编译阶段，编译后字节码里没有 `<T>`，运行时不知道存过什么类型 |
| 钻石表达式 | Java 7 `new ArrayList<>()`，右边类型由编译器从左边推断 |
| 泛型两大好处 | 类型安全（错误从运行时提前到编译期）+ 代码简洁（get 免强转） |
| 类上泛型 | `class MyClass<T>`，T 跟着对象走，new 时确定 |
| 静态方法泛型 | 类上的 T 静态方法用不了（没对象），必须自己声明 `static <T> T m(...)`，`<T>` 写在返回值前 |
| 接口泛型 | `interface Flyable<T>`；实现时知道类型写死 `<Bird>`，不知道 `class C<T> implements I<T>` 继续传 |
| 泛型无继承性 | `List<String>` 不是 `List<Object>` 的子类，即使 String 是 Object 的子类 |
| 通配符 `<?>` | 任意引用类型，元素类型未知，除 Object 外啥也不能加 |
| 上限通配符 | `<? extends Number>`：Number 及子类，适合只读（生产者） |
| 下限通配符 | `<? super Number>`：Number 及父类，适合只写（消费者） |
| PECS | Producer Extends / Consumer Super：读 extends，写 super |
| fail-fast 机制 | 快速失败：迭代期间发现结构修改立即抛异常，不带错运行 |
| `ConcurrentModificationException` | 遍历时用集合对象删元素触发；本质 `modCount ≠ expectedModCount` |
| `modCount` | 集合的修改计数字段，增/删都 +1 |
| `expectedModCount` | 迭代器创建时初始化为 modCount；`it.remove()` 会同步 +1，集合 remove 不会 |
| `it.remove()` | 删除"上一次 next() 返回的元素"，必须先 next 再 remove，否则 IllegalStateException |
| `removeIf` | JDK8+ 按条件删除，`list.removeIf(s -> s.equals("B"))`，不触发 fail-fast |
| Map | key/value 键值对集合，key 主导（不可重复、决定取值），value 是附属；与 Collection 无继承关系 |
| Map 家族 | HashMap（哈希无序）/ LinkedHashMap（链表+哈希有序）/ Hashtable（线程安全慢）/ TreeMap（红黑树可排序） |
| key 重复 | Map 的 key 重复时 value 覆盖（相当于修改） |
| Properties | 属性类，key 和 value 都必须是 String，配置文件专用 |
| SequencedMap | Java 21 新增接口，LinkedHashMap 实现 |
| HashSet 底层 | new 了一个 HashMap，元素存 key 位，value 放固定常量 PRESENT |
| TreeSet 底层 | new 了一个 TreeMap（红黑树），可排序 |
| LinkedHashSet 底层 | new 了一个 LinkedHashMap（双向链表+哈希表），有序 |
| `set.add(e)` | 实际是 `map.put(e, PRESENT)`，Set 特性全部来自 Map 的 key |
| HashMap 的 key | 无序、不可重复；key 重复 → value 覆盖 |
| HashMap 判重两步走 | 先比 hashCode（快筛），相同再比 equals（精判） |
| 自定义 key | 必须同时重写 hashCode + equals，否则去重失效 |
| equals / hashCode 规范 | equals 相等 ⇒ hashCode 必须相等 |
| HashMap 底层 | 哈希表 = 位桶数组 + 链表 + 红黑树，存取接近 O(1) |
| Node<K,V> | hash（缓存）· key（final）· value（可覆盖）· next（拉链） |
| HashMap 懒加载 | 首次 put 才初始化数组，new 时 table 为 null |
| 容量 2 的幂 | 为了 `hash & (capacity-1)` 位运算代替取模，快且散列均匀 |
| 树化条件 | 链表长度 ≥ 8 **且** 数组长度 ≥ 64，否则优先扩容 |
| `hash & (length-1)` | 等价于 `hash % length`，**仅当 length 是 2 的幂**；位运算更快 |
| 奇数容量的问题 | length-1 末位是 0 → 与运算末位恒 0 → 奇数下标桶全空，浪费一半空间 |
| loadFactor | 负载因子，默认 0.75；扩容阈值 = 容量 × loadFactor |
| 扩容 resize | 元素数超阈值 → 容量翻倍（16→32）+ 全部元素 rehash，非常耗性能 |
| tableSizeFor | 构造传入的容量只是建议值，向上取最近的 2 的幂（15→16，31→32） |
| 预估容量 | 存 1000 个元素设 2048（1024×0.75=768<1000 仍会扩容） |
| 进程 | 操作系统中正在执行的程序实例，有独立内存空间和系统资源 |
| 线程 | 进程中负责执行一段代码的单元，共享进程资源，私有栈和程序计数器 |
| 多线程的作用 | CPU 同时处理多个线程，充分利用 CPU 资源，提高效率 |
| 线程共享内存 | 堆 Heap、方法区（一份，线程通信的地方，也是冲突来源） |
| 线程私有内存 | 虚拟机栈、本地方法栈、程序计数器（各一份，互不干扰） |
| JVM 启动线程 | java 程序启动至少两个线程：main 主线程 + 垃圾回收线程 |

### 报错速查

| 代码 | 是否报错 | 原因 |
|------|----------|------|
| `long a = 10;` | ✅ | int → long 自动拓宽 |
| `long b = 2147483648;` | ❌ | 字面量超 int 范围 |
| `float c = 3.0;` | ❌ | double → float 大转小 |
| `short s = 100;` | ✅ | 常量在范围内自动窄化 |
| `s = s - 99;` | ❌ | 结果是 int |
| `b = b + 1;` | ❌ | 结果是 int |
| `b += 1;` | ✅ | 复合赋值自动强转 |
| `byte c = a1 + a2;` | ❌ | 小类型运算结果仍是 int |
| `double d = c + i + f;` | ✅ | 向最大类型自动提升 |
| `z == 2.3`（浮点） | ⚠️ | 逻辑上错，应用 epsilon |
| `new Student()`（只有有参构造时） | ❌ | 显式定义构造方法后默认无参构造消失 |
| `class C extends A, B { }` | ❌ | Java 不支持多继承，只能 extends 一个 |
| 子类里直接访问父类 private 成员 | ❌ | private 继承下来但不可见，需 getter/setter |
| 子类里直接调用父类构造方法 | ❌ | 构造方法不继承，用 `super(...)` 调用 |
| 覆盖方法把权限改成 private | ❌ | 访问权限不能变低 |
| 覆盖方法抛出比父类更多的异常 | ❌ | 异常不能变多，只能变少或是子类 |
| 子类覆盖父类 private 方法 | ❌ | private 不继承，子类写的只是同名新方法 |
| `@Override` 标在非覆盖方法上 | ❌ | 编译报错（这正是加注解的价值） |
| `Dog d = (Dog) new Cat()` 的引用 | ⚠️ | 编译过、运行抛 ClassCastException |
| 无继承关系的两个类型互转 | ❌ | 编译报错，转型前提是有继承 |
| 想靠多态调到子类独有方法 | ❌ | 编译期父类没有该方法，需先向下转型 |
| `new Animal()`（Animal 是抽象类） | ❌ | 抽象类不能实例化 |
| 非抽象子类不重写父类抽象方法 | ❌ | 编译器强制要求实现 |
| `private abstract void m();` | ❌ | private 不继承，无法被重写 |
| `final abstract void m();` | ❌ | final 禁止重写，与 abstract 矛盾 |
| `static abstract void m();` | ❌ | static 无多态，"重写"无意义 |
| 实现类不重写接口所有抽象方法 | ❌ | 非抽象实现类必须全部实现（或自己 abstract） |
| `Printer.info()`（info 是接口静态方法） | ❌ | 接口静态方法不被实现类继承，只能 `Usb.info()` |
| 接口中定义普通实例字段 | ❌ | 接口字段只能是 `public static final` 常量 |
| `new Usb()`（Usb 是接口） | ❌ | 接口完全没有构造方法，不能实例化 |
| 顶层类用 `private` 修饰 | ❌ | 类的访问权限只有 `public` 和缺省两种 |
| 顶层类用 `protected` 修饰 | ❌ | 同上，`protected` 不修饰顶层类 |
| 访问控制符修饰局部变量 | ❌ | 局部变量只在方法内，谈不上跨类访问 |
| 跨包普通类访问 protected 字段 | ❌ | `protected` 只对子类和同包开放，不对"路人"开放 |
| `new Outer.Inner()`（Inner 是实例内部类） | ❌ | 实例内部类必须 `outer.new Inner()` |
| 在实例内部类里定义 `static int a;` | ❌ | 实例内部类不能有静态成员（`static final` 常量除外） |
| 匿名内部类继承 2 个类 | ❌ | 匿名内部类只能继承一个类 或 实现一个接口（二选一） |
| 内部类里修改被捕获的局部变量 | ❌ | 局部变量被内部类用过后就被"冻结"（有效 final） |
| `void m(int... a, String b)` | ❌ | 可变长参数只能放形参列表最后 |
| `void m(int... a, int... b)` | ❌ | 一个方法最多一个可变长参数 |
| `m(int[])` 与 `m(int...)` 同时定义 | ❌ | 编译后签名相同 → 报"重复方法" |
| 测试方法没加 `@Test` 注解 | ❌ | JUnit 不识别为测试方法，运行时不会跑 |
| 测试方法返回值非 void | ❌ | JUnit 5 要求测试方法必须返回 void |
| `@BeforeAll` 标注非 static 方法 | ❌ | @BeforeAll/@AfterAll 必须标注 static 方法 |
| `@Test` 方法用了带参构造 | ❌ | JUnit 不会传参，测试方法形参必须为 0 |
| 编译时异常不写 try-catch / throws | ❌ | 受检异常必须处理，否则编译报错 |
| try-catch 捕获 `OutOfMemoryError` | ⚠️ | Error 接不住也没意义，出现即 JVM 终止 |
| `Integer.parseInt("abc")` | ❌ | 抛 NumberFormatException（运行时异常） |
| `new FileInputStream("不存在的文件")` | ❌ | 抛 FileNotFoundException（编译时异常，必须处理） |
| 自定义异常只有无参构造 | ⚠️ | 缺 String 构造 → 异常只有类型没信息，getMessage() 拿不到描述 |
| `throw` 后面还写代码 | ❌ | throw 抛出后方法立即终止，后面代码不可达（编译报错） |
| 方法 throws 编译时异常但调用方不处理 | ❌ | 调用方必须 try-catch 或继续 throws |
| 自定义类只重写 equals 不重写 hashCode 当 key | ⚠️ | 内容相同的两个对象散到不同桶 → 去重失效 |
| 自定义类只重写 hashCode 不重写 equals 当 key | ⚠️ | 同桶内 equals 判"不同" → 出现重复 key |
| new HashMap() 后立即 put 前访问内部数组 | ⚠️ | table 为 null，首次 put 才初始化（懒加载） |
