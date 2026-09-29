# JDBC

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

## 什么是JDBC
JDBC（Java DataBase Connectivity）就是Java数据库连接，说白了就是用Java语言来操作数据库。原来我们操作数据库是在控制台使用SQL语句来操作数据库，JDBC是用Java语言向数据库发送SQL语句。

## JDBC原理
早期SUN公司的天才们想编写一套可以连接天下所有数据库的API，但是当他们刚刚开始时就发现这是不可完成的任务，因为各个厂商的数据库服务器差异太大了。后来SUN开始与数据库厂商们讨论，最终得出的结论是，由SUN提供一套访问数据库的规范（就是一组接口），并提供连接数据库的协议标准，然后各个数据库厂商会遵循SUN的规范提供一套访问自己公司数据库服务器的API。SUN提供的规范命名为JDBC，而各个厂商提供的，遵循了JDBC规范的，可以访问自己数据库的API被称之为驱动！

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1760950127479-9b7564be-f04d-455b-a9bc-3e1737d881c4.png)

JDBC是接口，而JDBC驱动才是接口的实现，没有驱动无法完成数据库连接！每个数据库厂商都有自己的驱动，用来连接自己公司的数据库。

当然还有第三方公司专门为某一数据库提供驱动，这样的驱动往往不是开源免费的！

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

## 模拟JDBC接口
### 接口在开发中的作用
Java中接口的作用主要有以下几个方面：

1.  定义标准：接口可以用于定义标准，规范应该如何完成某个任务或应该具有哪些属性、方法等。 
2.  隐藏实现：接口隔离了类的实现和外界的逻辑使用，使得外部无论是访问接口的常量或是接口的方法都不需要关心接口的实现。 
3.  实现多态：一个类实现多个接口，在实现接口的过程中，类便会具有接口中的所有方法。这样我们就可以在实际应用中方便的实现多态的效果。 
4.  扩展性和灵活性：通过接口可以为项目提供更好的扩展性和灵活性，接口定义了一个共同的标准，使得新的类可以很容易地加入到已有的系统中，而且不需要修改现有的代码。 

总的来说，Java中的接口可以让我们通过规范来编写更加标准和灵活的代码，使得代码易于维护和扩展，并通过多态的特性来提高代码的重用性和可读性。**<font style="color:#DF2A3F;">Java接口在使用场景中，一定是存在两个角色的，一个是接口的调用者，一个是接口的实现者，接口的出现让调用者和实现者解耦合了。</font>**

****

### 编写程序模拟JDBC接口
**<font style="color:#DF2A3F;">接口的制定者</font>**：SUN公司负责制定的

```java
// SUN公司负责制定JDBC接口
public interface JDBC {
    // 负责连接数据库的方法
    void getConnection();
}
```

**<font style="color:#DF2A3F;">接口的实现者</font>**：各大数据库厂商分别对JDBC接口进行实现，实现类被称为**<font style="color:#DF2A3F;">驱动</font>**

MySQL数据库厂商对JDBC接口的实现：MySQL驱动

```java
public class MySQLDriver implements JDBC{
    public void getConnection(){
        System.out.println("与MySQL数据库连接建立成功，您正在操作MySQL数据库");
    }
}
```

Oracle数据库厂商对JDBC接口的实现：Oracle驱动

```java
public class OracleDriver implements JDBC{
    public void getConnection(){
        System.out.println("与Oracle数据库连接建立成功，您正在操作Oracle数据库");
    }
}
```

**<font style="color:#DF2A3F;">接口的调用者</font>**：要操作数据库的Java程序员（我们）

```java
public class Client{
    public static void main(String[] args){
        
        JDBC jdbc = new MySQLDriver();
        
        // 只需要面向接口编程即可，不需要关心具体的实现，不需要关心具体是哪个厂商的数据库
        jdbc.getConnection();
    }
}
```

以上是操作MySQL数据库，如果要操作Oracle数据库的话，需要new OracleDriver()：

```java
public class Client{
    public static void main(String[] args){
        
        JDBC jdbc = new OracleDriver();
        
        // 只需要面向接口编程即可，不需要关心具体的实现，不需要关心具体是哪个厂商的数据库
        jdbc.getConnection();
    }
}
```

可能你会说，最终还是修改了java代码，不符合OCP原则呀，如果你想达到OCP，那可以将创建对象的任务交给反射机制，将类名配置到文件中，例如：

配置文件如下：

```properties
driver=MySQLDriver
```

Java代码如下：

```java
import java.util.ResourceBundle;

public class Client{
    public static void main(String[] args) throws Exception{
        
        String driverClassName = ResourceBundle.getBundle("jdbc").getString("driver");
        Class c = Class.forName(driverClassName);
        JDBC jdbc = (JDBC)c.newInstance();
        
        // 只需要面向接口编程即可，不需要关心具体的实现，不需要关心具体是哪个厂商的数据库
        jdbc.getConnection();
    }
}
```

最终通过修改jdbc.properties配置文件即可做到数据库的切换。这样就完全做到了调用者和实现者的解耦合。调用者不需要关心实现者，实现者也不需要关心调用者。双方都是面向接口编程。这就是JDBC的本质：它就是一套接口。

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

## 配置CLASSPATH
经过上面内容的讲解，大家应该知道JDBC开发有三个角色的参与：

+ 我们（对数据库中数据进行增删改查的Java程序员）
+ JDBC接口的制定者
+ JDBC接口的实现者（驱动）

以上三者凑齐了我们才能进行JDBC的开发。它们三个都在哪里呢？“我们”就不用多说了，写操作数据库的代码就行了。JDBC接口在哪（接口的class文件在哪）？JDBC接口实现类在哪（驱动在哪）？

### JDBC接口在哪
JDBC接口在JDK中。对应的包是：**<font style="color:#DF2A3F;">java.sql.*;</font>**

JDBC API帮助文档就在JDK的帮助文档当中。

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1701939712048-f4487a29-3eb7-494f-b7c0-b72c6c0c03ad.png)

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1701939824373-e1c98bbf-cc6a-44c0-95b6-d2c3a0ecbf52.png)

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

### 驱动在哪
驱动是JDBC接口的实现类，这些实现类是各大数据库厂家自己实现的，所以这些实现类的就需要去数据库厂商相关的网站上下载了。通常这些实现类被全部放到一个xxx.jar包中。下面演示一下mysql的驱动如何下载【下载mysql的驱动jar包】：

打开页面：[https://dev.mysql.com/downloads/connector/j/](https://dev.mysql.com/downloads/connector/j/)

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1701940874635-9b10510f-2f00-4b7e-9b35-36425eaa9457.png)

下载后：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1701940923947-24cc167c-8fc4-4afa-92fd-9fab33ab6226.png)

解压：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1701940961500-9a610263-604c-4001-9020-98151a6bfc99.png)

上图中的“mysql-connector-j-8.2.0.jar”就是mysql数据库的驱动，8.2.0这个版本适用于目前最新版本的mysql数据库。可以使用解压工具打开这个jar包，看看里面是什么？

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1701941060668-654b02a2-956a-4765-87be-8be10997ce0a.png)

可以看到这个jar包中都是xxx.class文件，这就是JDBC接口的实现类。这个jar包就是连接mysql数据库的驱动。如果是oracle的驱动就需要去oracle的官网下载了。这里不再赘述。

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

### 如果使用文本编辑器开发
如果使用文本编辑器开发，不使用集成开发环境的话，以上的jar包就需要手动配置到环境变量CLASSPATH当中，配置如下：

如果jar包放在这里：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1701941355365-9101c03a-7016-463c-8860-f6cc41745553.png)

就需要这样配置环境变量CLASSPATH：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1701941302115-b531f7d3-3a17-487e-a3fe-7168e4022d40.png)

注意配置路径中的当前路径“.”是不能省略的。

### 如果使用IDEA工具开发
如果是采用集成开发工具，例如IDEA，就不需要手动配置CLASSPATH了，只需要将jar包放到IDEA中（实际上放到IDEA工具中的过程就是等同于在配置CLASSPATH）

+ 第一步：创建lib目录，将jar包拷贝到lib目录（不是必须叫做 lib 目录，也可以是其他目录。）
+ 第二步：在 jar 包上右键，Add as Lib...

## JDBC编程六步
JDBC编程的步骤是很固定的，通常包含以下六步：

+ 第一步：注册驱动
    - 作用一：将 JDBC 驱动程序从硬盘上的文件系统中加载到内存中。
    - 作用二：使得 DriverManager 可以通过一个统一的接口来管理该驱动程序的所有连接操作。
+ 第二步：获取数据库连接
    - 获取java.sql.Connection对象，该对象的创建标志着mysql进程和jvm进程之间的通道打开了。
+ 第三步：获取数据库操作对象
    - 获取java.sql.Statement对象，该对象负责将SQL语句发送给数据库，数据库负责执行该SQL语句。
+ 第四步：执行SQL语句
    - 执行具体的SQL语句，例如：insert delete update select等。
+ 第五步：处理查询结果集
    - 如果之前的操作是DQL查询语句，才会有处理查询结果集这一步。
    - 执行DQL语句通常会返回查询结果集对象：java.sql.ResultSet。
    - 对于ResultSet查询结果集来说，通常的操作是针对查询结果集进行结果集的遍历。
+ 第六步：释放资源
    - 释放资源可以避免资源的浪费。在 JDBC 编程中，每次使用完 Connection、Statement、ResultSet 等资源后，都需要显式地调用对应的 close() 方法来释放资源，避免资源的浪费。
    - 释放资源可以避免出现内存泄露问题。在 Java 中，当一个对象不再被引用时，会被 JVM 的垃圾回收机制进行回收。但是在 JDBC 编程中，如果不显式地释放资源，那么这些资源就不会被 JVM 的垃圾回收机制自动回收，从而导致内存泄露问题。

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

## 数据的准备
使用PowerDesigner设计用户表t_user。

使用Navicat for MySQL创建数据库，创建表，插入数据。

### PowerDesigner与Navicat for MySQL的区别
Navicat for MySQL 是一款常用的 MySQL 数据库管理工具，提供了丰富的数据库管理和开发工具，可以方便地进行数据库的连接、查询、管理、模型设计等操作，是 MySQL 开发和管理的效率工具。

而 PowerDesigner 工具则是一款专业的建模工具，它支持多种数据库和操作系统，可以完成数据库设计、数据建模、过程建模、企业业务建模等工作。PowerDesigner 可以帮助开发人员在数据库设计和开发过程中更好地理解和管理数据，便于协同开发和项目管理。各种数据库技术的建模形式都可以实现，有单个数据库建模到多个数据库建模和业务建模等高级功能，**<font style="color:#DF2A3F;">非常适用于大型项目中的数据库设计和建模</font>**。同时，PowerDesigner 还支持 UML，Java 等编程语言的建模，可以与开发语言无缝整合。

因此，Navicat for MySQL 和 PowerDesigner 的功能是不同的，可以根据实际需要来选用。如果只是针对 MySQL 的数据库连接、查询、管理等操作，可以使用 Navicat for MySQL 工具，而如果需要进行更复杂的数据库设计、建模和整合等工作，可以使用 PowerDesigner 工具来实现。**<font style="color:#DF2A3F;">如果使用 MySQL 数据库进行开发，使用 Navicat for MySQL 和 PowerDesigner 这两个工具相互配合，可以提高开发效率和数据管理质量</font>**。

### PowerDesigner工具的安装
双击安装包：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702030113007-3188761c-a3d6-43af-a7b2-b57285c5c59a.png)

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702029876181-f1cae0c3-56a7-4925-add3-c2cac74f64bf.png)

欢迎页：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702029889827-2e2c12d2-0ef0-400a-8a97-a4e094846227.png)

选择试用15天：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702029931270-dd2984c0-7154-4681-aeb7-daff6743770b.png)

选择香港，以及接受：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702029963307-ce94dc0e-631e-4fdd-bfab-cee55e430f2c.png)

设置安装位置：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702029981376-3f82d441-4b51-4ca0-9183-cb7b8853369b.png)

选择你要安装的（默认就行）：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702029994216-fa2e7123-ebb3-4e24-8a54-f70136665809.png)

选择要安装的用户配置文件（默认即可）：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702030015551-fb222d28-373c-4620-8cb7-119a796c73b6.png)

添加图标：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702030025893-0f3ccf82-2edf-4693-b40d-cdbd9b067808.png)

安装概览信息：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702030036757-b9429e96-81b1-4dcd-93d5-9eb30d61f24e.png)

安装中：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702030046163-e5983393-f38e-4c56-93cb-8e0da0a5cb0a.png)

安装完成：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702030092155-4ca5bf85-47ed-4398-98a5-864761106ce3.png)

如何破解？看到这个文件了吗？

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702030298080-4c0ab7e6-b191-4778-95ae-bd7a23bf4276.png)

把这个文件拷贝到这个安装目录当中：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702030371606-59034062-2a4d-46c5-80f2-9704563052b7.png)

会自动提醒你替换：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702030421073-75504dc7-d035-488c-ba8d-7442f32f00d9.png)

替换即可完成破解！！！！

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

### 使用PowerDesigner进行物理数据建模
打开PowerDesigner：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702352345350-1c1441c3-560f-4485-ba11-aff5522c7d42.png)

点击“Create Model...”来创建PDM（Physical Data Model，物理数据模型）：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702352495755-cdb4ac5b-cdf4-408f-b87c-6f08208eadb8.png)

**<font style="color:#DF2A3F;">什么是物理数据模型PDM？</font>**

`物理数据模型（Physical Data Model，PDM）是数据管理领域中表示数据库逻辑设计后，通过物理设计最终转化为实际数据结构的过程，即在逻辑模型的基础上，进行数据存储结构的设计。PDM 是一个详细的数据库设计计划，它描述了如何在关系数据库中存储数据。物理数据模型包含了所有数据表，列、键和索引以及物理存储的详细信息，包括数据类型、字段宽度、默认值、统计信息等。此外，PDM 还描述了如何将数据表存储在文件或表空间中，这些信息可以帮助开发人员建立实际的数据库系统。通常，PDM 包含了完整的 ER 模型，数据表和关系的详细信息，包括数据的主键、外键、唯一键、索引、约束条件等。物理数据模型可以使用各种建模工具来手工创建或自动生成。在数据库设计阶段，生成 PDM 是非常重要的一步，是将逻辑设计转换为实际实现的重要步骤之一。它可以帮助开发人员在实现时更加清晰地了解数据的存储结构，同时也方便后续的数据库管理和维护工作。`

创建完成后是这样的：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702352840475-faf7c39e-6a3e-4d72-872b-1de849baf668.png)

注意：右侧的小格子是可以放大和缩小的。看着像是很大的一张网。在每个格子当中可以容纳多个表。并且在这张网上可以清晰的看到表与表的关系。（一对多，一对一，多对多等。）

记得保存，ctrl+s保存时会生成一个xxx.pdm文件，以后如果要修改设计，双击这个xxx.pdm文件即可打开，进行编辑：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702353117948-32a0da6b-393c-4282-a2b0-d2e893d7d04b.png)

保存后的文件：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702353151163-22027c70-a1cc-463a-835e-30b23631ddf6.png)

开始进行表的设计，这里不搞那么复杂，先创建一张表即可：t_user，用户表：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702353507900-d3538143-07a6-4a08-b69e-4d7c23f1d6e3.png)

双击后，弹出设计窗口：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702353664176-dbbccc05-2711-4e31-b6fc-4cf6238bacea.png)

设计表名：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702354144428-887e8efb-c136-42e4-90de-4ec26815ab6f.png)

注意：

1. Name：用来设置显示的表名
2. Code：用来设置数据库中真实创建的表名
3. Comment：对表的注释说明

设计字段：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702356255883-27bed5c1-8cb5-41ed-ac06-d2a479327a93.png)

把每个字段设计好，包括：字段名，数据类型，长度，约束等。

设计完成后：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702356365447-df18d670-da99-40f0-b80f-95918bdf20f6.png)

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

### 使用PowerDesigner导出建表语句
![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702356449130-0ab2e139-0029-4db4-a89d-c4d46ca800e4.png)

```sql
drop table if exists t_user;

/*==============================================================*/
/* Table: t_user                                                */
/*==============================================================*/
create table t_user
(
   id                   bigint not null comment '用户的唯一标识',
   name                 varchar(255) not null,
   password             varchar(255) not null,
   realname             varchar(255),
   gender               char(2),
   tel                  char(11),
   primary key (id)
);

alter table t_user comment '用户表存储用户信息。';

```

### 使用Navicat for MySQL初始化数据
#### 建库
使用Navicat for MySQL创建一个MySQL数据库，起名：jdbc

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702356898211-79878d20-d32a-4764-b2d9-fa7de3c24053.png)

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702356942314-e5cb2d8a-3e9c-46b4-91b6-6ab59e7fbb0a.png)

#### 建表
执行jdbc.sql脚本：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702357035951-94877536-4153-4399-a6ae-9672bf97e062.png)

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702357083312-51eff97d-6686-4559-b15b-5069e5ed60ba.png)

