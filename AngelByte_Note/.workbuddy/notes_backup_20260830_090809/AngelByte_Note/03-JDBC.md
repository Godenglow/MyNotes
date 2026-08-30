# 什么是JDBC
JDBC（Java DataBase Connectivity）就是Java数据库连接，说白了就是用Java语言来操作数据库。原来我们操作数据库是在控制台使用SQL语句来操作数据库，JDBC是用Java语言向数据库发送SQL语句。![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1701931262247-009be90f-6a0e-4e63-a1f1-6d6c96df65ce.png#averageHue=%23efe7f7&clientId=ucd4dfa1f-8793-4&from=paste&height=374&id=u7ed5bac8&originHeight=374&originWidth=657&originalType=binary&ratio=1&rotation=0&showTitle=false&size=136883&status=done&style=shadow&taskId=u2ff2f08f-57be-4241-9660-c991fa1d540&title=&width=657)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=acVGP&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

# JDBC原理
早期SUN公司的天才们想编写一套可以连接天下所有数据库的API，但是当他们刚刚开始时就发现这是不可完成的任务，因为各个厂商的数据库服务器差异太大了。后来SUN开始与数据库厂商们讨论，最终得出的结论是，由SUN提供一套访问数据库的规范（就是一组接口），并提供连接数据库的协议标准，然后各个数据库厂商会遵循SUN的规范提供一套访问自己公司数据库服务器的API。SUN提供的规范命名为JDBC，而各个厂商提供的，遵循了JDBC规范的，可以访问自己数据库的API被称之为驱动！![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1701931393355-983a997d-c44c-4a48-b1b0-91b281b5a98b.png#averageHue=%23e9e9e8&clientId=ucd4dfa1f-8793-4&from=paste&height=308&id=u158f2a18&originHeight=308&originWidth=610&originalType=binary&ratio=1&rotation=0&showTitle=false&size=139132&status=done&style=shadow&taskId=u23552590-5180-4cee-9959-f9a4b44c308&title=&width=610)JDBC是接口，而JDBC驱动才是接口的实现，没有驱动无法完成数据库连接！每个数据库厂商都有自己的驱动，用来连接自己公司的数据库。当然还有第三方公司专门为某一数据库提供驱动，这样的驱动往往不是开源免费的！

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=jfU6l&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

# 模拟JDBC接口
## 接口在开发中的作用
Java中接口的作用主要有以下几个方面：

1. 定义标准：接口可以用于定义标准，规范应该如何完成某个任务或应该具有哪些属性、方法等。 
2. 隐藏实现：接口隔离了类的实现和外界的逻辑使用，使得外部无论是访问接口的常量或是接口的方法都不需要关心接口的实现。 
3. 实现多态：一个类实现多个接口，在实现接口的过程中，类便会具有接口中的所有方法。这样我们就可以在实际应用中方便的实现多态的效果。 
4. 扩展性和灵活性：通过接口可以为项目提供更好的扩展性和灵活性，接口定义了一个共同的标准，使得新的类可以很容易地加入到已有的系统中，而且不需要修改现有的代码。 

总的来说，Java中的接口可以让我们通过规范来编写更加标准和灵活的代码，使得代码易于维护和扩展，并通过多态的特性来提高代码的重用性和可读性。**Java接口在使用场景中，一定是存在两个角色的，一个是接口的调用者，一个是接口的实现者，接口的出现让调用者和实现者解耦合了。**

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=nA5ZY&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## 编写程序模拟JDBC接口
**接口的制定者**：SUN公司负责制定的

```plain
// SUN公司负责制定JDBC接口
public interface JDBC {
    // 负责连接数据库的方法
    void getConnection();
}
```

**接口的实现者**：各大数据库厂商分别对JDBC接口进行实现，实现类被称为**驱动**MySQL数据库厂商对JDBC接口的实现：MySQL驱动

```plain
public class MySQLDriver implements JDBC{
    public void getConnection(){
        System.out.println("与MySQL数据库连接建立成功，您正在操作MySQL数据库");
    }
}
```

Oracle数据库厂商对JDBC接口的实现：Oracle驱动

```plain
public class OracleDriver implements JDBC{
    public void getConnection(){
        System.out.println("与Oracle数据库连接建立成功，您正在操作Oracle数据库");
    }
}
```

**接口的调用者**：要操作数据库的Java程序员（我们）

```plain
public class Client{
    public static void main(String[] args){
        
        JDBC jdbc = new MySQLDriver();
        
        // 只需要面向接口编程即可，不需要关心具体的实现，不需要关心具体是哪个厂商的数据库
        jdbc.getConnection();
    }
}
```

以上是操作MySQL数据库，如果要操作Oracle数据库的话，需要new OracleDriver()：

```plain
public class Client{
    public static void main(String[] args){
        
        JDBC jdbc = new OracleDriver();
        
        // 只需要面向接口编程即可，不需要关心具体的实现，不需要关心具体是哪个厂商的数据库
        jdbc.getConnection();
    }
}
```

可能你会说，最终还是修改了java代码，不符合OCP原则呀，如果你想达到OCP，那可以将创建对象的任务交给反射机制，将类名配置到文件中，例如：配置文件如下：

driver=MySQLDriver

Java代码如下：

```plain
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

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=h2q4g&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

# 配置CLASSPATH
经过上面内容的讲解，大家应该知道JDBC开发有三个角色的参与：

- 我们（对数据库中数据进行增删改查的Java程序员）
- JDBC接口的制定者
- JDBC接口的实现者（驱动）

以上三者凑齐了我们才能进行JDBC的开发。它们三个都在哪里呢？“我们”就不用多说了，写操作数据库的代码就行了。JDBC接口在哪（接口的class文件在哪）？JDBC接口实现类在哪（驱动在哪）？

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=ZFsNv&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## JDBC接口在哪
JDBC接口在JDK中。对应的包是：**java.sql.*;**JDBC API帮助文档就在JDK的帮助文档当中。![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1701939712048-f4487a29-3eb7-494f-b7c0-b72c6c0c03ad.png#averageHue=%23f2f2f2&clientId=u88d51c01-0843-4&from=paste&height=258&id=u2929644e&originHeight=258&originWidth=422&originalType=binary&ratio=1&rotation=0&showTitle=false&size=21472&status=done&style=shadow&taskId=u3924f2fb-b1a5-4961-ae9f-35e5a0fbabb&title=&width=422)![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1701939824373-e1c98bbf-cc6a-44c0-95b6-d2c3a0ecbf52.png#averageHue=%23434541&clientId=u88d51c01-0843-4&from=paste&height=793&id=u969d5906&originHeight=793&originWidth=473&originalType=binary&ratio=1&rotation=0&showTitle=false&size=29261&status=done&style=shadow&taskId=u2686a26a-bd60-4c00-af46-2beeceb81d7&title=&width=473)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=pYLed&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## 驱动在哪
驱动是JDBC接口的实现类，这些实现类是各大数据库厂家自己实现的，所以这些实现类的就需要去数据库厂商相关的网站上下载了。通常这些实现类被全部放到一个xxx.jar包中。下面演示一下mysql的驱动如何下载【下载mysql的驱动jar包】：打开页面：[<font style="color:rgb(65, 131, 196);">https://dev.mysql.com/downloads/connector/j/</font>](https://dev.mysql.com/downloads/connector/j/)![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1701940874635-9b10510f-2f00-4b7e-9b35-36425eaa9457.png#averageHue=%23e2c193&clientId=u88d51c01-0843-4&from=paste&height=839&id=u969fd07e&originHeight=839&originWidth=1118&originalType=binary&ratio=1&rotation=0&showTitle=false&size=85771&status=done&style=shadow&taskId=u4544a600-db3b-4560-a3d2-9dc9cad3730&title=&width=1118)下载后：![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1701940923947-24cc167c-8fc4-4afa-92fd-9fab33ab6226.png#averageHue=%23fbfaf8&clientId=u88d51c01-0843-4&from=paste&height=46&id=u84c583c0&originHeight=46&originWidth=255&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1871&status=done&style=none&taskId=ub85fd9f4-77df-4219-8ae1-9ec14c6d3ab&title=&width=255)解压：![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1701940961500-9a610263-604c-4001-9020-98151a6bfc99.png#averageHue=%23fbf5f3&clientId=u88d51c01-0843-4&from=paste&height=196&id=u4a9d485d&originHeight=196&originWidth=239&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6234&status=done&style=shadow&taskId=u189b1d51-0178-4527-acad-26b527a382c&title=&width=239)上图中的“mysql-connector-j-8.2.0.jar”就是mysql数据库的驱动，8.2.0这个版本适用于目前最新版本的mysql数据库。可以使用解压工具打开这个jar包，看看里面是什么？![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1701941060668-654b02a2-956a-4765-87be-8be10997ce0a.png#averageHue=%23f9f4f1&clientId=u88d51c01-0843-4&from=paste&height=581&id=u4969b92c&originHeight=581&originWidth=451&originalType=binary&ratio=1&rotation=0&showTitle=false&size=25066&status=done&style=shadow&taskId=u4276fdb4-72f6-497c-9a1b-73c4c2a7b57&title=&width=451)可以看到这个jar包中都是xxx.class文件，这就是JDBC接口的实现类。这个jar包就是连接mysql数据库的驱动。如果是oracle的驱动就需要去oracle的官网下载了。这里不再赘述。

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=CqMSe&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## 如果使用文本编辑器开发
如果使用文本编辑器开发，不使用集成开发环境的话，以上的jar包就需要手动配置到环境变量CLASSPATH当中，配置如下：如果jar包放在这里：![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1701941355365-9101c03a-7016-463c-8860-f6cc41745553.png#averageHue=%23faf9f8&clientId=u88d51c01-0843-4&from=paste&height=264&id=ufa86982d&originHeight=264&originWidth=346&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13160&status=done&style=shadow&taskId=uca5f8530-035e-49c4-ba75-c8c6eb426c4&title=&width=346)就需要这样配置环境变量CLASSPATH：![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1701941302115-b531f7d3-3a17-487e-a3fe-7168e4022d40.png#averageHue=%23f0efee&clientId=u88d51c01-0843-4&from=paste&height=177&id=u9af25ce2&originHeight=177&originWidth=651&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8674&status=done&style=shadow&taskId=u1612016b-7741-45d3-bb17-43d00f24f94&title=&width=651)注意配置路径中的当前路径“.”是不能省略的。

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=hmiOT&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## 如果使用IDEA工具开发
如果是采用集成开发工具，例如IDEA，就不需要手动配置CLASSPATH了，只需要将jar包放到IDEA中（实际上放到IDEA工具中的过程就是等同于在配置CLASSPATH）

第一步：创建lib目录，将jar包拷贝到lib目录![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1701941544921-ebd72cf1-b7b1-4474-9044-5d5061e2cb16.png#averageHue=%23ebcca0&clientId=u88d51c01-0843-4&from=paste&height=140&id=ud0a37617&originHeight=140&originWidth=589&originalType=binary&ratio=1&rotation=0&showTitle=false&size=9818&status=done&style=shadow&taskId=u5cb4ad6c-346a-4cd4-b40a-8ecf431c14b&title=&width=589)

<font style="color:rgb(51, 51, 51);">第二步：把lib包引入项目环境</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1701941611962-8afef1cb-645e-4ae2-9c3b-63f374574806.png#averageHue=%23f1f1f1&clientId=u88d51c01-0843-4&from=paste&height=1326&id=u0dd3b46c&originHeight=1326&originWidth=2163&originalType=binary&ratio=1&rotation=0&showTitle=false&size=142476&status=done&style=shadow&taskId=ue03efd37-32eb-49c7-9420-92fae56ef8b&title=&width=2163)<font style="color:rgb(51, 51, 51);">  
</font>

# <font style="color:rgb(51, 51, 51);">JDBC编程六步</font>
<font style="color:rgb(51, 51, 51);">JDBC编程的步骤是很固定的，通常包含以下六步：</font>

- <font style="color:rgb(51, 51, 51);">第一步：注册驱动</font>
    - <font style="color:rgb(51, 51, 51);">作用一：将 JDBC 驱动程序从硬盘上的文件系统中加载到内存中。</font>
    - <font style="color:rgb(51, 51, 51);">作用二：使得 DriverManager 可以通过一个统一的接口来管理该驱动程序的所有连接操作。</font>
- <font style="color:rgb(51, 51, 51);">第二步：获取数据库连接</font>
    - <font style="color:rgb(51, 51, 51);">获取java.sql.Connection对象，该对象的创建标志着mysql进程和jvm进程之间的通道打开了。</font>
- <font style="color:rgb(51, 51, 51);">第三步：获取数据库操作对象</font>
    - <font style="color:rgb(51, 51, 51);">获取java.sql.Statement对象，该对象负责将SQL语句发送给数据库，数据库负责执行该SQL语句。</font>
- <font style="color:rgb(51, 51, 51);">第四步：执行SQL语句</font>
    - <font style="color:rgb(51, 51, 51);">执行具体的SQL语句，例如：insert delete update select等。</font>
- <font style="color:rgb(51, 51, 51);">第五步：处理查询结果集</font>
    - <font style="color:rgb(51, 51, 51);">如果之前的操作是DQL查询语句，才会有处理查询结果集这一步。</font>
    - <font style="color:rgb(51, 51, 51);">执行DQL语句通常会返回查询结果集对象：java.sql.ResultSet。</font>
    - <font style="color:rgb(51, 51, 51);">对于ResultSet查询结果集来说，通常的操作是针对查询结果集进行结果集的遍历。</font>
- <font style="color:rgb(51, 51, 51);">第六步：释放资源</font>
    - <font style="color:rgb(51, 51, 51);">释放资源可以避免资源的浪费。在 JDBC 编程中，每次使用完 Connection、Statement、ResultSet 等资源后，都需要显式地调用对应的 close() 方法来释放资源，避免资源的浪费。</font>
    - <font style="color:rgb(51, 51, 51);">释放资源可以避免出现内存泄露问题。在 Java 中，当一个对象不再被引用时，会被 JVM 的垃圾回收机制进行回收。但是在 JDBC 编程中，如果不显式地释放资源，那么这些资源就不会被 JVM 的垃圾回收机制自动回收，从而导致内存泄露问题。</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=acVGP&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

# <font style="color:rgb(51, 51, 51);">数据的准备</font>
<font style="color:rgb(51, 51, 51);">使用PowerDesigner设计用户表t_user。</font><font style="color:rgb(51, 51, 51);">使用Navicat for MySQL创建数据库，创建表，插入数据。</font>

## <font style="color:rgb(51, 51, 51);">PowerDesigner与Navicat for MySQL的区别</font>
<font style="color:rgb(51, 51, 51);">Navicat for MySQL 是一款常用的 MySQL 数据库管理工具，提供了丰富的数据库管理和开发工具，可以方便地进行数据库的连接、查询、管理、模型设计等操作，是 MySQL 开发和管理的效率工具。</font>

<font style="color:rgb(51, 51, 51);">而 PowerDesigner 工具则是一款专业的建模工具，它支持多种数据库和操作系统，可以完成数据库设计、数据建模、过程建模、企业业务建模等工作。PowerDesigner 可以帮助开发人员在数据库设计和开发过程中更好地理解和管理数据，便于协同开发和项目管理。各种数据库技术的建模形式都可以实现，有单个数据库建模到多个数据库建模和业务建模等高级功能，</font>**<font style="color:rgb(51, 51, 51);">非常适用于大型项目中的数据库设计和建模</font>**<font style="color:rgb(51, 51, 51);">。同时，PowerDesigner 还支持 UML，Java 等编程语言的建模，可以与开发语言无缝整合。</font>

<font style="color:rgb(51, 51, 51);">因此，Navicat for MySQL 和 PowerDesigner 的功能是不同的，可以根据实际需要来选用。如果只是针对 MySQL 的数据库连接、查询、管理等操作，可以使用 Navicat for MySQL 工具，而如果需要进行更复杂的数据库设计、建模和整合等工作，可以使用 PowerDesigner 工具来实现。</font>**<font style="color:rgb(51, 51, 51);">如果使用 MySQL 数据库进行开发，使用 Navicat for MySQL 和 PowerDesigner 这两个工具相互配合，可以提高开发效率和数据管理质量</font>**<font style="color:rgb(51, 51, 51);">。</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=sjA9p&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## <font style="color:rgb(51, 51, 51);">PowerDesigner工具的安装</font>
<font style="color:rgb(51, 51, 51);">来这里下载该工具：链接：</font>[<font style="color:rgb(65, 131, 196);">https://pan.baidu.com/s/1lRWC069K8GE-8rxr259ArQ?pwd=2009</font>](https://pan.baidu.com/s/1lRWC069K8GE-8rxr259ArQ?pwd=2009)<font style="color:rgb(51, 51, 51);"> 提取码：2009</font><font style="color:rgb(51, 51, 51);">双击安装包：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702030113007-3188761c-a3d6-43af-a7b2-b57285c5c59a.png#averageHue=%23caa664&clientId=u41c620b2-0cdd-4&from=paste&height=89&id=u4dcad848&originHeight=89&originWidth=241&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4195&status=done&style=none&taskId=u657aab7b-28bf-4a16-81ff-d15de5e203f&title=&width=241)![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702029876181-f1cae0c3-56a7-4925-add3-c2cac74f64bf.png#averageHue=%239fa909&clientId=u41c620b2-0cdd-4&from=paste&height=330&id=uf0bf2c52&originHeight=330&originWidth=500&originalType=binary&ratio=1&rotation=0&showTitle=false&size=31259&status=done&style=none&taskId=u339e35b0-277e-4cfd-8c81-47d598a01e8&title=&width=500)

<font style="color:rgb(51, 51, 51);">欢迎页：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702029889827-2e2c12d2-0ef0-400a-8a97-a4e094846227.png#averageHue=%23ecede1&clientId=u41c620b2-0cdd-4&from=paste&height=525&id=uab8659b9&originHeight=525&originWidth=696&originalType=binary&ratio=1&rotation=0&showTitle=false&size=23274&status=done&style=none&taskId=u78a92258-d072-4912-b0bf-89834c775bf&title=&width=696)

<font style="color:rgb(51, 51, 51);">选择试用15天：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702029931270-dd2984c0-7154-4681-aeb7-daff6743770b.png#averageHue=%23eaebdf&clientId=u41c620b2-0cdd-4&from=paste&height=525&id=ub0329bed&originHeight=525&originWidth=696&originalType=binary&ratio=1&rotation=0&showTitle=false&size=25889&status=done&style=none&taskId=uf3020af3-ca64-4686-8f8a-4b68ad5061a&title=&width=696)

<font style="color:rgb(51, 51, 51);">选择香港，以及接受：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702029963307-ce94dc0e-631e-4fdd-bfab-cee55e430f2c.png#averageHue=%23e4e4da&clientId=u41c620b2-0cdd-4&from=paste&height=514&id=ud1e27d6f&originHeight=514&originWidth=687&originalType=binary&ratio=1&rotation=0&showTitle=false&size=33479&status=done&style=none&taskId=u78eac6e6-db27-4b6a-996e-ef3a76951e3&title=&width=687)

<font style="color:rgb(51, 51, 51);">设置安装位置：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702029981376-3f82d441-4b51-4ca0-9183-cb7b8853369b.png#averageHue=%23ebebdf&clientId=u41c620b2-0cdd-4&from=paste&height=525&id=uf22c8884&originHeight=525&originWidth=696&originalType=binary&ratio=1&rotation=0&showTitle=false&size=25256&status=done&style=none&taskId=u4463e38b-dd51-4a55-8c11-7c0c937df49&title=&width=696)

<font style="color:rgb(51, 51, 51);">选择你要安装的（默认就行）：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702029994216-fa2e7123-ebb3-4e24-8a54-f70136665809.png#averageHue=%23e8e9dc&clientId=u41c620b2-0cdd-4&from=paste&height=525&id=uafed6552&originHeight=525&originWidth=696&originalType=binary&ratio=1&rotation=0&showTitle=false&size=33295&status=done&style=none&taskId=u24f0bc15-4a74-49be-a870-85b0660f508&title=&width=696)

<font style="color:rgb(51, 51, 51);">选择要安装的用户配置文件（默认即可）：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702030015551-fb222d28-373c-4620-8cb7-119a796c73b6.png#averageHue=%23ecede0&clientId=u41c620b2-0cdd-4&from=paste&height=525&id=ude3902f0&originHeight=525&originWidth=696&originalType=binary&ratio=1&rotation=0&showTitle=false&size=27364&status=done&style=none&taskId=u8b82d675-f2b3-4bec-b214-d8b76daefb2&title=&width=696)

<font style="color:rgb(51, 51, 51);">添加图标：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702030025893-0f3ccf82-2edf-4693-b40d-cdbd9b067808.png#averageHue=%23edede1&clientId=u41c620b2-0cdd-4&from=paste&height=525&id=u94d15691&originHeight=525&originWidth=696&originalType=binary&ratio=1&rotation=0&showTitle=false&size=29416&status=done&style=none&taskId=ue484533f-1bfe-453c-9089-b6a2b29a23b&title=&width=696)

<font style="color:rgb(51, 51, 51);">安装概览信息：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702030036757-b9429e96-81b1-4dcd-93d5-9eb30d61f24e.png#averageHue=%23e7e8db&clientId=u41c620b2-0cdd-4&from=paste&height=525&id=ud58cceb3&originHeight=525&originWidth=696&originalType=binary&ratio=1&rotation=0&showTitle=false&size=27404&status=done&style=none&taskId=u9c622da3-fd6a-4b6b-8c85-a44e8bc2c3d&title=&width=696)

<font style="color:rgb(51, 51, 51);">安装中：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702030046163-e5983393-f38e-4c56-93cb-8e0da0a5cb0a.png#averageHue=%23ecedde&clientId=u41c620b2-0cdd-4&from=paste&height=525&id=u45648fd0&originHeight=525&originWidth=696&originalType=binary&ratio=1&rotation=0&showTitle=false&size=22485&status=done&style=none&taskId=ufbf24086-f1b5-4244-a2a7-848863719d4&title=&width=696)

<font style="color:rgb(51, 51, 51);">安装完成：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702030092155-4ca5bf85-47ed-4398-98a5-864761106ce3.png#averageHue=%23edede1&clientId=u41c620b2-0cdd-4&from=paste&height=525&id=u0342f890&originHeight=525&originWidth=696&originalType=binary&ratio=1&rotation=0&showTitle=false&size=22667&status=done&style=none&taskId=u008adc77-0a9c-4568-8464-0ac79055972&title=&width=696)

<font style="color:rgb(51, 51, 51);">如何破解？看到这个文件了吗？</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702030298080-4c0ab7e6-b191-4778-95ae-bd7a23bf4276.png#averageHue=%23d2b379&clientId=u41c620b2-0cdd-4&from=paste&height=80&id=u0b68889c&originHeight=80&originWidth=244&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4023&status=done&style=none&taskId=u9ba52cda-36f3-407d-9aaf-74fa31a4ff5&title=&width=244)<font style="color:rgb(51, 51, 51);">把这个文件拷贝到这个安装目录当中：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702030371606-59034062-2a4d-46c5-80f2-9704563052b7.png#averageHue=%23fcfbf9&clientId=u41c620b2-0cdd-4&from=paste&height=164&id=ud8adf181&originHeight=164&originWidth=608&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13719&status=done&style=none&taskId=u0d3a7ce0-d257-4292-931a-4291eeb1b26&title=&width=608)<font style="color:rgb(51, 51, 51);">会自动提醒你替换：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702030421073-75504dc7-d035-488c-ba8d-7442f32f00d9.png#averageHue=%23f7f6f5&clientId=u41c620b2-0cdd-4&from=paste&height=294&id=u274a8627&originHeight=294&originWidth=463&originalType=binary&ratio=1&rotation=0&showTitle=false&size=18633&status=done&style=none&taskId=uf6bd0f75-2a3c-4cdc-9999-df7f9ea092d&title=&width=463)<font style="color:rgb(51, 51, 51);">替换即可完成破解！！！！</font>![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=l2blg&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## <font style="color:rgb(51, 51, 51);">使用PowerDesigner进行物理数据建模</font>
<font style="color:rgb(51, 51, 51);">打开PowerDesigner：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702352345350-1c1441c3-560f-4485-ba11-aff5522c7d42.png#averageHue=%239ec58f&clientId=u0cd9c8dc-062f-4&from=paste&height=694&id=u62d067c3&originHeight=694&originWidth=964&originalType=binary&ratio=1&rotation=0&showTitle=false&size=246317&status=done&style=shadow&taskId=u188417d2-31ad-44c7-b177-094b4303fc0&title=&width=964)

<font style="color:rgb(51, 51, 51);">点击“Create Model...”来创建PDM（Physical Data Model，物理数据模型）：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702352495755-cdb4ac5b-cdf4-408f-b87c-6f08208eadb8.png#averageHue=%23f1f0ef&clientId=u0cd9c8dc-062f-4&from=paste&height=693&id=ud8fcd53d&originHeight=693&originWidth=963&originalType=binary&ratio=1&rotation=0&showTitle=false&size=83783&status=done&style=none&taskId=u265fe6c8-c8b6-4f39-9dbc-2ba19711344&title=&width=963)![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=xyQoq&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)**<font style="color:rgb(51, 51, 51);">什么是物理数据模型PDM？</font>**`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">物理数据模型（Physical Data Model，PDM）是数据管理领域中表示数据库逻辑设计后，通过物理设计最终转化为实际数据结构的过程，即在逻辑模型的基础上，进行数据存储结构的设计。PDM 是一个详细的数据库设计计划，它描述了如何在关系数据库中存储数据。物理数据模型包含了所有数据表，列、键和索引以及物理存储的详细信息，包括数据类型、字段宽度、默认值、统计信息等。此外，PDM 还描述了如何将数据表存储在文件或表空间中，这些信息可以帮助开发人员建立实际的数据库系统。通常，PDM 包含了完整的 ER 模型，数据表和关系的详细信息，包括数据的主键、外键、唯一键、索引、约束条件等。物理数据模型可以使用各种建模工具来手工创建或自动生成。在数据库设计阶段，生成 PDM 是非常重要的一步，是将逻辑设计转换为实际实现的重要步骤之一。它可以帮助开发人员在实现时更加清晰地了解数据的存储结构，同时也方便后续的数据库管理和维护工作。</font>`

<font style="color:rgb(51, 51, 51);">创建完成后是这样的：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702352840475-faf7c39e-6a3e-4d72-872b-1de849baf668.png#averageHue=%23f0f0ef&clientId=u0cd9c8dc-062f-4&from=paste&height=331&id=u2e5d668a&originHeight=331&originWidth=843&originalType=binary&ratio=1&rotation=0&showTitle=false&size=35414&status=done&style=none&taskId=u6d34e397-b10c-4c92-8e2e-82c926f7d40&title=&width=843)<font style="color:rgb(51, 51, 51);">注意：右侧的小格子是可以放大和缩小的。看着像是很大的一张网。在每个格子当中可以容纳多个表。并且在这张网上可以清晰的看到表与表的关系。（一对多，一对一，多对多等。）</font>

<font style="color:rgb(51, 51, 51);">记得保存，ctrl+s保存时会生成一个xxx.pdm文件，以后如果要修改设计，双击这个xxx.pdm文件即可打开，进行编辑：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702353117948-32a0da6b-393c-4282-a2b0-d2e893d7d04b.png#averageHue=%23f4f3f1&clientId=u0cd9c8dc-062f-4&from=paste&height=423&id=u33b947b9&originHeight=423&originWidth=553&originalType=binary&ratio=1&rotation=0&showTitle=false&size=29718&status=done&style=none&taskId=uc05f19a2-26bf-4720-bd21-db4d30c3125&title=&width=553)<font style="color:rgb(51, 51, 51);">保存后的文件：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702353151163-22027c70-a1cc-463a-835e-30b23631ddf6.png#averageHue=%23383c95&clientId=u0cd9c8dc-062f-4&from=paste&height=88&id=u81c8d25f&originHeight=88&originWidth=82&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5944&status=done&style=none&taskId=u69e2e523-6384-4974-9bd9-b39ceed8c0d&title=&width=82)

<font style="color:rgb(51, 51, 51);">开始进行表的设计，这里不搞那么复杂，先创建一张表即可：t_user，用户表：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702353507900-d3538143-07a6-4a08-b69e-4d7c23f1d6e3.png#averageHue=%23e4ded3&clientId=u0cd9c8dc-062f-4&from=paste&height=292&id=uc0708eab&originHeight=292&originWidth=580&originalType=binary&ratio=1&rotation=0&showTitle=false&size=21497&status=done&style=none&taskId=u37987bcd-cc58-4272-9158-47add73ca55&title=&width=580)

<font style="color:rgb(51, 51, 51);">双击后，弹出设计窗口：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702353664176-dbbccc05-2711-4e31-b6fc-4cf6238bacea.png#averageHue=%23f6f5f5&clientId=u0cd9c8dc-062f-4&from=paste&height=593&id=ucdbe63e9&originHeight=593&originWidth=1093&originalType=binary&ratio=1&rotation=0&showTitle=false&size=33708&status=done&style=shadow&taskId=u5d1fdc0d-9fda-4133-a7da-91b18ffb6d6&title=&width=1093)

<font style="color:rgb(51, 51, 51);">设计表名：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702354144428-887e8efb-c136-42e4-90de-4ec26815ab6f.png#averageHue=%23f5f5f4&clientId=u0cd9c8dc-062f-4&from=paste&height=445&id=ufd3ac07c&originHeight=445&originWidth=1068&originalType=binary&ratio=1&rotation=0&showTitle=false&size=22473&status=done&style=none&taskId=u0fd54ac3-7fba-48bf-87d0-6eb844decba&title=&width=1068)<font style="color:rgb(51, 51, 51);">注意：</font>

1. <font style="color:rgb(51, 51, 51);">Name：用来设置显示的表名</font>
2. <font style="color:rgb(51, 51, 51);">Code：用来设置数据库中真实创建的表名</font>
3. <font style="color:rgb(51, 51, 51);">Comment：对表的注释说明</font>

<font style="color:rgb(51, 51, 51);">设计字段：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702356255883-27bed5c1-8cb5-41ed-ac06-d2a479327a93.png#averageHue=%23eceaea&clientId=u0cd9c8dc-062f-4&from=paste&height=726&id=ud50f83d4&originHeight=726&originWidth=1171&originalType=binary&ratio=1&rotation=0&showTitle=false&size=90439&status=done&style=shadow&taskId=u48387018-6792-4aa3-89c4-5fc6b175d4e&title=&width=1171)<font style="color:rgb(51, 51, 51);">把每个字段设计好，包括：字段名，数据类型，长度，约束等。</font>

<font style="color:rgb(51, 51, 51);">设计完成后：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702356365447-df18d670-da99-40f0-b80f-95918bdf20f6.png#averageHue=%23dee8f2&clientId=u0cd9c8dc-062f-4&from=paste&height=189&id=u223a5402&originHeight=189&originWidth=348&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10585&status=done&style=none&taskId=u6394b4c2-2385-400d-9a4a-b5ad2483556&title=&width=348)![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=KAK8Q&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## <font style="color:rgb(51, 51, 51);">使用PowerDesigner导出建表语句</font>
![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702356449130-0ab2e139-0029-4db4-a89d-c4d46ca800e4.png#averageHue=%23f5f4f4&clientId=u0cd9c8dc-062f-4&from=paste&height=663&id=u93450af9&originHeight=663&originWidth=1088&originalType=binary&ratio=1&rotation=0&showTitle=false&size=49050&status=done&style=shadow&taskId=u551f93ed-f4ad-4e51-b667-2fc25c38dbd&title=&width=1088)

```plain
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

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=TuLZs&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## <font style="color:rgb(51, 51, 51);">使用Navicat for MySQL初始化数据</font>
### <font style="color:rgb(51, 51, 51);">建库</font>
<font style="color:rgb(51, 51, 51);">使用Navicat for MySQL创建一个MySQL数据库，起名：jdbc</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702356898211-79878d20-d32a-4764-b2d9-fa7de3c24053.png#averageHue=%23f0eeed&clientId=u0cd9c8dc-062f-4&from=paste&height=487&id=ub2f26cb2&originHeight=487&originWidth=293&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24944&status=done&style=none&taskId=u71f5ac6e-a9cc-4a75-b621-4f724c14131&title=&width=293)![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702356942314-e5cb2d8a-3e9c-46b4-91b6-6ab59e7fbb0a.png#averageHue=%23f9f8f8&clientId=u0cd9c8dc-062f-4&from=paste&height=390&id=u4f4cc83e&originHeight=390&originWidth=438&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10115&status=done&style=none&taskId=u51c78507-6467-4fce-ae75-1c842cebf05&title=&width=438)![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=rkEnP&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

### <font style="color:rgb(51, 51, 51);">建表</font>
<font style="color:rgb(51, 51, 51);">执行jdbc.sql脚本：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702357035951-94877536-4153-4399-a6ae-9672bf97e062.png#averageHue=%23f0edeb&clientId=u0cd9c8dc-062f-4&from=paste&height=374&id=u41c592a0&originHeight=374&originWidth=293&originalType=binary&ratio=1&rotation=0&showTitle=false&size=21222&status=done&style=shadow&taskId=u6da02b5b-0bc8-49b2-88a1-806cbe27063&title=&width=293)![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702357083312-51eff97d-6686-4559-b15b-5069e5ed60ba.png#averageHue=%23f7f7f6&clientId=u0cd9c8dc-062f-4&from=paste&height=392&id=ued9efd1d&originHeight=392&originWidth=561&originalType=binary&ratio=1&rotation=0&showTitle=false&size=14995&status=done&style=shadow&taskId=u60682216-3bf0-4eda-9e71-9fb70795456&title=&width=561)

<font style="color:rgb(51, 51, 51);">最终创建的表：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702357196196-5a9db89b-b896-4bf0-88bb-c4d5aabd411b.png#averageHue=%23f6f6f5&clientId=u0cd9c8dc-062f-4&from=paste&height=284&id=ua74bad36&originHeight=284&originWidth=863&originalType=binary&ratio=1&rotation=0&showTitle=false&size=22932&status=done&style=shadow&taskId=u14f0bfdf-c432-4493-a95c-d82bea257b9&title=&width=863)![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=hmdt2&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

### <font style="color:rgb(51, 51, 51);">插入数据</font>
![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702357446508-4d4cdf35-d996-4fa2-b823-afe81b1e9c50.png#averageHue=%23f3f2f0&clientId=u0cd9c8dc-062f-4&from=paste&height=190&id=uf0f4611c&originHeight=190&originWidth=579&originalType=binary&ratio=1&rotation=0&showTitle=false&size=18948&status=done&style=shadow&taskId=u4c353718-bc1f-4e17-ae48-47401a0371d&title=&width=579)<font style="color:rgb(51, 51, 51);">注意：这里我将主键设置为了自增：auto_increment。其实这个也可以在PowerDesigner中设计时指定自增：勾选上它即可。</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702357560943-84503c36-4205-42bc-b488-6cca2f4dd16c.png#averageHue=%23f3f2f1&clientId=u0cd9c8dc-062f-4&from=paste&height=444&id=ude5a2110&originHeight=444&originWidth=540&originalType=binary&ratio=1&rotation=0&showTitle=false&size=23459&status=done&style=shadow&taskId=u795b2b6b-d5a5-40bc-a0a4-7672112dd8a&title=&width=540)![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=jb3Sy&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

# <font style="color:rgb(51, 51, 51);">JDBC完成新增操作</font>
<font style="color:rgb(51, 51, 51);">新增操作就是让数据库执行insert语句。通过这个操作来学习一下JDBC编程的每一步。刚开始编写JDBC代码的时候，建议使用文本编辑器，先不借助任何IDE。</font>

## <font style="color:rgb(51, 51, 51);">JDBC编程第一步：注册驱动</font>
<font style="color:rgb(51, 51, 51);">注册驱动有两个作用：</font>

1. <font style="color:rgb(51, 51, 51);">将 JDBC 驱动程序从硬盘上的文件系统中加载到内存。</font>
2. <font style="color:rgb(51, 51, 51);">让 DriverManager 可以通过一个统一的接口来管理该驱动程序的所有连接操作。</font>

<font style="color:rgb(51, 51, 51);">API帮助文档：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702375429683-7a25727f-4615-45f1-a56c-fd02eea60dd2.png#averageHue=%23fcfafa&clientId=u0cd9c8dc-062f-4&from=paste&height=276&id=uef30ca2c&originHeight=276&originWidth=606&originalType=binary&ratio=1&rotation=0&showTitle=false&size=23402&status=done&style=none&taskId=u9c2d9a52-6ae6-4a6e-abbf-d7c70b7909d&title=&width=606)

<font style="color:rgb(51, 51, 51);">代码如下：</font>

```plain
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

**<font style="color:rgb(51, 51, 51);">注意：注册驱动调用的是java.sql.DriverManager的registerDriver()方法。这些方法的使用要参阅JDK的API帮助文档。</font>****<font style="color:rgb(51, 51, 51);">思考1：为什么以上代码中new的时候，后面类名要带上包名呢？</font>****<font style="color:rgb(51, 51, 51);">思考2：以上代码中哪些是JDBC接口，哪些是JDBC接口的实现？</font>**![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=OJfIb&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## <font style="color:rgb(51, 51, 51);">JDBC编程第二步：获取连接</font>
<font style="color:rgb(51, 51, 51);">获取java.sql.Connection对象，该对象的创建标志着mysql进程和jvm进程之间的通道打开了。</font>

### <font style="color:rgb(51, 51, 51);">代码实现</font>
<font style="color:rgb(51, 51, 51);">API帮助文档：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702375535525-fad3b7e2-b7f5-4079-a2e1-31c597ae8165.png#averageHue=%23fcfbfb&clientId=u0cd9c8dc-062f-4&from=paste&height=449&id=u2c3fe33b&originHeight=449&originWidth=1601&originalType=binary&ratio=1&rotation=0&showTitle=false&size=53968&status=done&style=shadow&taskId=uc413cfe1-b449-46ca-9a38-3d0558c326b&title=&width=1601)

<font style="color:rgb(51, 51, 51);">代码如下：</font>

```plain
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

<font style="color:rgb(51, 51, 51);">执行结果如下：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702372789612-ac3b38a8-6f6d-44f2-8024-ccab0bac9380.png#averageHue=%23131110&clientId=u0cd9c8dc-062f-4&from=paste&height=71&id=u0eeaddfb&originHeight=71&originWidth=655&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8565&status=done&style=none&taskId=u2a5da5f4-1a21-4311-b1bd-7dd3561d11b&title=&width=655)<font style="color:rgb(51, 51, 51);">看到以上的输出结果，表示数据库已经连接成功了。</font>

<font style="color:rgb(51, 51, 51);">通过以上程序的输出结果得知：com.mysql.cj.jdbc.ConnectionImpl是java.sql.Connection接口的实现类，大家可以想象一下，如果换成Oracle数据库的话，这个实现类的类名是不是就会换一个呢？答案是肯定的。不过对于我们来说是不需要关心具体实现类的，因为后续的代码都是直接面向java.sql.Connection接口来调用方法的。面向接口编程在这里体现的淋漓尽致。确实降低了耦合度。</font>

<font style="color:rgb(51, 51, 51);">以上程序中演示了连接数据库需要提供三个信息：url，用户名，密码。其中用户名和密码容易理解。url是什么？</font>![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=s9plF&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

### <font style="color:rgb(51, 51, 51);">什么是URL</font>
<font style="color:rgb(51, 51, 51);">URL 是统一资源定位符 (Uniform Resource Locator) 的缩写，是互联网上标识、定位、访问资源的字符串。它可以用来指定互联网上各种类型的资源的位置，如网页、图片、视频等。</font>

<font style="color:rgb(51, 51, 51);">URL 通常由协议、服务器名、服务器端口、路径和查询字符串组成。其中：</font>

- <font style="color:rgb(51, 51, 51);">协议是规定了访问资源所采用的通信协议，例如 HTTP、HTTPS、FTP 等；</font>
- <font style="color:rgb(51, 51, 51);">服务器名是资源所在的服务器主机名或 IP 地址，可以是域名或 IP 地址；</font>
- <font style="color:rgb(51, 51, 51);">服务器端口是资源所在的服务器的端口号；</font>
- <font style="color:rgb(51, 51, 51);">路径是资源所在的服务器上的路径、文件名等信息；</font>
- <font style="color:rgb(51, 51, 51);">查询字符串是向服务器提交的参数信息，用来定位更具体的资源。</font>

<font style="color:rgb(51, 51, 51);">URL 在互联网中广泛应用，比如在浏览器中输入 URL 来访问网页或下载文件，在网站开发中使用 URL 来访问 API 接口或文件，在移动应用和桌面应用中使用 URL 来访问应用内部的页面或功能，在搜索引擎中使用 URL 来爬取网页内容等等。</font>

<font style="color:rgb(51, 51, 51);">总之，URL 是互联网上所有资源的唯一识别标识，是互联网通信的基础和核心技术之一。</font>![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=Uy1MQ&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

### <font style="color:rgb(51, 51, 51);">JDBC连接MySQL时的URL格式</font>
<font style="color:rgb(51, 51, 51);">JDBC URL 是在使用 JDBC 连接数据库时的一个 URL 字符串，它用来标识要连接的数据库的位置、认证信息和其他配置参数等。JDBC URL 的格式可以因数据库类型而异，但通常包括以下几个部分：</font>

- <font style="color:rgb(51, 51, 51);">协议：表示要使用的数据库管理系统（DBMS）的类型，如 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">jdbc:mysql</font>`<font style="color:rgb(51, 51, 51);"> 表示要使用 MySQL 数据库，</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">jdbc:postgresql</font>`<font style="color:rgb(51, 51, 51);"> 表示要使用 PostgreSQL 数据库。</font>
- <font style="color:rgb(51, 51, 51);">主机地址和端口号：表示要连接的数据库所在的服务器的 IP 地址或域名，以及数据库所在服务器监听的端口号。</font>
- <font style="color:rgb(51, 51, 51);">数据库名称：表示要连接的数据库的名称。</font>
- <font style="color:rgb(51, 51, 51);">其他可选参数：这些参数包括连接的超时时间、使用的字符集、连接池相关配置等。</font>

<font style="color:rgb(51, 51, 51);">例如，连接 MySQL 数据库的 JDBC URL 的格式一般如下：</font>

<font style="color:rgb(51, 51, 51);">jdbc:mysql://<host>:<port>/<database_name>?<connection_parameters></font>

<font style="color:rgb(51, 51, 51);">其中：</font>

- `<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);"><host></font>`<font style="color:rgb(51, 51, 51);"> 是 MySQL 数据库服务器的主机名或 IP 地址；</font>
- `<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);"><port></font>`<font style="color:rgb(51, 51, 51);"> 是 MySQL 服务器的端口号（默认为 3306）；</font>
- `<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);"><database_name></font>`<font style="color:rgb(51, 51, 51);"> 是要连接的数据库名称；</font>
- `<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);"><connection_parameters></font>`<font style="color:rgb(51, 51, 51);"> 包括连接的额外参数，例如用户名、密码、字符集等。</font>

<font style="color:rgb(51, 51, 51);">JDBC URL 是连接数据库的关键，通过 JDBC URL，应用程序可以通过特定的 JDBC 驱动程序与数据库服务器进行通信，从而实现与数据库的交互。在开发 Web 应用和桌面应用时，使用 JDBC URL 可以轻松地连接和操作各种类型的数据库，例如 MySQL、PostgreSQL、Oracle 等。</font>

<font style="color:rgb(51, 51, 51);">以下是一个常见的JDBC MySQL URL：</font>

<font style="color:rgb(51, 51, 51);">jdbc:mysql://localhost:3306/jdbc</font>

`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">jdbc:mysql://</font>`<font style="color:rgb(51, 51, 51);">是协议</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">localhost</font>`<font style="color:rgb(51, 51, 51);">表示连接本地主机的MySQL数据库，也可以写作</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">127.0.0.1</font>``<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">3306</font>`<font style="color:rgb(51, 51, 51);">是MySQL数据库的端口号</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">jdbc</font>`<font style="color:rgb(51, 51, 51);">是数据库实例名</font>![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=LELJD&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

### <font style="color:rgb(51, 51, 51);">MySQL URL中的其它常用配置</font>
<font style="color:rgb(51, 51, 51);">在 JDBC MySQL URL 中，常用的配置参数有：</font>

- `<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">serverTimezone</font>`<font style="color:rgb(51, 51, 51);">：MySQL 服务器时区，默认为 UTC，可以通过该参数来指定客户端和服务器的时区；</font>

<font style="color:rgb(51, 51, 51);">在 JDBC URL 中设置 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">serverTimezone</font>`<font style="color:rgb(51, 51, 51);"> 的作用是指定数据库服务器的时区。这个时区信息会影响 JDBC 驱动在处理日期时间相关数据类型时如何将其映射到服务器上的日期时间值。</font><font style="color:rgb(51, 51, 51);">如果不设置 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">serverTimezone</font>`<font style="color:rgb(51, 51, 51);">，则 JDBC 驱动程序默认将使用本地时区，也就是客户端机器上的系统时区，来处理日期时间数据。在这种情况下，如果服务器的时区和客户端机器的时区不同，那么处理日期时间数据时可能会出现问题，从而导致数据错误或不一致。</font><font style="color:rgb(51, 51, 51);">例如，假设服务器位于美国加州，而客户端位于中国上海，如果不设置 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">serverTimezone</font>`<font style="color:rgb(51, 51, 51);"> 参数，在客户端执行类似下面的查询：</font>

<font style="color:rgb(51, 51, 51);">SELECT * FROM orders WHERE order_date = '2022-11-11';</font>

<font style="color:rgb(51, 51, 51);">由于客户端和服务器使用了不同的时区，默认使用的是客户端本地的时区，那么实际查询的时间就是客户端本地时间对应的时间，而不是服务器的时间。这可能会导致查询结果不正确，因为服务器上的时间可能是比客户端慢或者快了多个小时。</font><font style="color:rgb(51, 51, 51);">通过在 JDBC URL 中设置 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">serverTimezone</font>`<font style="color:rgb(51, 51, 51);"> 参数，可以明确告诉 JDBC 驱动程序使用哪个时区来处理日期时间值，从而避免这种问题。在上述例子中，如果把时区设置为 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">America/Los_Angeles</font>`<font style="color:rgb(51, 51, 51);">（即加州的时区）：</font>

<font style="color:rgb(51, 51, 51);">jdbc:mysql://localhost:3306/mydatabase?user=myusername&password=mypassword&serverTimezone=America/Los_Angeles</font>

<font style="color:rgb(51, 51, 51);">那么上面的查询就会在数据库服务器上以加州的时间来执行，结果更加准确。</font>

- `<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">useSSL</font>`<font style="color:rgb(51, 51, 51);">：是否使用 SSL 进行连接，默认为 true；</font>

`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">useSSL</font>`<font style="color:rgb(51, 51, 51);"> 参数用于配置是否使用 SSL（Secure Sockets Layer）安全传输协议来加密 JDBC 和 MySQL 数据库服务器之间的通信。其设置为 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">true</font>`<font style="color:rgb(51, 51, 51);"> 表示使用 SSL 连接，设置为 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">false</font>`<font style="color:rgb(51, 51, 51);"> 表示不使用 SSL 连接。其区别如下：</font><font style="color:rgb(51, 51, 51);">当设置为 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">true</font>`<font style="color:rgb(51, 51, 51);"> 时，JDBC 驱动程序将使用 SSL 加密协议来保障客户端和服务器之间的通信安全。这种方式下，所有数据都会使用 SSL 加密后再传输，可以有效防止数据在传输过程中被窃听、篡改等安全问题出现。当然，也要求服务器端必须支持 SSL，否则会连接失败。</font><font style="color:rgb(51, 51, 51);">当设置为 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">false</font>`<font style="color:rgb(51, 51, 51);"> 时，JDBC 驱动程序会以明文方式传输数据，这种方式下，虽然数据传输的速度会更快，但也会存在被恶意攻击者截获和窃听数据的风险。因此，在不安全的网络环境下，或是要求数据传输安全性较高的情况下，建议使用 SSL 加密连接。</font><font style="color:rgb(51, 51, 51);">需要注意的是，使用 SSL 连接会对系统资源和性能消耗有一定的影响，特别是当连接数较多时，对 CPU 和内存压力都比较大。因此，在性能和安全之间需要权衡，根据实际应用场景合理设置 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">useSSL</font>`<font style="color:rgb(51, 51, 51);"> 参数。</font>

- <font style="color:rgb(51, 51, 51);">useUnicode：是否使用Unicode编码进行数据传输，默认是true启用</font>

`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">useUnicode</font>`<font style="color:rgb(51, 51, 51);">是 JDBC 驱动程序连接数据库时的一个参数，用于告诉驱动程序在传输数据时是否使用 Unicode 编码。Unicode 是计算机科学中的一种字符编码方案，可以用于表示全球各种语言中的字符，包括 ASCII 码、中文、日文、韩文等。因此，使用 Unicode 编码可以确保数据在传输过程中能够正确、完整地呈现各种语言的字符。</font><font style="color:rgb(51, 51, 51);">具体地说，如果设置 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">useUnicode=true</font>`<font style="color:rgb(51, 51, 51);">，JDBC 驱动程序会在传输数据时使用 Unicode 编码。这意味着，无论数据源中使用的是什么编码方案，都会先将数据转换为 Unicode 编码进行传输，确保数据能够跨平台、跨数据库正确传输。当从数据库中获取数据时，驱动程序会根据 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">characterEncoding</font>`<font style="color:rgb(51, 51, 51);"> 参数指定的字符集编码将数据转换为指定编码格式，以便应用程序正确处理数据。</font><font style="color:rgb(51, 51, 51);">需要注意的是，如果设置 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">useUnicode=false</font>`<font style="color:rgb(51, 51, 51);">，则表示使用当前平台默认的字符集进行数据传输。这可能会导致在跨平台或跨数据库时出现字符编码不一致的问题，因此通常建议在进行数据传输时启用 Unicode 编码。</font><font style="color:rgb(51, 51, 51);">综上所述，设置 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">useUnicode</font>`<font style="color:rgb(51, 51, 51);"> 参数可以确保数据在传输过程中正确呈现各种字符集编码。对于应用程序处理多语言环境数据的场景，启用 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">useUnicode</font>`<font style="color:rgb(51, 51, 51);"> 参数尤为重要。</font>

- `<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">characterEncoding</font>`<font style="color:rgb(51, 51, 51);">：连接使用的字符编码，默认为 UTF-8；</font>

`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">characterEncoding</font>`<font style="color:rgb(51, 51, 51);"> 参数用于设置 MySQL 服务器和 JDBC 驱动程序之间进行字符集转换时使用的字符集编码。其设置为 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">UTF-8</font>`<font style="color:rgb(51, 51, 51);"> 表示使用 UTF-8 编码进行字符集转换，设置为 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">GBK</font>`<font style="color:rgb(51, 51, 51);"> 表示使用 GBK 编码进行字符集转换。其区别如下：</font><font style="color:rgb(51, 51, 51);">UTF-8 编码是一种可变长度的编码方式，可以表示世界上的所有字符，包括 ASCII、Unicode 和不间断空格等字符，是一种通用的编码方式。UTF-8 编码在国际化应用中被广泛使用，并且其使用的字节数较少，有利于提高数据传输的效率和节约存储空间。</font><font style="color:rgb(51, 51, 51);">GBK 编码是一种固定长度的编码方式，只能表示汉字和部分符号，不能表示世界上的所有字符。GBK 编码通常只用于中文环境中，因为在英文和数字等字符中会出现乱码情况。</font><font style="color:rgb(51, 51, 51);">因此，在 MySQL 中使用 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">UTF-8</font>`<font style="color:rgb(51, 51, 51);"> 编码作为字符集编码的优势在于能够支持世界上的所有字符，而且在国际化应用中使用广泛，对于不同语言和地区的用户都能够提供良好的支持。而使用 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">GBK</font>`<font style="color:rgb(51, 51, 51);"> 编码则主要在于适用于中文环境中的数据存储和传输。</font><font style="color:rgb(51, 51, 51);">需要注意的是，在选择编码方式时需要考虑到应用本身的实际需要和数据的特性，根据具体情况进行选择，避免出现字符集编码错误的问题。同时，还要确保 MySQL 服务器、JDBC 驱动程序和应用程序之间的字符集编码一致，避免出现字符集转换错误的问题。</font>

**<font style="color:rgb(51, 51, 51);">注意：useUnicode和characterEncoding有什么区别？</font>**

- **<font style="color:rgb(51, 51, 51);">useUnicode设置的是数据在传输过程中是否使用Unicode编码方式。</font>**
- **<font style="color:rgb(51, 51, 51);">characterEncoding设置的是数据被传输到服务器之后，服务器采用哪一种字符集进行编码。</font>**

<font style="color:rgb(51, 51, 51);">例如，连接 MySQL 数据库的 JDBC URL 可以如下所示：</font>

<font style="color:rgb(51, 51, 51);">jdbc:mysql://localhost:3306/jdbc?useUnicode=true&serverTimezone=Asia/Shanghai&useSSL=true&characterEncoding=utf-8</font>

<font style="color:rgb(51, 51, 51);">这里演示的是使用本地 MySQL 数据库，使用Unicode编码进行数据传输，服务器时区为 Asia/Shanghai，启用 SSL 连接，服务器接收到数据后使用 UTF-8 编码。</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=QZO2x&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## <font style="color:rgb(51, 51, 51);">JDBC编程第三步：获取数据库操作对象</font>
<font style="color:rgb(51, 51, 51);">数据库操作对象是这个接口：java.sql.Statement。这个对象负责将SQL语句发送给数据库服务器，服务器接收到SQL后进行编译，然后执行SQL。</font>

<font style="color:rgb(51, 51, 51);">API帮助文档如下：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702441460073-15a0cb32-b979-442c-900b-ec3109722750.png#averageHue=%23fafafa&clientId=u250ab531-c195-4&from=paste&height=303&id=u1963efbb&originHeight=303&originWidth=730&originalType=binary&ratio=1&rotation=0&showTitle=false&size=26208&status=done&style=shadow&taskId=u5bd04c45-816c-4f5c-97c7-13e4ad184d2&title=&width=730)

<font style="color:rgb(51, 51, 51);">获取数据库操作对象代码如下：</font>

```plain
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

<font style="color:rgb(51, 51, 51);">执行结果如下：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702440942574-861f279e-3244-4834-98a3-491d913949f6.png#averageHue=%23141210&clientId=u6d14a91a-446b-4&from=paste&height=68&id=u227c2993&originHeight=68&originWidth=744&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10201&status=done&style=none&taskId=u970ba921-b119-4d28-b865-7b7331b642d&title=&width=744)

<font style="color:rgb(51, 51, 51);">同样可以看到：java.sql.Statement接口在MySQL驱动中的实现类是：com.mysql.cj.jdbc.StatementImpl。不过我们同样是不需要关心这个具体的实现类。因为后续的代码仍然是面向Statement接口写代码的。</font>

<font style="color:rgb(51, 51, 51);">另外，要知道的是通过一个Connection对象是可以创建多个Statement对象的：</font>

```plain
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

<font style="color:rgb(51, 51, 51);">执行结果：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702441181097-76775506-0d8a-4c6b-a077-4feaf637c82a.png#averageHue=%23191613&clientId=u6d14a91a-446b-4&from=paste&height=91&id=u8eec20a7&originHeight=91&originWidth=776&originalType=binary&ratio=1&rotation=0&showTitle=false&size=17888&status=done&style=none&taskId=u89073331-77cd-46a5-a1d9-2f49f793eb3&title=&width=776)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=wTCPN&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## <font style="color:rgb(51, 51, 51);">JDBC编程第四步：执行SQL</font>
<font style="color:rgb(51, 51, 51);">当获取到Statement对象后，调用这个接口中的相关方法即可执行SQL语句。</font>

<font style="color:rgb(51, 51, 51);">API帮助文档如下：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702441577751-223506b2-73c9-47ee-a614-4b95fe555df3.png#averageHue=%23fcfaf8&clientId=u250ab531-c195-4&from=paste&height=365&id=ub3a2fe5e&originHeight=365&originWidth=732&originalType=binary&ratio=1&rotation=0&showTitle=false&size=32783&status=done&style=shadow&taskId=u3f69ebe3-b598-441e-b8c2-cee4d4bd33b&title=&width=732)

**<font style="color:rgb(51, 51, 51);">该方法的参数是一个SQL语句，只要将insert语句传递过来即可。当执行executeUpdate(sql)方法时，JDBC会将sql语句发送给数据库服务器，数据库服务器对SQL语句进行编译，然后执行SQL。</font>****<font style="color:rgb(51, 51, 51);">该方法的返回值是int类型，返回值的含义是：影响了数据库表当中几条记录。例如：返回1表示1条数据插入成功，返回2表示2条数据插入成功，以此类推。如果一条也没有插入，则返回0。</font>****<font style="color:rgb(51, 51, 51);">该方法适合执行的SQL语句是DML，包括：insert delete update。</font>**

<font style="color:rgb(51, 51, 51);">代码实现如下：</font>

```plain
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

<font style="color:rgb(51, 51, 51);">执行结果如下：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702441948716-d8c4638f-5d7a-4d26-b3d0-a2ed4872e6a4.png#averageHue=%23151311&clientId=u250ab531-c195-4&from=paste&height=73&id=uaeff0e6c&originHeight=73&originWidth=276&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4955&status=done&style=shadow&taskId=u9c765ac6-0b5e-4f70-8035-34afb8d658c&title=&width=276)<font style="color:rgb(51, 51, 51);">数据库表变化了：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702441971625-ba842802-4881-48ab-a4f3-17acc229d9c2.png#averageHue=%23dbb26c&clientId=u250ab531-c195-4&from=paste&height=142&id=ud112604e&originHeight=142&originWidth=569&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11666&status=done&style=shadow&taskId=u47d5cce9-0e5d-426e-a707-2a0a1bc20b8&title=&width=569)![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=EwOpD&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## <font style="color:rgb(51, 51, 51);">JDBC编程第六步：释放资源</font>
<font style="color:rgb(51, 51, 51);">第五步去哪里了？第五步是处理查询结果集，以上操作不是select语句，所以第五步直接跳过，直接先看一下第六步释放资源。【后面学习查询语句的时候，再详细看第五步】</font>

### <font style="color:rgb(51, 51, 51);">为什么要释放资源</font>
<font style="color:rgb(51, 51, 51);">在 JDBC 编程中，建立数据库连接、创建 Statement 对象等操作都需要申请系统资源，例如打开网络端口、申请内存等。为了避免占用过多的系统资源和避免出现内存泄漏等问题，我们需要在使用完资源后及时释放它们。</font>

### <font style="color:rgb(51, 51, 51);">释放资源的原则</font>
<font style="color:rgb(51, 51, 51);">原则1：在finally语句块中释放</font>

- <font style="color:rgb(51, 51, 51);">建议在finally语句块中释放，因为程序执行过程中如果出现了异常，finally语句块中的代码是一定会执行的。也就是说：我们需要保证程序在执行过程中，不管是否出现了异常，最后的关闭是一定要执行的。当然了，也可以使用Java7的新特性：Try-with-resources。Try-with-resources 是 Java 7 引入的新特性。它简化了资源管理的代码实现，可以自动释放资源，减少了代码出错的可能性，同时也可以提供更好的代码可读性和可维护性。</font>

<font style="color:rgb(51, 51, 51);">原则2：释放有顺序</font>

- <font style="color:rgb(51, 51, 51);">从小到大依次释放，创建的时候，先创建Connection，再创建Statement。那么关闭的时候，先关闭Statement，再关闭Connection。</font>

<font style="color:rgb(51, 51, 51);">原则3：分别进行try...catch...</font>

- <font style="color:rgb(51, 51, 51);">关闭的时候调用close()方法，该方法有异常需要处理，建议分别对齐try...catch...进行异常捕获。如果只编写一个try...catch...进行一块捕获，在关闭过程中，如果某个关闭失败，会影响下一个资源的关闭。</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=e1WGj&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

### <font style="color:rgb(51, 51, 51);">代码如何实现</font>

```plain
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

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=F5fNP&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

# <font style="color:rgb(51, 51, 51);">注册驱动的常用方式</font>
<font style="color:rgb(51, 51, 51);">上面在注册驱动的时候，执行了这样的代码：</font>

```plain
java.sql.Driver driver = new com.mysql.cj.jdbc.Driver();
java.sql.DriverManager.registerDriver(driver);
```

<font style="color:rgb(51, 51, 51);">这种方式是自己new驱动对象，然后调用DriverManager的registerDriver()方法来完成驱动注册，还有另一种方式，并且这种方式是常用的：</font>

<font style="color:rgb(51, 51, 51);">Class.forName("com.mysql.cj.jdbc.Driver");</font>

<font style="color:rgb(51, 51, 51);">为什么这种方式常用？</font>

- <font style="color:rgb(51, 51, 51);">第一：代码少了很多。</font>
- <font style="color:rgb(51, 51, 51);">第二：这种方式可以很方便的将</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">com.mysql.cj.jdbc.Driver</font>`<font style="color:rgb(51, 51, 51);">类名配置到属性文件当中。</font>

<font style="color:rgb(51, 51, 51);">实现原理是什么？找一下</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">com.mysql.cj.jdbc.Driver</font>`<font style="color:rgb(51, 51, 51);">的源码：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702447203245-d68ebbe5-7d00-486c-be09-77ffa75c3407.png#averageHue=%23fbf9f8&clientId=u7c1aac3c-b9a1-4&from=paste&height=297&id=uccfd25eb&originHeight=297&originWidth=360&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12179&status=done&style=shadow&taskId=ud704ee4b-1b9b-4069-9173-110ec243516&title=&width=360)![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702447277996-c1526d49-f502-4925-8042-0d4edff0370d.png#averageHue=%23faf7f6&clientId=u7c1aac3c-b9a1-4&from=paste&height=633&id=u1781014f&originHeight=633&originWidth=675&originalType=binary&ratio=1&rotation=0&showTitle=false&size=82510&status=done&style=shadow&taskId=u584847eb-e7ea-45a6-bac9-aa7ad04fe44&title=&width=675)![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702447333885-23189b4e-5767-4dba-ae21-bdc543241db6.png#averageHue=%23fdfaf9&clientId=u7c1aac3c-b9a1-4&from=paste&height=680&id=uf6d27369&originHeight=680&originWidth=830&originalType=binary&ratio=1&rotation=0&showTitle=false&size=46959&status=done&style=shadow&taskId=u3d931415-f78b-48b4-bd14-348658e6392&title=&width=830)

<font style="color:rgb(51, 51, 51);">通过源码不难发现，在</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">com.mysql.cj.jdbc.Driver</font>`<font style="color:rgb(51, 51, 51);">类中有一个静态代码块，在这个静态代码块中调用了</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">java.sql.DriverManager.registerDriver(new Driver());</font>`<font style="color:rgb(51, 51, 51);">完成了驱动的注册。而</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">Class.forName("com.mysql.cj.jdbc.Driver");</font>`<font style="color:rgb(51, 51, 51);">代码的作用就是让</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">com.mysql.cj.jdbc.Driver</font>`<font style="color:rgb(51, 51, 51);">类完成加载，执行它的静态代码块。</font>

<font style="color:rgb(51, 51, 51);">编写代码测试一下：</font>

```plain
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

<font style="color:rgb(51, 51, 51);">执行结果：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702448305879-6a1fe86a-6da8-4127-8e6d-5dafeeffa94f.png#averageHue=%23191714&clientId=u7c1aac3c-b9a1-4&from=paste&height=63&id=u996e8b7d&originHeight=63&originWidth=253&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4977&status=done&style=shadow&taskId=u23ee8a99-53ce-438e-9119-bdf0a890e7d&title=&width=253)

<font style="color:rgb(51, 51, 51);">数据库表中数据也新增了：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702448335558-06ceaaf7-6b10-4fca-a9c1-0d9f81281f48.png#averageHue=%23dcb26c&clientId=u7c1aac3c-b9a1-4&from=paste&height=166&id=ud397ca1f&originHeight=166&originWidth=555&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13301&status=done&style=shadow&taskId=u93e0efd9-e2cc-41a6-8824-e8989bb718e&title=&width=555)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=acQ6d&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

# <font style="color:rgb(51, 51, 51);">JDBC 4.0后不用手动注册驱动（了解）</font>
<font style="color:rgb(51, 51, 51);">从JDBC 4.0（</font>**<font style="color:rgb(51, 51, 51);">也就是Java6</font>**<font style="color:rgb(51, 51, 51);">）版本开始，驱动的注册不需要再手动完成，由系统自动完成。</font>

```plain
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

<font style="color:rgb(51, 51, 51);">执行结果：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702448395728-8b99a1d5-eb2d-4541-b140-dbaf03d12e4c.png#averageHue=%23151211&clientId=u7c1aac3c-b9a1-4&from=paste&height=73&id=A3QO6&originHeight=73&originWidth=251&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4938&status=done&style=shadow&taskId=ufddd9ae9-54ec-4d51-a12a-e0276c72b5c&title=&width=251)

<font style="color:rgb(51, 51, 51);">数据库表中数据也添加了一条：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702448423567-a2526811-994b-496a-bd61-7ba47dfda8cb.png#averageHue=%23e4c17b&clientId=u7c1aac3c-b9a1-4&from=paste&height=181&id=u42d8e45b&originHeight=181&originWidth=556&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15314&status=done&style=shadow&taskId=ubebfbfc2-ee04-42b2-a495-f1c6ed41091&title=&width=556)**<font style="color:rgb(51, 51, 51);">注意：虽然大部分情况下不需要进行手动注册驱动了，但在实际的开发中有些数据库驱动程序不支持自动发现功能，仍然需要手动注册。所以建议大家还是别省略了。</font>**

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=tO7GD&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

# <font style="color:rgb(51, 51, 51);">动态配置连接数据库的信息</font>
<font style="color:rgb(51, 51, 51);">为了程序的通用性，为了切换数据库的时候不需要修改Java程序，为了符合OCP开闭原则，建议将连接数据库的信息配置到属性文件中，例如：</font>

```plain
driver=com.mysql.cj.jdbc.Driver
url=jdbc:mysql://localhost:3306/jdbc?useUnicode=true&serverTimezone=Asia/Shanghai&useSSL=true&characterEncoding=utf-8
user=root
password=123456
```

<font style="color:rgb(51, 51, 51);">然后使用IO流读取属性文件，动态获取连接数据库的信息：</font>

```plain
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

<font style="color:rgb(51, 51, 51);">执行结果如下：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702448811161-f8f9d0fc-025b-48a9-b9fa-a38d96b7b168.png#averageHue=%23171513&clientId=u7c1aac3c-b9a1-4&from=paste&height=73&id=uc696c982&originHeight=73&originWidth=260&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5011&status=done&style=shadow&taskId=ub6b01b11-82ea-452b-9e6d-e128953b256&title=&width=260)

<font style="color:rgb(51, 51, 51);">数据库表中也会新增一条记录：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702448831135-374bee91-f770-40aa-ba3b-eb35ded23435.png#averageHue=%23dcb36e&clientId=u7c1aac3c-b9a1-4&from=paste&height=205&id=uf0b9de72&originHeight=205&originWidth=548&originalType=binary&ratio=1&rotation=0&showTitle=false&size=17026&status=done&style=shadow&taskId=u81fcb1f5-df4c-41fb-8ad0-157052f6a32&title=&width=548)

<font style="color:rgb(51, 51, 51);">以后要连接其他数据库，只要修改属性文件中的配置即可。</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=P19kA&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

# <font style="color:rgb(51, 51, 51);">获取连接的其他方式（了解）</font>
<font style="color:rgb(51, 51, 51);">上面我们讲到了第一种获取连接的方式：</font>

<font style="color:rgb(51, 51, 51);">Connection conn = DriverManager.getConnection(url, user, password);</font>

<font style="color:rgb(51, 51, 51);">除了以上的这种方式之外，还有两种方式，通过API帮助文档可以看到：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702453145756-8174de75-a789-4030-b496-8b7fd700afb6.png#averageHue=%23848683&clientId=uad1d7c4b-3ad5-4&from=paste&height=114&id=u57e0b4f0&originHeight=114&originWidth=486&originalType=binary&ratio=1&rotation=0&showTitle=false&size=9318&status=done&style=shadow&taskId=u146edfbb-7091-4908-9205-66871e8b703&title=&width=486)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=wmT9v&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## <font style="color:rgb(51, 51, 51);">getConnection(String url)</font>
<font style="color:rgb(51, 51, 51);">这种方式参数只有一个url，那用户名和密码放在哪里呢？可以放到url当中，代码如下：</font>

```plain
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

<font style="color:rgb(51, 51, 51);">执行结果：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702455014436-0f8654ab-8919-444f-a5b3-03b8c11736ae.png#averageHue=%2313110f&clientId=uad1d7c4b-3ad5-4&from=paste&height=76&id=u583c9f06&originHeight=76&originWidth=632&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8658&status=done&style=shadow&taskId=u5cc7dddf-c500-4258-97a9-55f93a03d6a&title=&width=632)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=jg0kF&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## <font style="color:rgb(51, 51, 51);">getConnection(String url, Properties info)</font>
<font style="color:rgb(51, 51, 51);">这种方式有两个参数，一个是url，一个是Properties对象。</font>

- <font style="color:rgb(51, 51, 51);">url：可以单纯提供一个url地址</font>
- <font style="color:rgb(51, 51, 51);">info：可以将url的参数存放到该对象中</font>

<font style="color:rgb(51, 51, 51);">代码如下：</font>

```plain
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

<font style="color:rgb(51, 51, 51);">执行结果：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702455362524-bc4e9ffa-ca7d-433a-af73-01cf76d556a0.png#averageHue=%23141210&clientId=uad1d7c4b-3ad5-4&from=paste&height=70&id=u8e5e09e5&originHeight=70&originWidth=651&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8686&status=done&style=shadow&taskId=u5fc59869-8791-4891-9bf0-46233ec61a2&title=&width=651)

<font style="color:rgb(51, 51, 51);">以上这两种方式作为了解，不是重点。</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=gGqrD&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

# <font style="color:rgb(51, 51, 51);">JDBC完成修改操作</font>
<font style="color:rgb(51, 51, 51);">修改操作就是执行update语句。仍然调用Statement接口的executeUpdate(sql)方法即可。</font><font style="color:rgb(51, 51, 51);">业务要求：将name是tangsanzang的真实姓名修改为唐僧。</font><font style="color:rgb(51, 51, 51);">修改前的数据：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702456282356-5938ff92-a0ea-46d6-96f1-684c3fb29364.png#averageHue=%23f6f4f2&clientId=uad1d7c4b-3ad5-4&from=paste&height=229&id=u643b9072&originHeight=229&originWidth=564&originalType=binary&ratio=1&rotation=0&showTitle=false&size=17418&status=done&style=shadow&taskId=u8293e081-039b-4407-84b4-7e8446f739d&title=&width=564)

<font style="color:rgb(51, 51, 51);">代码如下：</font>

```plain
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

<font style="color:rgb(51, 51, 51);">执行结果：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702456438297-48fcead2-99e0-4bd8-9e65-8cc911eb529b.png#averageHue=%23191613&clientId=uad1d7c4b-3ad5-4&from=paste&height=65&id=uf1056966&originHeight=65&originWidth=245&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5013&status=done&style=shadow&taskId=u2027d896-51af-4d88-bcd0-545fddd147b&title=&width=245)

<font style="color:rgb(51, 51, 51);">更新后的数据：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702456454268-27e23605-5b36-4bb5-80b1-deb74ef1d5ac.png#averageHue=%23dbb069&clientId=uad1d7c4b-3ad5-4&from=paste&height=203&id=ud238080d&originHeight=203&originWidth=556&originalType=binary&ratio=1&rotation=0&showTitle=false&size=16844&status=done&style=shadow&taskId=u3daedd8f-84ea-4b95-a8b4-1a6f8add32f&title=&width=556)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=G92un&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

# <font style="color:rgb(51, 51, 51);">JDBC完成删除操作</font>
<font style="color:rgb(51, 51, 51);">删除操作就是执行delete语句。仍然调用Statement接口的executeUpdate(sql)方法即可。</font><font style="color:rgb(51, 51, 51);">业务要求：将id是15，16，17的数据删除。</font><font style="color:rgb(51, 51, 51);">删除前的数据：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702456454268-27e23605-5b36-4bb5-80b1-deb74ef1d5ac.png#averageHue=%23dbb069&clientId=uad1d7c4b-3ad5-4&from=paste&height=203&id=kdnEV&originHeight=203&originWidth=556&originalType=binary&ratio=1&rotation=0&showTitle=false&size=16844&status=done&style=shadow&taskId=u3daedd8f-84ea-4b95-a8b4-1a6f8add32f&title=&width=556)

<font style="color:rgb(51, 51, 51);">代码如下：</font>

```plain
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

<font style="color:rgb(51, 51, 51);">执行结果如下：</font>

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702456658043-1b44cb18-1150-4768-8296-737c4181f4d4.png#averageHue=%23181512&clientId=uad1d7c4b-3ad5-4&from=paste&height=71&id=u4ffdfcc1&originHeight=71&originWidth=238&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5258&status=done&style=shadow&taskId=u38d245b6-4707-484d-afc1-5d4ee82865b&title=&width=238)

<font style="color:rgb(51, 51, 51);">删除后的数据：</font>

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702456673845-d64ca45a-a540-4813-a223-5be1db975764.png#averageHue=%23f6f4f2&clientId=uad1d7c4b-3ad5-4&from=paste&height=145&id=u3a2ae7c9&originHeight=145&originWidth=551&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11614&status=done&style=shadow&taskId=uf46afae2-dae6-4d3d-ab33-b6d0105d553&title=&width=551)

# <font style="color:rgb(51, 51, 51);">JDBC的查询操作</font>
<font style="color:rgb(51, 51, 51);">ResultSet 是 JDBC （Java 数据库连接） API 提供的接口，它用于表示 SQL 查询的结果集。ResultSet 对象中包含了查询结果的所有行，可以通过 next() 方法逐行地获取并处理每一行的数据。它最常用于执行 SELECT 语句查询出来的结果集。</font>

<font style="color:rgb(51, 51, 51);">ResultSet 的遍历是基于 JDBC 的流式处理机制的，即一行一行地获取结果，避免将所有结果全部取出后再进行处理导致内存溢出问题。</font>

<font style="color:rgb(51, 51, 51);">在使用 ResultSet 遍历查询结果时，一般会采用以下步骤：</font>

1. <font style="color:rgb(51, 51, 51);">执行 SQL 查询，获取 ResultSet 对象。</font>
2. <font style="color:rgb(51, 51, 51);">使用 ResultSet 的 next() 方法移动游标指向结果集的下一行，判断是否有更多的数据行。</font>
3. <font style="color:rgb(51, 51, 51);">如果有更多的数据行，则使用 ResultSet 对象提供的 getXXX() 方法获取当前行的各个字段（XXX 表示不同的数据类型）。例如，getLong("id") 方法用于获取当前行的 id 列对应的 Long 类型的值。</font>
4. <font style="color:rgb(51, 51, 51);">处理当前行的数据，例如将其存入 Java 对象中。</font>
5. <font style="color:rgb(51, 51, 51);">重复执行步骤 2~4，直到结果集中的所有行都被遍历完毕。</font>
6. <font style="color:rgb(51, 51, 51);">调用 ResultSet 的 close() 方法释放资源。</font>

<font style="color:rgb(51, 51, 51);">需要注意的是，在使用完 ResultSet 对象之后，需要及时关闭它，以释放数据库资源并避免潜在的内存泄漏问题。否则，如果在多个线程中打开了多个 ResultSet 对象，并且没有正确关闭它们的话，可能会导致数据库连接过多，从而影响系统的稳定性和性能。</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=acVGP&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## <font style="color:rgb(51, 51, 51);">通过列索引获取数据（以String类型获取）</font>
<font style="color:rgb(51, 51, 51);">需求：获取t_user表中所有数据，在控制台打印输出每一行的数据。</font>

<font style="color:rgb(51, 51, 51);">select id,name,password,realname,gender,tel from t_user;</font>

<font style="color:rgb(51, 51, 51);">要查询的数据如下图：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702536722789-fc5bbe25-598a-4619-b5b0-2dc1871da569.png#averageHue=%23f5f3f1&clientId=u4be5fce1-1b74-4&from=paste&height=137&id=u4577f84c&originHeight=137&originWidth=543&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11309&status=done&style=none&taskId=u78254320-0cef-41c6-afba-771a9b8d6ea&title=&width=543)<font style="color:rgb(51, 51, 51);">代码如下（重点关注第4步 第5步 第6步）：</font>

```plain
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

<font style="color:rgb(51, 51, 51);">执行结果如下：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702537178277-7ea8b4eb-1088-45cb-9493-18fe44b90287.png#averageHue=%23141210&clientId=u858f9b9d-17d9-4&from=paste&height=173&id=uf0b4c7fe&originHeight=173&originWidth=731&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24609&status=done&style=none&taskId=u8a64269f-fa1a-42ab-82ef-88158483f59&title=&width=731)

<font style="color:rgb(51, 51, 51);">代码解读：</font>

```plain
// 4. 执行SQL语句
String sql = "select id,name,password,realname,gender,tel from t_user";
rs = stmt.executeQuery(sql);
```

<font style="color:rgb(51, 51, 51);">执行insert delete update语句的时候，调用Statement接口的executeUpdate()方法。</font><font style="color:rgb(51, 51, 51);">执行select语句的时候，</font>**<font style="color:rgb(51, 51, 51);">调用Statement接口的executeQuery()方法</font>**<font style="color:rgb(51, 51, 51);">。执行select语句后返回结果集对象：ResultSet。</font>

<font style="color:rgb(51, 51, 51);">代码解读：</font>

```plain
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

- **<font style="color:rgb(51, 51, 51);">rs.next() 将游标移动到下一行，如果移动后指向的这一行有数据则返回true，没有数据则返回false。</font>**
- **<font style="color:rgb(51, 51, 51);">while循环体当中的代码是处理当前游标指向的这一行的数据。（注意：是处理的一行数据）</font>**
- **<font style="color:rgb(51, 51, 51);">rs.getString(int columnIndex) 其中 int columnIndex 是查询结果的列下标，列下标从1开始，以1递增。</font>**

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702538306701-4341b895-f91b-4501-af67-4746b6327884.png#averageHue=%23f5f2f0&clientId=u858f9b9d-17d9-4&from=paste&height=149&id=ud9abd104&originHeight=149&originWidth=530&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12490&status=done&style=none&taskId=u49d40a9c-dcbc-4315-b6f2-d6ff94d7392&title=&width=530)

- **<font style="color:rgb(51, 51, 51);">rs.getString(...) 方法在执行时，不管底层数据库中的数据类型是什么，统一以字符串String类型来获取。</font>**

<font style="color:rgb(51, 51, 51);">代码解读：</font>

```plain
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

<font style="color:rgb(51, 51, 51);">ResultSet最终也是需要关闭的。</font>**<font style="color:rgb(51, 51, 51);">先关闭ResultSet，再关闭Statement，最后关闭Connection</font>**<font style="color:rgb(51, 51, 51);">。</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=O8j9i&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## <font style="color:rgb(51, 51, 51);">通过列名获取数据（以String类型获取）</font>
<font style="color:rgb(51, 51, 51);">获取当前行的数据，不仅可以通过列下标获取，还可以通过查询结果的列名来获取，通常这种方式是被推荐的，因为可读性好。</font><font style="color:rgb(51, 51, 51);">例如这样的SQL：</font>

<font style="color:rgb(51, 51, 51);">select id, name as username, realname from t_user;</font>

<font style="color:rgb(51, 51, 51);">执行结果是：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702539677907-26c84361-6874-421b-a612-dd754f7fb8f3.png#averageHue=%23f0eeed&clientId=u858f9b9d-17d9-4&from=paste&height=143&id=u41f963b6&originHeight=143&originWidth=276&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6326&status=done&style=shadow&taskId=ua525fbd3-c909-4c6b-89bc-78e79f519be&title=&width=276)<font style="color:rgb(51, 51, 51);">我们可以按照查询结果的列名来获取数据：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702540371842-53a5c738-db3b-4040-aa0a-cd6dc9b9bb22.png#averageHue=%23f2ebea&clientId=u858f9b9d-17d9-4&from=paste&height=154&id=uce35bc3e&originHeight=154&originWidth=296&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6783&status=done&style=none&taskId=u3f9d0389-5876-4cb1-8511-793740afc5e&title=&width=296)**<font style="color:rgb(51, 51, 51);">注意：是根据查询结果的列名，而不是表中的列名。以上查询的时候将字段name起别名username了，所以要根据username来获取，而不能再根据name来获取了。</font>**

```plain
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

<font style="color:rgb(51, 51, 51);">执行结果如下：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702540580699-757667a3-887c-4468-8a0e-fe29ea6d6674.png#averageHue=%23141210&clientId=u858f9b9d-17d9-4&from=paste&height=166&id=u6413404e&originHeight=166&originWidth=399&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15137&status=done&style=shadow&taskId=udc22c08e-2fff-4736-873c-a2f48e06a3f&title=&width=399)

<font style="color:rgb(51, 51, 51);">如果将上面代码中</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">rs.getString("username")</font>`<font style="color:rgb(51, 51, 51);">修改为</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">rs.getString("name")</font>`<font style="color:rgb(51, 51, 51);">，执行就会出现以下错误：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702540685314-fa65fdea-6aad-4781-99fa-c007955b5b3f.png#averageHue=%23191613&clientId=u858f9b9d-17d9-4&from=paste&height=225&id=ua4405eca&originHeight=225&originWidth=1042&originalType=binary&ratio=1&rotation=0&showTitle=false&size=40887&status=done&style=shadow&taskId=ub13101ac-bd74-45a7-81db-f89d783e604&title=&width=1042)<font style="color:rgb(51, 51, 51);">提示name列是不存在的。所以一定是根据查询结果中的列名来获取，而不是表中原始的列名。</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=InE0y&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## <font style="color:rgb(51, 51, 51);">以指定的类型获取数据</font>
<font style="color:rgb(51, 51, 51);">前面的程序可以看到，不管数据库表中是什么数据类型，都以String类型返回。当然，也能以指定类型返回。</font><font style="color:rgb(51, 51, 51);">使用PowerDesigner再设计一张商品表：t_product，使用Navicat for MySQL工具准备数据如下：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702541223024-4e5acb77-ef8b-4437-ba3d-10c02ba0999b.png#averageHue=%23faf8f8&clientId=u858f9b9d-17d9-4&from=paste&height=137&id=uc04a7f0d&originHeight=137&originWidth=715&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8990&status=done&style=shadow&taskId=u4d697cdc-11e5-45f9-9090-b8dbd5ff938&title=&width=715)![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702541500905-f5e0a70b-19b0-4469-97db-68e414f92984.png#averageHue=%23dab370&clientId=u858f9b9d-17d9-4&from=paste&height=92&id=u9977c004&originHeight=92&originWidth=489&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5846&status=done&style=shadow&taskId=u5b3fc4aa-5215-4125-8745-c27aadef887&title=&width=489)

<font style="color:rgb(51, 51, 51);">id以long类型获取，name以String类型获取，price以double类型获取，create_time以java.sql.Date类型获取，代码如下：</font>

```plain
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

<font style="color:rgb(51, 51, 51);">执行结果如下：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702541874721-10c9a4f2-370f-4ce4-985e-6cf8da2e3ffb.png#averageHue=%23131110&clientId=u858f9b9d-17d9-4&from=paste&height=122&id=ue711ac2d&originHeight=122&originWidth=522&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11018&status=done&style=shadow&taskId=u241eaa77-525f-4fbd-9bdd-9a7523caff4&title=&width=522)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=SE92d&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## <font style="color:rgb(51, 51, 51);">获取结果集的元数据信息（了解）</font>
<font style="color:rgb(51, 51, 51);">ResultSetMetaData 是一个接口，用于描述 ResultSet 中的元数据信息，即查询结果集的结构信息，例如查询结果集中包含了哪些列，每个列的数据类型、长度、标识符等。</font>

<font style="color:rgb(51, 51, 51);">ResultSetMetaData 可以通过 ResultSet 接口的 getMetaData() 方法获取，一般在对 ResultSet 进行元数据信息处理时使用。例如，可以使用 ResultSetMetaData 对象获取查询结果中列的信息，如列名、列的类型、列的长度等。通过 ResultSetMetaData 接口的方法，可以实现对查询结果的基本描述信息操作，例如获取查询结果集中有多少列、列的类型、列的标识符等。以下是一段通过 ResultSetMetaData 获取查询结果中列的信息的示例代码：</font>

```plain
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

<font style="color:rgb(51, 51, 51);">执行结果如下：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702542217121-d413b4dc-1bf2-45ca-80c8-551d2a3705b8.png#averageHue=%231a1714&clientId=u858f9b9d-17d9-4&from=paste&height=145&id=ubff5f259&originHeight=145&originWidth=576&originalType=binary&ratio=1&rotation=0&showTitle=false&size=26448&status=done&style=shadow&taskId=u4cc05a2e-3473-488b-afd7-094e12de4cb&title=&width=576)

<font style="color:rgb(51, 51, 51);">在上面的代码中，我们首先创建了一个 Statement 对象，然后执行了一条 SQL 查询语句，生成了一个 ResultSet 对象。接下来，我们通过 ResultSet 对象的 getMetaData() 方法获取了 ResultSetMetaData 对象，进而获取了查询结果中列的信息并进行输出。需要注意的是，在进行列信息的获取时，列的编号从 1 开始计算。该示例代码将获取查询结果集中所有列名、数据类型以及长度等信息。</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=iCiM1&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

# <font style="color:rgb(51, 51, 51);">获取新增行的主键值</font>
<font style="color:rgb(51, 51, 51);">有很多表的主键字段值都是自增的，在某些特殊的业务环境下，当我们插入了新数据后，希望能够获取到这条新数据的主键值，应该如何获取呢？</font><font style="color:rgb(51, 51, 51);">在 JDBC 中，如果要获取插入数据后的主键值，可以使用 Statement 接口的 executeUpdate() 方法的重载版本，该方法接受一个额外的参数，用于指定是否需要获取自动生成的主键值。然后，通过以下两个步骤获取插入数据后的主键值：</font>

1. <font style="color:rgb(51, 51, 51);">在执行 executeUpdate() 方法时指定一个标志位，表示需要返回插入的主键值。</font>
2. <font style="color:rgb(51, 51, 51);">调用 Statement 对象的 getGeneratedKeys() 方法，返回一个包含插入的主键值的 ResultSet 对象。 </font>

```plain
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

<font style="color:rgb(51, 51, 51);">执行结果如下：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702543846750-ba186e76-04fa-4ef1-8d57-7fc40598c02e.png#averageHue=%23181513&clientId=ucecc8983-3edd-4&from=paste&height=76&id=u73f30d19&originHeight=76&originWidth=287&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6899&status=done&style=shadow&taskId=ue1f27885-34fa-45d1-9da8-062ab8917fd&title=&width=287)![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702543887747-8bfa21c9-e7b4-49c9-8dec-dbca00a645a7.png#averageHue=%23dcb26c&clientId=ucecc8983-3edd-4&from=paste&height=164&id=uf79fbdbf&originHeight=164&originWidth=572&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13072&status=done&style=none&taskId=u91dfc8c2-3fff-4213-8df9-ef9c0ad88f7&title=&width=572)<font style="color:rgb(51, 51, 51);">以上代码中，我们将 Statement.RETURN_GENERATED_KEYS 传递给 executeUpdate() 方法，以指定需要获取插入的主键值。然后，通过调用 Statement 对象的 getGeneratedKeys() 方法获取包含插入的主键值的 ResultSet 对象，通过 ResultSet 对象获取主键值。需要注意的是，在使用 Statement 对象的 getGeneratedKeys() 方法获取自动生成的主键值时，主键值的获取方式具有一定的差异，需要根据不同的数据库种类和版本来进行调整。</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=lNBXU&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

# <font style="color:rgb(51, 51, 51);">使用IDEA工具编写JDBC程序</font>
## <font style="color:rgb(51, 51, 51);">创建空的工程并设置JDK</font>
<font style="color:rgb(51, 51, 51);">创建一个空的工程：mypro</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702892512796-0fb0ad4b-70cd-4d6b-89f1-49979a51206c.png#averageHue=%232b2e32&clientId=ud3d1e1b0-846a-4&from=paste&height=695&id=u9120ab6a&originHeight=695&originWidth=781&originalType=binary&ratio=1&rotation=0&showTitle=false&size=50800&status=done&style=none&taskId=u352ee1a4-4b8e-42cb-b73e-857b21fe5c1&title=&width=781)

<font style="color:rgb(51, 51, 51);">工程结构：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702891589679-f9b4b346-a814-41cd-9f22-002668a1eed7.png#averageHue=%232c2f34&clientId=ud3d1e1b0-846a-4&from=paste&height=605&id=u99c1addd&originHeight=605&originWidth=604&originalType=binary&ratio=1&rotation=0&showTitle=false&size=54915&status=done&style=none&taskId=u0abd9425-ca3e-48e6-b7ae-86ae986cee9&title=&width=604)

<font style="color:rgb(51, 51, 51);">设置JDK以及编译器版本：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702892572186-0d582f69-f12a-4de2-bb95-129857c2d1e4.png#averageHue=%232c2e32&clientId=ud3d1e1b0-846a-4&from=paste&height=847&id=ud8ca002c&originHeight=847&originWidth=1021&originalType=binary&ratio=1&rotation=0&showTitle=false&size=53825&status=done&style=none&taskId=u84774efb-5c51-4b23-916a-f38313bb791&title=&width=1021)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=Yn4QN&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## <font style="color:rgb(51, 51, 51);">创建一个模块</font>
![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702892712096-c8781789-2ea6-485e-8c43-9902923e7f48.png#averageHue=%232d3137&clientId=ud3d1e1b0-846a-4&from=paste&height=330&id=udd8c3bab&originHeight=330&originWidth=709&originalType=binary&ratio=1&rotation=0&showTitle=false&size=44439&status=done&style=none&taskId=u8ff7c0d2-4376-4ed5-9543-9e9fc343ccc&title=&width=709)![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702892635936-a0bd4576-c3ab-46d3-aa4f-83a5f93900c2.png#averageHue=%232c2f33&clientId=ud3d1e1b0-846a-4&from=paste&height=695&id=ubdc6b663&originHeight=695&originWidth=785&originalType=binary&ratio=1&rotation=0&showTitle=false&size=74639&status=done&style=none&taskId=u875b1e61-44de-4488-b79b-8690efbe73b&title=&width=785)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=wZv37&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## <font style="color:rgb(51, 51, 51);">将驱动加入到CLASSPATH</font>
<font style="color:rgb(51, 51, 51);">在模块jdbc下创建一个目录：lib</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702892792110-ddd13f59-bb68-4c4f-b3bc-83bf2bcbc49c.png#averageHue=%232e3239&clientId=ud3d1e1b0-846a-4&from=paste&height=264&id=uec6b76f7&originHeight=264&originWidth=695&originalType=binary&ratio=1&rotation=0&showTitle=false&size=39130&status=done&style=none&taskId=u9dd72139-6520-4abc-bc55-2a8b3712b4a&title=&width=695)![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702892805707-188d0436-dff6-4ed8-a1d5-f7d8168a8226.png#averageHue=%232c2f32&clientId=ud3d1e1b0-846a-4&from=paste&height=69&id=u537211f0&originHeight=69&originWidth=332&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2817&status=done&style=none&taskId=u33a34d07-105e-45f8-9340-dd3807bc84b&title=&width=332)

<font style="color:rgb(51, 51, 51);">将mysql的驱动jar包拷贝到lib目录当中：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702892848869-f45f725d-576b-464c-94c3-0383f27cf9d2.png#averageHue=%232c3139&clientId=ud3d1e1b0-846a-4&from=paste&height=215&id=ua7605ddb&originHeight=215&originWidth=652&originalType=binary&ratio=1&rotation=0&showTitle=false&size=23031&status=done&style=none&taskId=u1fc7d4d4-9beb-49e0-837d-e84bbf7a9e5&title=&width=652)![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702892860859-06a0d6a9-9877-4a59-9a31-ef5ba8d10fdd.png#averageHue=%232d3340&clientId=ud3d1e1b0-846a-4&from=paste&height=96&id=uc8136c66&originHeight=96&originWidth=454&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6344&status=done&style=none&taskId=u9f94b37a-0573-40c1-ad7f-2377a126331&title=&width=454)

<font style="color:rgb(51, 51, 51);">将jar包加入到classpath：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702892903594-755ad190-065b-449e-ac8c-ed8a1afa76c0.png#averageHue=%232c2f34&clientId=ud3d1e1b0-846a-4&from=paste&height=741&id=u3f61102d&originHeight=741&originWidth=527&originalType=binary&ratio=1&rotation=0&showTitle=false&size=59956&status=done&style=none&taskId=uf36d3bed-fd35-47d2-bf52-26a97da11b5&title=&width=527)![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702893616221-646481b5-e342-4a65-8be3-584c4eaa858a.png#averageHue=%232c3038&clientId=u9a05de91-3647-4&from=paste&height=200&id=u9d34df03&originHeight=200&originWidth=427&originalType=binary&ratio=1&rotation=0&showTitle=false&size=16406&status=done&style=none&taskId=u35217463-4c16-49b8-a1fe-57f37473c17&title=&width=427)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=EPMYm&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## <font style="color:rgb(51, 51, 51);">编写JDBC程序</font>
<font style="color:rgb(51, 51, 51);">新建软件包：com.powernode.jdbc</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702893004185-0ff79250-22f1-4153-9be6-07a52d8a55cd.png#averageHue=%232d3034&clientId=ud3d1e1b0-846a-4&from=paste&height=69&id=u7a92b1b5&originHeight=69&originWidth=332&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4465&status=done&style=none&taskId=u0678840b-8a8b-4bbf-9af6-95330314c2c&title=&width=332)

<font style="color:rgb(51, 51, 51);">新建JDBCTest01类：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702893035873-744a58aa-cca9-47a3-9258-f2c319695a7f.png#averageHue=%232c313a&clientId=ud3d1e1b0-846a-4&from=paste&height=200&id=ubb8824c9&originHeight=200&originWidth=332&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11107&status=done&style=none&taskId=uf458823f-4474-4dc2-8580-5a2024e5283&title=&width=332)

<font style="color:rgb(51, 51, 51);">在JDBCTest01类中编写main方法，main方法中编写JDBC代码：</font>

```plain
package com.powernode.jdbc;

import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Connection;
import java.sql.Statement;
import java.util.ResourceBundle;
import java.sql.ResultSet;

public class JDBCTest01 {
    public static void main(String[] args){

        // 通过以下代码获取属性文件中的配置信息
        ResourceBundle bundle = ResourceBundle.getBundle("com.powernode.jdbc.jdbc");
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

<font style="color:rgb(51, 51, 51);">提供配置文件，在com.powernode.jdbc包下新建jdbc.properties文件：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702893379551-5ae919a2-ab26-480b-8467-e5850b033d27.png#averageHue=%232d323a&clientId=ud3d1e1b0-846a-4&from=paste&height=177&id=ucd9511db&originHeight=177&originWidth=846&originalType=binary&ratio=1&rotation=0&showTitle=false&size=34872&status=done&style=none&taskId=udc95d6ba-b850-4892-bce1-31cdbf84b02&title=&width=846)![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702893391844-df62761e-464d-451b-871b-3b71a0e20ddb.png#averageHue=%232c2f33&clientId=ud3d1e1b0-846a-4&from=paste&height=69&id=u010a7d87&originHeight=69&originWidth=332&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3343&status=done&style=none&taskId=ua9efd98e-35f5-416a-a63e-8b221cafa2c&title=&width=332)![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702893405175-69b5e31a-5f20-4154-92a9-f88d07a889ff.png#averageHue=%232f3848&clientId=ud3d1e1b0-846a-4&from=paste&height=82&id=ubfc29e0e&originHeight=82&originWidth=236&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7347&status=done&style=none&taskId=uaa71bb82-bb8d-4457-ab38-19553f6a8e7&title=&width=236)

<font style="color:rgb(51, 51, 51);">jdbc.properties文件中如下配置：</font>

```plain
driver=com.mysql.cj.jdbc.Driver
url=jdbc:mysql://localhost:3306/jdbc?useUnicode=true&serverTimezone=Asia/Shanghai&useSSL=true&characterEncoding=utf-8
user=root
password=123456
```

<font style="color:rgb(51, 51, 51);">执行结果如下：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702893658315-fbe8119e-9ab0-40ba-99f1-9d5b68e8866b.png#averageHue=%2322252b&clientId=u9a05de91-3647-4&from=paste&height=147&id=u156fff41&originHeight=147&originWidth=183&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6497&status=done&style=none&taskId=u7e57202d-6b7d-4e58-8f00-4b9d0124e83&title=&width=183)

<font style="color:rgb(51, 51, 51);">  
</font>![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=O8j9i&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

# <font style="color:rgb(51, 51, 51);">SQL注入问题</font>
<font style="color:rgb(51, 51, 51);">SQL注入问题说的是：用户输入的信息中含有SQL语句关键字，和程序中的SQL语句进行字符串拼接，导致程序中的SQL语句改变了原意。（SQL注入问题是一种系统安全问题）</font><font style="color:rgb(51, 51, 51);">接下来我们来演示一下SQL注入问题。以用户登录为例。使用表：t_user</font><font style="color:rgb(51, 51, 51);">业务描述：系统启动后，给出登录页面，用户可以输入用户名和密码，用户名和密码全部正确，则登录成功，反之，则登录失败。</font><font style="color:rgb(51, 51, 51);">分析一下要执行怎样的SQL语句？是不是这样的？</font>

<font style="color:rgb(51, 51, 51);">select * from t_user where name = 用户输入的用户名 and password = 用户输入的密码;</font>

<font style="color:rgb(51, 51, 51);">如果以上的SQL语句能够查询到结果，说明用户名和密码是正确的，则登录成功。如果查不到，说明是错误的，则登录失败。</font><font style="color:rgb(51, 51, 51);">代码实现如下：</font>

```plain
package com.powernode.jdbc;

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
        ResourceBundle bundle = ResourceBundle.getBundle("com.powernode.jdbc.jdbc");
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

<font style="color:rgb(51, 51, 51);">如果用户名和密码正确的话，执行结果如下：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702976483919-52a9ff26-1ded-4a07-bcc8-d2846f17a045.png#averageHue=%231f2126&clientId=u156f6b41-7663-4&from=paste&height=141&id=ub10f6c60&originHeight=141&originWidth=362&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13354&status=done&style=none&taskId=u7106c062-d627-45bf-801f-95ca72438bb&title=&width=362)

<font style="color:rgb(51, 51, 51);">如果用户名不存在或者密码错误的话，执行结果如下：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702976532157-a3d29aad-a0e8-44c9-9571-63cc3052fe5b.png#averageHue=%23202327&clientId=u156f6b41-7663-4&from=paste&height=125&id=udffad2a4&originHeight=125&originWidth=357&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15356&status=done&style=none&taskId=uf2850b49-75b0-40b5-a3b3-ea7386b756d&title=&width=357)

<font style="color:rgb(51, 51, 51);">接下来，见证奇迹的时刻，当我分别输入以下的用户名和密码时，系统被攻破了：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702976830213-7483fb5c-6c7c-466c-b7c4-a2feb26b12bb.png#averageHue=%23202226&clientId=u156f6b41-7663-4&from=paste&height=134&id=u347825d4&originHeight=134&originWidth=325&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11860&status=done&style=none&taskId=u8826f589-046f-4233-af61-95d1c099bf2&title=&width=325)<font style="color:rgb(51, 51, 51);">这种现象就叫做：SQL注入。为什么会发生以上的事儿呢？原因是：用户提供的信息中有SQL语句关键字，并且和底层的SQL字符串进行了拼接，变成了一个全新的SQL语句。</font><font style="color:rgb(51, 51, 51);">例如：本来程序想表达的是这样的SQL：</font>

<font style="color:rgb(51, 51, 51);">select realname from t_user where name = 'sunwukong' and password = '123';</font>

<font style="color:rgb(51, 51, 51);">结果被SQL注入之后，SQL语句就变成这样了：</font>

<font style="color:rgb(51, 51, 51);">select realname from t_user where name = 'aaa' and password = 'bbb' or '1'='1';</font>

<font style="color:rgb(51, 51, 51);">我们可以执行一下这条SQL，看看结果是什么？</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702977070115-c06f8f95-d42f-43e7-9b69-53eac3b155b2.png#averageHue=%23f0efee&clientId=u156f6b41-7663-4&from=paste&height=171&id=ue79d55bc&originHeight=171&originWidth=144&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3817&status=done&style=shadow&taskId=u33810237-dd0a-4fa9-9aef-067015aad10&title=&width=144)<font style="color:rgb(51, 51, 51);">把所有结果全部查到了，这是因为 '1'='1' 是恒成立的，并且使用的是 or 运算符，所以 or 前面的条件等于是没有的。这样就会把所有数据全部查到。而在程序中的判断逻辑是只要结果集中有数据，则表示登录成功。所以以上的输入方式最终的结果就是登录成功。你设想一下，如果这个系统是一个高级别保密系统，只有登录成功的人才有权限，那么这个系统是不是极其危险了。</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=b1eb1&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

# <font style="color:rgb(51, 51, 51);">解决SQL注入问题</font>
<font style="color:rgb(51, 51, 51);">导致SQL注入的根本原因是什么？只有找到真正的原因，问题才能得到解决。</font>

<font style="color:rgb(51, 51, 51);">最根本的原因是：Statement造成的。</font>

<font style="color:rgb(51, 51, 51);">Statement执行原理是：先进行字符串的拼接，将拼接好的SQL语句发送给数据库服务器，数据库服务器进行SQL语句的编译，然后执行。因此用户提供的信息中如果含有SQL语句的关键字，那么这些关键字正好参加了SQL语句的编译，所以导致原SQL语句被扭曲。</font>

<font style="color:rgb(51, 51, 51);">因此，JDBC为了解决这个问题，引入了一个新的接口：PreparedStatement，我们称为：预编译的数据库操作对象。PreparedStatement是Statement接口的子接口。它俩是继承关系。</font>

<font style="color:rgb(51, 51, 51);">PreparedStatement执行原理是：先对SQL语句进行预先的编译，然后再向SQL语句指定的位置传值，也就是说：用户提供的信息中即使含有SQL语句的关键字，那么这个信息也只会被当做一个值传递给SQL语句，用户提供的信息不再参与SQL语句的编译了，这样就解决了SQL注入问题。</font>

<font style="color:rgb(51, 51, 51);">使用PreparedStatement解决SQL注入问题：</font>

```plain
package com.powernode.jdbc;

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
        ResourceBundle bundle = ResourceBundle.getBundle("com.powernode.jdbc.jdbc");
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

<font style="color:rgb(51, 51, 51);">用户名和密码正确的话，执行结果如下：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702978597923-7cce7d0a-6a79-43a5-b9f3-a8ce2e4785e6.png#averageHue=%23202226&clientId=u156f6b41-7663-4&from=paste&height=134&id=uf32095e8&originHeight=134&originWidth=324&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13158&status=done&style=none&taskId=u994aaff2-25f2-447f-b015-c44013c610c&title=&width=324)

<font style="color:rgb(51, 51, 51);">用户名和密码错误的话，执行结果如下：</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702978634050-b50580fc-f9ce-48ec-9200-425ea078782c.png#averageHue=%23202227&clientId=u156f6b41-7663-4&from=paste&height=136&id=u5810b10f&originHeight=136&originWidth=347&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15416&status=done&style=none&taskId=u122f18ad-44c3-425f-aa33-e826821bb0f&title=&width=347)

<font style="color:rgb(51, 51, 51);">尝试SQL注入，看看还能不能？</font>![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1702978663699-a5c38388-b4f5-43b6-8d00-3e56fdb77178.png#averageHue=%23202227&clientId=u156f6b41-7663-4&from=paste&height=136&id=u7ba6dcfc&originHeight=136&originWidth=349&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13154&status=done&style=none&taskId=u88bcd970-8d9d-43b2-91ef-7affbe84c1b&title=&width=349)<font style="color:rgb(51, 51, 51);">通过测试得知，SQL注入问题已经解决了。</font>**<font style="color:rgb(51, 51, 51);">根本原因是：bbb' or '1'='1 这个字符串中虽然含有SQL语句的关键字，但是只会被当做普通的值传到SQL语句中，并没有参与SQL语句的编译</font>**<font style="color:rgb(51, 51, 51);">。</font>

**<font style="color:rgb(51, 51, 51);">关于使用PreparedStatement要注意的是：</font>**

- <font style="color:rgb(51, 51, 51);">带有占位符 ? 的SQL语句我们称为：预处理SQL语句。</font>
- <font style="color:rgb(51, 51, 51);">占位符 ? 不能使用单引号或双引号包裹。如果包裹，占位符则不再是占位符，是一个普通的问号字符。</font>
- <font style="color:rgb(51, 51, 51);">在执行SQL语句前，必须给每一个占位符 ? 传值。</font>
- <font style="color:rgb(51, 51, 51);">如何给占位符 ? 传值，通过以下的方法：</font>
    - <font style="color:rgb(51, 51, 51);">pstmt.setXxx(第几个占位符, 传什么值)</font>
    - <font style="color:rgb(51, 51, 51);">“第几个占位符”：从1开始。第1个占位符则是1，第2个占位符则是2，以此类推。</font>
    - <font style="color:rgb(51, 51, 51);">“传什么值”：具体要看调用的什么方法？</font>
        * <font style="color:rgb(51, 51, 51);">如果调用pstmt.setString方法，则传的值必须是一个字符串。</font>
        * <font style="color:rgb(51, 51, 51);">如果调用pstmt.setInt方法，则传的值必须是一个整数。</font>
        * <font style="color:rgb(51, 51, 51);">以此类推......</font>

**<font style="color:rgb(51, 51, 51);">PreparedStatement和Statement都是用于执行SQL语句的接口，它们的主要区别在于：</font>**

- <font style="color:rgb(51, 51, 51);">PreparedStatement预编译SQL语句，Statement直接提交SQL语句；</font>
- <font style="color:rgb(51, 51, 51);">PreparedStatement执行速度更快，可以避免SQL注入攻击；(PreparedStatement对于同一条SQL语句来说，编译一次，执行N次。而Statement是每次都要进行编译的。因此PreparedStatement效率略微高一些。)</font>
- <font style="color:rgb(51, 51, 51);">PreparedStatement会做类型检查，是类型安全的；</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=ix3qZ&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

# <font style="color:rgb(51, 51, 51);">PreparedStatement的使用</font>
## <font style="color:rgb(51, 51, 51);">新增操作</font>
<font style="color:rgb(51, 51, 51);">需求：向 emp 表中插入这样一条记录：</font><font style="color:rgb(51, 51, 51);">empno：8888</font><font style="color:rgb(51, 51, 51);">ename：张三</font><font style="color:rgb(51, 51, 51);">job：销售员</font><font style="color:rgb(51, 51, 51);">mgr：7369</font><font style="color:rgb(51, 51, 51);">hiredate：2024-01-01</font><font style="color:rgb(51, 51, 51);">sal：1000.0</font><font style="color:rgb(51, 51, 51);">comm：500.0</font><font style="color:rgb(51, 51, 51);">deptno：10</font>

```plain
package com.powernode.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.time.LocalDate;
import java.util.ResourceBundle;

public class JDBCTest04 {
    public static void main(String[] args) {

        ResourceBundle bundle = ResourceBundle.getBundle("com.powernode.jdbc.jdbc");
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

<font style="color:rgb(51, 51, 51);">重点学习内容：如何给占位符 ? 传值。</font><font style="color:rgb(51, 51, 51);">执行结果如下：</font>![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1708238667879-fe0a662a-f9e8-4933-afd0-5290856c21fd.png#averageHue=%23f4eeeb&clientId=u12e62e1b-f7c7-4&from=paste&height=370&id=uef77b401&originHeight=370&originWidth=673&originalType=binary&ratio=1&rotation=0&showTitle=false&size=36467&status=done&style=none&taskId=uc7a3d803-b1e3-40ee-98ca-368bb593c98&title=&width=673)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=X4tEj&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## <font style="color:rgb(51, 51, 51);">修改操作</font>
<font style="color:rgb(51, 51, 51);">需求：将员工编号为8888的员工，姓名修改为李四，岗位修改为产品经理，月薪修改为5000.0，其他不变。</font>

```plain
package com.powernode.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.time.LocalDate;
import java.util.ResourceBundle;

public class JDBCTest05 {
    public static void main(String[] args) {
        ResourceBundle bundle = ResourceBundle.getBundle("com.powernode.jdbc.jdbc");
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

<font style="color:rgb(51, 51, 51);">执行结果如下：</font>![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1708239544671-626c918f-fd56-4cfa-8aa2-df1976979414.png#averageHue=%23f6f0ed&clientId=u12e62e1b-f7c7-4&from=paste&height=375&id=u7bfa3f92&originHeight=375&originWidth=675&originalType=binary&ratio=1&rotation=0&showTitle=false&size=36597&status=done&style=none&taskId=u16478375-ba9f-4cac-89e8-61688719844&title=&width=675)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=yiZjS&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## <font style="color:rgb(51, 51, 51);">删除操作</font>
<font style="color:rgb(51, 51, 51);">需求：将员工编号为8888的删除。</font>

```plain
package com.powernode.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.ResourceBundle;

public class JDBCTest06 {
    public static void main(String[] args) {
        ResourceBundle bundle = ResourceBundle.getBundle("com.powernode.jdbc.jdbc");
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

<font style="color:rgb(51, 51, 51);">执行结果如下：</font>![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1708240126660-979bd865-6e83-41c7-9724-68c247209e9e.png#averageHue=%23d9ac6c&clientId=u12e62e1b-f7c7-4&from=paste&height=344&id=u8aa56fc6&originHeight=344&originWidth=658&originalType=binary&ratio=1&rotation=0&showTitle=false&size=33453&status=done&style=none&taskId=u5931a97b-d280-4586-abc4-aab041a7523&title=&width=658)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=RDFvt&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## <font style="color:rgb(51, 51, 51);">模糊查询</font>
<font style="color:rgb(51, 51, 51);">需求：查询员工名字中第二个字母是 O 的。</font>

```plain
package com.powernode.jdbc;

import java.sql.*;
import java.util.ResourceBundle;

public class JDBCTest07 {
    public static void main(String[] args) {
        ResourceBundle bundle = ResourceBundle.getBundle("com.powernode.jdbc.jdbc");
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

<font style="color:rgb(51, 51, 51);">执行结果如下：</font>![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1708240400162-5eb57d8c-e52c-4780-9ec2-88f117377328.png#averageHue=%23fcfaf9&clientId=u12e62e1b-f7c7-4&from=paste&height=62&id=u2c407fa5&originHeight=62&originWidth=148&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1908&status=done&style=shadow&taskId=u33a476d5-410d-4341-824c-3a9327ab37e&title=&width=148)<font style="color:rgb(51, 51, 51);">通过这个例子主要告诉大家，程序不能这样写：</font>

```plain
String sql = "select ename from emp where ename like '_?%'";
pstmt.setString(1, "O");
```

<font style="color:rgb(51, 51, 51);">由于占位符 ? 被单引号包裹，因此这个占位符是无效的。</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=pU8Ea&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## <font style="color:rgb(51, 51, 51);">分页查询</font>
<font style="color:rgb(51, 51, 51);">对于MySQL来说，通用的分页SQL语句：</font><font style="color:rgb(51, 51, 51);">假设每页显示3条记录：pageSize = 3</font><font style="color:rgb(51, 51, 51);">第1页：limit 0, 3</font><font style="color:rgb(51, 51, 51);">第2页：limit 3, 3</font><font style="color:rgb(51, 51, 51);">第3页：limit 6, 3</font>**<font style="color:rgb(51, 51, 51);">第pageNo页：limit (pageNo - 1)*pageSize, pageSize</font>**<font style="color:rgb(51, 51, 51);">需求：查询所有员工姓名，每页显示3条(pageSize)，显示第2页(pageNo)。</font>

```plain
package com.powernode.jdbc;

import java.sql.*;
import java.util.ResourceBundle;

public class JDBCTest08 {
    public static void main(String[] args) {
        ResourceBundle bundle = ResourceBundle.getBundle("com.powernode.jdbc.jdbc");
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

<font style="color:rgb(51, 51, 51);">执行结果如下：</font>![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1708241685820-a51b06ef-5b38-4e64-806c-0c1b86fe1fab.png#averageHue=%23fbf9f8&clientId=u907c0c1a-424e-4&from=paste&height=99&id=u9d0f25ee&originHeight=99&originWidth=152&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3174&status=done&style=shadow&taskId=u2501bf73-20d4-4c69-a735-1ba98ec06af&title=&width=152)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=hAryG&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## <font style="color:rgb(51, 51, 51);">blob数据的插入和读取</font>
<font style="color:rgb(51, 51, 51);">准备一张表：t_img，三个字段，一个id主键，一个图片名字name，一个img。</font><font style="color:rgb(51, 51, 51);">建表语句如下：</font>

```plain
create table `t_img` (
  `id` bigint primary key auto_increment,
  `name` varchar(255),
  `img` blob
) engine=innodb;
```

<font style="color:rgb(51, 51, 51);">准备一张图片：</font>![](https://cdn.nlark.com/yuque/0/2024/jpeg/21376908/1708242724736-094b007d-d418-4c4d-9a21-b12f20176daf.jpeg#averageHue=%23b0b4b2&clientId=u907c0c1a-424e-4&from=paste&height=200&id=u4371d107&originHeight=200&originWidth=200&originalType=binary&ratio=1&rotation=0&showTitle=false&size=9603&status=done&style=shadow&taskId=u4fc1ce36-27c9-4401-8282-e7cb4e89bd9&title=&width=200)

<font style="color:rgb(51, 51, 51);">需求1：向t_img 表中插入一张图片。</font>

```plain
package com.powernode.jdbc;

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
        ResourceBundle bundle = ResourceBundle.getBundle("com.powernode.jdbc.jdbc");
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

<font style="color:rgb(51, 51, 51);">执行结果如下：</font>![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1708243266510-6d057b29-ab51-49d2-839b-322dae79a50e.png#averageHue=%23dde3b0&clientId=u907c0c1a-424e-4&from=paste&height=58&id=u1d8aaf1a&originHeight=58&originWidth=304&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1815&status=done&style=shadow&taskId=u1af58cb1-140b-4fcf-8434-0a7c1aeba9a&title=&width=304)

<font style="color:rgb(51, 51, 51);">需求2：从t_img 表中读取一张图片。（从数据库中读取一张图片保存到本地。）</font>

```plain
package com.powernode.jdbc;

import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.OutputStream;
import java.sql.*;
import java.util.ResourceBundle;

public class JDBCTest10 {
    public static void main(String[] args) {
        ResourceBundle bundle = ResourceBundle.getBundle("com.powernode.jdbc.jdbc");
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

<font style="color:rgb(51, 51, 51);">执行完毕之后，查看一下图片大小是否和原图片相同，打开看看是否可以正常显示。</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=mIusF&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

# <font style="color:rgb(51, 51, 51);">JDBC批处理操作</font>
<font style="color:rgb(51, 51, 51);">准备一张商品表：t_product</font><font style="color:rgb(51, 51, 51);">建表语句如下：</font>

```plain
create table t_product(
  id bigint primary key,
  name varchar(255)
);
```

## <font style="color:rgb(51, 51, 51);">不使用批处理</font>
<font style="color:rgb(51, 51, 51);">不使用批处理，向 t_product 表中插入一万条商品信息，并记录耗时！</font>

```plain
package com.powernode.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.ResourceBundle;

public class NoBatchTest {
    public static void main(String[] args) {
        ResourceBundle bundle = ResourceBundle.getBundle("com.powernode.jdbc.jdbc");
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

<font style="color:rgb(51, 51, 51);">执行结果如下：</font>![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1708249553654-263146be-a485-4313-831f-892a776abd1d.png#averageHue=%23edeceb&clientId=u21834790-ed4d-4&from=paste&height=67&id=u376a8236&originHeight=67&originWidth=175&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2603&status=done&style=shadow&taskId=u9b065934-65ea-4ab2-8bd0-0a29936bbb8&title=&width=175)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=PoOE1&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## <font style="color:rgb(51, 51, 51);">使用批处理</font>
<font style="color:rgb(51, 51, 51);">使用批处理，向 t_product 表中插入一万条商品信息，并记录耗时！</font>**<font style="color:rgb(51, 51, 51);">注意：启用批处理需要在URL后面添加这个的参数：rewriteBatchedStatements=true</font>**![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1708249622292-576aa82d-5874-4013-a9b4-d94c00cef0ce.png#averageHue=%23fefdfb&clientId=u21834790-ed4d-4&from=paste&height=177&id=u4263b9d7&originHeight=177&originWidth=1592&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24176&status=done&style=shadow&taskId=u444819ae-8458-45a1-b734-bb75ab7faf4&title=&width=1592)

```plain
package com.powernode.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.ResourceBundle;

public class BatchTest {
    public static void main(String[] args) {
        ResourceBundle bundle = ResourceBundle.getBundle("com.powernode.jdbc.jdbc");
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

<font style="color:rgb(51, 51, 51);">执行结果如下：</font>![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1708249131242-0bf6746b-86f7-4bc9-966b-00d22994e177.png#averageHue=%23ecebea&clientId=u21834790-ed4d-4&from=paste&height=62&id=u8650f4b7&originHeight=62&originWidth=176&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2142&status=done&style=shadow&taskId=u5e5c9eb2-21df-410b-bafb-e9edb16ccb3&title=&width=176)

<font style="color:rgb(51, 51, 51);">在进行大数据量插入时，批处理为什么可以提高程序的执行效率？</font>

1. <font style="color:rgb(51, 51, 51);">减少了网络通信次数：JDBC 批处理会将多个 SQL 语句一次性发送给服务器，减少了客户端和服务器之间的通信次数，从而提高了数据写入的速度，特别是对于远程服务器而言，优化效果更为显著。 </font>
2. <font style="color:rgb(51, 51, 51);">减少了数据库操作次数：JDBC 批处理会将多个 SQL 语句合并成一条 SQL 语句进行执行，从而减少了数据库操作的次数，减轻了数据库的负担，大大提高了数据写入的速度。 </font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=g9Pw5&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

# <font style="color:rgb(51, 51, 51);">DbUtils工具类的封装</font>
<font style="color:rgb(51, 51, 51);">JDBC编程六步中，很多代码是重复出现的，可以为这些代码封装一个工具类。让JDBC代码变的更简洁。</font>

```plain
package com.powernode.jdbc;

import java.sql.*;
import java.util.ResourceBundle;

/**
 * ClassName: DbUtils
 * Description: JDBC工具类
 * Datetime: 2024/4/10 22:29
 * Author: 老杜@动力节点
 * Version: 1.0
 */
public class DbUtils {
    private static String url;
    private static String user;
    private static String password;

    static {
        // 读取属性资源文件
        ResourceBundle bundle = ResourceBundle.getBundle("com.powernode.jdbc.jdbc");
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

<font style="color:rgb(51, 51, 51);">  
</font><font style="color:rgb(51, 51, 51);">   
</font>![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=O8j9i&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

# <font style="color:rgb(51, 51, 51);">什么是事务</font>
<font style="color:rgb(51, 51, 51);">事务是一个完整的业务，在这个业务中需要多条DML语句共同联合才能完成，而事务可以保证多条DML语句同时成功或者同时失败，从而保证数据的安全。例如A账户向B账户转账一万，A账户减去一万(update)和B账户加上一万(update)，必须同时成功或者同时失败，才能保证数据是正确的。</font>

<font style="color:rgb(51, 51, 51);">另请参见老杜发布的2024版MySQL教学视频。在本套教程中详细讲解了数据库事务机制。</font>![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712894899237-1fa7df77-5280-4f8c-a5a4-6871f3da1cd7.png#averageHue=%23e5e9ec&clientId=ue29f8164-f6f8-4&from=paste&height=343&id=u9b97baef&originHeight=343&originWidth=329&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24858&status=done&style=none&taskId=u934375cb-bdd7-4482-a28e-b9b34241ef0&title=&width=329)![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712903200531-94b35a50-694e-4295-a8db-23edcee137c9.png#averageHue=%23dee3e7&clientId=ue29f8164-f6f8-4&from=paste&height=101&id=udbdb240f&originHeight=101&originWidth=298&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8273&status=done&style=none&taskId=ua916b075-e34b-4f2b-bfa3-157432983bc&title=&width=298)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=qxrS1&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

# <font style="color:rgb(51, 51, 51);">使用转账案例演示事务</font>
## <font style="color:rgb(51, 51, 51);">表和数据的准备</font>
<font style="color:rgb(51, 51, 51);">t_act表：</font>![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712906363176-935497e0-164e-4dd7-9c0d-a461fec09668.png#averageHue=%23f3f1ef&clientId=u97001951-01ca-4&from=paste&height=162&id=u10ee4509&originHeight=162&originWidth=708&originalType=binary&ratio=1&rotation=0&showTitle=false&size=14804&status=done&style=shadow&taskId=udbf1b96a-bdb2-4fe5-b063-fcb0ac2fe9c&title=&width=708)![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712906313124-77170d5b-9a14-4973-a063-2404228e0c60.png#averageHue=%23d2a868&clientId=u97001951-01ca-4&from=paste&height=90&id=u3af1ccf6&originHeight=90&originWidth=216&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2558&status=done&style=shadow&taskId=ubd814fdf-4d6f-4ab9-9f29-289e6cd48d4&title=&width=216)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=jDh6I&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## <font style="color:rgb(51, 51, 51);">实现转账功能</font>

```plain
package com.powernode.jdbc;

import com.powernode.jdbc.utils.DbUtils;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

/**
 * ClassName: JDBCTest19
 * Description: 实现账户转账
 * Datetime: 2024/4/12 15:20
 * Author: 老杜@动力节点
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

<font style="color:rgb(51, 51, 51);">执行结果：</font>![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712911942800-db916080-94e4-4b32-be09-ce7b4b21287d.png#averageHue=%23d2a664&clientId=u97001951-01ca-4&from=paste&height=86&id=u2d4983d9&originHeight=86&originWidth=199&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2553&status=done&style=shadow&taskId=u02304cce-ffe2-4af8-92c6-e492cec7476&title=&width=199)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=fHdee&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## <font style="color:rgb(51, 51, 51);">JDBC事务默认是自动提交的</font>
<font style="color:rgb(51, 51, 51);">JDBC事务默认情况下是自动提交的，所谓的自动提交是指：只要执行一条DML语句则自动提交一次。测试一下，在以下代码位置添加断点：</font>![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712912172123-b229ef63-3755-4993-84f4-2e303874c710.png#averageHue=%23312f2d&clientId=u97001951-01ca-4&from=paste&height=373&id=u573a3f7b&originHeight=373&originWidth=957&originalType=binary&ratio=1&rotation=0&showTitle=false&size=59857&status=done&style=none&taskId=u17724b8f-dfd5-4e9f-a6f8-0a386f0d45b&title=&width=957)<font style="color:rgb(51, 51, 51);">让代码执行到断点处：</font>![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712912197579-f0e09df6-2183-4ace-addf-a2c7d3d9c5f7.png#averageHue=%23302f2d&clientId=u97001951-01ca-4&from=paste&height=290&id=u02cfda53&originHeight=290&originWidth=966&originalType=binary&ratio=1&rotation=0&showTitle=false&size=57805&status=done&style=none&taskId=u9df5ba14-964d-42cd-b50c-811a21a75d6&title=&width=966)<font style="color:rgb(51, 51, 51);">让程序停在此处，看看数据库表中的数据是否发生变化：</font>![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712912226628-a32ded77-a2fe-4788-b5b5-3e2083b0926e.png#averageHue=%23d3a766&clientId=u97001951-01ca-4&from=paste&height=89&id=u673ed043&originHeight=89&originWidth=226&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2614&status=done&style=none&taskId=ub49a46a4-439d-4766-ac4e-b856a169476&title=&width=226)<font style="color:rgb(51, 51, 51);">可以看到，整个转账的业务还没有执行完毕，act-001 账户的余额已经被修改为 30000了，为什么修改为 30000了，因为JDBC事务默认情况下是自动提交，只要执行一条DML语句则自动提交一次。这种自动提交是极其危险的。如果在此时程序发生了异常，act-002账户的余额未成功更新，则钱会丢失一万。我们可以测试一下：测试前先将数据恢复到起初的时候</font>![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712912419988-1a2030f1-6603-47a8-9d25-224f767322ea.png#averageHue=%23e4cd91&clientId=u97001951-01ca-4&from=paste&height=66&id=u315a789b&originHeight=66&originWidth=220&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2453&status=done&style=shadow&taskId=u689e596d-44f7-4cd1-8a17-09505c1a74c&title=&width=220)<font style="color:rgb(51, 51, 51);">在以下代码位置，让其发生异常：</font>![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712912470809-0f61ba45-3562-4531-8fa9-d1d5efba0b81.png#averageHue=%23302f2c&clientId=u97001951-01ca-4&from=paste&height=439&id=u3bd9f666&originHeight=439&originWidth=840&originalType=binary&ratio=1&rotation=0&showTitle=false&size=63429&status=done&style=none&taskId=u60a55628-103d-4326-a67b-ffaf8b4a37c&title=&width=840)<font style="color:rgb(51, 51, 51);">执行结果如下：</font>![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712912493027-d440b333-56ea-4995-935f-fd45355d8750.png#averageHue=%23322d2c&clientId=u97001951-01ca-4&from=paste&height=78&id=uc1d9654f&originHeight=78&originWidth=1298&originalType=binary&ratio=1&rotation=0&showTitle=false&size=18800&status=done&style=none&taskId=u0a612972-bba6-4f53-8491-4e4080fe61a&title=&width=1298)![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712912515925-d895e1d5-14c1-4858-8fe0-eab02faa8100.png#averageHue=%23d3ac6d&clientId=u97001951-01ca-4&from=paste&height=80&id=uda3f3356&originHeight=80&originWidth=217&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2500&status=done&style=none&taskId=ue40ea47f-e486-4281-8655-0de79757e1a&title=&width=217)<font style="color:rgb(51, 51, 51);">经过测试得知，丢失了一万元。</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=pDSoJ&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## <font style="color:rgb(51, 51, 51);">添加事务控制</font>
<font style="color:rgb(51, 51, 51);">如何解决以上问题，分三步：</font><font style="color:rgb(51, 51, 51);">第一步：将JDBC事务的自动提交机制修改为手动提交（即开启事务）</font>

<font style="color:rgb(51, 51, 51);">conn.setAutoCommit(false);</font>

<font style="color:rgb(51, 51, 51);">第二步：当整个业务完整结束后，手动提交事务（即提交事务，事务结束）</font>

<font style="color:rgb(51, 51, 51);">conn.commit();</font>

<font style="color:rgb(51, 51, 51);">第三步：在处理业务过程中，如果发生异常，则进入catch语句块进行异常处理，手动回滚事务（即回滚事务，事务结束）</font>

<font style="color:rgb(51, 51, 51);">conn.rollback();</font>

<font style="color:rgb(51, 51, 51);">代码如下：</font>

```plain
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

<font style="color:rgb(51, 51, 51);">将数据恢复如初：</font>![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712913009901-fda0cf51-2d89-4aed-907c-92803e51370a.png#averageHue=%23e4cd91&clientId=u97001951-01ca-4&from=paste&height=67&id=ue9b4ea30&originHeight=67&originWidth=214&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2451&status=done&style=none&taskId=u6166f100-beb6-4bf6-a902-c89810f708f&title=&width=214)<font style="color:rgb(51, 51, 51);">执行程序，仍然会出现异常：</font>![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712913037024-0052d9be-b8d1-4999-8449-8e574ff77b7b.png#averageHue=%23332d2c&clientId=u97001951-01ca-4&from=paste&height=125&id=u06ce920e&originHeight=125&originWidth=1588&originalType=binary&ratio=1&rotation=0&showTitle=false&size=36811&status=done&style=none&taskId=ud1dac9aa-e898-49ee-ac1c-baaaa07a47a&title=&width=1588)<font style="color:rgb(51, 51, 51);">但是数据库表中的数据是安全的：</font>![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712913054649-53befbcc-2748-433c-9f27-6c2dca4a1bd6.png#averageHue=%23d3ac6e&clientId=u97001951-01ca-4&from=paste&height=79&id=u7f62bbd8&originHeight=79&originWidth=221&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2524&status=done&style=none&taskId=u08b27fbc-4242-4975-a808-915f75e0f8a&title=&width=221)<font style="color:rgb(51, 51, 51);">当程序不出现异常时：</font>![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712913078723-158ff1de-43b9-4ae0-b1c5-68dc011ec2c7.png#averageHue=%232f2e2d&clientId=u97001951-01ca-4&from=paste&height=130&id=u253e2ea4&originHeight=130&originWidth=545&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10501&status=done&style=none&taskId=u7dbd8a8c-de19-4fcc-b76f-f46e22d3aa4&title=&width=545)<font style="color:rgb(51, 51, 51);">数据库表中的数据也是正确的：</font>![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712913097670-fd86b9a8-dab3-4bab-b5b5-ccfff28e1cba.png#averageHue=%23d5af70&clientId=u97001951-01ca-4&from=paste&height=99&id=ud6fe728c&originHeight=99&originWidth=201&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3862&status=done&style=none&taskId=u8b00c2e2-226c-45e2-8384-f91f1132a53&title=&width=201)<font style="color:rgb(51, 51, 51);">这样就采用了JDBC事务解决了数据安全的问题。</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=nEZmX&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

# <font style="color:rgb(51, 51, 51);">设置JDBC事务隔离级别</font>
<font style="color:rgb(51, 51, 51);">关于事务隔离级别相关内容另请参见：老杜发布的2024版MySQL教程。</font><font style="color:rgb(51, 51, 51);">设置事务的隔离级别也是比较重要的，在JDBC程序中应该如何设置事务的隔离级别呢？代码如下：</font>

```plain
public class JDBCTest20 {
    public static void main(String[] args) {
        Connection conn = null;
        try {
            conn = DbUtils.getConnection();
            conn.setTransactionIsolation(Connection.TRANSACTION_SERIALIZABLE);
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            DbUtils.close(conn, null, null);
        }
    }
}
```

<font style="color:rgb(51, 51, 51);">  
</font>![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=O8j9i&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

# <font style="color:rgb(51, 51, 51);">在MySQL中创建存储过程</font>

```plain
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

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=eRzbv&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

# <font style="color:rgb(51, 51, 51);">使用JDBC代码调用存储过程</font>

```plain
package com.powernode.jdbc;

import com.powernode.jdbc.utils.DbUtils;

import java.sql.CallableStatement;
import java.sql.Connection;
import java.sql.SQLException;
import java.sql.Types;

/**
 * ClassName: JDBCTest21
 * Description:
 * Datetime: 2024/4/12 17:42
 * Author: 老杜@动力节点
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

<font style="color:rgb(51, 51, 51);">执行结果：</font>![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1712915314800-457530dc-85bd-4592-b0e7-595349fb92cb.png#averageHue=%239e886a&clientId=u5cc1386e-7362-4&from=paste&height=99&id=u799c12bb&originHeight=99&originWidth=212&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5633&status=done&style=none&taskId=u00e009ad-cade-410a-88fb-32c53ff16b4&title=&width=212)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=G93kN&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

<font style="color:rgb(51, 51, 51);">程序解说：</font><font style="color:rgb(51, 51, 51);">使用JDBC代码调用存储过程需要以下步骤：</font>

1. <font style="color:rgb(51, 51, 51);">加载MySQL的JDBC驱动程序</font>

<font style="color:rgb(51, 51, 51);">使用以下代码加载MySQL的JDBC驱动程序：</font>

<font style="color:rgb(51, 51, 51);">Class.forName("com.mysql.jdbc.Driver");</font>

1. <font style="color:rgb(51, 51, 51);">连接到MySQL数据库</font>

<font style="color:rgb(51, 51, 51);">使用以下代码连接到MySQL数据库：</font>

<font style="color:rgb(51, 51, 51);">Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb", "user", "password");</font>

<font style="color:rgb(51, 51, 51);">其中，第一个参数为连接字符串，按照实际情况修改；第二个参数为用户名，按照实际情况修改；第三个参数为密码，按照实际情况修改。</font>

1. <font style="color:rgb(51, 51, 51);">创建CallableStatement对象</font>

<font style="color:rgb(51, 51, 51);">使用以下代码创建CallableStatement对象：</font>

<font style="color:rgb(51, 51, 51);">CallableStatement cstmt = conn.prepareCall("{call mypro(?, ?)}");</font>

<font style="color:rgb(51, 51, 51);">其中，第一个参数为调用存储过程的语句，按照实际情况修改；第二个参数是需要设定的参数。</font>

1. <font style="color:rgb(51, 51, 51);">设置输入参数</font>

<font style="color:rgb(51, 51, 51);">使用以下代码设置输入参数：</font>

<font style="color:rgb(51, 51, 51);">cstmt.setInt(1, n);</font>

<font style="color:rgb(51, 51, 51);">其中，第一个参数是参数在调用语句中的位置，第二个参数是实际要传入的值。</font>

1. <font style="color:rgb(51, 51, 51);">注册输出参数</font>

<font style="color:rgb(51, 51, 51);">使用以下代码注册输出参数：</font>

<font style="color:rgb(51, 51, 51);">cstmt.registerOutParameter(2, Types.INTEGER);</font>

<font style="color:rgb(51, 51, 51);">其中，第一个参数是要注册的参数在调用语句中的位置，第二个参数是输出参数的类型。</font>

1. <font style="color:rgb(51, 51, 51);">执行存储过程</font>

<font style="color:rgb(51, 51, 51);">使用以下代码执行存储过程：</font>

<font style="color:rgb(51, 51, 51);">cstmt.execute();</font>

1. <font style="color:rgb(51, 51, 51);">获取输出参数值</font>

<font style="color:rgb(51, 51, 51);">使用以下代码获取输出参数的值：</font>

<font style="color:rgb(51, 51, 51);">int sum = cstmt.getInt(2);</font>

<font style="color:rgb(51, 51, 51);">其中，第一个参数是输出参数在调用语句中的位置。</font>

1. <font style="color:rgb(51, 51, 51);">关闭连接</font>

<font style="color:rgb(51, 51, 51);">使用以下代码关闭连接和语句对象：</font>

```plain
cstmt.close();
conn.close();
```

<font style="color:rgb(51, 51, 51);">上述代码中，可以根据实际情况适当修改存储过程名、参数传递方式、参数类型等内容。</font>

<font style="color:rgb(51, 51, 51);">  
</font>![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=O8j9i&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

# <font style="color:rgb(51, 51, 51);">数据库表的准备</font>

```plain
drop table if exists t_employee;

create table t_employee(
  id bigint primary key auto_increment,
  name varchar(255),
  job varchar(255),
  hiredate char(10),
  salary decimal(10,2),
  address varchar(255)
);

insert into t_employee(name,job,hiredate,salary,address) values('张三','销售员','1999-10-11',5000.0,'北京朝阳');
insert into t_employee(name,job,hiredate,salary,address) values('李四','编码人员','1998-02-12',5000.0,'北京海淀');
insert into t_employee(name,job,hiredate,salary,address) values('王五','项目经理','2000-08-11',5000.0,'北京大兴');
insert into t_employee(name,job,hiredate,salary,address) values('赵六','产品经理','2022-09-11',5000.0,'北京东城');
insert into t_employee(name,job,hiredate,salary,address) values('钱七','测试员','2024-12-11',5000.0,'北京西城');

commit;

select * from t_employee;
```

![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1713071562929-40bc3b9b-59e0-4447-a6d2-ee9a402112d7.png#averageHue=%23161412&clientId=u0929d9a6-cc56-4&from=paste&height=215&id=uc93280dc&originHeight=215&originWidth=785&originalType=binary&ratio=1&rotation=0&showTitle=false&size=30172&status=done&style=none&taskId=u89bc78cb-d7b8-4d61-8c0d-3ab3a620ad7&title=&width=785)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=Tit1x&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

# <font style="color:rgb(51, 51, 51);">实现效果</font>
## <font style="color:rgb(51, 51, 51);">查看员工列表</font>
![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1713087932128-c20f65b8-19f2-435d-b926-4fcf9e76942b.png#averageHue=%23222326&clientId=u51a6216a-4bdd-4&from=paste&height=465&id=ubd9d0e1b&originHeight=465&originWidth=633&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15839&status=done&style=none&taskId=u5b9c816e-73d5-4892-8517-e1e5c7d7e4d&title=&width=633)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=eJf90&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## <font style="color:rgb(51, 51, 51);">查看员工详情</font>
![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1713087955719-046dd8f5-0e08-464b-99f2-e3082468e90d.png#averageHue=%23222326&clientId=u51a6216a-4bdd-4&from=paste&height=675&id=u6e8c1a73&originHeight=675&originWidth=589&originalType=binary&ratio=1&rotation=0&showTitle=false&size=27719&status=done&style=none&taskId=u69513093-6a8c-4064-a1f2-ad2aa7906c1&title=&width=589)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=sDZ4B&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## <font style="color:rgb(51, 51, 51);">新增员工</font>
![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1713088066941-2485c84a-81e3-4bed-b60b-d5ab1ce1e519.png#averageHue=%23222326&clientId=u51a6216a-4bdd-4&from=paste&height=621&id=u41b83656&originHeight=621&originWidth=624&originalType=binary&ratio=1&rotation=0&showTitle=false&size=26277&status=done&style=none&taskId=uee76f7c1-1123-42a8-8f30-49ae8c70a9d&title=&width=624)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=o3IRP&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## <font style="color:rgb(51, 51, 51);">修改员工</font>
![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1713088222666-785c5584-713d-45a0-b043-5df952816849.png#averageHue=%23212226&clientId=u51a6216a-4bdd-4&from=paste&height=811&id=u61d10dbc&originHeight=811&originWidth=489&originalType=binary&ratio=1&rotation=0&showTitle=false&size=38407&status=done&style=none&taskId=uc8d4c2e4-6e41-4c0f-b589-eb6705e34dc&title=&width=489)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=QMw6x&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## <font style="color:rgb(51, 51, 51);">删除员工</font>
![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1713088256331-8e3f1218-7136-4af7-957b-4ef3ed59fb30.png#averageHue=%23212226&clientId=u51a6216a-4bdd-4&from=paste&height=728&id=u273d2b97&originHeight=728&originWidth=629&originalType=binary&ratio=1&rotation=0&showTitle=false&size=22918&status=done&style=none&taskId=u0e89aba5-394b-48bb-82b5-693157a38a2&title=&width=629)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=e9yPL&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## <font style="color:rgb(51, 51, 51);">退出系统</font>
![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1713088276650-2f1eb4aa-10aa-45ac-b280-fd195590c294.png#averageHue=%23242529&clientId=u51a6216a-4bdd-4&from=paste&height=304&id=u8ff9e92f&originHeight=304&originWidth=581&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11582&status=done&style=none&taskId=ud6a33007-f21a-4260-84ec-c7e93dac5e8&title=&width=581)<font style="color:rgb(51, 51, 51);">  
</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=O8j9i&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

# <font style="color:rgb(51, 51, 51);">什么是DAO</font>
<font style="color:rgb(51, 51, 51);">DAO是：Data Access Object，翻译为：数据访问对象。  
</font><font style="color:rgb(51, 51, 51);">一种JavaEE的设计模式，专门用来做数据增删改查的类。  
</font><font style="color:rgb(51, 51, 51);">在实际的开发中，通常我们会将数据库的操作封装为一个单独的DAO去完成，这样做的目的是：提高代码的复用性，另外也可以降低程序的耦合度，提高扩展力。  
</font><font style="color:rgb(51, 51, 51);">例如：操作用户数据的叫做UserDao，操作员工数据的叫做EmployeeDao，操作产品数据的叫做ProductDao，操作订单数据的叫做OrderDao等。</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=B8M6O&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

# <font style="color:rgb(51, 51, 51);">使用DAO改造员工信息管理</font>
## <font style="color:rgb(51, 51, 51);">定义Employee封装数据</font>
<font style="color:rgb(51, 51, 51);">Employee类是一个Java Bean，专门用来封装员工的信息：</font>

```java
package com.powernode.jdbc.beans;

/**
 * ClassName: Employee
 * Description:
 * Datetime: 2024/4/14 23:32
 * Author: 老杜@动力节点
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

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=ZQhjT&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## <font style="color:rgb(51, 51, 51);">定义EmployeeDao</font>
<font style="color:rgb(51, 51, 51);">定义五个方法，分别完成五个功能：新增，修改，删除，查看一个，查看所有。</font>

```java
package com.powernode.jdbc.dao;

import com.powernode.jdbc.beans.Employee;
import com.powernode.jdbc.utils.DbUtils;

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
 * Author: 老杜@动力节点
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

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=QuvZJ&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

# <font style="color:rgb(51, 51, 51);">BaseDao的封装</font>

```java
package com.powernode.jdbc.dao;

import com.powernode.jdbc.utils.DbUtils;

import java.lang.reflect.Field;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

/**
 * ClassName: BaseDao
 * Description: 最基础的Dao，所有的Dao应该去继承该BaseDao
 * Datetime: 2024/4/15 11:08
 * Author: 老杜@动力节点
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

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=sQZNC&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=QuvZJ&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

# <font style="color:rgb(51, 51, 51);">连接池的理解</font>
## <font style="color:rgb(51, 51, 51);">不使用连接池有啥问题</font>
<font style="color:rgb(51, 51, 51);">Connection对象是重量级对象，创建Connection对象就是建立两个进程之间的通信，非常耗费资源。一次完整的数据库操作，大部分时间都耗费在连接对象的创建。</font><font style="color:rgb(51, 51, 51);">第一个问题：每一次请求都创建一个Connection连接对象，效率较低。</font><font style="color:rgb(51, 51, 51);">第二个问题：连接对象的数量无法限制。如果连接对象的数量过高，会导致mysql数据库服务器崩溃。</font>

## <font style="color:rgb(51, 51, 51);">使用连接池来解决什么问题</font>
<font style="color:rgb(51, 51, 51);">提前创建好N个连接对象，将其存放到一个集合中（这个集合就是一个缓存）。</font><font style="color:rgb(51, 51, 51);">用户请求时，需要连接对象直接从连接池中获取，不需要创建连接对象，因此效率较高。</font><font style="color:rgb(51, 51, 51);">另外，连接对象只能从连接池中获取，如果没有空闲的连接对象，只能等待，这样连接对象创建的数量就得到了控制。</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=EwEtJ&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## <font style="color:rgb(51, 51, 51);">javax.sql.DataSource</font>
<font style="color:rgb(51, 51, 51);">连接池有很多，不过所有的连接池都实现了 javax.sql.DataSource 接口。也就是说我们程序员在使用连接池的时候，不管使用哪家的连接池产品，只要面向javax.sql.DataSource接口调用方法即可。</font>

<font style="color:rgb(51, 51, 51);">另外，实际上我们也可以自定义属于我们自己的连接池。只要实现DataSource接口即可。</font>

## <font style="color:rgb(51, 51, 51);">连接池的属性</font>
<font style="color:rgb(51, 51, 51);">对于一个基本的连接池来说，一般都包含以下几个常见的属性：</font>

1. <font style="color:rgb(51, 51, 51);">初始化连接数（initialSize）：连接池初始化时创建的连接数。 </font>
2. <font style="color:rgb(51, 51, 51);">最大连接数（maxActive）：连接池中最大的连接数，也就是连接池所能容纳的最大连接数量，当连接池中的连接数量达到此值时，后续请求会被阻塞并等待连接池中有连接被释放后再处理。 </font>
3. <font style="color:rgb(51, 51, 51);">最小空闲连接数量（minIdle）： 指连接池中最小的空闲连接数，也就是即使当前没有请求，连接池中至少也要保持一定数量的空闲连接，以便应对高并发请求或突发连接请求的情况。</font>
4. <font style="color:rgb(51, 51, 51);">最大空闲连接数量（maxIdle）： 指连接池中最大的空闲连接数，也就是连接池中最多允许保持的空闲连接数量。当连接池中的空闲连接数量达到了maxIdle设定的值后，多余的空闲连接将会被连接池释放掉。</font>
5. <font style="color:rgb(51, 51, 51);">最大等待时间（maxWait）：当连接池中的连接数量达到最大值时，后续请求需要等待的最大时间，如果超过这个时间，则会抛出异常。 </font>
6. <font style="color:rgb(51, 51, 51);">连接有效性检查（testOnBorrow、testOnReturn）：为了确保连接池中只有可用的连接，一些连接池会定期对连接进行有效性检查，这里的属性就是配置这些检查的选项。 </font>
7. <font style="color:rgb(51, 51, 51);">连接的driver、url、user、password等。 </font>

<font style="color:rgb(51, 51, 51);">以上这些属性是连接池中较为常见的一些属性，不同的连接池在实现时可能还会有其他的一些属性，不过大多数连接池都包含了以上几个属性，对于使用者来说需要根据自己的需要进行灵活配置。</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=gbJUU&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

# <font style="color:rgb(51, 51, 51);">常用的连接池</font>
<font style="color:rgb(51, 51, 51);">市面上常用的数据库连接池有许多，以下是其中几种：</font>

1. <font style="color:rgb(51, 51, 51);">DBCP</font>
    1. <font style="color:rgb(51, 51, 51);">2001年诞生，最早的连接池。</font>
    2. <font style="color:rgb(51, 51, 51);">Apache Software Foundation的一个开源项目。</font>
    3. <font style="color:rgb(51, 51, 51);">DBCP的设计初衷是为了满足Tomcat服务器对连接池管理的需求。</font>
2. <font style="color:rgb(51, 51, 51);">c3p0</font>
    1. <font style="color:rgb(51, 51, 51);">2004年诞生</font>
    2. <font style="color:rgb(51, 51, 51);">c3p0是由Steve Waldman于2004年推出的，它是一个高性能、高可靠性、易配置的数据库连接池。c3p0能够提供连接池的容错能力、自动重连等功能，适用于高并发场景和数据量大的应用。</font>
3. <font style="color:rgb(51, 51, 51);">Druid</font>
    1. <font style="color:rgb(51, 51, 51);">2012年诞生</font>
    2. <font style="color:rgb(51, 51, 51);">Druid连接池由阿里巴巴集团开发，于2011年底开始对外公开，2012年正式发布。Druid是一个具有高性能、高可靠性、丰富功能的数据库连接池，不仅可以做连接池，还能做监控、分析和管理数据库，支持SQL防火墙、统计分析、缓存和访问控制等功能。</font>
4. <font style="color:rgb(51, 51, 51);">HikariCP</font>
    1. <font style="color:rgb(51, 51, 51);">2012年诞生</font>
    2. <font style="color:rgb(51, 51, 51);">HikariCP是由Brett Wooldridge于2012年创建的开源项目，它被认为是Java语言下最快的连接池之一，具有快速启动、低延迟、低资源消耗等优点。HikariCP连接池适用于高并发场景和云端应用。</font>
    3. <font style="color:rgb(51, 51, 51);">很单纯的一个连接池，这个产品只做连接池应该做的，其他的不做。所以性能是极致的。相对于Druid来说，它更加轻量级。</font>
    4. <font style="color:rgb(51, 51, 51);">Druid连接池在连接管理之外提供了更多的功能，例如SQL防火墙、统计分析、缓存、访问控制等，适用于在数据库访问过程中，需要进行细粒度控制的场景</font>
    5. <font style="color:rgb(51, 51, 51);">HikariCP则更侧重于性能方面的优化，对各种数据库的兼容性也更好</font>
5. <font style="color:rgb(51, 51, 51);">BoneCP</font>
    1. <font style="color:rgb(51, 51, 51);">2015年诞生</font>
    2. <font style="color:rgb(51, 51, 51);">BoneCP是一款Java语言下的高性能连接池，于2015年由Dominik Gruntz在GitHub上发布。BoneCP具有分布式事务、连接空闲检查、SQL语句跟踪和性能分析、特定类型的连接池等特点。BoneCP连接池适用于大型应用系统和高并发的负载场景</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=GF4Pn&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

# <font style="color:rgb(51, 51, 51);">连接池的使用</font>
## <font style="color:rgb(51, 51, 51);">Druid的使用</font>
<font style="color:rgb(51, 51, 51);">第一步：引入Druid的jar包</font>![](https://cdn.nlark.com/yuque/0/2024/png/21376908/1713164785681-0fdb049c-2a06-40e4-83cd-bfc876d8b696.png#averageHue=%23fdfcfb&clientId=u80e8c903-6055-4&from=paste&height=66&id=u7fa2aef7&originHeight=66&originWidth=180&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1594&status=done&style=shadow&taskId=u1da80432-7b19-4905-a407-56e3e288d88&title=&width=180)<font style="color:rgb(51, 51, 51);">第二步：配置文件</font><font style="color:rgb(51, 51, 51);">在类的根路径下创建一个属性资源文件：jdbc.properties</font>

```plain
url=jdbc:mysql://localhost:3306/jdbc
username=root
password=1234
driverClassName=com.mysql.cj.jdbc.Driver
initialSize=5
minIdle=10
maxActive=20
```

<font style="color:rgb(51, 51, 51);">第三步：编写代码，从连接池中获取连接对象</font>

```plain
// 读取属性配置文件
InputStream in = DruidConfig.class.getClassLoader().getResourceAsStream("jdbc.properties");
Properties props = new Properties();
props.load(in);
// 创建连接池
DataSource dataSource = DruidDataSourceFactory.createDataSource(props);
Connection conn = dataSource.getConnection();
```

<font style="color:rgb(51, 51, 51);">第四步：关闭连接</font><font style="color:rgb(51, 51, 51);">仍然调用Connection的close()方法，但是这个close()方法并不是真正的关闭连接，只是将连接归还到连接池，让其称为空闲连接对象。这样其他线程可以继续使用该空闲连接。</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=jWx0g&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

## <font style="color:rgb(51, 51, 51);">HikariCP的使用</font>
<font style="color:rgb(51, 51, 51);">第一步：引入jar包</font><font style="color:rgb(51, 51, 51);">第二步：编写配置文件</font><font style="color:rgb(51, 51, 51);">在类的根路径下创建一个属性资源文件：jdbc2.properties</font>

```plain
jdbcUrl=jdbc:mysql://localhost:3306/jdbc
username=root
password=1234
driverClassName=com.mysql.cj.jdbc.Driver
minimumIdle=5
maximumPoolSize=20
```

<font style="color:rgb(51, 51, 51);">第三步：编写代码，从连接池中获取连接</font>

```plain
InputStream in = HikariConfig.class.getClassLoader().getResourceAsStream("config.properties");
props.load(in);
HikariConfig config = new HikariConfig(props);
DataSource dataSource = new HikariDataSource(config);
Connection conn = dataSource.getConnection();
```

<font style="color:rgb(51, 51, 51);">第四步：关闭连接（调用conn.close()，将连接归还到连接池，连接对象为空闲状态。）</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1692002570088-3338946f-42b3-4174-8910-7e749c31e950.jpeg#averageHue=%23f9f8f8&from=url&id=ReZzm&originHeight=78&originWidth=1400&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=shadow&title=)

<font style="color:rgb(51, 51, 51);">  
</font>
