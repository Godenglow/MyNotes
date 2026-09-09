# JavaSE 基础问答笔记

> 来源：动力节点 JavaSE 教程 · 课堂答疑整理
> 整理日期：2026-08-31
> 适用：Obsidian 阅读
> 范围：基本数据类型、类型转换、Scanner、运算符、包机制、对象与内存、构造方法、this 关键字、继承、方法覆盖、多态、抽象类、接口、访问控制权限

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