最终创建的表：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702357196196-5a9db89b-b896-4bf0-88bb-c4d5aabd411b.png)

#### 插入数据
![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702357446508-4d4cdf35-d996-4fa2-b823-afe81b1e9c50.png)

注意：这里我将主键设置为了自增：auto_increment。其实这个也可以在PowerDesigner中设计时指定自增：勾选上它即可。

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702357560943-84503c36-4205-42bc-b488-6cca2f4dd16c.png)

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

## JDBC完成新增操作
新增操作就是让数据库执行insert语句。通过这个操作来学习一下JDBC编程的每一步。<font style="color:#DF2A3F;">刚开始编写JDBC代码的时候，建议使用文本编辑器，先不借助任何IDE。</font>

### JDBC编程第一步：注册驱动
注册驱动有两个作用：

1. 将 JDBC 驱动程序从硬盘上的文件系统中加载到内存。
2. 让 DriverManager 可以通过一个统一的接口来管理该驱动程序的所有连接操作。

API帮助文档：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702375429683-7a25727f-4615-45f1-a56c-fd02eea60dd2.png)

代码如下：

```java
import java.sql.Driver;
import java.sql.DriverManager;
import java.sql.SQLException;

public class JDBCTest01 {
    public static void main(String[] args){
        try {
            // 1. 注册驱动
            Driver driver = new com.mysql.cj.jdbc.Driver(); // 创建MySQL驱动对象
            DriverManager.registerDriver(driver); // 完成驱动注册
        } catch(SQLException e){
            e.printStackTrace();
        }
    }
}
```

**<font style="color:#DF2A3F;">注意：注册驱动调用的是java.sql.DriverManager的registerDriver()方法。这些方法的使用要参阅JDK的API帮助文档。</font>**

**<font style="color:#DF2A3F;">思考1：为什么以上代码中new的时候，后面类名要带上包名呢？</font>**

**<font style="color:#DF2A3F;">思考2：以上代码中哪些是JDBC接口，哪些是JDBC接口的实现？</font>**

### JDBC编程第二步：获取连接
获取java.sql.Connection对象，该对象的创建标志着mysql进程和jvm进程之间的通道打开了。

#### 代码实现
API帮助文档：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702375535525-fad3b7e2-b7f5-4079-a2e1-31c597ae8165.png)

代码如下：

```java
import java.sql.Driver;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Connection;

public class JDBCTest01 {
    public static void main(String[] args){
        try {
            // 1. 注册驱动
            Driver driver = new com.mysql.cj.jdbc.Driver(); // 创建MySQL驱动对象
            DriverManager.registerDriver(driver); // 完成驱动注册

            // 2. 获取连接
            String url = "jdbc:mysql://localhost:3306/jdbc";
            String user = "root";
            String password = "123456";
            Connection conn = DriverManager.getConnection(url, user, password);

            System.out.println("连接对象：" + conn);
        } catch(SQLException e){
            e.printStackTrace();
        }
    }
}
```

执行结果如下：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702372789612-ac3b38a8-6f6d-44f2-8024-ccab0bac9380.png)

看到以上的输出结果，表示数据库已经连接成功了。

通过以上程序的输出结果得知：com.mysql.cj.jdbc.ConnectionImpl是java.sql.Connection接口的实现类，大家可以想象一下，如果换成Oracle数据库的话，这个实现类的类名是不是就会换一个呢？答案是肯定的。不过对于我们来说是不需要关心具体实现类的，因为后续的代码都是直接面向java.sql.Connection接口来调用方法的。面向接口编程在这里体现的淋漓尽致。确实降低了耦合度。

以上程序中演示了连接数据库需要提供三个信息：url，用户名，密码。其中用户名和密码容易理解。url是什么？

#### 什么是URL
URL 是统一资源定位符 (Uniform Resource Locator) 的缩写，是互联网上标识、定位、访问资源的字符串。它可以用来指定互联网上各种类型的资源的位置，如网页、图片、视频等。

URL 通常由协议、服务器名、服务器端口、路径和查询字符串组成。其中：

+ 协议是规定了访问资源所采用的通信协议，例如 HTTP、HTTPS、FTP 等；
+ 服务器名是资源所在的服务器主机名或 IP 地址，可以是域名或 IP 地址；
+ 服务器端口是资源所在的服务器的端口号；
+ 路径是资源所在的服务器上的路径、文件名等信息；
+ 查询字符串是向服务器提交的参数信息，用来定位更具体的资源。

URL 在互联网中广泛应用，比如在浏览器中输入 URL 来访问网页或下载文件，在网站开发中使用 URL 来访问 API 接口或文件，在移动应用和桌面应用中使用 URL 来访问应用内部的页面或功能，在搜索引擎中使用 URL 来爬取网页内容等等。

总之，URL 是互联网上所有资源的唯一识别标识，是互联网通信的基础和核心技术之一。

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

#### JDBC连接MySQL时的URL格式
JDBC URL 是在使用 JDBC 连接数据库时的一个 URL 字符串，它用来标识要连接的数据库的位置、认证信息和其他配置参数等。JDBC URL 的格式可以因数据库类型而异，但通常包括以下几个部分：

+ 协议：表示要使用的数据库管理系统（DBMS）的类型，如 `jdbc:mysql` 表示要使用 MySQL 数据库，`jdbc:postgresql` 表示要使用 PostgreSQL 数据库。
+ 主机地址和端口号：表示要连接的数据库所在的服务器的 IP 地址或域名，以及数据库所在服务器监听的端口号。
+ 数据库名称：表示要连接的数据库的名称。
+ 其他可选参数：这些参数包括连接的超时时间、使用的字符集、连接池相关配置等。

例如，连接 MySQL 数据库的 JDBC URL 的格式一般如下：

```plain
jdbc:mysql://<host>:<port>/<database_name>?<connection_parameters>
```

其中：

+ `<host>` 是 MySQL 数据库服务器的主机名或 IP 地址；
+ `<port>` 是 MySQL 服务器的端口号（默认为 3306）；
+ `<database_name>` 是要连接的数据库名称；
+ `<connection_parameters>` 包括连接的额外参数，例如用户名、密码、字符集等。

JDBC URL 是连接数据库的关键，通过 JDBC URL，应用程序可以通过特定的 JDBC 驱动程序与数据库服务器进行通信，从而实现与数据库的交互。在开发 Web 应用和桌面应用时，使用 JDBC URL 可以轻松地连接和操作各种类型的数据库，例如 MySQL、PostgreSQL、Oracle 等。

以下是一个常见的JDBC MySQL URL：

```plain
jdbc:mysql://localhost:3306/jdbc
```

`jdbc:mysql://`是协议

`localhost`表示连接本地主机的MySQL数据库，也可以写作`127.0.0.1`

`3306`是MySQL数据库的端口号

`jdbc`是数据库实例名

#### MySQL URL中的其它常用配置
在 JDBC MySQL URL 中，常用的配置参数有：

+ `serverTimezone`<font style="color:#DF2A3F;">（默认值时：随客户端程序走）：告诉 MySQL 客户端程序服务器采用的是哪个时区</font>

MySQL 服务器默认的时区是根据系统自动获取的。如果不告诉 Java 程序 MySQL 服务器采用哪一个时区的话，它会默认认为服务器是采用和自己客户端一致的时区。如果 MySQL 服务器在美国加州（那 MySQL 服务器使用的是美国加州的时区），但 MySQL 客户端在中国北京（那 MySQL 客户端会认为 MySQL 服务器采用的是北京的时区）。这样就会导致时区不一致引起日期错乱的问题。可以使用 `serverTimezone`参数来告诉 MySQL 客户端服务器使用的是哪个时区。以保证客户端和服务器的时区一致。

如果把时区设置为 `America/Los_Angeles`（即加州的时区）：

```plain
jdbc:mysql://localhost:3306/mydatabase?user=myusername&password=mypassword&serverTimezone=America/Los_Angeles
```

+ `useSSL`<font style="color:#DF2A3F;">：是否使用 SSL 进行连接，默认为 true；</font>

`useSSL` 参数用于配置是否使用 SSL（Secure Sockets Layer）安全传输协议来加密 JDBC 和 MySQL 数据库服务器之间的通信。其设置为 `true` 表示使用 SSL 连接，设置为 `false` 表示不使用 SSL 连接。其区别如下：

当设置为 `true` 时，JDBC 驱动程序将使用 SSL 加密协议来保障客户端和服务器之间的通信安全。这种方式下，所有数据都会使用 SSL 加密后再传输，可以有效防止数据在传输过程中被窃听、篡改等安全问题出现。当然，也要求服务器端必须支持 SSL，否则会连接失败。

当设置为 `false` 时，JDBC 驱动程序会以明文方式传输数据，这种方式下，虽然数据传输的速度会更快，但也会存在被恶意攻击者截获和窃听数据的风险。因此，在不安全的网络环境下，或是要求数据传输安全性较高的情况下，建议使用 SSL 加密连接。

需要注意的是，使用 SSL 连接会对系统资源和性能消耗有一定的影响，特别是当连接数较多时，对 CPU 和内存压力都比较大。因此，在性能和安全之间需要权衡，根据实际应用场景合理设置 `useSSL` 参数。

+ <font style="color:#DF2A3F;">useUnicode：默认是 true，用来设置是否开启 Unicode 编码传输。</font>
+ `characterEncoding`<font style="color:#DF2A3F;">：指定具体的编码，默认为 UTF-8</font>

**UTF-8 是 Unicode 编码的一种具体实现，以上两个配置必须配合使用才生效。【useUnicode=true&characterEncoding=UTF-8，这样配置才会生效。】**

例如，连接 MySQL 数据库的 JDBC URL 可以如下所示：

```plain
jdbc:mysql://localhost:3306/jdbc?useUnicode=true&serverTimezone=Asia/Shanghai&useSSL=true&characterEncoding=utf-8
```

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

### JDBC编程第三步：获取数据库操作对象
数据库操作对象是这个接口：java.sql.Statement。这个对象负责将SQL语句发送给数据库服务器，服务器接收到SQL后进行编译，然后执行SQL。

API帮助文档如下：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702441460073-15a0cb32-b979-442c-900b-ec3109722750.png)

获取数据库操作对象代码如下：

```java
import java.sql.Driver;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Connection;
import java.sql.Statement;

public class JDBCTest01 {
    public static void main(String[] args){
        try {
            // 1. 注册驱动
            Driver driver = new com.mysql.cj.jdbc.Driver(); // 创建MySQL驱动对象
            DriverManager.registerDriver(driver); // 完成驱动注册

            // 2. 获取连接
            String url = "jdbc:mysql://localhost:3306/jdbc?useUnicode=true&serverTimezone=Asia/Shanghai&useSSL=true&characterEncoding=utf-8";
            String user = "root";
            String password = "123456";
            Connection conn = DriverManager.getConnection(url, user, password);

            // 3. 获取数据库操作对象
            Statement stmt = conn.createStatement();
            System.out.println("数据库操作对象stmt = " + stmt);
        } catch(SQLException e){
            e.printStackTrace();
        }
    }
}
```

执行结果如下：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702440942574-861f279e-3244-4834-98a3-491d913949f6.png)

同样可以看到：java.sql.Statement接口在MySQL驱动中的实现类是：com.mysql.cj.jdbc.StatementImpl。不过我们同样是不需要关心这个具体的实现类。因为后续的代码仍然是面向Statement接口写代码的。

另外，要知道的是通过一个Connection对象是可以创建多个Statement对象的：

```java
import java.sql.Driver;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Connection;
import java.sql.Statement;

public class JDBCTest01 {
    public static void main(String[] args){
        try {
            // 1. 注册驱动
            Driver driver = new com.mysql.cj.jdbc.Driver(); // 创建MySQL驱动对象
            DriverManager.registerDriver(driver); // 完成驱动注册

            // 2. 获取连接
            String url = "jdbc:mysql://localhost:3306/jdbc?useUnicode=true&serverTimezone=Asia/Shanghai&useSSL=true&characterEncoding=utf-8";
            String user = "root";
            String password = "123456";
            Connection conn = DriverManager.getConnection(url, user, password);

            // 3. 获取数据库操作对象
            Statement stmt = conn.createStatement();
            System.out.println("数据库操作对象stmt = " + stmt);

            Statement stmt2 = conn.createStatement();
            System.out.println("数据库操作对象stmt2 = " + stmt2);
            
        } catch(SQLException e){
            e.printStackTrace();
        }
    }
}
```

执行结果：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702441181097-76775506-0d8a-4c6b-a077-4feaf637c82a.png)

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

### JDBC编程第四步：执行SQL
当获取到Statement对象后，调用这个接口中的相关方法即可执行SQL语句。

API帮助文档如下：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702441577751-223506b2-73c9-47ee-a614-4b95fe555df3.png)

**<font style="color:#DF2A3F;">该方法的参数是一个SQL语句，只要将insert语句传递过来即可。当执行executeUpdate(sql)方法时，JDBC会将sql语句发送给数据库服务器，数据库服务器对SQL语句进行编译，然后执行SQL。</font>**

**<font style="color:#DF2A3F;">该方法的返回值是int类型，返回值的含义是：影响了数据库表当中几条记录。例如：返回1表示1条数据插入成功，返回2表示2条数据插入成功，以此类推。如果一条也没有插入，则返回0。</font>**

**<font style="color:#DF2A3F;">该方法适合执行的SQL语句是DML，包括：insert delete update。</font>**

代码实现如下：

```java
import java.sql.Driver;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Connection;
import java.sql.Statement;

public class JDBCTest01 {
    public static void main(String[] args){
        try {
            // 1. 注册驱动
            Driver driver = new com.mysql.cj.jdbc.Driver(); // 创建MySQL驱动对象
            DriverManager.registerDriver(driver); // 完成驱动注册

            // 2. 获取连接
            String url = "jdbc:mysql://localhost:3306/jdbc?useUnicode=true&serverTimezone=Asia/Shanghai&useSSL=true&characterEncoding=utf-8";
            String user = "root";
            String password = "123456";
            Connection conn = DriverManager.getConnection(url, user, password);

            // 3. 获取数据库操作对象
            Statement stmt = conn.createStatement();

            // 4. 执行SQL语句
            String sql = "insert into t_user(name,password,realname,gender,tel) values('tangsanzang','123','唐三藏','男','12566568956')"; // sql语句最后的分号';'可以不写。
            int count = stmt.executeUpdate(sql);
            System.out.println("插入了" + count + "条记录");
            
        } catch(SQLException e){
            e.printStackTrace();
        }
    }
}
```

执行结果如下：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702441948716-d8c4638f-5d7a-4d26-b3d0-a2ed4872e6a4.png)

数据库表变化了：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702441971625-ba842802-4881-48ab-a4f3-17acc229d9c2.png)

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

### JDBC编程第六步：释放资源
第五步去哪里了？第五步是处理查询结果集，以上操作不是select语句，所以第五步直接跳过，直接先看一下第六步释放资源。【后面学习查询语句的时候，再详细看第五步】

#### 为什么要释放资源
在 JDBC 编程中，建立数据库连接、创建 Statement 对象等操作都需要申请系统资源，例如打开网络端口、申请内存等。为了避免占用过多的系统资源和避免出现内存泄漏等问题，我们需要在使用完资源后及时释放它们。

#### 释放资源的原则
原则1：在finally语句块中释放

+ 建议在finally语句块中释放，因为程序执行过程中如果出现了异常，finally语句块中的代码是一定会执行的。也就是说：我们需要保证程序在执行过程中，不管是否出现了异常，最后的关闭是一定要执行的。当然了，也可以使用Java7的新特性：Try-with-resources。Try-with-resources 是 Java 7 引入的新特性。它简化了资源管理的代码实现，可以自动释放资源，减少了代码出错的可能性，同时也可以提供更好的代码可读性和可维护性。

原则2：释放有顺序

+ 从小到大依次释放，创建的时候，先创建Connection，再创建Statement。那么关闭的时候，先关闭Statement，再关闭Connection。

原则3：分别进行try...catch...

+ 关闭的时候调用close()方法，该方法有异常需要处理，建议分别对齐try...catch...进行异常捕获。如果只编写一个try...catch...进行一块捕获，在关闭过程中，如果某个关闭失败，会影响下一个资源的关闭。

#### 代码如何实现

```java
import java.sql.Driver;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Connection;
import java.sql.Statement;

public class JDBCTest01 {
    public static void main(String[] args){
        Connection conn = null;
        Statement stmt = null;
        try {
            // 1. 注册驱动
            Driver driver = new com.mysql.cj.jdbc.Driver(); // 创建MySQL驱动对象
            DriverManager.registerDriver(driver); // 完成驱动注册

            // 2. 获取连接
            String url = "jdbc:mysql://localhost:3306/jdbc?useUnicode=true&serverTimezone=Asia/Shanghai&useSSL=true&characterEncoding=utf-8";
            String user = "root";
            String password = "123456";
            conn = DriverManager.getConnection(url, user, password);

            // 3. 获取数据库操作对象
            stmt = conn.createStatement();

            // 4. 执行SQL语句
            String sql = "insert into t_user(name,password,realname,gender,tel) values('tangsanzang','123','唐三藏','男','12566568956')"; // sql语句最后的分号';'可以不写。
            int count = stmt.executeUpdate(sql);
            System.out.println("插入了" + count + "条记录");
            
        } catch(SQLException e){
            e.printStackTrace();
        } finally {
            // 6. 释放资源
            if(stmt != null){
                try{
                    stmt.close();
                }catch(SQLException e){
                    e.printStackTrace();
                }
            }
            if(conn != null){
                try{
                    conn.close();
                }catch(SQLException e){
                    e.printStackTrace();
                }
            }
        }
    }
}
```

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

