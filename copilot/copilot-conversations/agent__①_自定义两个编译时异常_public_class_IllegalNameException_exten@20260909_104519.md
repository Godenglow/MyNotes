---
epoch: 1788921919000
mode: agent
backendId: claude
sessionId: "13e2798e-2a25-44ef-becb-fb651d5d01ce"
agentLabel: "// ① 自定义两个编译时异常 public class IllegalNameException extends Ex…"
lastAccessedAt: 1788921990116
usage: '{"usedTokens":37186,"contextWindow":1000000,"inputTokens":15554,"outputTokens":0,"cacheReadTokens":21632,"cacheWriteTokens":0,"updatedAt":1788922034443}'
tags:
  - copilot-conversation
---

**user**: // ① 自定义两个编译时异常
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
介绍代码
[Timestamp: 2026/09/09 10:45:19]

**ai**: 我先看一下你附带的 JavaSE Q&A 笔记，确认这段代码的上下文（这段内容似乎出自笔记里的某个 Q&A），再给出讲解。笔记同时有 .md 版本，我先在 md 里找到这段代码对应的 Q&A 条目。
[Timestamp: 2026/09/09 10:45:19]

**user**: ?
[Timestamp: 2026/09/09 10:46:39]

**ai**: （抱歉，上一条只做了准备动作就被打断了——你贴的代码我在 [[JavaSE Q&A]] 的「二十六、自定义异常」里找到了原文，下面直接讲。）

## 这段代码在演示什么

它用「用户注册」当例子，完整演示了**自定义编译时异常的三件套**：定义异常类 → 业务方法里抛 → 调用方必须处理。

## ① 定义异常类

```java
public class IllegalNameException extends Exception { ... }
```

自定义异常的套路就两条：

- **继承 `Exception`** → 编译时异常（受检），编译器强制调用方处理。这里两个都继承了 `Exception`，所以整个例子围绕"不处理就编译不过"展开。
- **写两个构造方法**：无参的 + `String message` 有参的，有参构造里必须 `super(message)`。因为 message 字段存在父类 `Throwable` 里，不传给父类，后面 `e.getMessage()` 就拿不到报错内容——异常会变成"只有类型、没有信息"。

## ② 业务方法抛异常（throw + throws 各就各位）

```java
public void register(String name, int age)
        throws IllegalNameException, IllegalAgeException {
```

- **`throws`（签名上，声明）**：告诉编译器"我这个方法可能扔出这两种编译时异常"。因为抛的是编译时异常，这句不写直接编译报错。
- **`throw`（方法体内，动作）**：`throw new IllegalNameException("...")` 才是真正创建并扔出异常对象，`throw` 一执行，方法立刻终止，后面的代码不再运行。

判断逻辑就是两道业务校验：名字长度不在 6–12 位 → `IllegalNameException`；年龄小于 18 → `IllegalAgeException`；都通过才打印"注册成功"。

## ③ 调用方必须处理（try-catch）

```java
try {
    service.register("tom", 20);
    service.register("tom", 15);
} catch (IllegalNameException | IllegalAgeException e) {
    System.out.println("注册失败：" + e.getMessage());
}
```

- 因为 `register` 声明了抛编译时异常，`main` 里**不 try-catch 或继续 throws 就编译不过**——这就是"编译时异常"名字的由来：编译器在编译期就逼你处理。
- `catch (A | B e)` 是**多异常捕获**（Java 7+），两种异常共用一段处理代码，语法上要求两个异常类没有父子继承关系（这里没有，合法）。
- 被捕获后，`e.getMessage()` 取出 ① 里 `super(message)` 存进去的那句话，程序继续正常往下走，不会崩溃。

## ⚠️ 但这段代码有个 bug，运行结果和你笔记里写的不一样

笔记第 2512–2517 行写的预期输出是：

```
恭喜tom注册成功！
注册失败：年龄必须大于 18
```

这个输出**不可能出现**。`"tom"` 长度是 3，小于 6——第一个 `register("tom", 20)` 就会立刻抛 `IllegalNameException("名字长度必须在 6-12 位")`，控制流直接跳进 catch，"注册成功"打印不出来，第二行 `register("tom", 15)` 根本轮不到执行。真实输出应该是：

```
注册失败：名字长度必须在 6-12 位
```

想让示例按预期跑出"先成功、再因年龄失败"，把名字换成 **`"tomcat"`（正好 6 位）**：

```java
service.register("tomcat", 20);   // ✅ 恭喜tomcat注册成功！
service.register("tomcat", 15);   // ❌ 注册失败：年龄必须大于 18
```

这个 bug 本身反而是个好教学点：**try 块里一旦某一行抛异常，后面的行全部跳过**，跟"if 校验过了就不该有下一个异常"的直觉正好相反，出 bug 时经常从这里找。

## 顺带一提

你笔记前面"定义两步走"示例（JavaSE Q&A.md:2438）里，`IllegalAgeException` 继承的是 `Exception`、`IllegalNameException` 继承的是 `RuntimeException`——到了完整实战段，两个又都改成继承 `Exception` 了，前后不一致。学习阶段无伤大雅，但注意区分：继承 `Exception` 调用方**必须**处理，继承 `RuntimeException` 则"看着办"。笔记速记也写了：实际开发（尤其 Spring）业务异常基本都是 `RuntimeException` 派，就是不想逼每个调用方写 try-catch。

要不要我把笔记里这两处（运行效果 + 继承不一致）顺手改掉？
[Timestamp: 2026/09/09 10:46:39]