## 注册驱动的常用方式
上面在注册驱动的时候，执行了这样的代码：

```java
java.sql.Driver driver = new com.mysql.cj.jdbc.Driver();
java.sql.DriverManager.registerDriver(driver);
```

这种方式是自己new驱动对象，然后调用DriverManager的registerDriver()方法来完成驱动注册，还有另一种方式，并且这种方式是常用的：

```java
Class.forName("com.mysql.cj.jdbc.Driver");
```

为什么这种方式常用？

+ 第一：代码少了很多。
+ 第二：这种方式可以很方便的将`com.mysql.cj.jdbc.Driver`类名配置到属性文件当中。

实现原理是什么？找一下`com.mysql.cj.jdbc.Driver`的源码：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702447203245-d68ebbe5-7d00-486c-be09-77ffa75c3407.png)

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702447277996-c1526d49-f502-4925-8042-0d4edff0370d.png)

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702447333885-23189b4e-5767-4dba-ae21-bdc543241db6.png)

通过源码不难发现，在`com.mysql.cj.jdbc.Driver`类中有一个静态代码块，在这个静态代码块中调用了`java.sql.DriverManager.registerDriver(new Driver());`完成了驱动的注册。而`Class.forName("com.mysql.cj.jdbc.Driver");`代码的作用就是让`com.mysql.cj.jdbc.Driver`类完成加载，执行它的静态代码块。

编写代码测试一下：

```java
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Connection;
import java.sql.Statement;

public class JDBCTest02 {
    public static void main(String[] args){
        Connection conn = null;
        Statement stmt = null;
        try {
            // 1. 注册驱动
            Class.forName("com.mysql.cj.jdbc.Driver");

            // 2. 获取连接
            String url = "jdbc:mysql://localhost:3306/jdbc?useUnicode=true&serverTimezone=Asia/Shanghai&useSSL=true&characterEncoding=utf-8";
            String user = "root";
            String password = "123456";
            conn = DriverManager.getConnection(url, user, password);

            // 3. 获取数据库操作对象
            stmt = conn.createStatement();

            // 4. 执行SQL语句
            String sql = "insert into t_user(name,password,realname,gender,tel) values('tangsanzang','123','唐三藏','男','12566568956')"; // sql语句最后的分号';'可以不写。
            int count = stmt.executeUpdate(sql);
            System.out.println("插入了" + count + "条记录");
            
        } catch(SQLException | ClassNotFoundException e){
            e.printStackTrace();
        } finally {
            // 6. 释放资源
            if(stmt != null){
                try{
                    stmt.close();
                }catch(SQLException e){
                    e.printStackTrace();
                }
            }
            if(conn != null){
                try{
                    conn.close();
                }catch(SQLException e){
                    e.printStackTrace();
                }
            }
        }
    }
}
```

执行结果：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702448305879-6a1fe86a-6da8-4127-8e6d-5dafeeffa94f.png)

数据库表中数据也新增了：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702448335558-06ceaaf7-6b10-4fca-a9c1-0d9f81281f48.png)

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

## JDBC 4.0后不用手动注册驱动（了解）
从JDBC 4.0（**<font style="color:#DF2A3F;">也就是Java6</font>**）版本开始，驱动的注册不需要再手动完成，由系统自动完成。

```java
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Connection;
import java.sql.Statement;

public class JDBCTest03 {
    public static void main(String[] args){
        Connection conn = null;
        Statement stmt = null;
        try {
            // 2. 获取连接
            String url = "jdbc:mysql://localhost:3306/jdbc?useUnicode=true&serverTimezone=Asia/Shanghai&useSSL=true&characterEncoding=utf-8";
            String user = "root";
            String password = "123456";
            conn = DriverManager.getConnection(url, user, password);

            // 3. 获取数据库操作对象
            stmt = conn.createStatement();

            // 4. 执行SQL语句
            String sql = "insert into t_user(name,password,realname,gender,tel) values('tangsanzang','123','唐三藏','男','12566568956')"; // sql语句最后的分号';'可以不写。
            int count = stmt.executeUpdate(sql);
            System.out.println("插入了" + count + "条记录");
            
        } catch(SQLException e){
            e.printStackTrace();
        } finally {
            // 6. 释放资源
            if(stmt != null){
                try{
                    stmt.close();
                }catch(SQLException e){
                    e.printStackTrace();
                }
            }
            if(conn != null){
                try{
                    conn.close();
                }catch(SQLException e){
                    e.printStackTrace();
                }
            }
        }
    }
}
```

执行结果：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702448395728-8b99a1d5-eb2d-4541-b140-dbaf03d12e4c.png)

数据库表中数据也添加了一条：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702448423567-a2526811-994b-496a-bd61-7ba47dfda8cb.png)

**<font style="color:#DF2A3F;">注意：虽然大部分情况下不需要进行手动注册驱动了，但在实际的开发中有些数据库驱动程序不支持自动发现功能，仍然需要手动注册。所以建议大家还是别省略了。</font>**

****

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

## 动态配置连接数据库的信息
为了程序的通用性，为了切换数据库的时候不需要修改Java程序，为了符合OCP开闭原则，建议将连接数据库的信息配置到属性文件中，例如：

```properties
driver=com.mysql.cj.jdbc.Driver
url=jdbc:mysql://localhost:3306/jdbc?useUnicode=true&serverTimezone=Asia/Shanghai&useSSL=true&characterEncoding=utf-8
user=root
password=123456
```

然后使用IO流读取属性文件，动态获取连接数据库的信息：

```java
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Connection;
import java.sql.Statement;
import java.util.ResourceBundle;

public class JDBCTest04 {
    public static void main(String[] args){
        
    	// 通过以下代码获取属性文件中的配置信息
		ResourceBundle bundle = ResourceBundle.getBundle("jdbc");
		String driver = bundle.getString("driver");
		String url = bundle.getString("url");
		String user = bundle.getString("user");
		String password = bundle.getString("password");

        Connection conn = null;
        Statement stmt = null;
        try {
            // 1. 注册驱动
            Class.forName(driver);

            // 2. 获取连接
            conn = DriverManager.getConnection(url, user, password);

            // 3. 获取数据库操作对象
            stmt = conn.createStatement();

            // 4. 执行SQL语句
            String sql = "insert into t_user(name,password,realname,gender,tel) values('tangsanzang','123','唐三藏','男','12566568956')"; // sql语句最后的分号';'可以不写。
            int count = stmt.executeUpdate(sql);
            System.out.println("插入了" + count + "条记录");
            
        } catch(SQLException | ClassNotFoundException e){
            e.printStackTrace();
        } finally {
            // 6. 释放资源
            if(stmt != null){
                try{
                    stmt.close();
                }catch(SQLException e){
                    e.printStackTrace();
                }
            }
            if(conn != null){
                try{
                    conn.close();
                }catch(SQLException e){
                    e.printStackTrace();
                }
            }
        }
    }
}
```

执行结果如下：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702448811161-f8f9d0fc-025b-48a9-b9fa-a38d96b7b168.png)

数据库表中也会新增一条记录：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702448831135-374bee91-f770-40aa-ba3b-eb35ded23435.png)

以后要连接其他数据库，只要修改属性文件中的配置即可。

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

## 获取连接的其他方式（了解）
上面我们讲到了第一种获取连接的方式：

```java
Connection conn = DriverManager.getConnection(url, user, password);
```

除了以上的这种方式之外，还有两种方式，通过API帮助文档可以看到：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702453145756-8174de75-a789-4030-b496-8b7fd700afb6.png)

### getConnection(String url)
这种方式参数只有一个url，那用户名和密码放在哪里呢？可以放到url当中，代码如下：

```java
import java.sql.Driver;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Connection;

public class JDBCTest05 {
    public static void main(String[] args){
        try {
            // 1. 注册驱动
            Class.forName("com.mysql.cj.jdbc.Driver");

            // 2. 获取连接
            String url = "jdbc:mysql://localhost:3306/jdbc?user=root&password=123456";
            Connection conn = DriverManager.getConnection(url);

            System.out.println("连接对象：" + conn);
        } catch(SQLException|ClassNotFoundException e){
            e.printStackTrace();
        }
    }
}
```

执行结果：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702455014436-0f8654ab-8919-444f-a5b3-03b8c11736ae.png)

### getConnection(String url, Properties info)
这种方式有两个参数，一个是url，一个是Properties对象。

+ url：可以单纯提供一个url地址
+ info：可以将url的参数存放到该对象中

代码如下：

```java
import java.sql.Driver;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Connection;
import java.util.Properties;

public class JDBCTest06 {
    public static void main(String[] args){
        try {
            // 1. 注册驱动
            Class.forName("com.mysql.cj.jdbc.Driver");

            // 2. 获取连接
            String url = "jdbc:mysql://localhost:3306/jdbc";
            
            Properties info = new Properties();
            info.setProperty("user", "root");
            info.setProperty("password", "123456");
            info.setProperty("useUnicode", "true");
            info.setProperty("serverTimezone", "Asia/Shanghai");
            info.setProperty("useSSL", "true");
            info.setProperty("characterEncoding", "utf-8");
            
            Connection conn = DriverManager.getConnection(url, info);

            System.out.println("连接对象：" + conn);
        } catch(SQLException|ClassNotFoundException e){
            e.printStackTrace();
        }
    }
}
```

执行结果：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702455362524-bc4e9ffa-ca7d-433a-af73-01cf76d556a0.png)

以上这两种方式作为了解，不是重点。

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

## JDBC完成修改操作
修改操作就是执行update语句。仍然调用Statement接口的executeUpdate(sql)方法即可。

业务要求：将name是tangsanzang的真实姓名修改为唐僧。

修改前的数据：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702456282356-5938ff92-a0ea-46d6-96f1-684c3fb29364.png)

代码如下：

```java
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Connection;
import java.sql.Statement;
import java.util.ResourceBundle;

public class JDBCTest07 {
    public static void main(String[] args){
        
    	// 通过以下代码获取属性文件中的配置信息
		ResourceBundle bundle = ResourceBundle.getBundle("jdbc");
		String driver = bundle.getString("driver");
		String url = bundle.getString("url");
		String user = bundle.getString("user");
		String password = bundle.getString("password");

        Connection conn = null;
        Statement stmt = null;
        try {
            // 1. 注册驱动
            Class.forName(driver);

            // 2. 获取连接
            conn = DriverManager.getConnection(url, user, password);

            // 3. 获取数据库操作对象
            stmt = conn.createStatement();

            // 4. 执行SQL语句
            String sql = "update t_user set realname='唐僧' where name='tangsanzang'";
            int count = stmt.executeUpdate(sql);
            System.out.println("更新了" + count + "条记录");
            
        } catch(SQLException | ClassNotFoundException e){
            e.printStackTrace();
        } finally {
            // 6. 释放资源
            if(stmt != null){
                try{
                    stmt.close();
                }catch(SQLException e){
                    e.printStackTrace();
                }
            }
            if(conn != null){
                try{
                    conn.close();
                }catch(SQLException e){
                    e.printStackTrace();
                }
            }
        }
    }
}
```

执行结果：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702456438297-48fcead2-99e0-4bd8-9e65-8cc911eb529b.png)

更新后的数据：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702456454268-27e23605-5b36-4bb5-80b1-deb74ef1d5ac.png)

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

## JDBC完成删除操作
删除操作就是执行delete语句。仍然调用Statement接口的executeUpdate(sql)方法即可。

业务要求：将id是15，16，17的数据删除。

删除前的数据：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702456454268-27e23605-5b36-4bb5-80b1-deb74ef1d5ac.png)

代码如下：

```java
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Connection;
import java.sql.Statement;
import java.util.ResourceBundle;

public class JDBCTest08 {
    public static void main(String[] args){
        
    	// 通过以下代码获取属性文件中的配置信息
		ResourceBundle bundle = ResourceBundle.getBundle("jdbc");
		String driver = bundle.getString("driver");
		String url = bundle.getString("url");
		String user = bundle.getString("user");
		String password = bundle.getString("password");

        Connection conn = null;
        Statement stmt = null;
        try {
            // 1. 注册驱动
            Class.forName(driver);

            // 2. 获取连接
            conn = DriverManager.getConnection(url, user, password);

            // 3. 获取数据库操作对象
            stmt = conn.createStatement();

            // 4. 执行SQL语句
            String sql = "delete from t_user where id in(15, 16, 17)";
            int count = stmt.executeUpdate(sql);
            System.out.println("删除了" + count + "条记录");
            
        } catch(SQLException | ClassNotFoundException e){
            e.printStackTrace();
        } finally {
            // 6. 释放资源
            if(stmt != null){
                try{
                    stmt.close();
                }catch(SQLException e){
                    e.printStackTrace();
                }
            }
            if(conn != null){
                try{
                    conn.close();
                }catch(SQLException e){
                    e.printStackTrace();
                }
            }
        }
    }
}
```

执行结果如下：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702456658043-1b44cb18-1150-4768-8296-737c4181f4d4.png)

删除后的数据：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702456673845-d64ca45a-a540-4813-a223-5be1db975764.png)

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

## JDBC的查询操作
ResultSet 是 JDBC （Java 数据库连接） API 提供的接口，它用于表示 SQL 查询的结果集。ResultSet 对象中包含了查询结果的所有行，可以通过 next() 方法逐行地获取并处理每一行的数据。它最常用于执行 SELECT 语句查询出来的结果集。

ResultSet 的遍历是基于 JDBC 的流式处理机制的，即一行一行地获取结果，避免将所有结果全部取出后再进行处理导致内存溢出问题。

在使用 ResultSet 遍历查询结果时，一般会采用以下步骤：

1. 执行 SQL 查询，获取 ResultSet 对象。
2. 使用 ResultSet 的 next() 方法移动游标指向结果集的下一行，判断是否有更多的数据行。
3. 如果有更多的数据行，则使用 ResultSet 对象提供的 getXXX() 方法获取当前行的各个字段（XXX 表示不同的数据类型）。例如，getLong("id") 方法用于获取当前行的 id 列对应的 Long 类型的值。
4. 处理当前行的数据，例如将其存入 Java 对象中。
5. 重复执行步骤 2~4，直到结果集中的所有行都被遍历完毕。
6. 调用 ResultSet 的 close() 方法释放资源。

需要注意的是，在使用完 ResultSet 对象之后，需要及时关闭它，以释放数据库资源并避免潜在的内存泄漏问题。否则，如果在多个线程中打开了多个 ResultSet 对象，并且没有正确关闭它们的话，可能会导致数据库连接过多，从而影响系统的稳定性和性能。

### 通过列索引获取数据（以String类型获取）
需求：获取t_user表中所有数据，在控制台打印输出每一行的数据。

```sql
select id,name,password,realname,gender,tel from t_user;
```

要查询的数据如下图：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702536722789-fc5bbe25-598a-4619-b5b0-2dc1871da569.png)

代码如下（<font style="color:#DF2A3F;">重点关注第4步 第5步 第6步</font>）：

```java
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Connection;
import java.sql.Statement;
import java.util.ResourceBundle;
import java.sql.ResultSet;

public class JDBCTest09 {
    public static void main(String[] args){
        
    	// 通过以下代码获取属性文件中的配置信息
		ResourceBundle bundle = ResourceBundle.getBundle("jdbc");
		String driver = bundle.getString("driver");
		String url = bundle.getString("url");
		String user = bundle.getString("user");
		String password = bundle.getString("password");

        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        try {
            // 1. 注册驱动
            Class.forName(driver);

            // 2. 获取连接
            conn = DriverManager.getConnection(url, user, password);

            // 3. 获取数据库操作对象
            stmt = conn.createStatement();

            // 4. 执行SQL语句
            String sql = "select id,name,password,realname,gender,tel from t_user";
            rs = stmt.executeQuery(sql);

            // 5. 处理查询结果集（这里的处理方式就是：遍历所有数据并输出）
            while(rs.next()){
                String id = rs.getString(1);
                String name = rs.getString(2);
                String pwd = rs.getString(3);
                String realname = rs.getString(4);
                String gender = rs.getString(5);
                String tel = rs.getString(6);
                System.out.println(id + "\t" + name + "\t" + pwd + "\t" + realname + "\t" + gender + "\t" + tel);
            }
            
        } catch(SQLException | ClassNotFoundException e){
            e.printStackTrace();
        } finally {
            // 6. 释放资源
            if(rs != null){
                try{
                    rs.close();
                }catch(SQLException e){
                    e.printStackTrace();
                }
            }
            if(stmt != null){
                try{
                    stmt.close();
                }catch(SQLException e){
                    e.printStackTrace();
                }
            }
            if(conn != null){
                try{
                    conn.close();
                }catch(SQLException e){
                    e.printStackTrace();
                }
            }
        }
    }
}
```

执行结果如下：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702537178277-7ea8b4eb-1088-45cb-9493-18fe44b90287.png)

代码解读：

```java
// 4. 执行SQL语句
String sql = "select id,name,password,realname,gender,tel from t_user";
rs = stmt.executeQuery(sql);
```

执行insert delete update语句的时候，调用Statement接口的executeUpdate()方法。

执行select语句的时候，**<font style="color:#DF2A3F;">调用Statement接口的executeQuery()方法</font>**。执行select语句后返回结果集对象：ResultSet。

代码解读：

```java
// 5. 处理查询结果集（这里的处理方式就是：遍历所有数据并输出）
while(rs.next()){
    String id = rs.getString(1);
    String name = rs.getString(2);
    String pwd = rs.getString(3);
    String realname = rs.getString(4);
    String gender = rs.getString(5);
    String tel = rs.getString(6);
    System.out.println(id + "\t" + name + "\t" + pwd + "\t" + realname + "\t" + gender + "\t" + tel);
}
```

+ **<font style="color:#DF2A3F;">rs.next() 将游标移动到下一行，如果移动后指向的这一行有数据则返回true，没有数据则返回false。</font>**
+ **<font style="color:#DF2A3F;">while循环体当中的代码是处理当前游标指向的这一行的数据。（注意：是处理的一行数据）</font>**
+ **<font style="color:#DF2A3F;">rs.getString(int columnIndex) 其中 int columnIndex 是查询结果的列下标，列下标从1开始，以1递增。</font>**

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702538306701-4341b895-f91b-4501-af67-4746b6327884.png)

+ **<font style="color:#DF2A3F;">rs.getString(...) 方法在执行时，不管底层数据库中的数据类型是什么，统一以字符串String类型来获取。</font>**

代码解读：

```java
// 6. 释放资源
if(rs != null){
    try{
        rs.close();
    }catch(SQLException e){
        e.printStackTrace();
    }
}
if(stmt != null){
    try{
        stmt.close();
    }catch(SQLException e){
        e.printStackTrace();
    }
}
if(conn != null){
    try{
        conn.close();
    }catch(SQLException e){
        e.printStackTrace();
    }
}
```

ResultSet最终也是需要关闭的。**<font style="color:#DF2A3F;">先关闭ResultSet，再关闭Statement，最后关闭Connection</font>**。

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

### 通过列名获取数据（以String类型获取）
获取当前行的数据，不仅可以通过列下标获取，还可以通过查询结果的列名来获取，通常这种方式是被推荐的，因为可读性好。

例如这样的SQL：

```sql
select id, name as username, realname from t_user;
```

执行结果是：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702539677907-26c84361-6874-421b-a612-dd754f7fb8f3.png)

我们可以按照查询结果的列名来获取数据：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702540371842-53a5c738-db3b-4040-aa0a-cd6dc9b9bb22.png)

**<font style="color:#DF2A3F;">注意：是根据查询结果的列名，而不是表中的列名。以上查询的时候将字段name起别名username了，所以要根据username来获取，而不能再根据name来获取了。</font>**

```java
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Connection;
import java.sql.Statement;
import java.util.ResourceBundle;
import java.sql.ResultSet;

public class JDBCTest10 {
    public static void main(String[] args){
        
    	// 通过以下代码获取属性文件中的配置信息
		ResourceBundle bundle = ResourceBundle.getBundle("jdbc");
		String driver = bundle.getString("driver");
		String url = bundle.getString("url");
		String user = bundle.getString("user");
		String password = bundle.getString("password");

        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        try {
            // 1. 注册驱动
            Class.forName(driver);

            // 2. 获取连接
            conn = DriverManager.getConnection(url, user, password);

            // 3. 获取数据库操作对象
            stmt = conn.createStatement();

            // 4. 执行SQL语句
            String sql = "select id,name as username,realname from t_user";
            rs = stmt.executeQuery(sql);

            // 5. 处理查询结果集（这里的处理方式就是：遍历所有数据并输出）
            while(rs.next()){
                String id = rs.getString("id");
                String name = rs.getString("username");
                String realname = rs.getString("realname");
                System.out.println(id + "\t" + name + "\t" + realname);
            }
            
        } catch(SQLException | ClassNotFoundException e){
            e.printStackTrace();
        } finally {
            // 6. 释放资源
            if(rs != null){
                try{
                    rs.close();
                }catch(SQLException e){
                    e.printStackTrace();
                }
            }
            if(stmt != null){
                try{
                    stmt.close();
                }catch(SQLException e){
                    e.printStackTrace();
                }
            }
            if(conn != null){
                try{
                    conn.close();
                }catch(SQLException e){
                    e.printStackTrace();
                }
            }
        }
    }
}
```

执行结果如下：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702540580699-757667a3-887c-4468-8a0e-fe29ea6d6674.png)

如果将上面代码中`rs.getString("username")`修改为`rs.getString("name")`，执行就会出现以下错误：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702540685314-fa65fdea-6aad-4781-99fa-c007955b5b3f.png)

提示name列是不存在的。所以一定是根据查询结果中的列名来获取，而不是表中原始的列名。

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

### 以指定的类型获取数据
前面的程序可以看到，不管数据库表中是什么数据类型，都以String类型返回。当然，也能以指定类型返回。

使用PowerDesigner再设计一张商品表：t_product，使用Navicat for MySQL工具准备数据如下：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702541223024-4e5acb77-ef8b-4437-ba3d-10c02ba0999b.png)

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702541500905-f5e0a70b-19b0-4469-97db-68e414f92984.png)

id以long类型获取，name以String类型获取，price以double类型获取，create_time以java.sql.Date类型获取，代码如下：

```java
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Connection;
import java.sql.Statement;
import java.util.ResourceBundle;
import java.sql.ResultSet;

public class JDBCTest11 {
    public static void main(String[] args){
        
    	// 通过以下代码获取属性文件中的配置信息
		ResourceBundle bundle = ResourceBundle.getBundle("jdbc");
		String driver = bundle.getString("driver");
		String url = bundle.getString("url");
		String user = bundle.getString("user");
		String password = bundle.getString("password");

        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        try {
            // 1. 注册驱动
            Class.forName(driver);

            // 2. 获取连接
            conn = DriverManager.getConnection(url, user, password);

            // 3. 获取数据库操作对象
            stmt = conn.createStatement();

            // 4. 执行SQL语句
            String sql = "select id,name,price,create_time as createTime from t_product";
            rs = stmt.executeQuery(sql);

            // 5. 处理查询结果集（这里的处理方式就是：遍历所有数据并输出）
            while(rs.next()){
                long id = rs.getLong("id");
                String name = rs.getString("name");
                double price = rs.getDouble("price");
                java.sql.Date createTime = rs.getDate("createTime");
                // 以指定类型获取后是可以直接用的，例如获取到价格后，统一让价格乘以2
                System.out.println(id + "\t" + name + "\t" + price * 2 + "\t" + createTime);
            }
            
        } catch(SQLException | ClassNotFoundException e){
            e.printStackTrace();
        } finally {
            // 6. 释放资源
            if(rs != null){
                try{
                    rs.close();
                }catch(SQLException e){
                    e.printStackTrace();
                }
            }
            if(stmt != null){
                try{
                    stmt.close();
                }catch(SQLException e){
                    e.printStackTrace();
                }
            }
            if(conn != null){
                try{
                    conn.close();
                }catch(SQLException e){
                    e.printStackTrace();
                }
            }
        }
    }
}
```

执行结果如下：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702541874721-10c9a4f2-370f-4ce4-985e-6cf8da2e3ffb.png)

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

### 获取结果集的元数据信息（了解）
ResultSetMetaData 是一个接口，用于描述 ResultSet 中的元数据信息，即查询结果集的结构信息，例如查询结果集中包含了哪些列，每个列的数据类型、长度、标识符等。

ResultSetMetaData 可以通过 ResultSet 接口的 getMetaData() 方法获取，一般在对 ResultSet 进行元数据信息处理时使用。例如，可以使用 ResultSetMetaData 对象获取查询结果中列的信息，如列名、列的类型、列的长度等。通过 ResultSetMetaData 接口的方法，可以实现对查询结果的基本描述信息操作，例如获取查询结果集中有多少列、列的类型、列的标识符等。以下是一段通过 ResultSetMetaData 获取查询结果中列的信息的示例代码：

```java
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Connection;
import java.sql.Statement;
import java.util.ResourceBundle;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;

public class JDBCTest12 {
    public static void main(String[] args){
        
    	// 通过以下代码获取属性文件中的配置信息
		ResourceBundle bundle = ResourceBundle.getBundle("jdbc");
		String driver = bundle.getString("driver");
		String url = bundle.getString("url");
		String user = bundle.getString("user");
		String password = bundle.getString("password");

        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        try {
            // 1. 注册驱动
            Class.forName(driver);

            // 2. 获取连接
            conn = DriverManager.getConnection(url, user, password);

            // 3. 获取数据库操作对象
            stmt = conn.createStatement();

            // 4. 执行SQL语句
            String sql = "select id,name,price,create_time as createTime from t_product";
            rs = stmt.executeQuery(sql);

            // 获取元数据信息
            ResultSetMetaData rsmd = rs.getMetaData();
            int columnCount = rsmd.getColumnCount();
            for (int i = 1; i <= columnCount; i++) {
                System.out.println("列名：" + rsmd.getColumnName(i) + "，数据类型：" + rsmd.getColumnTypeName(i) +
                                   "，列的长度：" + rsmd.getColumnDisplaySize(i));
            }
            
        } catch(SQLException | ClassNotFoundException e){
            e.printStackTrace();
        } finally {
            // 6. 释放资源
            if(rs != null){
                try{
                    rs.close();
                }catch(SQLException e){
                    e.printStackTrace();
                }
            }
            if(stmt != null){
                try{
                    stmt.close();
                }catch(SQLException e){
                    e.printStackTrace();
                }
            }
            if(conn != null){
                try{
                    conn.close();
                }catch(SQLException e){
                    e.printStackTrace();
                }
            }
        }
    }
}
```

执行结果如下：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702542217121-d413b4dc-1bf2-45ca-80c8-551d2a3705b8.png)

在上面的代码中，我们首先创建了一个 Statement 对象，然后执行了一条 SQL 查询语句，生成了一个 ResultSet 对象。接下来，我们通过 ResultSet 对象的 getMetaData() 方法获取了 ResultSetMetaData 对象，进而获取了查询结果中列的信息并进行输出。需要注意的是，在进行列信息的获取时，列的编号从 1 开始计算。该示例代码将获取查询结果集中所有列名、数据类型以及长度等信息。

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

## 获取新增行的主键值
有很多表的主键字段值都是自增的，在某些特殊的业务环境下，当我们插入了新数据后，希望能够获取到这条新数据的主键值，应该如何获取呢？

在 JDBC 中，如果要获取插入数据后的主键值，可以使用 Statement 接口的 executeUpdate() 方法的重载版本，该方法接受一个额外的参数，用于指定是否需要获取自动生成的主键值。然后，通过以下两个步骤获取插入数据后的主键值：

1.  在执行 executeUpdate() 方法时指定一个标志位，表示需要返回插入的主键值。
2.  调用 Statement 对象的 getGeneratedKeys() 方法，返回一个包含插入的主键值的 ResultSet 对象。 

```java
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Connection;
import java.sql.Statement;
import java.util.ResourceBundle;
import java.sql.ResultSet;

public class JDBCTest13 {
    public static void main(String[] args){
        
    	// 通过以下代码获取属性文件中的配置信息
		ResourceBundle bundle = ResourceBundle.getBundle("jdbc");
		String driver = bundle.getString("driver");
		String url = bundle.getString("url");
		String user = bundle.getString("user");
		String password = bundle.getString("password");

        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        try {
            // 1. 注册驱动
            Class.forName(driver);

            // 2. 获取连接
            conn = DriverManager.getConnection(url, user, password);

            // 3. 获取数据库操作对象
            stmt = conn.createStatement();

            // 4. 执行SQL语句
            String sql = "insert into t_user(name,password,realname,gender,tel) values('zhangsan','111','张三','男','19856525352')";
            // 第一步
            int count = stmt.executeUpdate(sql, Statement.RETURN_GENERATED_KEYS);
            // 第二步
            rs = stmt.getGeneratedKeys();
            if(rs.next()){
                int id = rs.getInt(1);
                System.out.println("新增数据行的主键值：" + id);
            }
            
        } catch(SQLException | ClassNotFoundException e){
            e.printStackTrace();
        } finally {
            // 6. 释放资源
            if(rs != null){
                try{
                    rs.close();
                }catch(SQLException e){
                    e.printStackTrace();
                }
            }
            if(stmt != null){
                try{
                    stmt.close();
                }catch(SQLException e){
                    e.printStackTrace();
                }
            }
            if(conn != null){
                try{
                    conn.close();
                }catch(SQLException e){
                    e.printStackTrace();
                }
            }
        }
    }
}
```

执行结果如下：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702543846750-ba186e76-04fa-4ef1-8d57-7fc40598c02e.png)

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702543887747-8bfa21c9-e7b4-49c9-8dec-dbca00a645a7.png)

以上代码中，我们将 Statement.RETURN_GENERATED_KEYS 传递给 executeUpdate() 方法，以指定需要获取插入的主键值。然后，通过调用 Statement 对象的 getGeneratedKeys() 方法获取包含插入的主键值的 ResultSet 对象，通过 ResultSet 对象获取主键值。需要注意的是，在使用 Statement 对象的 getGeneratedKeys() 方法获取自动生成的主键值时，主键值的获取方式具有一定的差异，需要根据不同的数据库种类和版本来进行调整。

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

## 使用IDEA工具编写JDBC程序
### 创建空的工程并设置JDK
创建一个空的工程：mypro

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702892512796-0fb0ad4b-70cd-4d6b-89f1-49979a51206c.png)

工程结构：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702891589679-f9b4b346-a814-41cd-9f22-002668a1eed7.png)

设置JDK以及编译器版本：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702892572186-0d582f69-f12a-4de2-bb95-129857c2d1e4.png)

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

### 创建一个模块
![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702892712096-c8781789-2ea6-485e-8c43-9902923e7f48.png)

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702892635936-a0bd4576-c3ab-46d3-aa4f-83a5f93900c2.png)

### 将驱动加入到CLASSPATH
在模块jdbc下创建一个目录：lib

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702892792110-ddd13f59-bb68-4c4f-b3bc-83bf2bcbc49c.png)

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702892805707-188d0436-dff6-4ed8-a1d5-f7d8168a8226.png)

将mysql的驱动jar包拷贝到lib目录当中：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702892848869-f45f725d-576b-464c-94c3-0383f27cf9d2.png)

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702892860859-06a0d6a9-9877-4a59-9a31-ef5ba8d10fdd.png)

将jar包加入到classpath：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702892903594-755ad190-065b-449e-ac8c-ed8a1afa76c0.png)

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702893616221-646481b5-e342-4a65-8be3-584c4eaa858a.png)

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

### 编写JDBC程序
新建软件包：com.test.jdbc

新建JDBCTest01类：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702893035873-744a58aa-cca9-47a3-9258-f2c319695a7f.png)

在JDBCTest01类中编写main方法，main方法中编写JDBC代码：

```java
package com.test.jdbc;

import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Connection;
import java.sql.Statement;
import java.util.ResourceBundle;
import java.sql.ResultSet;

public class JDBCTest01 {
    public static void main(String[] args){

        // 通过以下代码获取属性文件中的配置信息
        ResourceBundle bundle = ResourceBundle.getBundle("com.test.jdbc.jdbc");
        String driver = bundle.getString("driver");
        String url = bundle.getString("url");
        String user = bundle.getString("user");
        String password = bundle.getString("password");

        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        try {
            // 1. 注册驱动
            Class.forName(driver);

            // 2. 获取连接
            conn = DriverManager.getConnection(url, user, password);

            // 3. 获取数据库操作对象
            stmt = conn.createStatement();

            // 4. 执行SQL语句
            String sql = "select id,name,password from t_user";
            rs = stmt.executeQuery(sql);
            while (rs.next()) {
                int id = rs.getInt("id");
                String name = rs.getString("name");
                String pwd = rs.getString("password");
                System.out.println(id + "," + name + "," + pwd);
            }

        } catch(SQLException | ClassNotFoundException e){
            e.printStackTrace();
        } finally {
            // 6. 释放资源
            if(rs != null){
                try{
                    rs.close();
                }catch(SQLException e){
                    e.printStackTrace();
                }
            }
            if(stmt != null){
                try{
                    stmt.close();
                }catch(SQLException e){
                    e.printStackTrace();
                }
            }
            if(conn != null){
                try{
                    conn.close();
                }catch(SQLException e){
                    e.printStackTrace();
                }
            }
        }
    }
}
```

提供配置文件，在com.test.jdbc包下新建jdbc.properties文件，jdbc.properties文件中如下配置：

```properties
driver=com.mysql.cj.jdbc.Driver
url=jdbc:mysql://localhost:3306/jdbc?useUnicode=true&serverTimezone=Asia/Shanghai&useSSL=true&characterEncoding=utf-8
user=root
password=123456
```

执行结果如下：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702893658315-fbe8119e-9ab0-40ba-99f1-9d5b68e8866b.png)

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

## SQL注入问题
SQL注入问题说的是：用户输入的信息中含有SQL语句关键字，和程序中的SQL语句进行字符串拼接，导致程序中的SQL语句改变了原意。（SQL注入问题是一种系统安全问题）

接下来我们来演示一下SQL注入问题。以用户登录为例。使用表：t_user

业务描述：系统启动后，给出登录页面，用户可以输入用户名和密码，用户名和密码全部正确，则登录成功，反之，则登录失败。

分析一下要执行怎样的SQL语句？是不是这样的？

```sql
select * from t_user where name = 用户输入的用户名 and password = 用户输入的密码;
```

如果以上的SQL语句能够查询到结果，说明用户名和密码是正确的，则登录成功。如果查不到，说明是错误的，则登录失败。

代码实现如下：

```java
package com.test.jdbc;

import java.sql.*;
import java.util.ResourceBundle;
import java.util.Scanner;

/**
 * 用户登录案例演示SQL注入问题
 */
public class JDBCTest02 {
    public static void main(String[] args) {
        // 输出欢迎页面
        System.out.println("欢迎使用用户管理系统，请登录！");
        // 接收用户名和密码
        Scanner scanner = new Scanner(System.in);
        System.out.print("用户名：");
        String loginName = scanner.nextLine();
        System.out.print("密码：");
        String loginPwd = scanner.nextLine();
        // 读取属性配置文件，获取连接数据库的信息。
        ResourceBundle bundle = ResourceBundle.getBundle("com.test.jdbc.jdbc");
        String driver = bundle.getString("driver");
        String url = bundle.getString("url");
        String user = bundle.getString("user");
        String password = bundle.getString("password");
        // JDBC程序验证用户名和密码是否正确
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        try {
            // 1.注册驱动
            Class.forName(driver);
            // 2.获取连接
            conn = DriverManager.getConnection(url, user, password);
            // 3.获取数据库操作对象
            stmt = conn.createStatement();
            // 4.执行SQL语句
            String sql = "select realname from t_user where name = '"+loginName+"' and password = '"+loginPwd+"'";
            rs = stmt.executeQuery(sql);
            // 5.处理查询结果集
            if (rs.next()) { // 如果可以确定结果集中最多只有一条记录的话，可以使用if语句，不一定非要用while循环。
                String realname = rs.getString("realname");
                System.out.println("登录成功，欢迎您" + realname);
            } else {
                System.out.println("登录失败，用户名不存在或者密码错误。");
            }
        } catch (ClassNotFoundException | SQLException e) {
            throw new RuntimeException(e);
        } finally {
            // 6.释放资源
            if (rs != null) {
                try {
                    rs.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (stmt != null) {
                try {
                    stmt.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (conn != null) {
                try {
                    conn.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
        }
    }
}

```

如果用户名和密码正确的话，执行结果如下：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702976483919-52a9ff26-1ded-4a07-bcc8-d2846f17a045.png)

如果用户名不存在或者密码错误的话，执行结果如下：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702976532157-a3d29aad-a0e8-44c9-9571-63cc3052fe5b.png)

接下来，见证奇迹的时刻，当我分别输入以下的用户名和密码时，系统被攻破了：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702976830213-7483fb5c-6c7c-466c-b7c4-a2feb26b12bb.png)

这种现象就叫做：SQL注入。为什么会发生以上的事儿呢？原因是：用户提供的信息中有SQL语句关键字，并且和底层的SQL字符串进行了拼接，变成了一个全新的SQL语句。

例如：本来程序想表达的是这样的SQL：

```sql
select realname from t_user where name = 'sunwukong' and password = '123';
```

结果被SQL注入之后，SQL语句就变成这样了：

```sql
select realname from t_user where name = 'aaa' and password = 'bbb' or '1'='1';
```

我们可以执行一下这条SQL，看看结果是什么？

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702977070115-c06f8f95-d42f-43e7-9b69-53eac3b155b2.png)

把所有结果全部查到了，这是因为 '1'='1' 是恒成立的，并且使用的是 or 运算符，所以 or 前面的条件等于是没有的。这样就会把所有数据全部查到。而在程序中的判断逻辑是只要结果集中有数据，则表示登录成功。所以以上的输入方式最终的结果就是登录成功。你设想一下，如果这个系统是一个高级别保密系统，只有登录成功的人才有权限，那么这个系统是不是极其危险了。

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

## 解决SQL注入问题
导致SQL注入的根本原因是什么？只有找到真正的原因，问题才能得到解决。

最根本的原因是：Statement造成的。

Statement执行原理是：先进行字符串的拼接，将拼接好的SQL语句发送给数据库服务器，数据库服务器进行SQL语句的编译，然后执行。因此用户提供的信息中如果含有SQL语句的关键字，那么这些关键字正好参加了SQL语句的编译，所以导致原SQL语句被扭曲。

因此，JDBC为了解决这个问题，引入了一个新的接口：PreparedStatement，我们称为：预编译的数据库操作对象。PreparedStatement是Statement接口的子接口。它俩是继承关系。

PreparedStatement执行原理是：先对SQL语句进行预先的编译，然后再向SQL语句指定的位置传值，也就是说：用户提供的信息中即使含有SQL语句的关键字，那么这个信息也只会被当做一个值传递给SQL语句，用户提供的信息不再参与SQL语句的编译了，这样就解决了SQL注入问题。

使用PreparedStatement解决SQL注入问题：

```java
package com.test.jdbc;

import java.sql.*;
import java.util.ResourceBundle;
import java.util.Scanner;

/**
 * PreparedStatement解决SQL注入问题
 */
public class JDBCTest03 {
    public static void main(String[] args) {
        // 输出欢迎页面
        System.out.println("欢迎使用用户管理系统，请登录！");
        // 接收用户名和密码
        Scanner scanner = new Scanner(System.in);
        System.out.print("用户名：");
        String loginName = scanner.nextLine();
        System.out.print("密码：");
        String loginPwd = scanner.nextLine();
        // 读取属性配置文件，获取连接数据库的信息。
        ResourceBundle bundle = ResourceBundle.getBundle("com.test.jdbc.jdbc");
        String driver = bundle.getString("driver");
        String url = bundle.getString("url");
        String user = bundle.getString("user");
        String password = bundle.getString("password");
        // JDBC程序验证用户名和密码是否正确
        Connection conn = null;
        PreparedStatement pstmt = null;
        ResultSet rs = null;
        try {
            // 1.注册驱动
            Class.forName(driver);
            // 2.获取连接
            conn = DriverManager.getConnection(url, user, password);
            // 3.获取数据库操作对象（获取的是预编译的数据库操作对象）
            String sql = "select realname from t_user where name=? and password=?";
            pstmt = conn.prepareStatement(sql);
            pstmt.setString(1, loginName);
            pstmt.setString(2, loginPwd);
            // 4.执行SQL语句
            rs = pstmt.executeQuery();
            // 5.处理查询结果集
            if (rs.next()) {
                String realname = rs.getString("realname");
                System.out.println("登录成功，欢迎您" + realname);
            } else {
                System.out.println("登录失败，用户名不存在或者密码错误。");
            }
        } catch (ClassNotFoundException | SQLException e) {
            throw new RuntimeException(e);
        } finally {
            // 6.释放资源
            if (rs != null) {
                try {
                    rs.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (pstmt != null) {
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (conn != null) {
                try {
                    conn.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
        }
    }
}

```

用户名和密码正确的话，执行结果如下：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702978597923-7cce7d0a-6a79-43a5-b9f3-a8ce2e4785e6.png)

用户名和密码错误的话，执行结果如下：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702978634050-b50580fc-f9ce-48ec-9200-425ea078782c.png)

尝试SQL注入，看看还能不能？

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702978663699-a5c38388-b4f5-43b6-8d00-3e56fdb77178.png)

通过测试得知，SQL注入问题已经解决了。**<font style="color:#DF2A3F;">根本原因是：bbb' or '1'='1 这个字符串中虽然含有SQL语句的关键字，但是只会被当做普通的值传到SQL语句中，并没有参与SQL语句的编译</font>**。

**<font style="color:#DF2A3F;">关于使用PreparedStatement要注意的是：</font>**

+ 带有占位符 ? 的SQL语句我们称为：预处理SQL语句。
+ 占位符 ? 不能使用单引号或双引号包裹。如果包裹，占位符则不再是占位符，是一个普通的问号字符。
+ 在执行SQL语句前，必须给每一个占位符 ? 传值。
+ 如何给占位符 ? 传值，通过以下的方法：
    - pstmt.setXxx(第几个占位符, 传什么值)
    - “第几个占位符”：从1开始。第1个占位符则是1，第2个占位符则是2，以此类推。
    - “传什么值”：具体要看调用的什么方法？
        * 如果调用pstmt.setString方法，则传的值必须是一个字符串。
        * 如果调用pstmt.setInt方法，则传的值必须是一个整数。
        * 以此类推......

**<font style="color:#DF2A3F;">PreparedStatement和Statement都是用于执行SQL语句的接口，它们的主要区别在于：</font>**

+ PreparedStatement预编译SQL语句，Statement直接提交SQL语句；
+ PreparedStatement执行速度更快，可以避免SQL注入攻击；
+ PreparedStatement会做类型检查，是类型安全的；
+ Statement适用于处理静态的SQL语句，而PreparedStatement适用于处理在运行时动态生成的SQL语句。

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

## PreparedStatement的使用
### 新增操作
需求：向 emp 表中插入这样一条记录：

empno：8888

ename：张三

job：销售员

mgr：7369

hiredate：2024-01-01

sal：1000.0

comm：500.0

deptno：10

```java
package com.test.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.time.LocalDate;
import java.util.ResourceBundle;

public class JDBCTest04 {
    public static void main(String[] args) {

        ResourceBundle bundle = ResourceBundle.getBundle("com.test.jdbc.jdbc");
        String driver = bundle.getString("driver");
        String url = bundle.getString("url");
        String user = bundle.getString("user");
        String password = bundle.getString("password");

        Connection conn = null;
        PreparedStatement pstmt = null;
        try {
            // 1. 注册驱动
            Class.forName(driver);
            // 2. 获取连接
            conn = DriverManager.getConnection(url, user, password);
            // 3. 获取预编译的数据操作对象
            String sql = "insert into emp(empno,ename,sal,comm,job,mgr,hiredate,deptno) values(?,?,?,?,?,?,?,?)";
            // 预编译SQL语句
            pstmt = conn.prepareStatement(sql);
            // 给 ? 传值
            pstmt.setInt(1, 8888);
            pstmt.setString(2, "张三");
            pstmt.setDouble(3, 10000.0);
            pstmt.setDouble(4, 500.0);
            pstmt.setString(5, "销售员");
            pstmt.setInt(6, 7369);
            LocalDate localDate = LocalDate.parse("2024-01-01");
            pstmt.setDate(7, java.sql.Date.valueOf(localDate));
            pstmt.setInt(8, 10);
            // 4. 执行SQL语句
            int count = pstmt.executeUpdate();
            if (1 == count) {
                System.out.println("成功更新" + count + "条记录");
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // 6. 释放资源
            if (pstmt != null) {
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (conn != null) {
                try {
                    conn.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
        }
    }
}
```

重点学习内容：如何给占位符 ? 传值。

执行结果如下：

![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1708238667879-fe0a662a-f9e8-4933-afd0-5290856c21fd.png)

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

### 修改操作
需求：将员工编号为8888的员工，姓名修改为李四，岗位修改为产品经理，月薪修改为5000.0，其他不变。

```java
package com.test.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.time.LocalDate;
import java.util.ResourceBundle;

public class JDBCTest05 {
    public static void main(String[] args) {
        ResourceBundle bundle = ResourceBundle.getBundle("com.test.jdbc.jdbc");
        String driver = bundle.getString("driver");
        String url = bundle.getString("url");
        String user = bundle.getString("user");
        String password = bundle.getString("password");

        Connection conn = null;
        PreparedStatement pstmt = null;
        try {
            // 1. 注册驱动
            Class.forName(driver);
            // 2. 获取连接
            conn = DriverManager.getConnection(url, user, password);
            // 3. 获取预编译的数据操作对象
            String sql = "update emp set ename = ?, job = ?, sal = ? where empno = ?";
            // 预编译SQL语句
            pstmt = conn.prepareStatement(sql);
            // 给 ? 传值
            pstmt.setString(1, "李四");
            pstmt.setString(2, "产品经理");
            pstmt.setDouble(3, 5000.0);
            pstmt.setInt(4, 8888);
            // 4. 执行SQL语句
            int count = pstmt.executeUpdate();
            if (1 == count) {
                System.out.println("成功更新" + count + "条记录");
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // 6. 释放资源
            if (pstmt != null) {
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (conn != null) {
                try {
                    conn.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
        }
    }
}
```

执行结果如下：

![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1708239544671-626c918f-fd56-4cfa-8aa2-df1976979414.png)

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

### 删除操作
需求：将员工编号为8888的删除。

```java
package com.test.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.ResourceBundle;

public class JDBCTest06 {
    public static void main(String[] args) {
        ResourceBundle bundle = ResourceBundle.getBundle("com.test.jdbc.jdbc");
        String driver = bundle.getString("driver");
        String url = bundle.getString("url");
        String user = bundle.getString("user");
        String password = bundle.getString("password");

        Connection conn = null;
        PreparedStatement pstmt = null;
        try {
            // 1. 注册驱动
            Class.forName(driver);
            // 2. 获取连接
            conn = DriverManager.getConnection(url, user, password);
            // 3. 获取预编译的数据操作对象
            String sql = "delete from emp where empno = ?";
            // 预编译SQL语句
            pstmt = conn.prepareStatement(sql);
            // 给 ? 传值
            pstmt.setInt(1, 8888);
            // 4. 执行SQL语句
            int count = pstmt.executeUpdate();
            if (1 == count) {
                System.out.println("成功更新" + count + "条记录");
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // 6. 释放资源
            if (pstmt != null) {
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (conn != null) {
                try {
                    conn.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
        }
    }
}

```

执行结果如下：

![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1708240126660-979bd865-6e83-41c7-9724-68c247209e9e.png)

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

### 模糊查询
需求：查询员工名字中第二个字母是 O 的。

```java
package com.test.jdbc;

import java.sql.*;
import java.util.ResourceBundle;

public class JDBCTest07 {
    public static void main(String[] args) {
        ResourceBundle bundle = ResourceBundle.getBundle("com.test.jdbc.jdbc");
        String driver = bundle.getString("driver");
        String url = bundle.getString("url");
        String user = bundle.getString("user");
        String password = bundle.getString("password");

        Connection conn = null;
        PreparedStatement pstmt = null;
        ResultSet rs = null;
        try {
            // 1. 注册驱动
            Class.forName(driver);
            // 2. 获取连接
            conn = DriverManager.getConnection(url, user, password);
            // 3. 获取预编译的数据操作对象
            String sql = "select ename from emp where ename like ?";
            // 预编译SQL语句
            pstmt = conn.prepareStatement(sql);
            // 给 ? 传值
            pstmt.setString(1, "_O%");
            // 4. 执行SQL语句
            rs = pstmt.executeQuery();
            // 5. 处理查询结果集
            while (rs.next()) {
                String ename = rs.getString("ename");
                System.out.println(ename);
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // 6. 释放资源
            if (rs != null) {
                try {
                    rs.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (pstmt != null) {
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (conn != null) {
                try {
                    conn.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
        }
    }
}
```

执行结果如下：

![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1708240400162-5eb57d8c-e52c-4780-9ec2-88f117377328.png)

通过这个例子主要告诉大家，程序不能这样写：

```java
String sql = "select ename from emp where ename like '_?%'";
pstmt.setString(1, "O");
```

由于占位符 ? 被单引号包裹，因此这个占位符是无效的。

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

### 分页查询
对于MySQL来说，通用的分页SQL语句：

假设每页显示3条记录：pageSize = 3

第1页：limit 0, 3

第2页：limit 3, 3

第3页：limit 6, 3

**<font style="color:#DF2A3F;">第pageNo页：limit (pageNo - 1)*pageSize, pageSize</font>**

需求：查询所有员工姓名，每页显示3条(pageSize)，显示第2页(pageNo)。

```java
package com.test.jdbc;

import java.sql.*;
import java.util.ResourceBundle;

public class JDBCTest08 {
    public static void main(String[] args) {
        ResourceBundle bundle = ResourceBundle.getBundle("com.test.jdbc.jdbc");
        String driver = bundle.getString("driver");
        String url = bundle.getString("url");
        String user = bundle.getString("user");
        String password = bundle.getString("password");

        Connection conn = null;
        PreparedStatement pstmt = null;
        ResultSet rs = null;

        // 每页显示记录条数
        int pageSize = 3;
        // 显示第几页
        int pageNo = 2;

        try {
            // 1. 注册驱动
            Class.forName(driver);
            // 2. 获取连接
            conn = DriverManager.getConnection(url, user, password);
            // 3. 获取预编译的数据操作对象
            String sql = "select ename from emp limit ?, ?";
            // 预编译SQL语句
            pstmt = conn.prepareStatement(sql);
            // 给 ? 传值
            pstmt.setInt(1, (pageNo - 1) * pageSize);
            pstmt.setInt(2, pageSize);
            // 4. 执行SQL语句
            rs = pstmt.executeQuery();
            // 5. 处理查询结果集
            while (rs.next()) {
                String ename = rs.getString("ename");
                System.out.println(ename);
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // 6. 释放资源
            if (rs != null) {
                try {
                    rs.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (pstmt != null) {
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (conn != null) {
                try {
                    conn.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
        }
    }
}
```

执行结果如下：

![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1708241685820-a51b06ef-5b38-4e64-806c-0c1b86fe1fab.png)

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

### blob数据的插入和读取（了解）
准备一张表：t_img，两个字段，一个id主键，一个img。

建表语句如下：

```sql
CREATE TABLE `t_img` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `img` MEDIUMBLOB,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB;
```

UNSIGNED：表示无符号整数。

准备一张图片：

![](https://cdn.nlark.com/yuque/0/2024/jpeg/21376908/1708242724736-094b007d-d418-4c4d-9a21-b12f20176daf.jpeg)

需求1：向t_img 表中插入一张图片。

```java
package com.test.jdbc;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.ResourceBundle;

public class JDBCTest09 {
    public static void main(String[] args) {
        ResourceBundle bundle = ResourceBundle.getBundle("com.test.jdbc.jdbc");
        String driver = bundle.getString("driver");
        String url = bundle.getString("url");
        String user = bundle.getString("user");
        String password = bundle.getString("password");

        Connection conn = null;
        PreparedStatement pstmt = null;
        InputStream in = null;
        try {
            // 1. 注册驱动
            Class.forName(driver);
            // 2. 获取连接
            conn = DriverManager.getConnection(url, user, password);
            // 3. 获取预编译的数据操作对象
            String sql = "insert into t_img(img) values(?)";
            pstmt = conn.prepareStatement(sql);
            // 获取文件输入流
            in = new FileInputStream("d:/dog.jpg");
            pstmt.setBlob(1, in);
            // 4. 执行SQL语句
            int count = pstmt.executeUpdate();
            System.out.println("插入了" + count + "条记录");
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // 6. 释放资源
            if (in != null) {
                try {
                    in.close();
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            if (pstmt != null) {
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (conn != null) {
                try {
                    conn.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
        }
    }
}
```

执行结果如下：

![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1708243266510-6d057b29-ab51-49d2-839b-322dae79a50e.png)

需求2：从t_img 表中读取一张图片。（从数据库中读取一张图片保存到本地。）

```java
package com.test.jdbc;

import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.OutputStream;
import java.sql.*;
import java.util.ResourceBundle;

public class JDBCTest10 {
    public static void main(String[] args) {
        ResourceBundle bundle = ResourceBundle.getBundle("com.test.jdbc.jdbc");
        String driver = bundle.getString("driver");
        String url = bundle.getString("url");
        String user = bundle.getString("user");
        String password = bundle.getString("password");

        Connection conn = null;
        PreparedStatement pstmt = null;
        ResultSet rs = null;
        try {
            // 1. 注册驱动
            Class.forName(driver);
            // 2. 获取连接
            conn = DriverManager.getConnection(url, user, password);
            // 3. 获取预编译的数据操作对象
            String sql = "select img from t_img where id = ?";
            pstmt = conn.prepareStatement(sql);
            pstmt.setInt(1, 1);
            // 4. 执行SQL语句
            rs = pstmt.executeQuery();
            // 5. 处理查询结果集
            if (rs.next()) {
                // 获取二进制大对象
                Blob img = rs.getBlob("img");
                // 获取输入流
                InputStream binaryStream = img.getBinaryStream();
                // 创建输出流，该输出流负责写到本地
                OutputStream out = new FileOutputStream("d:/dog2.jpg");
                byte[] bytes = new byte[1024];
                int readCount = 0;
                while ((readCount = binaryStream.read(bytes)) != -1) {
                    out.write(bytes, 0, readCount);
                }
                out.flush();
                binaryStream.close();
                out.close();
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // 6. 释放资源
            if (rs != null) {
                try {
                    rs.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (pstmt != null) {
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (conn != null) {
                try {
                    conn.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
        }
    }
}
```

执行完毕之后，查看一下图片大小是否和原图片相同，打开看看是否可以正常显示。

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

## JDBC批处理操作
准备一张商品表：t_product

建表语句如下：

```sql
create table t_product(
  id bigint primary key,
  name varchar(255)
);
```

### 不使用批处理
不使用批处理，向 t_product 表中插入一万条商品信息，并记录耗时！

```java
package com.test.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.ResourceBundle;

public class NoBatchTest {
    public static void main(String[] args) {
        ResourceBundle bundle = ResourceBundle.getBundle("com.test.jdbc.jdbc");
        String driver = bundle.getString("driver");
        String url = bundle.getString("url");
        String user = bundle.getString("user");
        String password = bundle.getString("password");

        long begin = System.currentTimeMillis();
        Connection conn = null;
        PreparedStatement pstmt = null;
        try {
            // 1. 注册驱动
            Class.forName(driver);
            // 2. 获取连接
            conn = DriverManager.getConnection(url, user, password);
            // 3. 获取预编译的数据操作对象
            String sql = "insert into t_product(id, name) values (?, ?)";
            pstmt = conn.prepareStatement(sql);
            int count = 0;
            for (int i = 1; i <= 10000; i++) {
                pstmt.setInt(1, i);
                pstmt.setString(2, "product" + i);
                // 4. 执行SQL语句
                count += pstmt.executeUpdate();
            }
            System.out.println("插入了" + count + "条记录");
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // 6. 释放资源
            if (pstmt != null) {
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (conn != null) {
                try {
                    conn.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
        }
        long end = System.currentTimeMillis();
        System.out.println("总耗时" + (end - begin) + "毫秒");
    }
}

```

执行结果如下：

![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1708249553654-263146be-a485-4313-831f-892a776abd1d.png)

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

### 使用批处理
使用批处理，向 t_product 表中插入一万条商品信息，并记录耗时！

**<font style="color:#DF2A3F;">注意：启用批处理需要在URL后面添加这个的参数：</font>****`rewriteBatchedStatements=true`**

![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1708249622292-576aa82d-5874-4013-a9b4-d94c00cef0ce.png)

```java
package com.test.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.ResourceBundle;

public class BatchTest {
    public static void main(String[] args) {
        ResourceBundle bundle = ResourceBundle.getBundle("com.test.jdbc.jdbc");
        String driver = bundle.getString("driver");
        String url = bundle.getString("url");
        String user = bundle.getString("user");
        String password = bundle.getString("password");

        long begin = System.currentTimeMillis();
        Connection conn = null;
        PreparedStatement pstmt = null;
        try {
            // 1. 注册驱动
            Class.forName(driver);
            // 2. 获取连接
            conn = DriverManager.getConnection(url, user, password);
            // 3. 获取预编译的数据操作对象
            String sql = "insert into t_product(id, name) values (?, ?)";
            pstmt = conn.prepareStatement(sql);
            int count = 0;
            for (int i = 1; i <= 10000; i++) {
                pstmt.setInt(1, i);
                pstmt.setString(2, "product" + i);
                pstmt.addBatch();
            }
            count += pstmt.executeBatch().length;
            System.out.println("插入了" + count + "条记录");
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // 6. 释放资源
            if (pstmt != null) {
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (conn != null) {
                try {
                    conn.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
        }
        long end = System.currentTimeMillis();
        System.out.println("总耗时" + (end - begin) + "毫秒");
    }
}

```

执行结果如下：

![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1708249131242-0bf6746b-86f7-4bc9-966b-00d22994e177.png)

在进行大数据量插入时，批处理为什么可以提高程序的执行效率？

1.  减少了网络通信次数：JDBC 批处理会将多个 SQL 语句一次性发送给服务器，减少了客户端和服务器之间的通信次数，从而提高了数据写入的速度，特别是对于远程服务器而言，优化效果更为显著。 
2.  减少了数据库操作次数：JDBC 批处理会将多个 SQL 语句合并成一条 SQL 语句进行执行，从而减少了数据库操作的次数，减轻了数据库的负担，大大提高了数据写入的速度。  

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

## DbUtils工具类的封装
JDBC编程六步中，很多代码是重复出现的，可以为这些代码封装一个工具类。让JDBC代码变的更简洁。

```java
package com.test.jdbc;

import java.sql.*;
import java.util.ResourceBundle;

/**
 * ClassName: DbUtils
 * Description: JDBC工具类
 * Datetime: 2024/4/10 22:29
 * Author: 老杜@极课未来
 * Version: 1.0
 */
public class DbUtils {
    private static String url;
    private static String user;
    private static String password;

    static {
        // 读取属性资源文件
        ResourceBundle bundle = ResourceBundle.getBundle("com.test.jdbc.jdbc");
        String driver = bundle.getString("driver");
        url = bundle.getString("url");
        user = bundle.getString("user");
        password = bundle.getString("password");
        // 注册驱动
        try {
            Class.forName(driver);
        } catch (ClassNotFoundException e) {
            throw new RuntimeException(e);
        }
    }

    /**
     * 获取数据库连接
     * @return
     * @throws SQLException
     */
    public static Connection getConnection() throws SQLException {
        Connection conn = DriverManager.getConnection(url, user, password);
        return conn;
    }

    /**
     * 释放资源
     * @param conn 连接对象
     * @param stmt 数据库操作对象
     * @param rs 结果集对象
     */
    public static void close(Connection conn, Statement stmt, ResultSet rs){
        if (rs != null) {
            try {
                rs.close();
            } catch (SQLException e) {
                throw new RuntimeException(e);
            }
        }
        if (stmt != null) {
            try {
                stmt.close();
            } catch (SQLException e) {
                throw new RuntimeException(e);
            }
        }
        if (conn != null) {
            try {
                conn.close();
            } catch (SQLException e) {
                throw new RuntimeException(e);
            }
        }
    }
}

```

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

## 什么是事务
事务是一个完整的业务，在这个业务中需要多条DML语句共同联合才能完成，而事务可以保证多条DML语句同时成功或者同时失败，从而保证数据的安全。例如A账户向B账户转账一万，A账户减去一万(update)和B账户加上一万(update)，必须同时成功或者同时失败，才能保证数据是正确的。

## 使用转账案例演示事务
### 表和数据的准备
t_act表：

![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712906363176-935497e0-164e-4dd7-9c0d-a461fec09668.png)

![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712906313124-77170d5b-9a14-4973-a063-2404228e0c60.png)

```sql
drop table if exists t_act;
create table t_act(
  act_no varchar(255) primary key,
  balance double(10,2)
);
insert into t_act(act_no, balance) values('act-001', 50000.0);
insert into t_act(act_no, balance) values('act-002', 0.0);
commit;
select * from t_act;
```

### 实现转账功能

```java
package com.test.jdbc;

import com.test.jdbc.utils.DbUtils;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

/**
 * ClassName: JDBCTest19
 * Description: 实现账户转账
 * Datetime: 2024/4/12 15:20
 * Author: 老杜@极课未来
 * Version: 1.0
 */
public class JDBCTest19 {
    public static void main(String[] args) {
        // 转账金额
        double money = 10000.0;

        Connection conn = null;
        PreparedStatement ps1 = null;
        PreparedStatement ps2 = null;
        try {
            conn = DbUtils.getConnection();

            // 更新 act-001 账户
            String sql1 = "update t_act set balance = balance - ? where actno = ?";
            ps1 = conn.prepareStatement(sql1);
            ps1.setDouble(1, money);
            ps1.setString(2, "act-001");
            int count1 = ps1.executeUpdate();

            // 更新 act-002账户
            String sql2 = "update t_act set balance = balance + ? where actno = ?";
            ps2 = conn.prepareStatement(sql2);
            ps2.setDouble(1, money);
            ps2.setString(2, "act-002");
            int count2 = ps2.executeUpdate();

        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            DbUtils.close(null, ps1, null);
            DbUtils.close(conn, ps1, null);
        }

    }
}

```

执行结果：

![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712911942800-db916080-94e4-4b32-be09-ce7b4b21287d.png)

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

### JDBC事务默认是自动提交的
JDBC事务默认情况下是自动提交的，所谓的自动提交是指：只要执行一条DML语句则自动提交一次。测试一下，在以下代码位置添加断点：

![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712912172123-b229ef63-3755-4993-84f4-2e303874c710.png)

让代码执行到断点处：

![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712912197579-f0e09df6-2183-4ace-addf-a2c7d3d9c5f7.png)

让程序停在此处，看看数据库表中的数据是否发生变化：

![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712912226628-a32ded77-a2fe-4788-b5b5-3e2083b0926e.png)

可以看到，整个转账的业务还没有执行完毕，act-001 账户的余额已经被修改为 30000了，为什么修改为 30000了，因为JDBC事务默认情况下是自动提交，只要执行一条DML语句则自动提交一次。这种自动提交是极其危险的。如果在此时程序发生了异常，act-002账户的余额未成功更新，则钱会丢失一万。我们可以测试一下：测试前先将数据恢复到起初的时候

![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712912419988-1a2030f1-6603-47a8-9d25-224f767322ea.png)

在以下代码位置，让其发生异常：

![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712912470809-0f61ba45-3562-4531-8fa9-d1d5efba0b81.png)

执行结果如下：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1760950988734-b3c25fcc-0ba8-4fca-981f-0f4b2b53d567.png)

![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712912515925-d895e1d5-14c1-4858-8fe0-eab02faa8100.png)

经过测试得知，丢失了一万元。

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

### 添加事务控制
如何解决以上问题，分三步：

第一步：将JDBC事务的自动提交机制修改为手动提交（即开启事务）

```java
conn.setAutoCommit(false);
```

第二步：当整个业务完整结束后，手动提交事务（即提交事务，事务结束）

```java
conn.commit();
```

第三步：在处理业务过程中，如果发生异常，则进入catch语句块进行异常处理，手动回滚事务（即回滚事务，事务结束）

```java
conn.rollback();
```

代码如下：

```java
public class JDBCTest19 {
    public static void main(String[] args) {
        // 转账金额
        double money = 10000.0;

        Connection conn = null;
        PreparedStatement ps1 = null;
        PreparedStatement ps2 = null;
        try {
            conn = DbUtils.getConnection();
            
            // 开启事务（关闭自动提交机制）
            conn.setAutoCommit(false);

            // 更新 act-001 账户
            String sql1 = "update t_act set balance = balance - ? where actno = ?";
            ps1 = conn.prepareStatement(sql1);
            ps1.setDouble(1, money);
            ps1.setString(2, "act-001");
            int count1 = ps1.executeUpdate();

            String s = null;
            s.toString();

            // 更新 act-002账户
            String sql2 = "update t_act set balance = balance + ? where actno = ?";
            ps2 = conn.prepareStatement(sql2);
            ps2.setDouble(1, money);
            ps2.setString(2, "act-002");
            int count2 = ps2.executeUpdate();
            
            // 提交事务
            conn.commit();

        } catch (Exception e) {
            // 遇到异常回滚事务
            try {
                conn.rollback();
            } catch (SQLException ex) {
                throw new RuntimeException(ex);
            }
            throw new RuntimeException(e);
        } finally {
            DbUtils.close(null, ps1, null);
            DbUtils.close(conn, ps1, null);
        }

    }
}
```

将数据恢复如初：

![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712913009901-fda0cf51-2d89-4aed-907c-92803e51370a.png)

执行程序，仍然会出现异常：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1760951016097-cf55dbe7-f0c6-419a-bbf2-b1d0a28f65ac.png)

但是数据库表中的数据是安全的：

![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712913054649-53befbcc-2748-433c-9f27-6c2dca4a1bd6.png)

当程序不出现异常时：

![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712913078723-158ff1de-43b9-4ae0-b1c5-68dc011ec2c7.png)

数据库表中的数据也是正确的：

![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712913097670-fd86b9a8-dab3-4bab-b5b5-ccfff28e1cba.png)

这样就采用了JDBC事务解决了数据安全的问题。

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

## 设置JDBC事务隔离级别
对于 MySQL 数据库来说，通常不需要设置事务隔离级别，因为默认的可重复读基本上可以满足大部分的业务需求。如果需要完全避免幻读问题，可以设置事务的隔离级别，在JDBC程序中应该如何设置事务的隔离级别呢？代码如下：

```java
public class JDBCTest20 {
    public static void main(String[] args) {
        Connection conn = null;
        try {
            conn = DbUtils.getConnection();
            // 设置事务隔离级别
            conn.setTransactionIsolation(Connection.TRANSACTION_SERIALIZABLE);
            // 开启事务
            conn.setAutoCommit(false);
            
            // .....
            
            // 提交事务
            conn.commit();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            DbUtils.close(conn, null, null);
        }
    }
}
```

## 在MySQL中创建存储过程

```sql
create procedure mypro(in n int, out sum int)
begin 
	set sum := 0;
	repeat 
		if n % 2 = 0 then 
		  set sum := sum + n;
		end if;
		set n := n - 1;
		until n <= 0
	end repeat;
end;
```

以上存储过程完成的功能是：0 到 n 的偶数求和。

## 使用JDBC代码调用存储过程

```java
package com.test.jdbc;

import com.test.jdbc.utils.DbUtils;

import java.sql.CallableStatement;
import java.sql.Connection;
import java.sql.SQLException;
import java.sql.Types;

/**
 * ClassName: JDBCTest21
 * Description:
 * Datetime: 2024/4/12 17:42
 * Author: 老杜@极课未来
 * Version: 1.0
 */
public class JDBCTest21 {
    public static void main(String[] args) {
        Connection conn = null;
        CallableStatement cs = null;
        try {
            conn = DbUtils.getConnection();
            String sql = "{call mypro(?, ?)}";
            cs = conn.prepareCall(sql);
            // 给第1个 ? 传值
            cs.setInt(1, 100);
            // 将第2个 ? 注册为出参
            cs.registerOutParameter(2, Types.INTEGER);
            // 执行存储过程
            cs.execute();
            // 通过出参获取结果
            int result = cs.getInt(2);
            System.out.println("计算结果：" + result);
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            DbUtils.close(conn, cs, null);
        }
    }
}

```

执行结果：

![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712915314800-457530dc-85bd-4592-b0e7-595349fb92cb.png)

程序解说：

使用JDBC代码调用存储过程需要以下步骤：

1. 加载MySQL的JDBC驱动程序

使用以下代码加载MySQL的JDBC驱动程序：

```java
Class.forName("com.mysql.jdbc.Driver");
```

2. 连接到MySQL数据库

使用以下代码连接到MySQL数据库：

```java
Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb", "user", "password");
```

其中，第一个参数为连接字符串，按照实际情况修改；第二个参数为用户名，按照实际情况修改；第三个参数为密码，按照实际情况修改。

3. 创建CallableStatement对象

使用以下代码创建CallableStatement对象：

```java
CallableStatement cstmt = conn.prepareCall("{call mypro(?, ?)}");
```

其中，第一个参数为调用存储过程的语句，按照实际情况修改；第二个参数是需要设定的参数。

4. 设置输入参数

使用以下代码设置输入参数：

```java
cstmt.setInt(1, n);
```

其中，第一个参数是参数在调用语句中的位置，第二个参数是实际要传入的值。

5. 注册输出参数

使用以下代码注册输出参数：

```java
cstmt.registerOutParameter(2, Types.INTEGER);
```

其中，第一个参数是要注册的参数在调用语句中的位置，第二个参数是输出参数的类型。

6. 执行存储过程

使用以下代码执行存储过程：

```java
cstmt.execute();
```

7. 获取输出参数值

使用以下代码获取输出参数的值：

```java
int sum = cstmt.getInt(2);
```

其中，第一个参数是输出参数在调用语句中的位置。

8. 关闭连接

使用以下代码关闭连接和语句对象：

```java
cstmt.close();
conn.close();
```

上述代码中，可以根据实际情况适当修改存储过程名、参数传递方式、参数类型等内容。

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

## 数据库表的准备

```sql
drop table if exists t_employee;

create table t_employee(
  id bigint primary key auto_increment,
  name varchar(255),
  job varchar(255),
  hire_date char(10),
  salary decimal(10,2),
  address varchar(255)
);

insert into t_employee(name,job,hire_date,salary,address) values('张三','销售员','1999-10-11',5000.0,'北京朝阳');
insert into t_employee(name,job,hire_date,salary,address) values('李四','编码人员','1998-02-12',5000.0,'北京海淀');
insert into t_employee(name,job,hire_date,salary,address) values('王五','项目经理','2000-08-11',5000.0,'北京大兴');
insert into t_employee(name,job,hire_date,salary,address) values('赵六','产品经理','2022-09-11',5000.0,'北京东城');
insert into t_employee(name,job,hire_date,salary,address) values('钱七','测试员','2024-12-11',5000.0,'北京西城');

commit;

select * from t_employee;
```

![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1713071562929-40bc3b9b-59e0-4447-a6d2-ee9a402112d7.png)

## 实现效果
### 查看员工列表
![](https://cdn.nlark.com/yuque/0/2026/png/21376908/1780239984435-07b42877-65c3-4835-a19b-af848aafd3bb.png)

### 查看员工详情
![](https://cdn.nlark.com/yuque/0/2026/png/21376908/1780240017712-26b28b3d-afa7-4c36-a6fe-e911dac6986b.png)

### 新增员工
![](https://cdn.nlark.com/yuque/0/2026/png/21376908/1780240071690-f31e11df-9d0d-41c8-8e3b-a5c94c988c95.png)

### 修改员工
![](https://cdn.nlark.com/yuque/0/2026/png/21376908/1780240182934-f0dcc2f4-48a2-41e8-b098-fefabc146998.png)

### 删除员工
![](https://cdn.nlark.com/yuque/0/2026/png/21376908/1780240226257-13dd2edb-24ca-4c6b-86ee-c24429890133.png)

### 退出系统
![](https://cdn.nlark.com/yuque/0/2026/png/21376908/1780240243363-1212e013-7a7c-434b-bfea-162d7c7de415.png)

## 参考代码
可以将以下代码作为参考，完善的实现了员工信息管理：

```java
package com.jkweilai.jdbc.empmgt;

import java.sql.*;
import java.util.Scanner;

public class EmployeeSystem {

    // 数据库连接信息
    private static final String URL = "jdbc:mysql://localhost:3306/test";
    private static final String USER = "root";
    private static final String PASSWORD = "123456";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("欢迎使用员工管理系统，通过该系统可以完成员工信息的：");
            System.out.println("新增员工、修改员工、删除员工、查看某个员工详细信息、查看员工列表");
            System.out.println("请输入对应的功能编号来使用对应的功能：");
            System.out.println("[1]查看员工列表");
            System.out.println("[2]查看某个员工详细信息");
            System.out.println("[3]新增员工");
            System.out.println("[4]修改员工");
            System.out.println("[5]删除员工");
            System.out.println("[0]退出系统");
            System.out.print("请输入功能编号：");

            int choice = scanner.nextInt();
            scanner.nextLine();

            switch (choice) {
                case 1:
                    listEmployees();
                    break;
                case 2:
                    viewEmployeeDetail(scanner);
                    break;
                case 3:
                    addEmployee(scanner);
                    break;
                case 4:
                    updateEmployee(scanner);
                    break;
                case 5:
                    deleteEmployee(scanner);
                    break;
                case 0:
                    System.out.println("感谢使用，再见！");
                    scanner.close();
                    return;
                default:
                    System.out.println("无效的编号，请重新输入！");
            }
            System.out.println();
        }
    }

    // 1. 查看员工列表
    private static void listEmployees() {
        String sql = "SELECT * FROM t_employee";

        try (Connection conn = DriverManager.getConnection(URL, USER, PASSWORD); Statement stmt = conn.createStatement(); ResultSet rs = stmt.executeQuery(sql)) {

            System.out.println("员工列表如下：");
            System.out.println("ID\t\t姓名\t\t职位\t\t\t入职日期\t\t\t薪水\t\t\t地址");
            System.out.println("-------------------------------------------------------------");

            while (rs.next()) {
                long id = rs.getLong("id");
                String name = rs.getString("name");
                String job = rs.getString("job");
                String hireDate = rs.getString("hire_date");
                double salary = rs.getDouble("salary");
                String address = rs.getString("address");

                System.out.println(id + "\t\t" + name + "\t\t" + job + "\t\t" + hireDate + "\t\t" + salary + "\t\t" + address);
            }

        } catch (SQLException e) {
            System.out.println("查询员工列表失败：" + e.getMessage());
            e.printStackTrace();
        }
    }

    // 2. 查看某个员工详细信息
    private static void viewEmployeeDetail(Scanner scanner) {
        System.out.print("请输入要查看的员工ID：");
        Long id = scanner.nextLong();
        scanner.nextLine();

        String sql = "SELECT * FROM t_employee WHERE id = ?";

        try (Connection conn = DriverManager.getConnection(URL, USER, PASSWORD); PreparedStatement pstmt = conn.prepareStatement(sql)) {

            pstmt.setLong(1, id);
            ResultSet rs = pstmt.executeQuery();

            if (rs.next()) {
                System.out.println("========== 员工详细信息 ==========");
                System.out.println("ID：" + rs.getLong("id"));
                System.out.println("姓名：" + rs.getString("name"));
                System.out.println("职位：" + rs.getString("job"));
                System.out.println("入职日期：" + rs.getString("hire_date"));
                System.out.println("薪水：" + rs.getDouble("salary"));
                System.out.println("地址：" + rs.getString("address"));
                System.out.println("=================================");
            } else {
                System.out.println("未找到ID为 " + id + " 的员工！");
            }

        } catch (SQLException e) {
            System.out.println("查询员工详情失败：" + e.getMessage());
            e.printStackTrace();
        }
    }

    // 3. 新增员工
    private static void addEmployee(Scanner scanner) {
        System.out.println("请输入员工信息：");

        System.out.print("姓名：");
        String name = scanner.nextLine();

        System.out.print("职位：");
        String job = scanner.nextLine();

        System.out.print("入职日期(格式：YYYY-MM-DD)：");
        String hireDate = scanner.nextLine();

        System.out.print("薪水：");
        double salary = scanner.nextDouble();
        scanner.nextLine();

        System.out.print("地址：");
        String address = scanner.nextLine();

        String sql = "INSERT INTO t_employee(name, job, hire_date, salary, address) VALUES(?, ?, ?, ?, ?)";

        try (Connection conn = DriverManager.getConnection(URL, USER, PASSWORD); PreparedStatement pstmt = conn.prepareStatement(sql)) {

            pstmt.setString(1, name);
            pstmt.setString(2, job);
            pstmt.setString(3, hireDate);
            pstmt.setDouble(4, salary);
            pstmt.setString(5, address);

            int rows = pstmt.executeUpdate();
            if (rows > 0) {
                System.out.println("员工 " + name + " 新增成功！");
            } else {
                System.out.println("新增失败！");
            }

        } catch (SQLException e) {
            System.out.println("新增员工失败：" + e.getMessage());
            e.printStackTrace();
        }
    }

    // 4. 修改员工
    private static void updateEmployee(Scanner scanner) {
        System.out.print("请输入要修改的员工ID：");
        Long id = scanner.nextLong();
        scanner.nextLine();

        // 先检查员工是否存在
        if (!checkEmployeeExists(id)) {
            System.out.println("员工ID " + id + " 不存在！");
            return;
        }

        System.out.println("请输入新的员工信息（直接回车表示不修改）：");

        System.out.print("姓名（原值：" + getEmployeeField(id, "name") + "）：");
        String name = scanner.nextLine();

        System.out.print("职位（原值：" + getEmployeeField(id, "job") + "）：");
        String job = scanner.nextLine();

        System.out.print("入职日期（原值：" + getEmployeeField(id, "hire_date") + "）：");
        String hireDate = scanner.nextLine();

        System.out.print("薪水（原值：" + getEmployeeField(id, "salary") + "）：");
        String salaryStr = scanner.nextLine();

        System.out.print("地址（原值：" + getEmployeeField(id, "address") + "）：");
        String address = scanner.nextLine();

        // 构建动态SQL
        StringBuilder sql = new StringBuilder("UPDATE t_employee SET ");
        boolean hasUpdate = false;

        if (!name.isEmpty()) {
            sql.append("name = ?, ");
            hasUpdate = true;
        }
        if (!job.isEmpty()) {
            sql.append("job = ?, ");
            hasUpdate = true;
        }
        if (!hireDate.isEmpty()) {
            sql.append("hire_date = ?, ");
            hasUpdate = true;
        }
        if (!salaryStr.isEmpty()) {
            sql.append("salary = ?, ");
            hasUpdate = true;
        }
        if (!address.isEmpty()) {
            sql.append("address = ?, ");
            hasUpdate = true;
        }

        if (!hasUpdate) {
            System.out.println("没有输入任何修改内容！");
            return;
        }

        // 删除最后的逗号和空格
        sql.delete(sql.length() - 2, sql.length());
        sql.append(" WHERE id = ?");

        try (Connection conn = DriverManager.getConnection(URL, USER, PASSWORD); PreparedStatement pstmt = conn.prepareStatement(sql.toString())) {

            int index = 1;
            if (!name.isEmpty()) {
                pstmt.setString(index++, name);
            }
            if (!job.isEmpty()) {
                pstmt.setString(index++, job);
            }
            if (!hireDate.isEmpty()) {
                pstmt.setString(index++, hireDate);
            }
            if (!salaryStr.isEmpty()) {
                pstmt.setDouble(index++, Double.parseDouble(salaryStr));
            }
            if (!address.isEmpty()) {
                pstmt.setString(index++, address);
            }
            pstmt.setLong(index, id);

            int rows = pstmt.executeUpdate();
            if (rows > 0) {
                System.out.println("员工ID " + id + " 修改成功！");
            } else {
                System.out.println("修改失败！");
            }

        } catch (SQLException e) {
            System.out.println("修改员工失败：" + e.getMessage());
            e.printStackTrace();
        }
    }

    // 5. 删除员工
    private static void deleteEmployee(Scanner scanner) {
        System.out.print("请输入要删除的员工ID：");
        Long id = scanner.nextLong();
        scanner.nextLine();

        // 先检查员工是否存在
        if (!checkEmployeeExists(id)) {
            System.out.println("员工ID " + id + " 不存在！");
            return;
        }

        System.out.print("确认删除员工ID " + id + " 吗？(y/n)：");
        String confirm = scanner.nextLine();

        if (!"y".equalsIgnoreCase(confirm)) {
            System.out.println("已取消删除！");
            return;
        }

        String sql = "DELETE FROM t_employee WHERE id = ?";

        try (Connection conn = DriverManager.getConnection(URL, USER, PASSWORD); PreparedStatement pstmt = conn.prepareStatement(sql)) {

            pstmt.setLong(1, id);
            int rows = pstmt.executeUpdate();
            if (rows > 0) {
                System.out.println("员工ID " + id + " 删除成功！");
            } else {
                System.out.println("删除失败！");
            }

        } catch (SQLException e) {
            System.out.println("删除员工失败：" + e.getMessage());
            e.printStackTrace();
        }
    }

    // 辅助方法：检查员工是否存在
    private static boolean checkEmployeeExists(Long id) {
        String sql = "SELECT id FROM t_employee WHERE id = ?";

        try (Connection conn = DriverManager.getConnection(URL, USER, PASSWORD); PreparedStatement pstmt = conn.prepareStatement(sql)) {

            pstmt.setLong(1, id);
            ResultSet rs = pstmt.executeQuery();
            return rs.next();

        } catch (SQLException e) {
            System.out.println("检查员工存在性失败：" + e.getMessage());
            return false;
        }
    }

    // 辅助方法：获取员工某个字段的值
    private static String getEmployeeField(Long id, String field) {
        String sql = "SELECT " + field + " FROM t_employee WHERE id = ?";

        try (Connection conn = DriverManager.getConnection(URL, USER, PASSWORD); PreparedStatement pstmt = conn.prepareStatement(sql)) {

            pstmt.setLong(1, id);
            ResultSet rs = pstmt.executeQuery();
            if (rs.next()) {
                return rs.getString(1);
            }

        } catch (SQLException e) {
            e.printStackTrace();
        }
        return "";
    }
}
```

**关于以上代码中的 **`**Scanner**`**，为什么要在 **`**nextXxx()**`**方法后面添加 **`**nextLine()**`**方法？**

+ **首先你要知道 **`**nextLine()**`**方法是干啥的？**
    - **该方法的作用是为了读取一个完整的行，例如用户输入 **`**abc**`**回车，实际上用户输入的是 **`**abc\n**`**，那么 **`**nextLine()**`**方法可以将 **`**abc\n**`**都读取到，读到了一个完整行。**
+ **什么时候需要加 ****`scanner.nextLine()`****？**
    - **当 ****`nextInt()`**** / ****`nextDouble()`**** / ****`next()`**** 后面跟着的是 ****`nextLine()`**** 时，中间必须加一个 ****`nextLine()`**** 吃掉遗留的换行符。当用户输入 ****`123`****并回车，实际上输入的内容是 ****`123\n`****，****`nextInt()`****方法只能读取到 ****`123`****，因此在缓冲区还会残留一个 ****`\n`****，如果此时紧接着调用 ****`nextLine()`****方法，该方法只会吃掉缓存中残留的换行符，返回一个空字符串。**
+ **什么时候不需要？**
    - **当 ****`nextInt()`**** / ****`nextDouble()`**** / ****`next()`**** 后面跟着的还是 ****`nextInt()`**** / ****`nextDouble()`**** / ****`next()`**** 时，不需要。因为 ****`nextXxx()`****方法在执行时会自动跳过它前面的空白和换行符。**

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

## 什么是DAO
DAO是：Data Access Object，翻译为：数据访问对象。

一种JavaEE的设计模式，专门用来做数据增删改查的类（**DAO 中不应该出现业务代码，很纯粹的 CRUD，才能很好的复用**）。

在实际的开发中，通常我们会将数据库的操作封装为一个单独的DAO去完成，这样做的目的是：提高代码的复用性，另外也可以降低程序的耦合度，提高扩展力。

例如：操作用户数据的叫做UserDao，操作员工数据的叫做EmployeeDao，操作产品数据的叫做ProductDao，操作订单数据的叫做OrderDao等。

## 使用DAO改造员工信息管理
### 定义Employee封装数据
Employee类是一个Java Bean，专门用来封装员工的信息：

```java
package com.test.jdbc.beans;

/**
 * ClassName: Employee
 * Description:
 * Datetime: 2024/4/14 23:32
 * Author: 老杜@极课未来
 * Version: 1.0
 */
public class Employee {
    private Long id;
    private String name;
    private String job;
    private Double salary;
    private String hiredate;
    private String address;

    @Override
    public String toString() {
        return "Employee{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", job='" + job + '\'' +
                ", salary=" + salary +
                ", hiredate='" + hiredate + '\'' +
                ", address='" + address + '\'' +
                '}';
    }

    public Employee() {
    }

    public Employee(Long id, String name, String job, Double salary, String hiredate, String address) {
        this.id = id;
        this.name = name;
        this.job = job;
        this.salary = salary;
        this.hiredate = hiredate;
        this.address = address;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getJob() {
        return job;
    }

    public void setJob(String job) {
        this.job = job;
    }

    public Double getSalary() {
        return salary;
    }

    public void setSalary(Double salary) {
        this.salary = salary;
    }

    public String getHiredate() {
        return hiredate;
    }

    public void setHiredate(String hiredate) {
        this.hiredate = hiredate;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
}

```

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

### 定义EmployeeDao
定义五个方法，分别完成五个功能：新增，修改，删除，查看一个，查看所有。

```java
package com.test.jdbc.dao;

import com.test.jdbc.beans.Employee;
import com.test.jdbc.utils.DbUtils;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

/**
 * ClassName: EmployeeDao
 * Description:
 * Datetime: 2024/4/14 23:34
 * Author: 老杜@极课未来
 * Version: 1.0
 */
public class EmployeeDao {
    /**
     * 新增员工
     * @param employee
     * @return
     */
    public int insert(Employee employee) {
        Connection conn = null;
        PreparedStatement ps = null;
        int count = 0;
        try {
            conn = DbUtils.getConnection();
            String sql = "insert into t_employee(name,job,salary,hiredate,address) values(?,?,?,?,?)";
            ps = conn.prepareStatement(sql);
            ps.setString(1, employee.getName());
            ps.setString(2, employee.getJob());
            ps.setDouble(3, employee.getSalary());
            ps.setString(4, employee.getHiredate());
            ps.setString(5, employee.getAddress());
            count = ps.executeUpdate();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            DbUtils.close(conn, ps, null);
        }
        return count;
    }

    /**
     * 修改员工
     * @param employee
     * @return
     */
    public int update(Employee employee){
        Connection conn = null;
        PreparedStatement ps = null;
        int count = 0;
        try {
            conn = DbUtils.getConnection();
            String sql = "update t_employee set name=?, job=?, salary=?, hiredate=?, address=? where id=?";
            ps = conn.prepareStatement(sql);
            ps.setString(1, employee.getName());
            ps.setString(2, employee.getJob());
            ps.setDouble(3, employee.getSalary());
            ps.setString(4, employee.getHiredate());
            ps.setString(5, employee.getAddress());
            ps.setLong(6, employee.getId());
            count = ps.executeUpdate();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            DbUtils.close(conn, ps, null);
        }
        return count;
    }

    /**
     * 根据id删除员工信息
     * @param id 员工id
     * @return 1表示成功
     */
    public int deleteById(Long id){
        Connection conn = null;
        PreparedStatement ps = null;
        int count = 0;
        try {
            conn = DbUtils.getConnection();
            String sql = "delete from t_employee where id = ?";
            ps = conn.prepareStatement(sql);
            ps.setLong(1, id);
            count = ps.executeUpdate();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            DbUtils.close(conn, ps, null);
        }
        return count;
    }

    /**
     * 根据id查询所有员工
     * @param id
     * @return
     */
    public Employee selectById(Long id){
        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        Employee employee = null;
        try {
            conn = DbUtils.getConnection();
            String sql = "select * from t_employee where id = ?";
            ps = conn.prepareStatement(sql);
            ps.setLong(1, id);
            rs = ps.executeQuery();
            if(rs.next()){
                employee = new Employee();
                employee.setId(id);
                employee.setName(rs.getString("name"));
                employee.setJob(rs.getString("job"));
                employee.setSalary(rs.getDouble("salary"));
                employee.setHiredate(rs.getString("hiredate"));
                employee.setAddress(rs.getString("address"));
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            DbUtils.close(conn, ps, rs);
        }
        return employee;
    }

    /**
     * 查询所有员工信息
     * @return 员工列表
     */
    public List<Employee> selectAll(){
        List<Employee> employees = new ArrayList<>();
        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        try {
            conn = DbUtils.getConnection();
            String sql = "select * from t_employee";
            ps = conn.prepareStatement(sql);
            rs = ps.executeQuery();
            while(rs.next()){
                Employee employee = new Employee();
                employee.setId(rs.getLong("id"));
                employee.setName(rs.getString("name"));
                employee.setJob(rs.getString("job"));
                employee.setSalary(rs.getDouble("salary"));
                employee.setHiredate(rs.getString("hiredate"));
                employee.setAddress(rs.getString("address"));
                employees.add(employee);
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            DbUtils.close(conn, ps, rs);
        }
        return employees;
    }
}
```

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

## BaseDao的封装

```java
package com.test.jdbc.dao;

import com.test.jdbc.utils.DbUtils;

import java.lang.reflect.Field;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

/**
 * ClassName: BaseDao
 * Description: 最基础的Dao，所有的Dao应该去继承该BaseDao
 * Datetime: 2024/4/15 11:08
 * Author: 老杜@极课未来
 * Version: 1.0
 */
public class BaseDao {

    /**
     * 这是一个通用的执行insert delete update语句的方法。
     * @param sql
     * @param params
     * @return
     */
    public int executeUpdate(String sql, Object... params) {
        Connection conn = null;
        PreparedStatement ps = null;
        int count = 0;
        try {
            // 获取连接
            conn = DbUtils.getConnection();
            // 获取预编译的数据库操作对象
            ps = conn.prepareStatement(sql);
            // 给 ? 占位符传值
            if(params != null && params.length > 0){
                // 有占位符 ?
                for (int i = 0; i < params.length; i++) {
                    ps.setObject(i + 1, params[i]);
                }
            }
            // 执行SQL语句
            count = ps.executeUpdate();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            DbUtils.close(conn, ps, null);
        }
        return count;
    }

    /**
     * 这是一个通用的查询语句
     * @param clazz
     * @param sql
     * @param params
     * @return
     * @param <T>
     */
    public <T> List<T> executeQuery(Class<T> clazz, String sql, Object... params){
        List<T> list = new ArrayList<>();
        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        try {
            // 获取连接
            conn = DbUtils.getConnection();
            // 获取预编译的数据库操作对象
            ps = conn.prepareStatement(sql);
            // 给?传值
            if(params != null && params.length > 0){
                for (int i = 0; i < params.length; i++) {
                    ps.setObject(i + 1, params[i]);
                }
            }
            // 执行SQL语句
            rs = ps.executeQuery();

            // 获取查询结果集元数据
            ResultSetMetaData rsmd = rs.getMetaData();

            // 获取列数
            int columnCount = rsmd.getColumnCount();

            // 处理查询结果集
            while(rs.next()){
                // 封装bean对象
                T obj = clazz.newInstance();
                // 给bean对象属性赋值
                /*
                比如现在有一张表：t_user，然后表中有两个字段，一个是 user_id，一个是user_name
                现在javabean是User类，该类中的属性名是：userId,username
                执行这样的SQL语句：select user_id as userId, user_name as username from t_user;
                 */
                for (int i = 1; i <= columnCount; i++) {
                    // 获取查询结果集中的列的名字
                    // 这个列的名字是通过as关键字进行了起别名，这个列名就是bean的属性名。
                    String fieldName = rsmd.getColumnLabel(i);
                    // 获取属性Field对象
                    Field declaredField = clazz.getDeclaredField(fieldName);
                    // 打破封装
                    declaredField.setAccessible(true);
                    // 给属性赋值
                    declaredField.set(obj, rs.getObject(i));
                }

                // 将对象添加到List集合
                list.add(obj);
            }
        } catch (Exception e) {
            throw new RuntimeException(e);
        } finally {
            DbUtils.close(conn, ps, rs);
        }
        // 返回List集合
        return list;
    }


    /**
     *
     * @param clazz
     * @param sql
     * @param params
     * @return
     * @param <T>
     */
    public <T> T queryOne(Class<T> clazz, String sql, Object... params){
        List<T> list = executeQuery(clazz, sql, params);
        if(list == null || list.size() == 0){
            return null;
        }
        return list.get(0);
    }

}

```

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

## 连接池的理解
### 不使用连接池有啥问题
Connection对象是重量级对象，创建Connection对象就是建立两个进程之间的通信，非常耗费资源。一次完整的数据库操作，大部分时间都耗费在连接对象的创建。

第一个问题：每一次请求都创建一个Connection连接对象，效率较低。

第二个问题：连接对象的数量无法限制。如果连接对象的数量过高，会导致mysql数据库服务器崩溃。

### 使用连接池来解决什么问题
提前创建好N个连接对象，将其存放到一个集合中（这个集合就是一个缓存）。

用户请求时，需要连接对象直接从连接池中获取，不需要创建连接对象（**省去了对象的创建过程**），因此效率较高。

另外，连接对象只能从连接池中获取，如果没有空闲的连接对象，只能等待，这样连接对象创建的数量就得到了控制。

### javax.sql.DataSource
连接池有很多，不过所有的连接池都实现了 javax.sql.DataSource 接口。也就是说我们程序员在使用连接池的时候，不管使用哪家的连接池产品，只要面向javax.sql.DataSource接口调用方法即可。

另外，实际上我们也可以自定义属于我们自己的连接池。只要实现DataSource接口即可。

### 连接池的属性
对于一个基本的连接池来说，一般都包含以下几个常见的属性：

1.  初始化连接数（initialSize）：连接池初始化时创建的连接数。 
2.  最大连接数（maxActive）：连接池中最大的连接数，也就是连接池所能容纳的最大连接数量，当连接池中的连接数量达到此值时，后续请求会被阻塞并等待连接池中有连接被释放后再处理。 
3.  最小空闲连接数量（minIdle）： 指连接池中最小的空闲连接数，也就是即使当前没有请求，连接池中至少也要保持一定数量的空闲连接，以便应对高并发请求或突发连接请求的情况。
4.  最大空闲连接数量（maxIdle）： 指连接池中最大的空闲连接数，也就是连接池中最多允许保持的空闲连接数量。当连接池中的空闲连接数量达到了maxIdle设定的值后，多余的空闲连接将会被连接池释放掉。
5.  最大等待时间（maxWait）：当连接池中的连接数量达到最大值时，后续请求需要等待的最大时间，如果超过这个时间，则会抛出异常。 
6.  连接有效性检查（testOnBorrow、testOnReturn）：为了确保连接池中只有可用的连接，一些连接池会定期对连接进行有效性检查，这里的属性就是配置这些检查的选项。 
7.  连接的driver、url、user、password等。 

以上这些属性是连接池中较为常见的一些属性，不同的连接池在实现时可能还会有其他的一些属性，不过大多数连接池都包含了以上几个属性，对于使用者来说需要根据自己的需要进行灵活配置。

## 常用的连接池
市面上常用的数据库连接池有许多，以下是其中几种：

1. DBCP
    1. 2001年诞生，最早的连接池。
    2. Apache Software Foundation的一个开源项目。
    3. DBCP的设计初衷是为了满足Tomcat服务器对连接池管理的需求。
2. c3p0
    1. 2004年诞生
    2. c3p0是由Steve Waldman于2004年推出的，它是一个高性能、高可靠性、易配置的数据库连接池。c3p0能够提供连接池的容错能力、自动重连等功能，适用于高并发场景和数据量大的应用。
3. Druid
    1. 2012年诞生
    2. Druid连接池由阿里巴巴集团开发，于2011年底开始对外公开，2012年正式发布。Druid是一个具有高性能、高可靠性、丰富功能的数据库连接池，不仅可以做连接池，还能做监控、分析和管理数据库，支持SQL防火墙、统计分析、缓存和访问控制等功能。
4. HikariCP
    1. 2012年诞生
    2. HikariCP是由Brett Wooldridge于2012年创建的开源项目，它被认为是Java语言下最快的连接池之一，具有快速启动、低延迟、低资源消耗等优点。HikariCP连接池适用于高并发场景和云端应用。
    3. 很单纯的一个连接池，这个产品只做连接池应该做的，其他的不做。所以性能是极致的。相对于Druid来说，它更加轻量级。
    4. Druid连接池在连接管理之外提供了更多的功能，例如SQL防火墙、统计分析、缓存、访问控制等，适用于在数据库访问过程中，需要进行细粒度控制的场景
    5. HikariCP则更侧重于性能方面的优化，对各种数据库的兼容性也更好
5. BoneCP
    1. 2015年诞生
    2. BoneCP是一款Java语言下的高性能连接池，于2015年由Dominik Gruntz在GitHub上发布。BoneCP具有分布式事务、连接空闲检查、SQL语句跟踪和性能分析、特定类型的连接池等特点。BoneCP连接池适用于大型应用系统和高并发的负载场景

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

## 连接池的使用
### Druid的使用
[https://github.com/alibaba/druid](https://github.com/alibaba/druid) 

这里是所有官方文档、使用手册和源代码的核心入口。在仓库的Wiki页面，你可以找到最为详尽和权威的配置指南、功能说明以及常见问题解答

**第一步：引入Druid的jar包**

![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1713164785681-0fdb049c-2a06-40e4-83cd-bfc876d8b696.png)

jar 包在 Maven 的中央仓库中有提供：[https://repo1.maven.org/maven2/com/alibaba/druid/](https://repo1.maven.org/maven2/com/alibaba/druid/)

**第二步：配置文件**

在类的根路径下创建一个属性资源文件：jdbc.properties

```properties
url=jdbc:mysql://localhost:3306/jdbc
username=root
password=1234
driverClassName=com.mysql.cj.jdbc.Driver
initialSize=5
minIdle=10
maxActive=20
```

**第三步：编写代码，从连接池中获取连接对象**

```java
// 读取属性配置文件
InputStream in = DruidConfig.class.getClassLoader().getResourceAsStream("jdbc.properties");
Properties props = new Properties();
props.load(in);
// 创建连接池
DataSource dataSource = DruidDataSourceFactory.createDataSource(props);
Connection conn = dataSource.getConnection();
```

第四步：关闭连接

仍然调用Connection的close()方法，但是这个close()方法并不是真正的关闭连接，只是将连接归还到连接池，让其称为空闲连接对象。这样其他线程可以继续使用该空闲连接。

![](https://cdn.nlark.com/yuque/0/2025/jpeg/21376908/1757681056420-39d1bc52-55fe-4f3b-8183-b4d7ba79b166.jpeg)

### HikariCP的使用
Spring Boot 框架默认使用的就是这个连接池。

**第一步：引入jar包**

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1761575984591-fa65fd12-0433-44b5-891c-7e3ac1aab3ae.png)

jar 包的 Maven 中央仓库地址：[https://repo1.maven.org/maven2/com/zaxxer/HikariCP/](https://repo1.maven.org/maven2/com/zaxxer/HikariCP/)

**第二步：编写配置文件**

在类的根路径下创建一个属性资源文件：jdbc2.properties

```properties
jdbcUrl=jdbc:mysql://localhost:3306/jdbc
username=root
password=1234
driverClassName=com.mysql.cj.jdbc.Driver
minimumIdle=5
maximumPoolSize=20
```

****

**第三步：编写代码，从连接池中获取连接**

```java
InputStream in = HikariConfig.class.getClassLoader().getResourceAsStream("jdbc2.properties");
Properties props = new Properties();
props.load(in);
HikariConfig config = new HikariConfig(props);
DataSource dataSource = new HikariDataSource(config);
Connection conn = dataSource.getConnection();
```

第四步：关闭连接（调用conn.close()，将连接归还到连接池，连接对象为空闲状态。）
