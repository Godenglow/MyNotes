# 🥽 课件&资料


> 课件（老杜原版笔记）：[老杜MyBatis--原版:【https://www.yuque.com/zuihoudewu/java_note/mt2812】](https://www.yuque.com/zuihoudewu/java_note/mt2812)  
资料：[【https://pan.baidu.com/s/1SsN1Zbs-VrJBqlLbvL5k7g?pwd=1234 】](https://pan.baidu.com/s/1SsN1Zbs-VrJBqlLbvL5k7g?pwd=1234)  
提取码：1234
>



# 🥽 Mybatis下载


[【Mybatis github地址：https://github.com/mybatis/mybatis-3】](https://github.com/mybatis/mybatis-3)



![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851532930-16b0cac0-1ba8-44a2-95ca-ccd8a518fdd7.png)  
![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851532912-6e157c74-0762-4a38-96e5-55da810382f4.png)  
![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851532931-70844217-1baa-4ce4-b099-93b558fc427e.png)  
![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851532937-3b46bb26-05c5-43cc-88e0-23ac73da7480.png)



[【Mybatis中文使用手册：Mybatis中文网 https://mybatis.net.cn/】](https://mybatis.net.cn/)



# 🥽 了解Mybatis


+ MyBatis本质上就是对JDBC的封装，通过MyBatis完成CRUD。
+ MyBatis在三层架构中负责持久层的，属于持久层框架。



## 🌊 ORM思想


+ ORM：对象关系映射 
    - O（Object）：Java虚拟机中的Java对象
    - R（Relational）：关系型数据库
    - M（Mapping）：映射，将Java虚拟机中的Java对象映射到数据库表中⼀⾏记录，或是将数据库表中⼀⾏记录映射成Java虚拟机中的⼀个Java对象。
+ 在ORM思想中，一个Java类对应数据库中一个表，该Java类实例化出来的对象对应数据库表中的一条记录，其中Java对象到数据库表中每条记录的对应关系为映射。
+ 在ORM中，数据库表对应的Java类被称为pojo(普通Java类)、javabean(咖啡豆)或domain(邻域模型)。  
![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851532990-49d94258-af1c-4bec-be6a-8c2b36339e43.png)



## 🌊 Mybatis与ORM


+ Mybatis可以实现Java对象与数据库表中一条记录的映射。
+ MyBatis属于半⾃动化ORM框架。MyBatis中SQL语句需要我们自己编写。
+ Hibernate属于全⾃动化的ORM框架。Hibernate中SQL语句不需要我们自己编写，SQL语句可以自动生成。



![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851533511-6905f39a-7b89-4463-a3a7-8d8a06227cb7.png)



## 🌊 MyBatis框架特点


+ ⽀持定制化 SQL、存储过程、基本映射以及⾼级映射
+ 避免了⼏乎所有的 JDBC 代码中⼿动设置参数以及获取结果集
+ ⽀持XML开发，也⽀持注解式开发。【为了保证sql语句的灵活，所以mybatis⼤部分是采⽤XML⽅式开发。】
+ 将接⼝和 Java 的 POJOs(Plain Ordinary Java Object，简单普通的Java对象)映射成数据库中的记录
+ 体积⼩好学：两个jar包，两个XML配置⽂件。
+ 完全做到sql解耦合。
+ 提供了基本映射标签。
+ 提供了⾼级映射标签。
+ 提供了XML标签，⽀持动态SQL的编写。
+ ......



# 🥽 Mybatis入门程序


## 🌊 数据库表的准备


+ 准备数据库表：汽⻋表t_car，字段包括： 
    - 数据库中字段名小写，单词之间使用下划线分割
    - id：主键（⾃增）【bigint】
    - car_num：汽⻋编号【varchar】
    - brand：品牌【varchar】
    - guide_price：⼚家指导价【decimal类型，专⻔为财务数据准备的类型】
    - produce_time：⽣产时间【char，年⽉⽇即可，10个⻓度，'2022-10-11'】
    - car_type：汽⻋类型（燃油⻋、电⻋、氢能源）【varchar】



```sql
# 创建数据库
CREATE DATABASE mybatis_study;
# 使用数据库
USE mybatis_study;
# 创建表 汽⻋表t_car
CREATE TABLE t_car(
    id BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT '自然主键',
    car_num VARCHAR(255) COMMENT '汽车编号',
    brand VARCHAR(255) COMMENT '汽车品牌',
    guide_price DECIMAL(10, 2) COMMENT '厂家指导价',
    produce_time CHAR(10) COMMENT '生产时间 如：2022-10-11',
    car_type VARCHAR(255) COMMENT '汽车类型'
);
# 添加数据
INSERT INTO t_car(car_num, brand, guide_price, produce_time, car_type)
VALUES ('1001', '宝马520Li', 10.00, '2022-10-11', '燃油车'),
       ('1002', '奔驰E300L', 55.00, '2022-11-11', '新能源');
```



![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851533564-b30936b5-fd94-4ecf-840d-9bbb99ff6ce9.png)



## 🌊 创建Project


建议创建Empty Project，设置Java版本以及编译版本等。  
![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851533589-20292eae-bfbd-4044-9220-11784976311a.png)  
![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851533608-a22113aa-5251-4b23-a76f-9d597d8426ca.png)  
![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851533764-cdbb04e1-ec64-4176-b457-ad5b108837a6.png)  
![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851534202-484b80ac-7862-4eb1-82cc-e2f4ee977f07.png)  
![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851534288-b540af42-5a3b-436b-b5f6-91bfcd6c564c.png)



## 🌊 创建Module


普通的Maven Java模块



![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851534405-b8d34179-c03b-4bb7-8467-cf7e10635f8e.png)  
![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851534245-0994194a-c70c-42f1-bdff-21d873950a1c.png)  
![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851534651-e0c3d53a-26f9-47db-b8ab-ca77a44b364e.png)



> resources用于存放配置文件或资源文件，放在该目录下的文件，相当于放到了类的根路径下。  
不管是maven还是普通的java模块,只要是idea文件夹中变成蓝色的部分,就是可以理解为类路径的起始地点(之后的编译就是由蓝色文件夹开始算类路径)  
自定义文件夹后用idea标记为resource后的文件夹也会被最终打包到类路径下  
![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851534745-31b26443-026b-4497-87f7-50b2c3cc2332.png)
>



## 🌊 设置打包⽅式


设置打包⽅式为jar（不需要war，因为mybatis封装的是jdbc。）



```xml
    <!-- 打包方式 -->
    <packaging>jar</packaging>
```



## 🌊 引⼊依赖


mybatis依赖 + mysql驱动依赖



```xml
    <dependencies>
        <!--mybatis核⼼依赖-->
        <dependency>
            <groupId>org.mybatis</groupId>
            <artifactId>mybatis</artifactId>
            <version>3.5.10</version>
        </dependency>
        <!--mysql驱动依赖-->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>8.0.30</version>
        </dependency>
    </dependencies>
```



## 🌊 编写mybatis核心配置文件：mybatis-config.xml


+ 从 XML 中构建 SqlSessionFactory 
    - 通过官方的这句话，你能想到什么呢？ 
        * 第一：在MyBatis中一定是有一个很重要的对象，这个对象是：SqlSessionFactory对象。
        * 第二：SqlSessionFactory对象的创建需要XML。
    - XML是什么？ 
        * 它一定是一个配置文件。
+ 注意： 
    - 第一：这个文件名不是必须叫做mybatis-config.xml，可以用其他的名字。只是大家都采用这个名字。
    - 第二：这个文件存放的位置也不是固定的，可以随意，但一般情况下，会放到类的根路径下。(打包后在classes的目录下)
+ mybatis-config.xml文件中的配置信息不理解没关系，先把连接数据库的信息修改以下即可。
+ 其他的别动。



![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851534945-d89ebd78-3d24-4573-9d56-815a2524e6fe.png)



```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE configuration
        PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
    <environments default="development">
        <environment id="development">
            <transactionManager type="JDBC"/>
            <dataSource type="POOLED">
            	<!-- 修改链接数据库的配置信息 -->
                <property name="driver" value="com.mysql.cj.jdbc.Driver"/>
                <property name="url" value="jdbc:mysql://localhost:3306/po
wernode"/>
                <property name="username" value="root"/>
                <property name="password" value="123456"/>
            </dataSource>
        </environment>
    </environments>
    <mappers>
        <!--sql映射⽂件创建好之后，需要将该⽂件路径配置到这⾥-->
        <mapper resource=""/>
    </mappers>
</configuration>
```



## 🌊 mybatis中有两个主要的配置文件：


+ 其中一个是：mybatis-config.xml，这是核心配置文件，主要配置连接数据库的信息等。（一个）
+ 另一个是：XxxxMapper.xml，这个文件是专门用来编写SQL语句的配置文件。（一个表一个） 
    - t_user表，一般会对应一个UserMapper.xml
    - t_student表，一般会对应一个StudentMapper.xml



## 🌊 编写XxxxMapper.xml文件


+ 在这个配置文件当中编写SQL语句。
+ 这个文件名也不是固定的，放的位置也不是固定，我们这里给它起个名字，叫做：CarMapper.xml
+ 把它暂时放到类的根路径下。



![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851534908-ad467fbf-678e-418b-8c47-08e624631f0a.png)



```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<!--namespace先随意写⼀个-->
<mapper namespace="car">
    <!--insert sql：保存⼀个汽⻋信息-->
    <!-- id 是这条SQL语句的唯一标识，这个id就代表了这条SQL语句 -->
    <insert id="insertCar">
        insert into t_car
            (id,car_num,brand,guide_price,produce_time,car_type)
        values
            (null,'102','丰⽥mirai',40.30,'2014-10-05','氢能源')
    </insert>
</mapper>
```



+ 注意1：sql语句最后结尾可以不写“;”
+ 注意2：CarMapper.xml⽂件的名字不是固定的。可以使⽤其它名字。
+ 注意3：CarMapper.xml⽂件的位置也是随意的。这⾥选择放在resources根下，相当于放到了类的根路径下。



## 🌊 在mybatis-config.xml文件中指定XxxxMapper.xml文件的路径：


+ `<mapper resource="CarMapper.xml"/>`
+ 注意：resource属性会自动从类的根路径下开始查找资源。



```xml
    <mappers>
        <!--sql映射⽂件创建好之后，需要将该⽂件路径配置到这⾥-->
        <!-- resource属性自动会从类的根路径下开始查找资源 -->
        <mapper resource="CarMapper.xml"/>
    </mappers>
```



## 🌊 编写MyBatis程序。


+  使用mybatis的类库，编写mybatis程序，连接数据库，做增删改查就行了。 
+  在MyBatis当中，负责执行SQL语句的那个对象叫做什么呢？ 
    - SqlSession
    - SqlSession是专门用来执行SQL语句的，是一个Java程序和数据库之间的一次会话。
    - 要想获取SqlSession对象，需要先获取SqlSessionFactory对象，通过SqlSessionFactory工厂来生产SqlSession对象。
    - 怎么获取SqlSessionFactory对象呢？ 
        * 需要首先获取SqlSessionFactoryBuilder对象。
        * 通过SqlSessionFactoryBuilder对象的build方法，来获取一个SqlSessionFactory对象。
+  mybatis的核心对象包括： 
    - SqlSessionFactoryBuilder
    - SqlSessionFactory
    - SqlSession
    - SqlSessionFactoryBuilder --> SqlSessionFactory --> SqlSession



![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851535551-31752df8-5447-47d9-98aa-8eac6988af2b.png)



```java
package cw.mybatis;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

import java.io.InputStream;

public class MybatisTest {
    public static void main(String[] args) throws Exception{
        // 获取SqlSessionFactoryBuilder对象
        SqlSessionFactoryBuilder sqlSessionFactoryBuilder = new SqlSessionFactoryBuilder();

        // 获取SqlSessionFactory对象
        InputStream is = Resources.getResourceAsStream("mybatis-config.xml"); // Resources.getResourceAsStream默认就是从类的根路径下开始查找资源。
        //InputStream is = ClassLoader.getSystemClassLoader().getResourceAsStream("mybatis-config.xml");
        SqlSessionFactory sqlSessionFactory = sqlSessionFactoryBuilder.build(is); // 需要传入核心配置文件对应的输入流，一般情况下都是一个数据库对应一个SqlSessionFactory对象。

        // 获取SqlSession对象
        SqlSession sqlSession = sqlSessionFactory.openSession();

        // 执行SQL语句
        int count = sqlSession.insert("insertCar"); // 传入SQL语句对应的id，返回值是影响数据库表当中的记录条数。

        System.out.println("插入了几条记录：" + count);

        // 手动提交
        sqlSession.commit();
    }
}
```



![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851535804-e16ce35a-ae5c-4077-9688-00f1ca158b74.png)  
![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851535371-65e3b37f-d88b-4096-be84-ef43816b9411.png)



## 🌊 关于第一个程序的小细节


+ mybatis中sql语句的结尾";"可以省略。
+ `Resources.getResourceAsStream` 
    - 小技巧：以后凡是遇到resource这个单词，大部分情况下，这种加载资源的方式就是从类的根路径下开始加载。（开始查找）
    - 优点：采用这种方式，从类路径当中加载资源，项目的移植性很强。项目从windows移植到linux，代码不需要修改，因为这个资源文件一直都在类路径当中。
+ `InputStream is = new FileInputStream("d:\\mybatis-config.xml");`  
采用这种方式也可以。 
    - 缺点：可移植性太差，程序不够健壮。可能会移植到其他的操作系统当中。导致以上路径无效，还需要修改java代码中的路径。这样违背了OCP原则。
+ 已经验证了： 
    - mybatis核心配置文件的名字，不一定是：mybatis-config.xml。可以是其它名字。
    - mybatis核心配置文件存放的路径，也不一定是在类的根路径下。可以放到其它位置。但为了项目的移植性，健壮性，最好将这个配置文件放到类路径下面。
+ `InputStream is = ClassLoader.getSystemClassLoader().getResourceAsStream("mybatis-config.xml");` 
    - ClassLoader.getSystemClassLoader() 获取系统的类加载器。
    - 系统类加载器有一个方法叫做：getResourceAsStream，它就是从类路径当中加载资源的。
    - 通过源代码分析发现：`InputStream is = Resources.getResourceAsStream("mybatis-config.xml");`，底层的源代码其实就是：`InputStream is = ClassLoader.getSystemClassLoader().getResourceAsStream("mybatis-config.xml");`
+ CarMapper.xml文件的名字是固定的吗？CarMapper.xml文件的路径是固定的吗？ 
    - 都不是固定的。
    - `<mapper resource="CarMapper.xml"/>` resource属性：这种方式是从类路径当中加载资源。
    - `<mapper url="file:///d:/CarMapper.xml"/>` url属性：这种方式是从绝对路径当中加载资源。（绝对路径前需要加上`file:///`）



## 🌊 关于mybatis的事务管理机制。（深度剖析）


+ 在mybatis-config.xml文件中，可以通过以下的配置进行mybatis的事务管理 
    - `<transactionManager type="JDBC"/>`
    - type属性的值包括两个： 
        * JDBC(jdbc)
        * MANAGED(managed)
        * type后面的值，只有以上两个值可选，不区分大小写。
+ 在mybatis中提供了两种事务管理机制： 
    - 第一种：JDBC事务管理器
    - 第二种：MANAGED事务管理器
+ JDBC事务管理器： 
    - mybatis框架自己管理事务，自己采用原生的JDBC代码去管理事务： 
        * conn.setAutoCommit(false); 开启事务。
        * ....业务处理...
        * conn.commit(); 手动提交事务

```java
// 获取SqlSession对象
SqlSession sqlSession = sqlSessionFactory.openSession(); // 如果使用的事务管理器是JDBC的话，底层实际上会执行：conn.setAutoCommit(false);

// 执行SQL语句
int count = sqlSession.insert("insertCar"); // 返回值是影响数据库表当中的记录条数。

System.out.println("插入了几条记录：" + count);

// 手动提交
sqlSession.commit(); // 如果使用的事务管理器是JDBC的话，底层实际上还是会执行conn.commit();
```

    - 使用JDBC事务管理器的话，底层创建的事务管理器对象：JdbcTransaction对象。
    - 如果你编写的代码是下面的代码：
    - `SqlSession sqlSession = sqlSessionFactory.openSession(true);`，表示没有开启事务。因为这种方式压根不会执行：`conn.setAutoCommit(false);`
    - 在JDBC事务中，没有`执行conn.setAutoCommit(false);`那么autoCommit就是true。如果autoCommit是true，就表示没有开启事务(事务自动提交)。只要执行任意一条DML语句就提交一次。
+ MANAGED事务管理器： 
    - mybatis不再负责事务的管理了。事务管理交给其它容器来负责。例如：spring。我不管事务了，你来负责吧。
    - 对于我们当前的单纯的只有mybatis的情况下，如果配置为：MANAGED，那么事务这块是没人管的。没有人管理事务表示事务压根没有开启。
    - 没有人管理事务就是没有事务。不开启事务，autoCommit是true，就表示没有事务。只要执行任意一条DML语句就提交一次。
+ JDBC中的事务： 
    - 如果你没有在JDBC代码中执行：`conn.setAutoCommit(false);`的话，默认的autoCommit是true。
+ 重点： 
    - 以后注意了，只要你的autoCommit是true，就表示没有开启事务(事务自动提交)。
    - 只有你的autoCommit是false的时候，就表示开启了事务。



## 🌊 MyBatis第⼀个⽐较完整的代码写法


```java
package com.powernode.mybatis.test;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

public class MyBatisCompleteTest {
    public static void main(String[] args) {
        SqlSession sqlSession = null;
        try {
            SqlSessionFactoryBuilder sqlSessionFactoryBuilder = new SqlSessionFactoryBuilder();
            SqlSessionFactory sqlSessionFactory = sqlSessionFactoryBuilder.build(Resources.getResourceAsStream("mybatis-config.xml"));
            // 开启会话（底层会开启事务）
            sqlSession = sqlSessionFactory.openSession();
            // 执行SQL语句，处理相关业务
            int count = sqlSession.insert("insertCar");
            System.out.println(count);
            // 执行到这里，没有发生任何异常，提交事务。终止事务。
            sqlSession.commit();
        } catch (Exception e) {
            // 最好回滚事务
            if (sqlSession != null) {
                sqlSession.rollback();
            }
            e.printStackTrace();
        } finally {
            // 关闭会话（释放资源）
            if (sqlSession != null) {
                sqlSession.close();
            }
        }
    }
}
```



## 🌊 引⼊JUnit


+ JUnit是专⻔做单元测试的组件。
+ 在实际开发中，单元测试⼀般是由我们Java程序员来完成的。
+ 我们要对我们⾃⼰写的每⼀个业务⽅法负责任，要保证每个业务⽅法在进⾏测试的时候都能通过。
+ 测试的过程中涉及到两个概念： 
    - 期望值：执行了这个业务方法之后，你期望的执行结果是多少
    - 实际值：被测试的业务方法的真正执行结果
    - 期望值和实际值相同表示测试通过，期望值和实际值不同则单元测试执⾏时会报错。
+ 引⼊JUnit是为了代替main⽅法。



### 💦 JUnit的使用


第⼀步：引⼊依赖



```xml
<!--junit依赖-->
<dependency>
    <groupId>junit</groupId>
    <artifactId>junit</artifactId>
    <version>4.13.2</version>
    <scope>test</scope>
</dependency>
```



第⼆步：编写单元测试类【测试⽤例】，测试⽤例中每⼀个测试⽅法上使⽤@Test注解进⾏标注



```java
package com.powernode.junit.service;

import org.junit.Assert;
import org.junit.Test;

public class MathServiceTest { // 名字规范：你要测试的类名+Test

    // 单元测试方法写多少个。
    // 一般是一个业务方法对应一个测试方式。
    // 测试方法的规范: public void testXxxx(){}
    // 测试方法的方法名：以test开始。假设测试的方法是sum，这个测试方法名：testSum
    // @Test注解非常重要，被这个注解标注的方法就是一个单元测试方法。
    @Test
    public void testSum(){
        // 单元测试中有两个重要的概念：
        // 一个是：实际值（被测试的业务方法的真正执行结果）
        // 一个是：期望值（执行了这个业务方法之后，你期望的执行结果是多少）
        MathService mathService = new MathService();
        // 获取实际值
        int actual = mathService.sum(1, 2);
        // 期望值
        //int expected = 3;
        int expected = 30;
        // 加断言进行测试
        Assert.assertEquals(expected, actual);
    }

    @Test
    public void testSub(){
        MathService mathService = new MathService();
        // 实际值
        int actual = mathService.sub(10, 5);
        // 期望值
        int expected = 5;
        // 添加断言机制
        Assert.assertEquals(expected, actual);
    }

}
```



## 🌊 关于mybatis集成日志组件。


+ mybatis常见的集成的日志组件有哪些呢？ 
    - SLF4J（沙拉风）：沙拉风是一个日志标准，其中有一个框架叫做logback，它实现了沙拉风规范。
    - LOG4J
    - LOG4J2
    - STDOUT_LOGGING
    - ....
    - 注意：log4j log4j2 logback都是同一个作者开发的。
+ 其中STDOUT_LOGGING是标准日志，mybatis已经实现了这种标准日志。mybatis框架本身已经实现了这种标准。只要开启即可。 
    - 怎么开启呢？在mybatis-config.xml文件中使用settings标签进行配置开启。([可参考mybatis⼿册](https://mybatis.net.cn/configuration.html#settings))

```xml
<settings>
<setting name="logImpl" value="STDOUT_LOGGING"/>
</settings>
```

 

    - 这个标签在编写的时候要注意，它应该出现在environments标签之前。注意顺序。
    - 当然，不需要记忆这个顺序。因为有dtd文件进行约束呢。我们只要参考dtd约束即可。
    - 这种实现也是可以的，可以看到一些信息，比如：连接对象什么时候创建，什么时候关闭，sql语句是怎样的。但是没有详细的日期，线程名字，等。如果你想使用更加丰富的配置，可以集成第三方的log组件。  
![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851535555-d8a5ce7c-a7d0-4950-81c2-dbefde8d5261.png)



### 💦 集成logback日志框架。


logback日志框架实现了slf4j标准。(沙拉风：日志门面。日志标准。)



使用标准日志STDOUT_LOGGING之外的其他日志框架，可以不在mybatis的配置文件中指定 MyBatis 所用日志的具体实现，未指定时将会自动查找，只需要引入相应日志框架的依赖即可。



第一步：引入logback的依赖。



```xml
<!-- 引入logback依赖，logback日志框架实现了slf4j规范 -->
<dependency>
    <groupId>ch.qos.logback</groupId>
    <artifactId>logback-classic</artifactId>
    <version>1.2.11</version>
</dependency>
```



第二步：引入logback所必须的xml配置文件。  
这个配置文件的名字必须叫做：logback.xml或者logback-test.xml，不能是其它的名字。  
这个配置文件必须放到类的根路径下。不能是其他位置。



```xml
<?xml version="1.0" encoding="UTF-8"?>

<configuration debug="false">
    <!-- 控制台输出 -->
    <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
        <encoder class="ch.qos.logback.classic.encoder.PatternLayoutEncoder">
            <!--格式化输出：%d表示日期，%thread表示线程名，%-5level：级别从左显示5个字符宽度%msg：日志消息，%n是换行符-->
            <pattern>[%thread] %-5level %logger{50} - %msg%n</pattern>
        </encoder>
    </appender>

    <!--mybatis log configure-->
    <logger name="com.apache.ibatis" level="TRACE"/>
    <logger name="java.sql.Connection" level="DEBUG"/>
    <logger name="java.sql.Statement" level="DEBUG"/>
    <logger name="java.sql.PreparedStatement" level="DEBUG"/>

    <!-- 日志输出级别,logback日志级别包括五个：TRACE < DEBUG < INFO < WARN < ERROR -->
    <!-- 级别越低输出的信息越多 -->
    <root level="DEBUG">
        <appender-ref ref="STDOUT"/>
        <appender-ref ref="FILE"/>
    </root>

</configuration>
```



![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851535794-e7c37053-fb2e-4144-b284-b79abae49d72.png)



## 🌊 MyBatis⼯具类SqlSessionUtil的封装


```java
package cw.mybatis.utils;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

import java.io.IOException;

/**
 * Mybatis工具类
 */
public class SqlSessionUtils {
    // 工具类的构造方法一般为私有，防止实例化对象
    // 工具类中的方法都是静态的，可以直接采用类名进行调用，不需要new对象，方便调用
    private SqlSessionUtils() {}
    
    private static SqlSessionFactory sqlSessionFactory;
    
    // 类加载时执行
    // SqlSessionUtil工具类在进行第一次加载的时候，解析mybatis-config.xml文件。创建SqlSessionFactory对象。
    static {
        SqlSessionFactoryBuilder sqlSessionFactoryBuilder = new SqlSessionFactoryBuilder();
        // SqlSessionFactory对象：一个SqlSessionFactory对应一个environment，一个environment通常是一个数据库。
        try {
            sqlSessionFactory = sqlSessionFactoryBuilder.build(Resources.getResourceAsStream("mybatis-config.xml"));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
    
    /**
     * 获取数据库会话对象
     * @return 数据库会话对象
     */
    public static SqlSession openSession() {
        // SqlSessionFactoryBuilder sqlSessionFactoryBuilder = new SqlSessionFactoryBuilder();
        // SqlSessionFactory对象：一个SqlSessionFactory对应一个environment，一个environment通常是一个数据库。
        // SqlSessionFactory sqlSessionFactory = sqlSessionFactoryBuilder.build(Resources.getResourceAsStream("mybatis-config.xml"));
        SqlSession sqlSession = sqlSessionFactory.openSession();
        return sqlSession;
    }
}
```



测试：



```java
package cw.mybatis.test;

import cw.mybatis.utils.SqlSessionUtils;
import org.apache.ibatis.session.SqlSession;
import org.junit.Test;

public class SqlSessionUtilsTest {
    @Test
    public void testOpenSession() {
        SqlSession sqlSession = SqlSessionUtils.openSession();
        int count = sqlSession.insert("insertCar");
        System.out.println(count);
        sqlSession.commit();
        sqlSession.close();
    }
}
```



![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851535931-2fe4319a-317d-4433-85e8-aef56c81e331.png)



# 🥽 使用MyBatis完成CRUD


+ CRUD 
    - C: Create增
    - R: Retrieve查（检索）
    - U: Update改
    - D: Delete删



## 🌊 insert


```xml
<!--namespace先随便写-->
<mapper namespace="car">
    <insert id="insertCar">
        insert into t_car(car_num,brand,guide_price,produce_time,car_type) 
      	values('103', '奔驰E300L', 50.3, '2022-01-01', '燃油车')
    </insert>
</mapper>
```



+ 这样写的问题是？ 
    - 值，显然是写死到配置文件中的。
    - 这个在实际开发中是不存在的。
    - 一定是前端的form表单提交过来数据。然后将值传给sql语句。



JDBC的代码是怎么写的？



```java
String sql = "insert into t_car(id,car_num,brand,guide_price,produce_time,car_type) values(null,?,?,?,?,?)";
ps.setString(1, xxx);
ps.setString(2, yyy);
....
```



+ 在JDBC当中占位符采用的是?，在mybatis当中是什么呢？ 
    - 和?等效的写法是：#{}
+ 在mybatis当中不能使用?占位符，必须使用 #{} 来代替JDBC当中的 ?
+ #{} 和 JDBC当中的 ? 是等效的。



```xml
<!--namespace先随便写-->
<mapper namespace="car">
    <insert id="insertCar">
        insert into t_car(car_num,brand,guide_price,produce_time,car_type) 
      	values(#{}, #{}, #{}, #{}, #{})
    </insert>
</mapper>
```



### 💦 使用Map集合传参


java程序中使用Map可以给SQL语句的占位符传值，占位符中写map集合的key，如果key不存在，获取的是null，一般map集合的key起名的时候要见名知意。



```xml
<mapper namespace="car">
    <!--insert sql：保存⼀个汽⻋信息-->
    <insert id="insertCar">
        insert into t_car
            (id,car_num,brand,guide_price,produce_time,car_type)
        values
            (null, #{k1}, #{k2}, #{k3}, #{k4}, #{k5})
    </insert>
</mapper>
```



```java
package cw.mybatis;

import cw.mybatis.utils.SqlSessionUtils;
import org.apache.ibatis.session.SqlSession;

import java.util.HashMap;
import java.util.Map;

public class CarMapperTest {
	
	@Test
    public void testInsertCar() {
        // 使用map集合进行数据的封装。
        Map<String, Object> map = new HashMap<>();
        map.put("k1", "1111");
        map.put("k2", "比亚迪汉");
        map.put("k3", 10.0);
        map.put("k4", "2020-11-11");
        map.put("k5", "电车");
    
        SqlSession sqlSession = SqlSessionUtils.openSession();
    
        // 执行SQL语句
        // insert方法的参数：
        // 第一个参数：sqlId，从CarMapper.xml文件中复制。
        // 第二个参数：封装数据的对象。
        sqlSession.insert("insertCar", map);
        
        sqlSession.commit();
        sqlSession.close();
    }
}
```



![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851536049-c952dc12-0d16-4e01-8d20-27d0356c2e92.png)



### 💦 使用POJO(简单普通的java对象)传参


第一步：定义一个pojo类Car，提供相关属性



```java
package cw.mybatis.pojo;

/**
 * 封装汽车相关信息的pojo类。普通的java类。
 */
public class Car {
    // 数据库表当中的字段应该和pojo类的属性一一对应。
    // 建议使用包装类，这样可以防止null的问题。
    private Long id;
    private String carNum;
    private String brand;
    private Double guidePrice;
    private String produceTime;
    private String carType;
    
    public Car() {
    }
    
    public Car(Long id, String carNum, String brand, Double guidePrice, String produceTime, String carType) {
        this.id = id;
        this.carNum = carNum;
        this.brand = brand;
        this.guidePrice = guidePrice;
        this.produceTime = produceTime;
        this.carType = carType;
    }
    
    public Long getId() {
        return id;
    }
    
    public void setId(Long id) {
        this.id = id;
    }
    
    public String getCarNum() {
        return carNum;
    }
    
    public void setCarNum(String carNum) {
        this.carNum = carNum;
    }
    
    public String getBrand() {
        return brand;
    }
    
    public void setBrand(String brand) {
        this.brand = brand;
    }
    
    public Double getGuidePrice() {
        return guidePrice;
    }
    
    public void setGuidePrice(Double guidePrice) {
        this.guidePrice = guidePrice;
    }
    
    public String getProduceTime() {
        return produceTime;
    }
    
    public void setProduceTime(String produceTime) {
        this.produceTime = produceTime;
    }
    
    public String getCarType() {
        return carType;
    }
    
    public void setCarType(String carType) {
        this.carType = carType;
    }
    
    @Override
    public String toString() {
        return "Car{" + "id=" + id + ", carNum='" + carNum + '\'' + ", brand='" + brand + '\'' + ", guidePrice=" + guidePrice + ", produceTime='" + produceTime + '\'' + ", carType='" + carType + '\'' + '}';
    }
}
```



第二步：Java程序



```java
@Test
public void testInsertCarPOJO() {
    // 封装数据
    Car car = new Car(null, "3333", "比亚迪", 30.0, "2020-11-11", "新能源");

    SqlSession sqlSession = SqlSessionUtils.openSession();
    
    // 执行sql
    sqlSession.insert("insertCar", car);
    
    sqlSession.commit();
    sqlSession.close();
}
```



第三步：SQL语句



```xml
<mapper namespace="car">
    <!--insert sql：保存⼀个汽⻋信息-->
    <!-- 占位符 #{} 中写POJO的属性名 -->
    <insert id="insertCar">
        insert into t_car
            (id,car_num,brand,guide_price,produce_time,car_type)
        values
            (null, #{carNum}, #{brand}, #{guidePrice}, #{produceTime}, #{carType})
    </insert>
</mapper>
```



![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851536049-d2a579f4-ded0-4a10-b9b7-83ac1eb98154.png)



+ 把SQL语句写成这个德行：

```sql
insert into t_car(id,car_num,brand,guide_price,produce_time,car_type)
values(null,#{xyz},#{brand},#{guidePrice},#{produceTime},#{carType})
```

 

+ 出现了什么问题呢？ 
    - There is no getter for property named 'xyz' in 'class com.powernode.mybatis.pojo.Car'
    - mybatis去找：Car类中的getXyz()方法去了。没找到。报错了。
+ 怎么解决的？ 
    - 可以在Car类中提供一个getXyz()方法。这样问题就解决了。
+ 通过这个测试，得出一个结论： 
    - 严格意义上来说：如果使用POJO对象传递值的话，#{}这个大括号中到底写什么？
    - 写的是get方法的方法名去掉get，然后将剩下的单词首字母小写，然后放进去。 
        * 例如：getUsername() --> #{username}
        * 例如：getEmail() --> #{email}
        * ....
+ 也就是说mybatis在底层给?传值的时候，先要获取值，怎么获取的？ 
    - 调用了pojo对象的get方法。例如：car.getCarNum()，car.getCarType()，car.getBrand()



## 🌊 delete


需求：根据id删除数据



实现：  
SQL语句



```xml
<!-- 当sql语句中的占位符只有一个时，占位符中的内容可以任意写，但是不能不写，一般采用见名知意的命名 -->
<!-- 只有一个占位符时，mybatis可以知道数据填放的位置 -->
<delete id="deleteById">
    delete from t_car where id = #{id}
</delete>
```



java程序



```java
@Test
public void testDeleteById() {
    SqlSession sqlSession = SqlSessionUtils.openSession();

	// 第二个参数会被自动装箱成相应的类型
    sqlSession.delete("deleteById", 10);
    
    sqlSession.commit();
    sqlSession.close();
}
```



![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851536323-85fe09a6-3609-4305-92f0-41709395bcf8.png)



注意：如果占位符只有一个，那么#{}的大括号里可以随意。但是最好见名知意。



## 🌊 update


需求：根据id修改某条记录。



```xml
<update id="updateById">
    update t_car set
        car_num = #{carNum}, brand = #{brand},
        guide_price = #{guidePrice}, produce_time = #{produceTime},
        car_type = #{carType}
    where id = #{id}
</update>
```



```java
@Test
public void testUpdateById() {
    SqlSession sqlSession = SqlSessionUtils.openSession();

    // 封装数据
    Car car = new Car(4L, "9999", "凯美瑞", 30.3, "1999-11-10", "燃油车");

    int count = sqlSession.update("updateById", car);
    System.out.println(count);
    
    sqlSession.commit();
    sqlSession.close();
}
```



![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851536420-a5f146fd-e75d-4915-8e49-937eace51085.png)



## 🌊 select


### 💦 查一条数据


需求：根据id查询。



```xml
<!-- 查询时需要告诉mybatis查询结果集封装成的java对象类型 -->
<!-- select标签中resultType属性，这个属性用来告诉mybatis，查询结果集封装成什么类型的java对象。你需要告诉mybatis。 -->
<!-- resultType通常写的是：全限定类名。 -->
<!-- sql语句中如果表的字段名与相应的java类的属性名不一致需要使用别名为查询语句的字段指定别名，否则对应字段的查询为null -->
<select id="selectById" resultType="cw.mybatis.pojo.Car">
    select
        id,car_num as carNum,brand,guide_price as guidePrice,
        produce_time as produceTime,
        car_type as carType
    from
        t_car
    where
        id = #{id}
</select>
```



```java
@Test
public void testSelectById() {
    SqlSession sqlSession = SqlSessionUtils.openSession();

    // 执行DQL语句。查询。根据id查询。返回结果一定是一条。
    // mybatis底层执行了select语句之后，一定会返回一个结果集对象：ResultSet
    // JDBC中叫做ResultSet，接下来就是mybatis应该从ResultSet中取出数据，封装java对象。
    Object car = sqlSession.selectOne("selectById", 1);
    System.out.println(car);

    sqlSession.close();
}
```



![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851536707-9dddc1ce-3ba4-44c3-b628-94fd58737d86.png)



### 💦 查多条数据


```xml
<!-- resultType还是指定要封装的结果集的类型。不是指定List类型，是指定List集合中元素的类型。 -->
<!-- selectList方法：mybatis通过这个方法就可以得知你需要一个List集合。它会自动给你返回一个List集合。 -->
<select id="selectAll" resultType="cw.mybatis.pojo.Car">
    select
        id,car_num as carNum,brand,guide_price as guidePrice,
        produce_time as produceTime,
        car_type as carType
    from
        t_car
</select>
```



```java
@Test
public void testSelectAll() {
    SqlSession sqlSession = SqlSessionUtils.openSession();

    List<Car> cars = sqlSession.selectList("selectAll");
    cars.forEach(System.out::println);

    sqlSession.close();
}
```



![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851536689-066a9a9a-3d33-419a-8293-c15a1f6926c2.png)



## 🌊 SQL Mapper的namespace


在sql mapper.xml文件当中有一个namespace,这个属性是用来指定命名空间的。用来防止id重复。



实际上，本质上，mybatis中的sqlId的完整写法：namespace.id



创建CarMapper2.xml文件，代码如下：



```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">

<mapper namespace="car2">
    <select id="selectCarAll" resultType="com.powernode.mybatis.pojo.Car">
        select
            id, car_num as carNum, brand, guide_price as guidePrice, produce_time as produceTime, car_type as carType
        from
            t_car
    </select>
</mapper>
```



CarMapper.xml和CarMapper2.xml文件中都有 id="selectCarAll"



将CarMapper2.xml配置到mybatis-config.xml文件中。



```xml
<mappers>
  <mapper resource="CarMapper.xml"/>
  <mapper resource="CarMapper2.xml"/>
</mappers>
```



Java代码



```java
@Test
public void testSelectAll() {
    SqlSession sqlSession = SqlSessionUtils.openSession();

    List<Car> cars = sqlSession.selectList("selectAll");
    cars.forEach(System.out::println);

    sqlSession.close();
}
```



![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851536639-963093ea-28e9-455d-8455-c6a61ecb0700.png)



```bash
org.apache.ibatis.exceptions.PersistenceException: 
### Error querying database.  Cause: java.lang.IllegalArgumentException: 
  selectCarAll is ambiguous in Mapped Statements collection (try using the full name including the namespace, or rename one of the entries) 
  【翻译】selectCarAll在Mapped Statements集合中不明确（请尝试使用包含名称空间的全名，或重命名其中一个条目）
  【大致意思是】selectCarAll重名了，你要么在selectCarAll前添加一个名称空间，要有你改个其它名字。
```



Java代码修改如下：



```java
@Test
public void testSelectAll() {
    SqlSession sqlSession = SqlSessionUtils.openSession();

    List<Car> cars = sqlSession.selectList("car.selectAll");
    cars.forEach(System.out::println);

    sqlSession.close();
}
```



![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851537005-2537efe2-afc3-4e90-a706-825104897a56.png)



# 🥽 MyBatis核心配置文件详解


```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!-- 文档类型说明中的 configuration，是根标签的名称，一个文档一个根标签 -->
<!--
    http://mybatis.org/dtd/mybatis-3-config.dtd
    xml文档的dtd约束，约束文档中可以出现什么标签、标签能有什么子标签、标签中可以有什么属性以及标签出现的顺序
-->
<!DOCTYPE configuration
        PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-config.dtd">

<!-- configuration：根标签，表示配置信息。 -->
<configuration>

    <!--java.util.Properties类。是一个Map集合。key和value都是String类型-->
    <!-- property标签中的name属性为key，value属性为value -->
    <!--在properties标签中可以配置很多属性-->
    <!-- 在下面的标签中可以使用property配置的属性值，使用 ${property的name属性} 取出相应的值 -->
    <!--<properties>-->
        <!--这是其中的一个属性-->
        <!--<property name="属性名" value="属性值"/>-->
        <!--<property name="jdbc.driver" value="com.mysql.cj.jdbc.Driver"/>
        <property name="jdbc.url" value="jdbc:mysql://localhost:3306/powernode"/>
        <property name="jdbc.username" value="root"/>
        <property name="jdbc.password" value="root"/>-->
    <!--</properties>-->

    <!-- properties中的property可以配置到配置文件中 -->
    <!--resource,一定是从类路径下开始查找资源-->
    <properties resource="jdbc.properties" />

    <!--从绝对路径当中加载资源。绝对路径怎么写？file:///路径-->
    <!--<properties url="file:///d:/jdbc.properties" />-->


    <!-- environments：环境（多个），以“s”结尾表示复数，也就是说mybatis的环境可以配置多个数据源。 -->
    <!--default表示默认使用的环境。-->
    <!--默认环境什么意思？当你使用mybatis创建SqlSessionFactory对象的时候，没有指定环境的话，默认使用哪个环境。-->
    <environments default="powernodeDB">

        <!--其中的一个环境。连接的数据库是powernode-->
        <!--一般一个数据库会对应一个SqlSessionFactory对象。-->
        <!--一个环境environment会对应一个SqlSessionFactory对象-->
        <!-- 一个数据库对应一个环境 -->
        <!--
            // 这种方式就是获取的默认环境
            SqlSessionFactory sqlSessionFactory =
                   sqlSessionFactoryBuilder.build(Resources.getResourceAsStream("mybatis-config.xml"));
            // 这种方式就是通过环境id来使用指定的环境，第二个参数为环境id
            SqlSessionFactory sqlSessionFactory1 =
                sqlSessionFactoryBuilder.build(Resources.getResourceAsStream("mybatis-config.xml"), "powernodeDB");
        -->
        <environment id="powernodeDB">
            <!--
                transactionManager标签：
                    1.作用：配置事务管理器。指定mybatis具体使用什么方式去管理事务。
                    2.type属性有两个值：
                        第一个：JDBC: 使用原生的JDBC代码来管理事务。
                            conn.setAutoCommit(false);
                            ....
                            conn.commit();
                        第二个：MANAGED：mybatis不再负责事务的管理，将事务管理交给其它的JEE(JavaEE)容器来管理。例如：spring
                    3. 大小写无所谓。不缺分大小写。但是不能写其他值。只能是二选一：
                        jdbc、managed
                    4. 在mybatis中提供了一个事务管理器接口：Transaction
                        该接口下有两个实现类：
                            JdbcTransaction
                            ManagedTransaction
                        如果type="JDBC"，那么底层会实例化JdbcTransaction对象。
                        如果type="MANAGED"，那么底层会实例化ManagedTransaction
            -->
            <transactionManager type="JDBC"/>
            <!--
                dataSource配置：
                    1.dataSource被称为数据源。
                    2.dataSource作用是什么？为程序提供Connection对象。（但凡是给程序提供Connection对象的，都叫做数据源。）
                    3.数据源实际上是一套规范。JDK中有这套规范：javax.sql.DataSource（这个数据源的规范，这套接口实际上是JDK规定的。）
                    4.我们自己也可以编写数据源组件，只要实现javax.sql.DataSource接口就行了。实现接口当中所有的方法。这样就有了自己的数据源。
                    比如你可以写一个属于自己的数据库连接池（数据库连接池是提供连接对象的，所以数据库连接池就是一个数据源）。
                    5.常见的数据源组件有哪些呢【常见的数据库连接池有哪些呢】？
                        阿里巴巴的德鲁伊连接池：druid
                        c3p0
                        dbcp
                        ....
                    6. type属性用来指定数据源的类型，就是指定具体使用什么方式来获取Connection对象：
                        type属性有三个值：必须是三选一。
                        type="[UNPOOLED|POOLED|JNDI]"
                        UNPOOLED：不使用数据库连接池技术。每一次请求过来之后，都是创建新的Connection对象。
                        POOLED：使用mybatis自己实现的数据库连接池。
                        JNDI：集成其它第三方的数据库连接池。

                        JNDI是一套规范。谁实现了这套规范呢？大部分的web容器都实现了JNDI规范：
                            例如：Tomcat、Jetty、WebLogic、WebSphere，这些服务器(容器)都实现了JNDI规范。
                        JNDI是：java命名目录接口。Tomcat服务器实现了这个规范。
            -->
            <!-- 数据源的type属性指定不同的值，需要配置不太的属性 https://mybatis.net.cn/configuration.html#environments -->
            <dataSource type="POOLED">
                <property name="driver" value="${jdbc.driver}"/>
                <property name="url" value="${jdbc.url}"/>
                <property name="username" value="${jdbc.username}"/>
                <property name="password" value="${jdbc.password}"/>
                <!-- 以下配置数据库连接池的参数 -->
                <!--提醒：正常使用连接池的话，池中有很多参数是需要设置的。设置好参数，可以让连接池发挥的更好。事半功倍的效果。-->
                <!--具体连接池当中的参数如何配置呢？需要反复的根据当前业务情况进行测试。-->
                <!--poolMaximumActiveConnections：连接池当中最多的正在使用的连接对象的数量上限。最多有多少个连接可以活动。默认值10-->
                <property name="poolMaximumActiveConnections" value="10"/>
                <!--每隔2秒打印日志，并且尝试获取连接对象-->
                <property name="poolTimeToWait" value="2000"/>
                <!--强行让某个连接空闲，超时时间的设置-->
                <property name="poolMaximumCheckoutTime" value="10000"/>
                <!--最多的空闲数量-->
                <!--
                    假设最多的连接数量为10个，最多空闲数量为5个，现在已经空闲5个了，马上第六个也要空闲了
                    如果第六个空闲下来，连接池为了保证空闲的数量最多5个，会真正关闭多余的空闲连接对象
                    可以节省系统资源
                -->
                <property name="poolMaximumIdleConnections" value="5"/>
            </dataSource>

        </environment>

        <!--这是mybatis的另一个环境，也就是连接的数据库是另一个数据库mybatis-->
        <environment id="mybatisDB">
            <transactionManager type="JDBC"/>
            <dataSource type="POOLED">
                <property name="driver" value="com.mysql.cj.jdbc.Driver"/>
                <property name="url" value="jdbc:mysql://localhost:3306/mybatis"/>
                <property name="username" value="root"/>
                <property name="password" value="root"/>
            </dataSource>
        </environment>

    </environments>

    <!-- mappers：在mappers标签中可以配置多个sql映射文件的路径。 -->
    <mappers>
        <!-- mapper：配置某个sql映射文件的路径 -->
        <!-- resource属性：使用相对于类路径的资源引用方式 -->
        <!-- url属性：使用完全限定资源定位符（URL）方式 -->
        <mapper resource="CarMapper.xml"/>
    </mappers>
</configuration>
```



# 🥽 手写MyBatis框架


## 🌊 dom4j解析XML文件


引入dom4j的依赖



```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>org.group</groupId>
    <artifactId>parse-xml-by-dom4j</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>jar</packaging>

    <dependencies>
    	<!-- dom4j解析XML文件需要dom4j依赖与jaxen依赖 -->
        <!--dom4j依赖-->
        <dependency>
            <groupId>org.dom4j</groupId>
            <artifactId>dom4j</artifactId>
            <version>2.1.3</version>
        </dependency>
        <!--jaxen依赖-->
        <dependency>
            <groupId>jaxen</groupId>
            <artifactId>jaxen</artifactId>
            <version>1.2.0</version>
        </dependency>
        <!--junit依赖-->
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.13.2</version>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
    </properties>

</project>
```



mybatis核心配置文件mybatis-config.xml：



```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE configuration
		PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
		"http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
	
	<environments default="development">
		<environment id="development">
			<transactionManager type="JDBC"/>
			<dataSource type="POOLED">
				<property name="driver" value="com.mysql.cj.jdbc.Driver"/>
				<property name="url" value="jdbc:mysql://localhost:3306/mybatis_study"/>
				<property name="username" value="root"/>
				<property name="password" value="123123"/>
			</dataSource>
		</environment>
	</environments>
	<mappers>
		<mapper resource="CarMapper.xml"/>
	</mappers>
</configuration>
```



CarMapper.xml



```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
		PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
		"http://mybatis.org/dtd/mybatis-3-mapper.dtd">

<mapper namespace="car">
	<insert id="insertCar">
		insert into t_car
			(id,car_num,brand,guide_price,produce_time,car_type)
		values
			(null,'102','丰⽥mirai',40.30,'2014-10-05','氢能源')
	</insert>
</mapper>
```



```java
package com.powernode.xml.test;

import org.dom4j.Document;
import org.dom4j.Element;
import org.dom4j.Node;
import org.dom4j.io.SAXReader;
import org.junit.Test;

import java.io.InputStream;
import java.util.List;

public class ParseXMLByDom4jTest {

    @Test
    public void testParseMyBatisConfigXML() throws Exception{
        // 创建SAXReader对象
        SAXReader reader = new SAXReader();
        // 获取输入流
        InputStream is = ClassLoader.getSystemClassLoader().getResourceAsStream("mybatis-config.xml");
        // 读XML文件，返回document对象。document对象是文档对象，代表了整个XML文件。
        Document document = reader.read(is);
        // 获取文档当中的根标签
        //Element rootElt = document.getRootElement();
        //String rootEltName = rootElt.getName();
        //System.out.println("根节点的名字：" + rootEltName);

        //获取default默认的环境id
        // xpath是做标签路径匹配的。能够让我们快速定位XML文件中的元素。
        // 以下的xpath代表了：从根下开始找configuration标签，然后找configuration标签下的子标签environments
        String xpath = "/configuration/environments";
        Element environments = (Element) document.selectSingleNode(xpath); // Element是Node类的子类，方法更多，使用更便捷。
        // 获取属性的值
        String defaultEnvironmentId = environments.attributeValue("default");
        //System.out.println("默认环境的id：" + defaultEnvironmentId);
        // 获取具体的环境environment
        xpath = "/configuration/environments/environment[@id='"+defaultEnvironmentId+"']";
        //System.out.println(xpath);
        Element environment = (Element) document.selectSingleNode(xpath);
        // 获取environment节点下的transactionManager节点(Element的element()方法用来获取孩子节点)
        Element transactionManager = environment.element("transactionManager");
        String transactionType = transactionManager.attributeValue("type");
        System.out.println("事务管理器的类型：" + transactionType);
        // 获取dataSource节点
        Element dataSource = environment.element("dataSource");
        String dataSourceType = dataSource.attributeValue("type");
        System.out.println("数据源的类型：" + dataSourceType);
        // 获取dataSource节点下的所有子节点
        List<Element> propertyElts = dataSource.elements();
        // 遍历
        propertyElts.forEach(propertyElt -> {
            String name = propertyElt.attributeValue("name");
            String value = propertyElt.attributeValue("value");
            System.out.println(name + "=" + value);
        });
        // 获取所有的mapper标签
        // 不想从根下开始获取，你想从任意位置开始，获取所有的某个标签，xpath该这样写
        xpath = "//mapper";
        List<Node> mappers = document.selectNodes(xpath);
        // 遍历
        mappers.forEach(mapper -> {
            Element mapperElt = (Element) mapper;
            String resource = mapperElt.attributeValue("resource");
            System.out.println(resource);
        });
    }

    @Test
    public void testParseSqlMapperXML() throws Exception{
        SAXReader reader = new SAXReader();
        InputStream is = ClassLoader.getSystemClassLoader().getResourceAsStream("CarMapper.xml");
        Document document = reader.read(is);
        // 获取namespace
        String xpath = "/mapper";
        Element mapper = (Element) document.selectSingleNode(xpath);
        String namespace = mapper.attributeValue("namespace");
        System.out.println(namespace);
        // 获取mapper节点下所有的子节点
        List<Element> elements = mapper.elements();
        // 遍历
        elements.forEach(element -> {
            // 获取sqlId
            String id = element.attributeValue("id");
            System.out.println(id);
            // 获取resultType
            String resultType = element.attributeValue("resultType"); // 没有这个属性的话，会自动返回"null"
            System.out.println(resultType);
            // 获取标签中的sql语句（表示获取标签中的文本内容，而且去除前后空白）
            String sql = element.getTextTrim();
            System.out.println(sql);
            // insert into t_car values(null,#{carNum},#{brand},#{guidePrice},#{produceTime},#{carType})
            // insert into t_car values(null,?,?,?,?,?)
            // mybaits封装了jdbc。早晚要执行带有?的sql语句。
            // 转换
            String newSql = sql.replaceAll("#\\{[0-9A-Za-z_$]*}", "?");
            System.out.println(newSql);
        });
    }
}
```



## 🌊 GodBatis


GodBatis：[https://www.yuque.com/zuihoudewu/java_note/mt2812#g4aW0](https://www.yuque.com/zuihoudewu/java_note/mt2812#g4aW0)



# 🥽 在WEB中应用MyBatis（使用MVC架构模式）


+ 目标： 
    - 掌握mybatis在web应用中怎么用
    - mybatis三大对象的作用域和生命周期
    - ThreadLocal原理及使用
    - 巩固MVC架构模式
    - 为学习MyBatis的接口代理机制做准备
+ 实现功能： 
    - 银行账户转账
+ 使用技术： 
    - HTML + Servlet + MyBatis
+ WEB应用的名称： 
    - bank



## 🌊 需求描述


![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851537026-6594c593-9626-4078-b302-e21964fff2c9.png)



## 🌊 数据库表的设计和准备数据


```sql
USE dbtest;
DROP TABLE IF EXISTS t_act;
CREATE TABLE t_act (
    id int PRIMARY KEY AUTO_INCREMENT,
    actno VARCHAR(255),
    balance DECIMAL(10, 2)
);
INSERT INTO t_act(actno, balance) VALUES ('act001', 50000);
INSERT INTO t_act(actno, balance) VALUES ('act002', 0);
```



![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851537267-c38dee84-3c80-4b5b-b37a-d94fed715e33.png)



## 🌊 环境搭建


+  IDEA中创建Maven WEB应用（mybatis-004）  
![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851537228-4aea1671-a68f-4aa1-aaea-4753df3a86b2.png) 
+  默认创建的maven web应用没有java和resources目录，包括两种解决方案  
![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851537460-fca4a09b-f566-4fce-88dc-99f5fb71be65.png) 
    - 第一种：自己手动加上。
    - 第二种：修改maven-archetype-webapp-1.4.jar中的配置文件  
![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851537684-ed58b0d8-7447-45a5-9fd9-03ca5d95c4af.png)  
![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851537658-9b265430-8d97-48c8-814e-2e9bcd39c0db.png)
+  web.xml文件的版本较低，可以从tomcat10的样例文件中复制，然后修改 

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="https://jakarta.ee/xml/ns/jakartaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="https://jakarta.ee/xml/ns/jakartaee
                      https://jakarta.ee/xml/ns/jakartaee/web-app_5_0.xsd"
         version="5.0"
         metadata-complete="true">
<!-- metadata-complete="true" 只支持配置文件 -->
<!-- metadata-complete="false" 支持配置文件与注解 -->
</web-app>
```

 

+  删除index.jsp文件，因为我们这个项目不使用JSP。只使用html。 
+  确定pom.xml文件中的打包方式是war包。  
![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851537901-b5148925-084c-47a4-93b3-aed1b84205cb.png) 
+  引入相关依赖 
    - 编译器版本修改为17

```xml
	<properties>
		<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
		<maven.compiler.source>17</maven.compiler.source>
		<maven.compiler.target>17</maven.compiler.target>
	</properties>
```

 

    - 引入的依赖包括：mybatis，mysql驱动，logback，servlet。

```xml
	<dependencies>
		<!-- mybatis -->
		<dependency>
			<groupId>org.mybatis</groupId>
			<artifactId>mybatis</artifactId>
			<version>3.5.10</version>
		</dependency>
		<!-- mysql -->
		<dependency>
			<groupId>mysql</groupId>
			<artifactId>mysql-connector-java</artifactId>
			<version>8.0.30</version>
		</dependency>
		<!-- logback -->
		<dependency>
			<groupId>ch.qos.logback</groupId>
			<artifactId>logback-classic</artifactId>
			<version>1.2.11</version>
		</dependency>
		<!-- servlet -->
		<dependency>
			<groupId>javax.servlet</groupId>
			<artifactId>javax.servlet-api</artifactId>
			<version>3.1.0</version>
		</dependency>
	</dependencies>
```

 

+  IDEA配置Tomcat，这里Tomcat使用10+版本。并部署应用到tomcat。 
+  引入相关配置文件，放到resources目录下（全部放到类的根路径下） 
    -  mybatis-config.xml 

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE configuration
        PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>

    <properties resource="jdbc.properties"/>

    <environments default="dev">
        <environment id="dev">
            <transactionManager type="JDBC"/>
            <dataSource type="POOLED">
                <property name="driver" value="${jdbc.driver}"/>
                <property name="url" value="${jdbc.url}"/>
                <property name="username" value="${jdbc.username}"/>
                <property name="password" value="${jdbc.password}"/>
            </dataSource>
        </environment>
    </environments>
    <mappers>
        <!--一定要注意这里的路径哦！！！-->
        <mapper resource="AccountMapper.xml"/>
    </mappers>
</configuration>
```

 

    -  AccountMapper.xml 

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">

<mapper namespace="account">

</mapper>
```

 

    -  logback.xml 

```xml
<?xml version="1.0" encoding="UTF-8"?>

<configuration debug="false">
    <!-- 控制台输出 -->
    <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
        <encoder class="ch.qos.logback.classic.encoder.PatternLayoutEncoder">
            <!--格式化输出：%d表示日期，%thread表示线程名，%-5level：级别从左显示5个字符宽度%msg：日志消息，%n是换行符-->
            <pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{50} - %msg%n</pattern>
        </encoder>
    </appender>
    <!-- 按照每天生成日志文件 -->
    <appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <!--日志文件输出的文件名-->
            <FileNamePattern>${LOG_HOME}/TestWeb.log.%d{yyyy-MM-dd}.log</FileNamePattern>
            <!--日志文件保留天数-->
            <MaxHistory>30</MaxHistory>
        </rollingPolicy>
        <encoder class="ch.qos.logback.classic.encoder.PatternLayoutEncoder">
            <!--格式化输出：%d表示日期，%thread表示线程名，%-5level：级别从左显示5个字符宽度%msg：日志消息，%n是换行符-->
            <pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{50} - %msg%n</pattern>
        </encoder>
        <!--日志文件最大的大小-->
        <triggeringPolicy class="ch.qos.logback.core.rolling.SizeBasedTriggeringPolicy">
            <MaxFileSize>100MB</MaxFileSize>
        </triggeringPolicy>
    </appender>

    <!--mybatis log configure-->
    <logger name="com.apache.ibatis" level="TRACE"/>
    <logger name="java.sql.Connection" level="DEBUG"/>
    <logger name="java.sql.Statement" level="DEBUG"/>
    <logger name="java.sql.PreparedStatement" level="DEBUG"/>

    <!-- 日志输出级别,logback日志级别包括五个：TRACE < DEBUG < INFO < WARN < ERROR -->
    <root level="DEBUG">
        <appender-ref ref="STDOUT"/>
        <appender-ref ref="FILE"/>
    </root>

</configuration>
```

 

    -  jdbc.properties 

```json
jdbc.driver=com.mysql.cj.jdbc.Driver
jdbc.url=jdbc:mysql://localhost:3306/powernode
jdbc.username=root
jdbc.password=root
```

 



## 🌊 前端页面index.html


```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>银行账户转账</title>
</head>
<body>
<!--/bank是应用的根，部署web应用到tomcat的时候一定要注意这个名字-->
<form action="/bank/transfer" method="post">
    转出账户：<input type="text" name="fromActno"/><br>
    转入账户：<input type="text" name="toActno"/><br>
    转账金额：<input type="text" name="money"/><br>
    <input type="submit" value="转账"/>
</form>
</body>
</html>
```



## 🌊 创建pojo包、service包、dao包、web包、utils包(MVC架构模式)


+  com.powernode.bank.pojo 
+  com.powernode.bank.service 
+  com.powernode.bank.service.impl 
+  com.powernode.bank.dao 
+  com.powernode.bank.dao.impl 
+  com.powernode.bank.web.controller 
+  com.powernode.bank.exception 
+  com.powernode.bank.utils：将之前编写的SqlSessionUtil工具类拷贝到该包下。 

```java
public class SqlSessionUtil {
    
    private SqlSessionUtil(){}
    
    private static SqlSessionFactory sqlSessionFactory;
    
    static {
        try {
            sqlSessionFactory = new SqlSessionFactoryBuilder().build(Resources.getResourceAsStream("mybatis-config.xml"));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
    
    /**
     * 获取会话对象。
     * @return 会话对象
     */
    public static SqlSession openSession(){
        return sqlSessionFactory.openSession();
    }
    
}
```

 



## 🌊 定义pojo类：Account


```java
public class Account {
    private Long id;
    private String actno;
    private Double balance;

    @Override
    public String toString() {
        return "Account{" +
                "id=" + id +
                ", actno='" + actno + '\'' +
                ", balance=" + balance +
                '}';
    }

    public Account() {
    }

    public Account(Long id, String actno, Double balance) {
        this.id = id;
        this.actno = actno;
        this.balance = balance;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getActno() {
        return actno;
    }

    public void setActno(String actno) {
        this.actno = actno;
    }

    public Double getBalance() {
        return balance;
    }

    public void setBalance(Double balance) {
        this.balance = balance;
    }
}
```



## 🌊 后端代码实现


```java
@WebServlet({"/transfer"})
public class AccountServlet extends HttpServlet {
    
    // 为了让这个对象在其他方法中也可以用。声明为实例变量。
    private AccountService accountService = new AccountServiceImpl();
    
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        // 获取数据
        String fromActno = request.getParameter("fromActno");
        String toActno = request.getParameter("toActno");
        double money = Double.parseDouble(request.getParameter("money"));
        // 调用业务层
        try {
            accountService.transfer(fromActno, toActno, money);
            // 到这转账成功
            // 调用视图完成结果展示
            response.sendRedirect(request.getContextPath() + "/success.html");
        } catch (MoneyNotEnoughException e) {
            response.sendRedirect(request.getContextPath() + "/error1.html");
        } catch (TransferException e) {
            response.sendRedirect(request.getContextPath() + "/error2.html");
        } catch (Exception e) {
            response.sendRedirect(request.getContextPath() + "/error2.html");
        }
        
    }
}
```



```java
/**
 * 注意：业务类当中的业务方法的名字在起名的时候，最好见名知意，能够体现出具体的业务是做什么的。
 * 账户业务类
 */
public interface AccountService {
    
    /**
     * 转账业务
     * @param fromActno 转出账户
     * @param toActno 转入账户
     * @param money 转账金额
     */
    void transfer(String fromActno, String toActno, double money) throws MoneyNotEnoughException, TransferException;
    
}
```



```java
public class AccountServiceImpl implements AccountService {
    
    private AccountDao accountDao = new AccountDaoImpl();
    
    @Override
    public void transfer(String fromActno, String toActno, double money)
            throws MoneyNotEnoughException, TransferException {
        // 1. 判断转出账户的余额是否充足(select)
        Account fromAct = accountDao.selectByActno(fromActno);
        // 2. 如果转出账户余额不足，提示用户
        if (fromAct.getBalance() < money) { // 转出账户余额不足
            throw new MoneyNotEnoughException("余额不足");
        }
        // 3. 如果转出账户余额充足，更新转出账户余额(update)
        // 先更新java内存中对象的余额再更新数据库
        Account toAct = accountDao.selectByActno(toActno);
        fromAct.setBalance(fromAct.getBalance() - money);
        toAct.setBalance(toAct.getBalance() + money);
        int count = accountDao.updateByAccount(fromAct);
        // 4. 更新转入账户余额(update)
        count += accountDao.updateByAccount(toAct);
        if (count != 2) {
            throw new TransferException("转账失败");
        }
    }
}
```



```java
/**
 * 账户的DAO对象。负责t_act表中数据的CRUD.
 * 强调一下：DAO对象中的任何一个方法和业务不挂钩。没有任何业务逻辑在里面。
 * DAO中的方法就是做CRUD的。所以方法名大部分是：insertXXX deleteXXX updateXXX selectXXX
 */
public interface AccountDao {
    
    /**
     * 根据账号查询账户信息。
     * @param actno 账号
     * @return 账户信息
     */
    Account selectByActno(String actno);
    
    /**
     * 更新账户信息
     * @param act  被更新的账户对象
     * @return 1表示更新成功，其他值表示失败。
     */
    int updateByAccount(Account act);
}
```



```java
public class AccountDaoImpl implements AccountDao {
    
    @Override
    public Account selectByActno(String actno) {
        SqlSession sqlSession = SqlSessionUtil.openSession();
        Account account = (Account) sqlSession.selectOne("account.selectByActno", actno);
        sqlSession.close();
        return account;
    }
    
    @Override
    public int updateByAccount(Account act) {
        SqlSession sqlSession = SqlSessionUtil.openSession();
        int count = sqlSession.update("account.updateByAccount", act);
        sqlSession.commit();
        sqlSession.close();
        return count;
    }
}
```



```java
public class MoneyNotEnoughException extends Exception{
    public MoneyNotEnoughException() {
    }
    
    public MoneyNotEnoughException(String message) {
        super(message);
    }
}
```



```java
public class TransferException extends Exception{
    public TransferException() {
    }
    
    public TransferException(String message) {
        super(message);
    }
}
```



```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>转账报告</title>
</head>
<body>
<h1>转账成功！</h1>
</body>
</html>
```



```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>转账报告</title>
</head>
<body>
<h1>余额不足！！！</h1>
</body>
</html>
```



```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>转账报告</title>
</head>
<body>
<h1>转账失败，未知原因！！！</h1>
</body>
</html>
```



## 🌊 使用ThreadLocal进行事务控制


```java
public class SqlSessionUtil {
    
    private SqlSessionUtil(){}
    
    private static SqlSessionFactory sqlSessionFactory;
    
    static {
        try {
            sqlSessionFactory = new SqlSessionFactoryBuilder().build(Resources.getResourceAsStream("mybatis-config.xml"));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
    
    // 全局的，服务器级别的，一个服务器当中定义一个即可。
    // 为什么把SqlSession对象放到ThreadLocal当中呢？为了保证一个线程对应一个SqlSession。
    private static ThreadLocal<SqlSession> local = new ThreadLocal<>();
    
    /**
     * 获取会话对象。
     * @return 会话对象
     */
    public static SqlSession openSession(){
        SqlSession sqlSession = local.get();
        if (sqlSession == null) {
            sqlSession = sqlSessionFactory.openSession();
            // 将sqlSession对象绑定到当前线程上。
            local.set(sqlSession);
        }
        return sqlSession;
    }
    
    /**
     * 关闭SqlSession对象(从当前线程中移除SqlSession对象。)
     * @param sqlSession
     */
    public static void close(SqlSession sqlSession) {
        if (sqlSession != null) {
            sqlSession.close();
            // 注意移除SqlSession对象和当前线程的绑定关系。
            // 因为Tomcat服务器支持线程池。也就是说：用过的线程对象t1，可能下一次还会使用这个t1线程。
            local.remove();
        }
    }
    
}
```



```java
public class AccountServiceImpl implements AccountService {
    
    private AccountDao accountDao = new AccountDaoImpl();
    
    @Override
    public void transfer(String fromActno, String toActno, double money)
            throws MoneyNotEnoughException, TransferException {
        // 添加事务控制代码
        SqlSession sqlSession = SqlSessionUtil.openSession();
        
        // 1. 判断转出账户的余额是否充足(select)
        Account fromAct = accountDao.selectByActno(fromActno);
        // 2. 如果转出账户余额不足，提示用户
        if (fromAct.getBalance() < money) { // 转出账户余额不足
            throw new MoneyNotEnoughException("余额不足");
        }
        // 3. 如果转出账户余额充足，更新转出账户余额(update)
        // 先更新java内存中对象的余额再更新数据库
        Account toAct = accountDao.selectByActno(toActno);
        fromAct.setBalance(fromAct.getBalance() - money);
        toAct.setBalance(toAct.getBalance() + money);
        int count = accountDao.updateByAccount(fromAct);
        
        String s = null;
        s.toUpperCase();
        
        // 4. 更新转入账户余额(update)
        count += accountDao.updateByAccount(toAct);
        if (count != 2) {
            throw new TransferException("转账失败");
        }
        
        // 提交事务
        sqlSession.commit();
        // 关闭事务
        SqlSessionUtil.close(sqlSession);
    }
}
```



```java
public class AccountDaoImpl implements AccountDao {
    
    @Override
    public Account selectByActno(String actno) {
        SqlSession sqlSession = SqlSessionUtil.openSession();
        Account account = (Account) sqlSession.selectOne("account.selectByActno", actno);
        // sqlSession.close();
        return account;
    }
    
    @Override
    public int updateByAccount(Account act) {
        SqlSession sqlSession = SqlSessionUtil.openSession();
        int count = sqlSession.update("account.updateByAccount", act);
        // sqlSession.commit();
        // sqlSession.close();
        return count;
    }
}
```



## 🌊 MyBatis核心对象的作用域


+ SqlSessionFactoryBuilder 
    - 这个类可以被实例化、使用和丢弃，一旦创建了 SqlSessionFactory，就不再需要它了。 因此 SqlSessionFactoryBuilder 实例的最佳作用域是方法作用域（也就是局部方法变量）。 你可以重用 SqlSessionFactoryBuilder 来创建多个 SqlSessionFactory 实例，但最好还是不要一直保留着它，以保证所有的 XML 解析资源可以被释放给更重要的事情。
+ SqlSessionFactory 
    - SqlSessionFactory 一旦被创建就应该在应用的运行期间一直存在，没有任何理由丢弃它或重新创建另一个实例。 使用 SqlSessionFactory 的最佳实践是在应用运行期间不要重复创建多次，多次重建 SqlSessionFactory 被视为一种代码“坏习惯”。因此 SqlSessionFactory 的最佳作用域是应用作用域。 有很多方法可以做到，最简单的就是使用单例模式或者静态单例模式。
+ SqlSession 
    - 每个线程都应该有它自己的 SqlSession 实例。SqlSession 的实例不是线程安全的，因此是不能被共享的，所以它的最佳的作用域是请求或方法作用域。 绝对不能将 SqlSession 实例的引用放在一个类的静态域，甚至一个类的实例变量也不行。 也绝不能将 SqlSession 实例的引用放在任何类型的托管作用域中，比如 Servlet 框架中的 HttpSession。 如果你现在正在使用一种 Web 框架，考虑将 SqlSession 放在一个和 HTTP 请求相似的作用域中。 换句话说，每次收到 HTTP 请求，就可以打开一个 SqlSession，返回一个响应后，就关闭它。 这个关闭操作很重要，为了确保每次都能执行关闭操作，你应该把这个关闭操作放到 finally 块中。 下面的示例就是一个确保 SqlSession 关闭的标准模式：

```java
try (SqlSession session = sqlSessionFactory.openSession()) {
  // 你的应用逻辑代码
}
```

 



# 🥽 使用javassist生成类 & MyBatis中接口代理机制及使用


> 来自百度百科：  
Javassist是一个开源的分析、编辑和创建Java字节码的类库。是由东京工业大学的数学和计算机科学系的 Shigeru Chiba （千叶 滋）所创建的。它已加入了开放源代码JBoss 应用服务器项目，通过使用Javassist对字节码操作为JBoss实现动态"AOP"框架。
>



## 🌊 Javassist的使用


要使用javassist，首先要引入它的依赖



```xml
<dependency>
  <groupId>org.javassist</groupId>
  <artifactId>javassist</artifactId>
  <version>3.29.1-GA</version>
</dependency>
```



样例代码：



```java
import javassist.ClassPool;
import javassist.CtClass;
import javassist.CtMethod;
import javassist.Modifier;

import java.lang.reflect.Method;

public class JavassistTest {
    public static void main(String[] args) throws Exception {
        // 获取类池
        ClassPool pool = ClassPool.getDefault();
        // 创建类
        CtClass ctClass = pool.makeClass("com.powernode.javassist.Test");
        // 创建方法
        // 1.返回值类型 2.方法名 3.形式参数列表 4.所属类
        CtMethod ctMethod = new CtMethod(CtClass.voidType, "execute", new CtClass[]{}, ctClass);
        // 设置方法的修饰符列表
        ctMethod.setModifiers(Modifier.PUBLIC);
        // 设置方法体
        ctMethod.setBody("{System.out.println(\"hello world\");}");
        // 给类添加方法
        ctClass.addMethod(ctMethod);
        // 调用方法
        Class<?> aClass = ctClass.toClass();
        Object o = aClass.newInstance();
        Method method = aClass.getDeclaredMethod("execute");
        method.invoke(o);
    }
}
```



```java
    @Test
    public void testGenerateFirstClass() throws Exception{
        // 获取类池，这个类池就是用来给我生成class的
        ClassPool pool = ClassPool.getDefault();
        // 制造类（需要告诉javassist，类名是啥）
        CtClass ctClass = pool.makeClass("com.powernode.bank.dao.impl.AccountDaoImpl");
        // 制造方法
        String methodCode = "public void insert(){System.out.println(123);}";
        // 第一个参数：方法
        // 第二个参数：将来方法要放到哪个类中
        CtMethod ctMethod = CtMethod.make(methodCode, ctClass);
        // 将方法添加到类中
        ctClass.addMethod(ctMethod);
        // 在内存中生成class
        ctClass.toClass();


        // 类加载到JVM当中，返回AccountDaoImpl类的字节码
        Class<?> clazz = Class.forName("com.powernode.bank.dao.impl.AccountDaoImpl");
        // 创建对象
        Object obj = clazz.newInstance();
        // 获取AccountDaoImpl中的insert方法
        Method insertMethod = clazz.getDeclaredMethod("insert");
        // 调用方法insert
        insertMethod.invoke(obj);
    }
```



+ 运行要注意：加两个参数，要不然会有异常InaccessibleObjectException. 
    - --add-opens java.base/java.lang=ALL-UNNAMED
    - --add-opens java.base/sun.net.util=ALL-UNNAMED  
![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851537807-fdef6404-7785-4dfe-ae5f-ac574e706bc8.png)![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851537950-b9c6707e-fb2f-4481-8767-5a3a2c1e437a.png)  
![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851538247-1b6bd9cf-55ee-477b-9f99-937b94536c2f.png)



## 🌊 使用javassist动态生成类并实现接口


```java
    @Test
    public void testGenerateImpl() throws Exception{
        // 获取类池
        ClassPool pool = ClassPool.getDefault();
        // 制造类
        CtClass ctClass = pool.makeClass("com.powernode.bank.dao.impl.AccountDaoImpl");
        // 制造接口
        CtClass ctInterface = pool.makeInterface("com.powernode.bank.dao.AccountDao");
        // 添加接口到类中，类实现接口
        ctClass.addInterface(ctInterface); // AccountDaoImpl implements AccountDao
        // 实现接口中的方法
        // 制造方法
        CtMethod ctMethod = CtMethod.make("public void delete(){System.out.println(\"hello delete!\");}", ctClass);
        // 将方法添加到类中
        ctClass.addMethod(ctMethod);
        // 在内存中生成类，同时将生成的类加载到JVM当中。
        Class<?> clazz = ctClass.toClass();
        AccountDao accountDao = (AccountDao)clazz.newInstance();
        accountDao.delete();
    }
```



```java
    @Test
    public void testGenerateAccountDaoImpl() throws Exception{
        // 获取类池
        ClassPool pool = ClassPool.getDefault();
        // 制造类
        CtClass ctClass = pool.makeClass("com.powernode.bank.dao.impl.AccountDaoImpl");
        // 制造接口
        CtClass ctInterface = pool.makeInterface("com.powernode.bank.dao.AccountDao");
        // 实现接口
        ctClass.addInterface(ctInterface);
        // 实现接口中所有的方法
        // 获取接口中所有的方法
        Method[] methods = AccountDao.class.getDeclaredMethods();
        Arrays.stream(methods).forEach(method -> {
            // method是接口中的抽象方法
            // 把method抽象方法给实现了。
            try {
                // public void delete(){}
                // public int update(String actno, Double balance){}
                StringBuilder methodCode = new StringBuilder();
                methodCode.append("public "); // 追加修饰符列表
                methodCode.append(method.getReturnType().getName()); // 追加返回值类型
                methodCode.append(" ");
                methodCode.append(method.getName()); //追加方法名
                methodCode.append("(");
                // 拼接参数 String actno, Double balance
                Class<?>[] parameterTypes = method.getParameterTypes();
                for (int i = 0; i < parameterTypes.length; i++) {
                    Class<?> parameterType = parameterTypes[i];
                    methodCode.append(parameterType.getName());
                    methodCode.append(" ");
                    methodCode.append("arg" + i);
                    if(i != parameterTypes.length - 1){
                        methodCode.append(",");
                    }
                }
                methodCode.append("){System.out.println(11111); ");
                // 动态的添加return语句
                // 返回类型的简单名字
                String returnTypeSimpleName = method.getReturnType().getSimpleName();
                if ("void".equals(returnTypeSimpleName)) {

                }else if("int".equals(returnTypeSimpleName)){
                    methodCode.append("return 1;");
                }else if("String".equals(returnTypeSimpleName)){
                    methodCode.append("return \"hello\";");
                }
                methodCode.append("}");
                System.out.println(methodCode);
                CtMethod ctMethod = CtMethod.make(methodCode.toString(), ctClass);
                ctClass.addMethod(ctMethod); // 方法添加到类中
            } catch (Exception e) {
                e.printStackTrace();
            }

        });

        // 在内存中生成class，并且加载到JVM当中
        Class<?> clazz = ctClass.toClass();
        // 创建对象
        AccountDao accountDao = (AccountDao) clazz.newInstance();
        // 调用方法
        accountDao.insert("aaaaa");
        accountDao.delete();
        accountDao.update("aaaa", 1000.0);
        accountDao.selectByActno("aaaa");
    }
```



## 🌊 工具类GenerateDaoProxy的实现


```java
package com.powernode.bank.utils;

import org.apache.ibatis.javassist.ClassPool;
import org.apache.ibatis.javassist.CtClass;
import org.apache.ibatis.javassist.CtMethod;
import org.apache.ibatis.mapping.SqlCommandType;
import org.apache.ibatis.session.SqlSession;

import java.lang.reflect.Method;
import java.util.Arrays;

/**
 * 工具类：可以动态的生成DAO的实现类。（或者说可以动态生成DAO的代理类）
 * 注意注意注意注意注意！！！！！！：
 *      凡是使用GenerateDaoProxy的，SQLMapper.xml映射文件中namespace必须是dao接口的全名，id必须是dao接口中的方法名。
 * @author 动力节点
 * @version 1.0
 * @since 1.0
 */
public class GenerateDaoProxy { // GenerateDaoProxy是mybatis框架的开发者写的。

    /**
     * 生成dao接口实现类，并且将实现类的对象创建出来并返回。
     * @param daoInterface dao接口
     * @return dao接口实现类的实例化对象。
     */
    public static Object generate(SqlSession sqlSession, Class daoInterface){
        // 类池
        ClassPool pool = ClassPool.getDefault();
        // 制造类(com.powernode.bank.dao.AccountDao --> com.powernode.bank.dao.AccountDaoProxy)
        CtClass ctClass = pool.makeClass(daoInterface.getName() + "Proxy"); // 实际本质上就是在内存中动态生成一个代理类。
        // 制造接口
        CtClass ctInterface = pool.makeInterface(daoInterface.getName());
        // 实现接口
        ctClass.addInterface(ctInterface);
        // 实现接口中所有的方法
        Method[] methods = daoInterface.getDeclaredMethods();
        Arrays.stream(methods).forEach(method -> {
            // method是接口中的抽象方法
            // 将method这个抽象方法进行实现
            try {
                // Account selectByActno(String actno);
                // public Account selectByActno(String actno){ 代码; }
                StringBuilder methodCode = new StringBuilder();
                methodCode.append("public ");
                methodCode.append(method.getReturnType().getName());
                methodCode.append(" ");
                methodCode.append(method.getName());
                methodCode.append("(");
                // 需要方法的形式参数列表
                Class<?>[] parameterTypes = method.getParameterTypes();
                for (int i = 0; i < parameterTypes.length; i++) {
                    Class<?> parameterType = parameterTypes[i];
                    methodCode.append(parameterType.getName());
                    methodCode.append(" ");
                    methodCode.append("arg" + i);
                    if(i != parameterTypes.length - 1){
                        methodCode.append(",");
                    }
                }
                methodCode.append(")");
                methodCode.append("{");
                // 需要方法体当中的代码
                // 对于javassist变量的类型需要使用全限定包名
                methodCode.append("org.apache.ibatis.session.SqlSession sqlSession = com.powernode.bank.utils.SqlSessionUtil.openSession();");
                // 需要知道是什么类型的sql语句
                // sql语句的id是框架使用者提供的，具有多变性。对于我框架的开发人员来说。我不知道。
                // 既然我框架开发者不知道sqlId，怎么办呢？mybatis框架的开发者于是就出台了一个规定：凡是使用GenerateDaoProxy机制的。
                // sqlId都不能随便写。namespace必须是dao接口的全限定名称。id必须是dao接口中方法名。
                String sqlId = daoInterface.getName() + "." + method.getName();
                // getConfiguration() 获取mybatis核心配置
                // getMappedStatement() 获取sql
                // getSqlCommandType() 获取sql的类型 CRUD
                // 获取sql语句的类型
                SqlCommandType sqlCommandType = sqlSession.getConfiguration().getMappedStatement(sqlId).getSqlCommandType();
                if (sqlCommandType == SqlCommandType.INSERT) {

                }
                if (sqlCommandType == SqlCommandType.DELETE) {

                }
                if (sqlCommandType == SqlCommandType.UPDATE) {
                    methodCode.append("return sqlSession.update(\""+sqlId+"\", arg0);");
                }
                if (sqlCommandType == SqlCommandType.SELECT) {
                    String returnType = method.getReturnType().getName();
                    methodCode.append("return ("+returnType+")sqlSession.selectOne(\""+sqlId+"\", arg0);");
                }

                methodCode.append("}");
                CtMethod ctMethod = CtMethod.make(methodCode.toString(), ctClass);
                ctClass.addMethod(ctMethod);
            } catch (Exception e) {
                e.printStackTrace();
            }

        });

        // 创建对象
        Object obj = null;
        try {
            Class<?> clazz = ctClass.toClass();
            obj = clazz.newInstance();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return obj;
    }

}
```



## 🌊 工具类GenerateDaoProxy测试与Mybatis的getMapper方法


+ 要想使用工具类GenerateDaoProxy这种自动生成Dao接口实现类的机制： 
    - namespace必须是dao接口的全限定名称。
    - id必须是dao接口的方法名。



```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">

<!--sqlMapper.xml文件的编写者，提供者是谁？使用你mybatis框架的java程序员负责提供的。-->
<!--要想使用这种机制：namespace必须是dao接口的全限定名称。-->
<mapper namespace="com.powernode.bank.dao.AccountDao">

    <!--要想使用这种机制：id必须是dao接口的方法名。-->
    <select id="selectByActno" resultType="com.powernode.bank.pojo.Account">
        select * from t_act where actno = #{actno}
    </select>

    <update id="updateByActno">
        update t_act set balance = #{balance} where actno = #{actno}
    </update>

</mapper>
```



```java
package com.powernode.bank.service.impl;

import com.powernode.bank.dao.AccountDao;
import com.powernode.bank.dao.impl.AccountDaoImpl;
import com.powernode.bank.exceptions.MoneyNotEnoughException;
import com.powernode.bank.exceptions.TransferException;
import com.powernode.bank.pojo.Account;
import com.powernode.bank.service.AccountService;
import com.powernode.bank.utils.GenerateDaoProxy;
import com.powernode.bank.utils.SqlSessionUtil;
import org.apache.ibatis.session.SqlSession;

public class AccountServiceImpl implements AccountService {

    //private AccountDao accountDao = new AccountDaoImpl();

    // 这是咱们自己封装的。
    // SqlSession对象用于获取sql生成与sql对应的方法(不然要读配置文件获取sql)
    //private AccountDao accountDao = (AccountDao) GenerateDaoProxy.generate(SqlSessionUtil.openSession(), AccountDao.class);

    // 在mybatis当中，mybatis提供了相关的机制。也可以动态为我们生成dao接口的实现类。（代理类：dao接口的代理）
    // mybatis当中实际上采用了代理模式。在内存中生成dao接口的代理类，然后创建代理类的实例。
    // 使用mybatis的这种代理机制的前提：SqlMapper.xml文件中namespace必须是dao接口的全限定名称，id必须是dao接口中的方法名。
    // 通过SqlSession调用，不用额外传入SqlSession对象
    // 怎么用？代码怎么写？AccountDao accountDao = sqlSession.getMapper(AccountDao.class);
    // getMapper 映射器
    private AccountDao accountDao = SqlSessionUtil.openSession().getMapper(AccountDao.class);

    @Override
    public void transfer(String fromActno, String toActno, double money) throws MoneyNotEnoughException, TransferException {

        // 添加事务控制代码
        SqlSession sqlSession = SqlSessionUtil.openSession();

        // 1. 判断转出账户的余额是否充足(select)
        Account fromAct = accountDao.selectByActno(fromActno);
        if (fromAct.getBalance() < money) {
            // 2. 如果转出账户余额不足，提示用户
            throw new MoneyNotEnoughException("对不起，余额不足！");
        }
        // 3. 如果转出账户余额充足，更新转出账户余额(update)
        // 先更新内存中java对象account的余额
        Account toAct = accountDao.selectByActno(toActno);
        fromAct.setBalance(fromAct.getBalance() - money);
        toAct.setBalance(toAct.getBalance() + money);
        int count = accountDao.updateByActno(fromAct);

        // 模拟异常
        /*String s = null;
        s.toString();*/

        // 4. 更新转入账户余额(update)
        count += accountDao.updateByActno(toAct);
        if (count != 2) {
            throw new TransferException("转账异常，未知原因");
        }

        // 提交事务
        sqlSession.commit();
        // 关闭事务
        SqlSessionUtil.close(sqlSession);
    }


}
```



# 🥽 面向接口进行CRUD


![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851538273-0f67f812-00db-48c9-9a7e-6a4d78bc2761.png)



SqlSessionUtil



```java
package com.powernode.mybatis.utils;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

import java.io.IOException;

/**
 * MyBatis工具类
 * @author 动力节点
 * @version 1.0
 * @since 1.0
 */
public class SqlSessionUtil {

    private SqlSessionUtil(){}

    private static SqlSessionFactory sqlSessionFactory;

    static {
        try {
            sqlSessionFactory = new SqlSessionFactoryBuilder().build(Resources.getResourceAsStream("mybatis-config.xml"));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    // 全局的，服务器级别的，一个服务器当中定义一个即可。
    // 为什么把SqlSession对象放到ThreadLocal当中呢？为了保证一个线程对应一个SqlSession。
    private static ThreadLocal<SqlSession> local = new ThreadLocal<>();

    /**
     * 获取会话对象。
     * @return 会话对象
     */
    public static SqlSession openSession(){
        SqlSession sqlSession = local.get();
        if (sqlSession == null) {
            sqlSession = sqlSessionFactory.openSession();
            // 将sqlSession对象绑定到当前线程上。
            local.set(sqlSession);
        }
        return sqlSession;
    }

    /**
     * 关闭SqlSession对象(从当前线程中移除SqlSession对象。)
     * @param sqlSession
     */
    public static void close(SqlSession sqlSession){
        if (sqlSession != null) {
            sqlSession.close();
            // 注意移除SqlSession对象和当前线程的绑定关系。
            // 因为Tomcat服务器支持线程池。也就是说：用过的线程对象t1，可能下一次还会使用这个t1线程。
            local.remove();
        }
    }

}
```



Car



```java
package com.powernode.mybatis.pojo;

/**
 * 封装汽车相关信息的pojo类。普通的java类。
 * @author 动力节点
 * @version 1.0
 * @since 1.0
 */
public class Car {
    // 数据库表当中的字段应该和pojo类的属性一一对应。
    // 建议使用包装类，这样可以防止null的问题。
    private Long id;
    private String carNum;
    private String brand;
    private Double guidePrice;
    private String produceTime;
    private String carType;

    @Override
    public String toString() {
        return "Car{" +
                "id=" + id +
                ", carNum='" + carNum + '\'' +
                ", brand='" + brand + '\'' +
                ", guidePrice=" + guidePrice +
                ", produceTime='" + produceTime + '\'' +
                ", carType='" + carType + '\'' +
                '}';
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getCarNum() {
        return carNum;
    }

    /*public String getXyz() {
        return carNum;
    }*/

    public void setCarNum(String carNum) {
        this.carNum = carNum;
    }

    public String getBrand() {
        return brand;
    }

    public void setBrand(String brand) {
        this.brand = brand;
    }

    public Double getGuidePrice() {
        return guidePrice;
    }

    public void setGuidePrice(Double guidePrice) {
        this.guidePrice = guidePrice;
    }

    public String getProduceTime() {
        return produceTime;
    }

    public void setProduceTime(String produceTime) {
        this.produceTime = produceTime;
    }

    public String getCarType() {
        return carType;
    }

    public void setCarType(String carType) {
        this.carType = carType;
    }

    public Car(Long id, String carNum, String brand, Double guidePrice, String produceTime, String carType) {
        this.id = id;
        this.carNum = carNum;
        this.brand = brand;
        this.guidePrice = guidePrice;
        this.produceTime = produceTime;
        this.carType = carType;
    }

    public Car() {
    }
}
```



CarMapper



```java
package com.powernode.mybatis.mapper; // 包名也有叫做：com.powernode.mybatis.dao
                                    //mapper包就是dao包。

import com.powernode.mybatis.pojo.Car;

import java.util.List;

// 一般使用mybatis的话，一般不叫做XXXDao了。一般都是XXXMapper。
public interface CarMapper { //CarDao。

    /**
     * 新增Car
     * @param car
     * @return
     */
    int insert(Car car);

    /**
     * 根据id删除Car
     * @param id
     * @return
     */
    int deleteById(Long id);

    /**
     * 修改汽车信息
     * @param car
     * @return
     */
    int update(Car car);

    /**
     * 根据id查询汽车信息
     * @param id
     * @return
     */
    Car selectById(Long id);

    /**
     * 获取所有的汽车信息。
     * @return
     */
    List<Car> selectAll();

}
```



CarMapper.xml



```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">

<mapper namespace="com.powernode.mybatis.mapper.CarMapper">

    <insert id="insert">
        insert into t_car values(null, #{carNum},#{brand},#{guidePrice},#{produceTime},#{carType})
    </insert>
    <delete id="deleteById">
        delete from t_car where id = #{id}
    </delete>
    <update id="update">
        update t_car set
        car_num=#{carNum},brand=#{brand},guide_price=#{guidePrice},produce_time=#{produceTime},car_type=#{carType}
        where id = #{id}
    </update>
    <select id="selectById" resultType="com.powernode.mybatis.pojo.Car">
        select
            id,
            car_num as carNum,
            brand,
            guide_price as guidePrice,
            produce_time as produceTime,
            car_type as carType
        from t_car where id = #{id}
    </select>
    <select id="selectAll" resultType="com.powernode.mybatis.pojo.Car">
        select
            id,
            car_num as carNum,
            brand,
            guide_price as guidePrice,
            produce_time as produceTime,
            car_type as carType
        from t_car
    </select>

</mapper>
```



```java
package com.powernode.mybatis.test;

import com.powernode.mybatis.mapper.CarMapper;
import com.powernode.mybatis.pojo.Car;
import com.powernode.mybatis.utils.SqlSessionUtil;
import org.apache.ibatis.session.SqlSession;
import org.junit.Test;

import java.util.List;

public class CarMapperTest {
    @Test
    public void testInsert(){
        SqlSession sqlSession = SqlSessionUtil.openSession();
        // 面向接口获取接口的代理对象
        CarMapper mapper = sqlSession.getMapper(CarMapper.class);
        Car car = new Car(null, "4444", "奔驰C200", 32.0, "2000-10-10", "新能源");
        int count = mapper.insert(car);
        System.out.println(count);
        sqlSession.commit();
    }
    @Test
    public void testDeleteById(){
        SqlSession sqlSession = SqlSessionUtil.openSession();
        CarMapper mapper = sqlSession.getMapper(CarMapper.class);
        int count = mapper.deleteById(154L);
        System.out.println(count);
        sqlSession.commit();
    }
    @Test
    public void testUpdate(){
        SqlSession sqlSession = SqlSessionUtil.openSession();
        CarMapper mapper = sqlSession.getMapper(CarMapper.class);
        Car car = new Car(155L, "2222", "凯美瑞222", 3.0, "2000-10-10", "新能源");
        mapper.update(car);
        sqlSession.commit();
    }
    @Test
    public void testSelectById(){
        SqlSession sqlSession = SqlSessionUtil.openSession();
        CarMapper mapper = sqlSession.getMapper(CarMapper.class);
        Car car = mapper.selectById(155L);
        System.out.println(car);
    }
    @Test
    public void testSelectAll(){
        SqlSession sqlSession = SqlSessionUtil.openSession();
        CarMapper mapper = sqlSession.getMapper(CarMapper.class);
        List<Car> cars = mapper.selectAll();
        cars.forEach(car -> System.out.println(car));
    }
}
```



# 🥽 MyBatis小技巧


## 🌊 #{}和${}


```java
#{}的执行结果：

[main] DEBUG c.p.mybatis.mapper.CarMapper.selectByCarType - ==>  
Preparing: 
	select 
		id, 
		car_num as carNum, 
		brand, 
		guide_price as guidePrice, 
		produce_time as produceTime, 
		car_type as carType 
	from t_car where car_type = ?
[main] DEBUG c.p.mybatis.mapper.CarMapper.selectByCarType - ==> 
Parameters: 新能源(String)
[main] DEBUG c.p.mybatis.mapper.CarMapper.selectByCarType - <==      
Total: 2
```



```java
${}的执行结果：

[main] DEBUG c.p.mybatis.mapper.CarMapper.selectByCarType - ==>  
Preparing: 
	select 
		id, 
		car_num as carNum, 
		brand, 
		guide_price as guidePrice, 
		produce_time as produceTime, 
		car_type as carType 
	from t_car where car_type = 新能源
[main] DEBUG c.p.mybatis.mapper.CarMapper.selectByCarType - ==> 
Parameters:
org.apache.ibatis.exceptions.PersistenceException:
### Error querying database.  Cause: java.sql.SQLSyntaxErrorException: Unknown column '新能源' in 'where clause'
### The error may exist in CarMapper.xml
### The error may involve defaultParameterMap
### The error occurred while setting parameters
### SQL: select             id,             car_num as carNum,             brand,             guide_price as guidePrice,             produce_time as produceTime,             car_type as carType         from             t_car         where             car_type = 新能源
### Cause: java.sql.SQLSyntaxErrorException: Unknown column '新能源' in 'where clause'
```



+ #{}和${}的区别： 
    - #{}: 底层使用PreparedStatement。特点：先进行SQL语句的编译，然后给SQL语句的占位符问号?传值。可以避免SQL注入的风险。
    - ${}：底层使用Statement。特点：先进行SQL语句的拼接，然后再对SQL语句进行编译。存在SQL注入的风险。
+ 优先使用#{}，这是原则。避免SQL注入的风险。



对查询结果进行升序或降序排序：



```java
public interface CarMapper {

    /**
     * 查询所有的汽车信息。然后通过asc升序，desc降序。
     * @param ascOrDesc
     * @return
     */
    List<Car> selectAllByAscOrDesc(String ascOrDesc);

}
```



```xml
    <select id="selectAllByAscOrDesc" resultType="car">
        select
            id,
            car_num as carNum,
            brand,
            guide_price as guidePrice,
            produce_time as produceTime,
            car_type as carType
        from
            t_car
        order by
            produce_time ${ascOrDesc}
    </select>
```



```java
    @Test
    public void testSelectAllByAscOrDesc(){
        SqlSession sqlSession = SqlSessionUtil.openSession();
        CarMapper mapper = sqlSession.getMapper(CarMapper.class);
        List<Car> cars = mapper.selectAllByAscOrDesc("desc");
        cars.forEach(car -> System.out.println(car));
        sqlSession.close();
    }
```



```java
#{}的执行结果：

Preparing: 
	select
	     id, car_num as carNum, brand, guide_price as guidePrice, produce_time as produceTime, car_type as carType
	from t_car order by produce_time ?
Parameters: asc(String)

// 填充后的sql语句
select
    id, car_num as carNum, brand, guide_price as guidePrice, produce_time as produceTime, car_type as carType
from t_car order by produce_time 'asc'
```



```java
${}的执行结果：

Preparing:
    select id, car_num as carNum, brand, guide_price as guidePrice, produce_time as produceTime, car_type as carType
    from t_car order by produce_time asc
Parameters:
```



+ 如果需要SQL语句的关键字放到SQL语句中，只能使用${}，因为#{}是以值的形式放到SQL语句当中的。



## 🌊 向SQL语句当中拼接表名


+ 向SQL语句当中拼接表名，就需要使用${}
+ 现实业务当中，可能会存在分表存储数据的情况。因为一张表存的话，数据量太大。查询效率比较低。
+ 可以将这些数据有规律的分表存储，这样在查询的时候效率就比较高。因为扫描的数据量变少了。
+ 日志表：专门存储日志信息的。如果t_log只有一张表，这张表中每一天都会产生很多log，慢慢的，这个表中数据会很多。
+ 怎么解决问题？  
可以每天生成一个新表。每张表以当天日期作为名称，例如：  
t_log_20220901  
t_log_20220902  
....
+ 你想知道某一天的日志信息怎么办？  
假设今天是20220901，那么直接查：t_log_20220901的表即可。



```xml
<!--namespace不能使用别名机制。必须写全限定接口名称。带有包名的。-->
<mapper namespace="com.powernode.mybatis.mapper.LogMapper">

    <select id="selectAllByTable" resultType="Log">
        <!--select * from t_log_#{date}-->
        select * from t_log_${date}
    </select>

</mapper>
```



```java
public class LogMapperTest {
    @Test
    public void testSelectAllByTable(){
        SqlSession sqlSession = SqlSessionUtil.openSession();
        LogMapper mapper = sqlSession.getMapper(LogMapper.class);
        List<Log> logs = mapper.selectAllByTable("20220901");
        logs.forEach(log -> System.out.println(log));
    }
}
```



## 🌊 批量删除：一次删除多条记录。


批量删除的SQL语句有两种写法：  
第一种or：delete from t_car where id=1 or id=2 or id=3;  
第二种int：delete from t_car where id in(1,2,3);



应该采用`${}`的方式：  
delete from t_car where id in(${ids});



```java
public interface CarMapper {

    /**
     * 批量删除，根据id
     * @param ids
     * @return
     */
    int deleteBatch(String ids);

}
```



```xml
    <delete id="deleteBatch">
        <!--delete from t_car where id in(#{ids})-->
        delete from t_car where id in(${ids})
    </delete>
```



```java
    public void testDeleteBatch(){
        SqlSession sqlSession = SqlSessionUtil.openSession();
        CarMapper mapper = sqlSession.getMapper(CarMapper.class);
        int count = mapper.deleteBatch("155,156,157");
        System.out.println(count);
        sqlSession.commit();
        sqlSession.close();
    }
```



## 🌊 模糊查询：like


+ 需求：根据汽车品牌进行模糊查询  
select * from t_car where brand like '%奔驰%';  
select * from t_car where brand like '%比亚迪%';
+ 第一种方案：  
`'%${brand}%'`
+ 第二种方案：concat函数，这个是mysql数据库当中的一个函数，专门进行字符串拼接  
`concat('%',#{brand},'%')`
+ 第三种方案：比较鸡肋了。可以不算。  
`concat('%','${brand}','%')`
+ 第四种方案：  
`"%"#{brand}"%"`



```java
    <select id="selectByBrandLike" resultType="CAR">
        select
            id,
            car_num as carNum,
            brand,
            guide_price as guidePrice,
            produce_time as produceTime,
            car_type as carType
        from
            t_car
        where
            <!--brand like '%#{brand}%' 先进行编译 brand like '%?%' 里面的？被认为字符串的一部分无法进行数据的填充-->
            <!--brand like '%${brand}%'-->
            <!--brand like concat('%',#{brand},'%')-->
            <!--brand like concat('%','${brand}','%')-->
            brand like "%"#{brand}"%"
    </select>
```



## 🌊 别名机制


+ namespace不能使用别名机制。必须写全限定接口名称。带有包名的。



### 💦 typeAliases


```xml
    <!--起别名-->
    <!-- 该标签需要再settings标签之后，写在Mybatis核心配置文件中 -->
    <typeAliases>
        <!--
            type: 指定给哪个类型起别名
            alias：指定别名
            注意：别名不缺分大小写。
            alias属性是可以省略的。有默认的别名。
        -->
        <!--别名自己指定的-->
        <!--<typeAlias type="com.powernode.mybatis.pojo.Car" alias="aaa"/>
        <typeAlias type="com.powernode.mybatis.pojo.Log" alias="bbb"/>-->

		<!--采用默认的别名机制-->
        <!--省略alias之后，别名就是类的简名，比如：com.powernode.mybatis.pojo.Car的别名就是Car/car/cAR/cAr，不区分大小写。 -->
        <typeAlias type="com.powernode.mybatis.pojo.Car"/>
        <typeAlias type="com.powernode.mybatis.pojo.Log"/>

    </typeAliases>
```



```xml
<select id="selectByBrandLike" resultType="CAR">
<select id="selectAllByAscOrDesc" resultType="car">
<select id="selectByCarType" resultType="cAr">
```



### 💦 package


```xml
    <!--起别名-->
    <!-- 该标签需要再settings标签之后，写在Mybatis核心配置文件中 -->
    <typeAliases>
    
        <!--将这个包下的所有的类全部自动起别名。别名就是类简名。不区分大小写。-->
        <package name="com.powernode.mybatis.pojo"/>

    </typeAliases>
```



## 🌊 mybatis-config.xml文件中的mappers标签。


+ `<mapper resource="CarMapper.xml"/>` 要求类的根路径下必须有：CarMapper.xml
+ `<mapper url="file:///d:/CarMapper.xml"/>` 要求在d:/下有CarMapper.xml文件
+ `<mapper class="全限定接口名，带有包名"/>`
+ mapper标签的属性可以有三个： 
    - resource:这种方式是从类的根路径下开始查找资源。采用这种方式的话，你的配置文件需要放到类路径当中才行。
    - url: 这种方式是一种绝对路径的方式，这种方式不要求配置文件必须放到类路径当中，哪里都行，只要提供一个绝对路径就行。这种方式使用极少，因为移植性太差。
    - class: 这个位置提供的是mapper接口的全限定接口名，必须带有包名的。
+ 思考：mapper标签的作用是指定SqlMapper.xml文件的路径，指定接口名有什么用呢？ 
    - `<mapper class="com.powernode.mybatis.mapper.CarMapper"/>`
    - 如果你class指定是：com.powernode.mybatis.mapper.CarMapper
    - 那么mybatis框架会自动去com/powernode/mybatis/mapper目录下查找CarMapper.xml文件。
    - 注意：也就是说：如果你采用这种方式，那么你必须保证CarMapper.xml文件和CarMapper接口必须在同一个目录下。并且名字一致。
    - CarMapper接口-> CarMapper.xml
    - LogMapper接口-> LogMapper.xml
    - ....
+ 将类和配置文件放在同一个目录下，可以采用如下方式建包，因为resources相当于类的根路径，就是打包后的根路径，java也相当于类的根路径，所以打包完成后resources下与java下相同的文件会被放在一起  
![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851538417-a7073062-232e-4f6f-bde9-8694f7bccca6.png)
+ 在IDEA的resources目录下新建多重目录的话，必须是这样创建： 
    - com/powernode/mybatis/mapper
    - 不能这样：
    - com.powernode.mybatis.mapper 这个会被整个当成一个目录名



```xml
    <mappers>

        <!--<mapper resource="CarMapper.xml"/>
        <mapper resource="LogMapper.xml"/>-->

        <!--使用这种方式的前提：CarMapper.xml文件的位置不能随便放-->
        <!--必须和CarMapper接口放在一起。-->
        <!--XML文件的名字必须和接口名一致。-->
        <!--<mapper class="com.powernode.mybatis.mapper.CarMapper"/>
        <mapper class="com.powernode.mybatis.mapper.LogMapper"/>-->

        <!-- 这种方式在实际开发中是使用的。-->
        <!--前提是：XML文件必须和接口放在一起。并且名字一致。-->
        <!-- 指定xml文件放在com.powernode.mybatis.mapper包下 -->
        <package name="com.powernode.mybatis.mapper"/>
        

    </mappers>
```



## 🌊 idea配置文件模板


mybatis-config.xml和SqlMapper.xml文件可以在IDEA中提前创建好模板，以后通过模板创建配置文件。



![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851538411-1fba2f4c-a984-47b3-9794-d5c421a52bf1.png)



mybatis-config.xml 模板



```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE configuration
        PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-config.dtd">

<configuration>
    <properties resource=""/>
    <typeAliases>
        <package name=""/>
    </typeAliases>
    <environments default="dev">
        <environment id="dev">
            <transactionManager type="JDBC"/>
            <dataSource type="POOLED">
                <property name="driver" value="${jdbc.driver}"/>
                <property name="url" value="${jdbc.url}"/>
                <property name="username" value="${jdbc.username}"/>
                <property name="password" value="${jdbc.password}"/>
            </dataSource>
        </environment>
    </environments>
    <mappers>
        <package name=""/>
    </mappers>
</configuration>
```



![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851538522-bf89ea43-39a4-4814-bdcc-c0016af69b06.png)



SqlMapper.xml 模板



```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">

<mapper namespace="">
</mapper>
```



![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851538831-70029afa-1e3c-4202-9b65-7196b8abb7f1.png)  
![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851538775-82363656-ee32-4c03-a922-c866534f18ff.png)



## 🌊 插入数据时获取自动生成的主键


+  前提是：主键是自动生成的。 
+  插入一条新的记录之后，自动生成了主键，而这个主键需要在其他表中使用时。 
+  插入一个用户数据的同时需要给该用户分配角色：需要将生成的用户的id插入到角色表的user_id字段上。  
![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851538901-ba2ec472-5196-4b71-8345-4ca35b1ae67c.png) 
+  第一种方式：可以先插入用户数据，再写一条查询语句获取id，然后再插入user_id字段。【比较麻烦】 
+  第二种方式：mybatis提供了一种方式更加便捷。 

```xml
    <!--
        useGeneratedKeys="true" 使用自动生成的主键值。
        keyProperty="id" 指定主键值赋值给对象的哪个属性。这个就表示将主键值赋值给Car对象的id属性。
        /**
         * 插入Car信息，并且使用生成的主键值。
         * @param car
         * @return
         */
        int insertCarUseGeneratedKeys(Car car); keyProperty="id" 会将自动生成的主键值赋值给传入的car对象的id属性
    -->
    <insert id="insertCarUseGeneratedKeys" useGeneratedKeys="true" keyProperty="id">
        insert into t_car values(null,#{carNum},#{brand},#{guidePrice},#{produceTime},#{carType})
    </insert>
```

  



# 🥽 MyBatis参数处理


表：t_student



```sql
USE dbtest;
DROP TABLE IF EXISTS t_student;
CREATE TABLE t_student (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    age INT,
    height DOUBLE,
    birth DATE,
    sex CHAR(1)
);
INSERT INTO t_student(name, age, height, birth, sex) VALUES ('张三', 20, 1.77, '2001-01-02', '男');
INSERT INTO t_student(name, age, height, birth, sex) VALUES ('李四', 20, 1.67, '2001-11-22', '女');
```



![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851538919-456880df-ac66-49b9-b09f-b2fb82aa2eb4.png)



pojo类：



```java
package com.powernode.mybatis.pojo;

import java.util.Date;

/**
 * 学生类
 * @author 老杜
 * @version 1.0
 * @since 1.0
 */
public class Student {
    private Long id;
    private String name;
    private Integer age;
    private Double height;
    private Character sex;
    private Date birth;
    // constructor
    // setter and getter
    // toString
}
```



## 🌊单个简单类型参数


+ 简单类型包括： 
    - byte short int long float double char
    - Byte Short Integer Long Float Double Character
    - String
    - java.util.Date
    - java.sql.Date



```xml
    <!--
    当接口中的方法的参数只有一个（单个参数），并且参数的数据类型都是简单类型。
    根据id查询、name查询、birth查询、sex查询
    List<Student> selectById(Long id);
    List<Student> selectByName(String name);
    List<Student> selectByBirth(Date birth);
    List<Student> selectBySex(Character sex);

    parameterType属性的作用：
        告诉mybatis框架，我这个方法的参数类型是什么类型。
        mybatis框架自身带有类型自动推断机制，所以大部分情况下parameterType属性都是可以省略不写的。

        SQL语句最终是这样的：
            select * from t_student where id = ?
        JDBC代码是一定要给?传值的。
        怎么传值？ps.setXxx(第几个问号, 传什么值);
            ps.setLong(1, 1L);
            ps.setString(1, "zhangsan");
            ps.setDate(1, new Date());
            ps.setInt(1, 100);
            ...
        mybatis底层到底调用setXxx的哪个方法，取决于parameterType属性的值。

    注意：mybatis框架实际上内置了很多别名。可以参考开发手册。
    -->
    <select id="selectById" resultType="Student" parameterType="long">
        select * from t_student where id = #{id}
    </select>

	<!-- javaType=String 填充参数的Java类型, jdbcType=VARCHAR 填充参数对应数据库的类型 -->
    <select id="selectByName" resultType="student">
        select * from t_student where name = #{name, javaType=String, jdbcType=VARCHAR}
    </select>

    <select id="selectByBirth" resultType="student">
        select * from t_student where birth = #{birth}
    </select>

    <select id="selectBySex" resultType="student">
        select * from t_student where sex = #{sex}
    </select>
```



> [【开发手册 -- 内置别名】](https://mybatis.net.cn/configuration.html#typeAliases)
>



## 🌊 Map集合


```xml
    <!--
        保存学生信息，通过Map参数。以下是单个参数。但是参数的类型不是简单类型。是Map集合。
        int insertStudentByMap(Map<String, Object> map);
    -->
    <!--<insert id="insertStudentByMap" parameterType="map">-->
    <!-- 这种方式是手动封装Map集合，将每个条件以key和value的形式存放到集合中。然后在使用的时候通过#{map集合的key}来取值。 -->
    <!-- 使用Map集合的key取值, 可以自动推出传入的参数为map集合，使用集合中的数据 -->
    <insert id="insertStudentByMap">
        insert into t_student(id,name,age,sex,birth,height) values(null,#{姓名},#{年龄},#{性别},#{生日},#{身高})
    </insert>
```



## 🌊 实体类参数


```java
    <!--
        保存学生信息，通过POJO参数。Student是单个参数。但是不是简单类型。
        int insertStudentByPOJO(Student student);
    -->
    <!-- 这里需要注意的是：#{} 里面写的是属性名字。这个属性名其本质上是：set/get方法名去掉set/get之后的名字。-->
    <!--<insert id="insertStudentByPOJO" parameterType="student">-->
    <!-- 可以自动推出类型为Student类 -->
    <insert id="insertStudentByPOJO">
        insert into t_student(id,name,age,sex,birth,height) values(null,#{name},#{age},#{sex},#{birth},#{height})
    </insert>
```



## 🌊 多参数


```xml
    <!--
         这是多参数。
         根据name和sex查询Student信息。
         如果是多个参数的话，mybatis框架底层是怎么做的呢？
              mybatis框架会自动创建一个Map集合。并且Map集合是以这种方式存储参数的：
                  map.put("arg0", name);
                  map.put("arg1", sex);
                  map.put("param1", name);
                  map.put("param2", sex);
    
        注意：低版本的mybatis中，使用的是：#{0}和#{1}，以及#{2}...
        使用mybatis3.4.2之前的版本时：要用#{0}和#{1}这种形式。
        高版本的mybatis中，使用的是：
            #{arg0}
            #{arg1}
            #{arg2}
            #{arg3}
            #{arg4}

            #{param1}
            #{param2}
            #{param3}
            #{param4}
    -->
    <!-- 
        List<Student> selectByNameAndSex(String name, Character sex); 
    -->
    <select id="selectByNameAndSex" resultType="Student">
        <!--select * from t_student where name = #{arg0} and sex = #{arg1}-->
        <!--select * from t_student where name = #{param1} and sex = #{param2}-->
        select * from t_student where name = #{arg0} and sex = #{param2}
    </select>
```



## 🌊 @Param注解（命名参数）


```xml
    <!-- 
         Param注解。
         mybatis框架底层的实现原理：
         map.put("name", name);
         map.put("sex", sex);
    -->
    <!--  
        List<Student> selectByNameAndSex2(@Param("name") String name, @Param("sex") Character sex);
    -->
    <select id="selectByNameAndSex2" resultType="Student">
        <!--使用了@Param注解之后，arg0和arg1失效了-->
        <!--select * from t_student where name = #{arg0} and sex = #{arg1}-->

        <!--使用了@Param注解之后，param1和param2还可以用-->
        <!--select * from t_student where name = #{param1} and sex = #{param2}-->

        select * from t_student where name = #{name} and sex = #{sex}

    </select>
```



## 🌊 @Param源码分析


![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851539006-76040b46-d039-4c00-b669-18398149dd4a.png)



# 🥽 MyBatis查询语句专题


## 🌊 返回Map


![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851539204-eac90cb8-9be3-4e65-a487-5128bdf2807d.png)



+ 当返回的数据，没有合适的实体类对应的话，可以采用Map集合接收。字段名做key，字段值做value。
+ 查询如果可以保证只有一条数据，则返回一个Map集合即可。



```xml
    <!--resultType="java.util.Map"有别名：map-->
    <select id="selectByIdRetMap" resultType="map">
        select * from t_car where id = #{id}
    </select>
```



```java
    /**
     * 根据id获取汽车信息。将汽车信息放到Map集合中。
     * +-----+---------+----------+-------------+--------------+----------+
     * | id  | car_num | brand    | guide_price | produce_time | car_type |
     * +-----+---------+----------+-------------+--------------+----------+
     * | 158 | 1111    | 比亚迪汉 |        3.00 | 2000-10-10   | 新能源   |
     * +-----+---------+----------+-------------+--------------+----------+
     *
     * Map<String, Object>
     *     k                 v
     *     -----------------------
     *     "id"             158
     *     "car_num"        1111
     *     "brand"          比亚迪汉
     *     ....
     *
     * @param id
     * @return
     */
    Map<String, Object> selectByIdRetMap(Long id);
```



## 🌊 返回`List<Map>`


![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851539444-de8023f2-5986-4220-88c7-4c7ba8796d0d.png)



查询结果条数大于等于1条数据，则可以返回一个存储Map集合的List集合。`List<Map>`等同于`List<Car>`



```java
    /**
     * 查询所有的Car信息。返回一个存放Map集合的List集合。
     * @return
     */
    List<Map<String,Object>> selectAllRetListMap();
```



```xml
    <!--这个resultType不是list，是map-->
    <!-- 返回的每个数据记录使用map封装，只是多个数据记录放在list中，类型最终还是map -->
    <select id="selectAllRetListMap" resultType="map">
        select * from t_car
    </select>
```



## 🌊 返回Map<String,Map>


拿Car的id做key，以后取出对应的Map集合时更方便。  
![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851539339-0988224d-cda8-47a5-adb4-0a4c2b82d802.png)



```java
    /**
     * 查询所有的Car，返回一个大Map集合。
     * Map集合的key是每条记录的主键值。
     * Map集合的value是每条记录。
     * {
     *      160={car_num=3333, id=160, guide_price=32.00, produce_time=2000-10-10, brand=奔驰E300L, car_type=新能源},
     *      161={car_num=4444, id=161, guide_price=32.00, produce_time=2000-10-10, brand=奔驰C200, car_type=新能源},
     *      162={car_num=9999, id=162, guide_price=30.00, produce_time=2020-10-11, brand=帕萨特, car_type=燃油车},
     *      163={car_num=9991, id=163, guide_price=30.00, produce_time=2020-11-11, brand=凯美瑞, car_type=燃油车},
     *      158={car_num=1111, id=158, guide_price=3.00, produce_time=2000-10-10, brand=比亚迪汉, car_type=新能源},
     *      159={car_num=2222, id=159, guide_price=32.00, produce_time=2000-10-10, brand=比亚迪秦, car_type=新能源}
     * }
     * @return
     */
    @MapKey("id") // 将查询结果的id值作为整个大Map集合的key。
    Map<Long, Map<String,Object>> selectAllRetMap();
```



```xml
    <select id="selectAllRetMap" resultType="map">
        select * from t_car
    </select>
```



## 🌊 resultMap结果映射


+ 查询结果的列名和java对象的属性名对应不上怎么办？ 
    - 第一种方式：as 给列起别名
    - 第二种方式：使用resultMap进行结果映射
    - 第三种方式：是否开启驼峰命名自动映射（配置settings）



### 💦 使用resultMap进行结果映射


```java
    /**
     * 查询所有的Car信息。使用resultMap标签进行结果映射。
     * @return
     */
    List<Car> selectAllByResultMap();
```



```xml
    <!--
        1.专门定义一个结果映射，在这个结果映射当中指定数据库表的字段名和Java类的属性名的对应关系。
        2. type属性：用来指定POJO类的类名。
        3. id属性：指定resultMap的唯一标识。这个id将来要在select标签中使用。
    -->
    <resultMap id="carResultMap" type="Car">
        <!--如果数据库表中有主键，一般都是有主键，要不然不符合数据库设计第一范式。-->
        <!--如果有主键，建议这里配置一个id标签，注意：这不是必须的。但是官方的解释是什么呢？这样的配置可以让mybatis提高效率。-->
        <id property="id" column="id"/>
        <!--<result property="id" column="id"/>-->
        <!--property后面填写POJO类的属性名-->
        <!--column后面填写数据库表的字段名-->
        <result property="carNum" column="car_num" javaType="java.lang.String" jdbcType="VARCHAR"/>
        <!--如果column和property是一样的，这个可以省略。-->
        <!--<result property="brand" column="brand"/>-->
        <result property="guidePrice" column="guide_price"/>
        <result property="produceTime" column="produce_time"/>
        <result property="carType" column="car_type" javaType="string" jdbcType="VARCHAR"/>
    </resultMap>

    <!--select标签的resultMap属性，用来指定使用哪个结果映射。resultMap后面的值是resultMap的id-->
    <select id="selectAllByResultMap" resultMap="carResultMap">
        select * from t_car
    </select>
```



### 💦 开启驼峰命名自动映射


+ 使用这种方式的前提是：属性名遵循Java的命名规范，数据库表的列名遵循SQL的命名规范。
+ Java命名规范：首字母小写，后面每个单词首字母大写，遵循驼峰命名方式。
+ SQL命名规范：全部小写，单词之间采用下划线分割。
+ 比如以下的对应关系：  
![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851539396-4a579832-ca64-471f-ac81-923905a06aeb.png)



在mybatis核心配置文件中进行配置



```xml
    <!--mybatis的全局设置，开启驼峰命名自动映射-->
    <settings>
        <setting name="mapUnderscoreToCamelCase" value="true"/>
    </settings>
```



```java
    /**
     * 查询所有的Car信息。但是启用了驼峰命名自动映射机制。
     * @return
     */
    List<Car> selectAllByMapUnderscoreToCamelCase();
```



```xml
    <select id="selectAllByMapUnderscoreToCamelCase" resultType="Car">
        select * from t_car
    </select>
```



## 🌊 返回总记录条数


```java
    /**
     * 获取Car的总记录条数。
     * @return
     */
    Long selectTotal();
```



```xml
    <!--<select id="selectTotal" resultType="java.lang.Long">-->
    <select id="selectTotal" resultType="_long">
        select count(*) from t_car
    </select>
```



# 🥽 动态SQL


+ 有的业务场景，也需要SQL语句进行动态拼接，例如：
+ 批量删除  
![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851539733-cde2bb3b-8b95-4c8e-91c0-de2addc8fa9e.png)

```sql
delete from t_car where id in(1,2,3,4,5,6,......这里的值是动态的，根据用户选择的id不同，值是不同的);
```

 

+ 多条件查询  
![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851540041-2a3e8446-a0b0-4251-ae0a-24dce72e053c.png)

```sql
select * from t_car where brand like '丰田%' and guide_price > 30 and .....;
```

 



## 🌊 if标签


```java
/**
     * 多条件查询
     * @param brand 品牌
     * @param guidePrice 指导价
     * @param carType 汽车类型
     * @return
     */
    List<Car> selectByMultiCondition(@Param("brand") String brand, @Param("guidePrice") Double guidePrice, @Param("carType") String carType);
```



```xml
    <select id="selectByMultiCondition" resultType="Car">
    	<!-- where 1 = 1 保证条件都为空时sql语法可以通过 -->
        select * from t_car where 1 = 1
        <!--
            1. if标签中test属性是必须的。
            2. if标签中test属性的值是false或者true。
            3. 如果test是true，则if标签中的sql语句就会拼接。反之，则不会拼接。
            4. test属性中可以使用的是：
                当使用了@Param注解，那么test中要出现的是@Param注解指定的参数名。@Param("brand")，那么这里只能使用brand
                当没有使用@Param注解，那么test中要出现的是：param1 param2 param3 arg0 arg1 arg2....
                当使用了POJO，那么test中出现的是POJO类的属性名。
            5. 在mybatis的动态SQL当中，不能使用&&，只能使用and。
        -->
        <if test="brand != null and brand != ''">
            and brand like "%"#{brand}"%"
        </if>
        <if test="guidePrice != null and guidePrice != ''">
            and guide_price > #{guidePrice}
        </if>
        <if test="carType != null and carType != ''">
            and car_type = #{carType}
        </if>
    </select>
```



```java
    @Test
    public void testSelectByMultiCondition(){
        SqlSession sqlSession = SqlSessionUtil.openSession();
        CarMapper mapper = sqlSession.getMapper(CarMapper.class);

        // 假设三个条件都不是空
        //List<Car> cars = mapper.selectByMultiCondition("比亚迪", 2.0, "新能源");

        // 假设三个条件都是空
        //List<Car> cars = mapper.selectByMultiCondition("", null, "");

        // 假设后两个条件不为空，第一个条件为空
        //List<Car> cars = mapper.selectByMultiCondition("", 2.0, "新能源");

        // 假设第一个条件不是空，后两个条件是空
        List<Car> cars = mapper.selectByMultiCondition("比亚迪", null, "");

        cars.forEach(car -> System.out.println(car));
        sqlSession.close();
    }
```



## 🌊 where标签


+ where标签的作用：让where子句更加动态智能。
+ 所有条件都为空时，where标签保证不会生成where子句。
+ 自动去除某些条件前面多余的and或or。



```java
    /**
     * 使用where标签，让where子句更加的智能。
     * @param brand
     * @param guidePrice
     * @param carType
     * @return
     */
    List<Car> selectByMultiConditionWithWhere(@Param("brand") String brand, @Param("guidePrice") Double guidePrice, @Param("carType") String carType);
```



```xml
    <select id="selectByMultiConditionWithWhere" resultType="Car">
        select * from t_car
        <!--where标签是专门负责where子句动态生成的。-->
        <where>
            <if test="brand != null and brand != ''">
                and brand like "%"#{brand}"%"
            </if>
            <if test="guidePrice != null and guidePrice != ''">
                and guide_price > #{guidePrice}
            </if>
            <if test="carType != null and carType != ''">
                and car_type = #{carType}
            </if>
        </where>
    </select>
```



```java
    @Test
    public void testSelectByMultiConditionWithWhere(){
        SqlSession sqlSession = SqlSessionUtil.openSession();
        CarMapper mapper = sqlSession.getMapper(CarMapper.class);
        // 三个条件都不是空
        //List<Car> cars = mapper.selectByMultiConditionWithWhere("比亚迪", 2.0, "新能源");
        // 三个条件都是空
        //List<Car> cars = mapper.selectByMultiConditionWithWhere("", null, "");
        // 如果第一个条件是空
        //List<Car> cars = mapper.selectByMultiConditionWithWhere("", 2.0, "新能源");
        // 后面两个条件是空
        List<Car> cars = mapper.selectByMultiConditionWithWhere("比亚迪", null, "");
        cars.forEach(car -> System.out.println(car));
        sqlSession.close();
    }
```



## 🌊 trim标签


```xml
    <select id="selectByMultiConditionWithTrim" resultType="Car">
        select * from t_car
        <!--
            prefix：加前缀
            suffix：加后缀
            prefixOverrides：删除前缀
            suffixOverrides：删除后缀
        -->
        <!--prefix="where" 是在trim标签所有内容的前面添加 where-->
        <!--suffixOverrides="and|or" 把trim标签中内容的后缀and或or去掉-->
        <trim prefix="where" suffixOverrides="and|or">
            <if test="brand != null and brand != ''">
                brand like "%"#{brand}"%" or
            </if>
            <if test="guidePrice != null and guidePrice != ''">
                guide_price > #{guidePrice} and
            </if>
            <if test="carType != null and carType != ''">
                car_type = #{carType}
            </if>
        </trim>

    </select>
```



## 🌊 set标签


+ 主要使用在update语句当中，用来生成set关键字，同时去掉最后多余的“,”
+ 比如我们只更新提交的不为空的字段，如果提交的数据是空或者""，那么这个字段我们将不更新



```xml
    <update id="updateBySet">
        update t_car
        <set>
            <if test="carNum != null and carNum != ''">car_num = #{carNum},</if>
            <if test="brand != null and brand != ''">brand = #{brand},</if>
            <if test="guidePrice != null and guidePrice != ''">guide_price = #{guidePrice},</if>
            <if test="produceTime != null and produceTime != ''">produce_time = #{produceTime},</if>
            <if test="carType != null and carType != ''">car_type = #{carType},</if>
        </set>
        where
            id = #{id}
    </update>
```



## 🌊 choose when otherwise


这三个标签是必须在一起使用的：



```xml
<choose>
  <when></when>
  <when></when>
  <when></when>
  <otherwise></otherwise>
</choose>
```



等同于：



```java
if(){
    
}else if(){
    
}else if(){
    
}else if(){
    
}else{

}
```



只有一个分支会被选择！！！！



```xml
    <select id="selectByChoose" resultType="Car">
        select * from t_car
        <where>
            <choose>
                <when test="brand != null and brand != ''">
                    brand like "%"#{brand}"%"
                </when>
                <when test="guidePrice != null and guidePrice != ''">
                    guide_price > #{guidePrice}
                </when>
                <otherwise>
                    car_type = #{carType}
                </otherwise>
            </choose>
        </where>
    </select>
```



## 🌊 foreach标签


循环数组或集合，动态生成sql，比如这样的SQL：



```sql
delete from t_car where id in(1,2,3);
delete from t_car where id = 1 or id = 2 or id = 3;
```



```sql
insert into t_car values
  (null,'1001','凯美瑞',35.0,'2010-10-11','燃油车'),
  (null,'1002','比亚迪唐',31.0,'2020-11-11','新能源'),
  (null,'1003','比亚迪宋',32.0,'2020-10-11','新能源')
```



```java
    /**
     * 批量删除。foreach标签
     * @param ids
     * @return
     */
    int deleteByIds(@Param("ids") Long[] ids);
```



```xml
    <!--
        foreach标签的属性：
            collection：指定数组或者集合
            item：代表数组或集合中的元素
            separator：循环之间的分隔符
            open: foreach循环拼接的所有sql语句的最前面以什么开始。
            close: foreach循环拼接的所有sql语句的最后面以什么结束。

        collection="ids" 第一次写这个的时候报错了，错误信息是：[array, arg0]
        什么意思？
            map.put("array", 数组);
            map.put("arg0", 数组);
    -->
    <delete id="deleteByIds">
        <!--
        delete from t_car where id in(
        <foreach collection="ids" item="aaaaaaa" separator=",">
            #{aaaaaaa}
        </foreach>
        )
        -->
        delete from t_car where id in
        <foreach collection="ids" item="id" separator="," open="(" close=")">
            #{id}
        </foreach>
    </delete>
```



```java
    /**
     * 批量插入，一次插入多条Car信息
     * @param cars
     * @return
     */
    int insertBatch(@Param("cars") List<Car> cars);
```



```xml
    <insert id="insertBatch">
        insert into t_car values
        <foreach collection="cars" item="car" separator=",">
            (null,#{car.carNum},#{car.brand},#{car.guidePrice},#{car.produceTime},#{car.carType})
        </foreach>
    </insert>
```



```java
    /**
     * 根据id批量删除 使用or关键字。
     * @param ids
     * @return
     */
    int deleteByIds2(@Param("ids") Long[] ids);
```



```xml
    <delete id="deleteByIds2">
        delete from t_car where
        <foreach collection="ids" item="id" separator="or">
            id=#{id}
        </foreach>
    </delete>
```



## 🌊 sql标签与include标签


+ sql标签用来声明sql片段
+ include标签用来将声明的sql片段包含到某个sql语句当中
+ 作用：代码复用。易维护。



```xml
<!-- 声明sql片段 -->
<sql id="carCols">
	id,
	car_num carNum,
	brand,
	guide_price guidePrice,
	produce_time produceTime,
	car_type carType
</sql>

<select id="selectAllRetMap" resultType="map">
  <!-- 包含使用声明的sql片段 -->
  select <include refid="carCols"/> from t_car
</select>

<select id="selectAllRetListMap" resultType="map">
  select <include refid="carCols"/> carType from t_car
</select>

<select id="selectByIdRetMap" resultType="map">
  select <include refid="carCols"/> from t_car where id = #{id}
</select>
```



# 🥽 MyBatis的高级映射及延迟加载


![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851539852-bc6b54d6-ed97-40fa-89ab-0058d984289c.png)  
![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851539965-eea00b86-f6bc-4cc6-893b-60de4ac7a882.png)



## 🌊 多对一


多对一的映射实体类设计：



![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851539968-af4d6525-54a6-4ab1-b8fb-aca12b0a1358.png)



```java
/**
 * 学生信息
 */
public class Student { // Student是多的一方
    private Integer sid;
    private String sname;
    private Clazz clazz; // Clazz是一的一方。
    ......
}
```



```java
/**
 * 班级信息
 */
public class Clazz {
    private Integer cid;
    private String cname;
	......
}
```



+ 多对一映射的多种方式，常见的包括三种： 
    - 第一种方式：一条SQL语句，级联属性映射。
    - 第二种方式：一条SQL语句，association。
    - 第三种方式：两条SQL语句，分步查询。（这种方式常用：优点一是可复用。优点二是支持懒加载。）



### 💦 第一种方式：级联属性映射


```java
    /**
     * 根据id获取学生信息。同时获取学生关联的班级信息。
     * @param id 学生的id
     * @return 学生对象，但是学生对象当中含有班级对象。
     */
    Student selectById(Integer id);
```



```xml
    <!--多对一映射的第一种方式：一条SQL语句，级联属性映射。-->
    <resultMap id="studentResultMap" type="Student">
        <id property="sid" column="sid"/>
        <result property="sname" column="sname"/>
        <!-- clazz为学生对象中的班级属性 班级为一个对象 -->
        <result property="clazz.cid" column="cid"/>
        <result property="clazz.cname" column="cname"/>
    </resultMap>

    <!-- 查询结果会按配置的结果集进行赋值 -->
    <!-- 哪个表在前哪个表为主表，多对一，多为主表 -->
    <select id="selectById" resultMap="studentResultMap">
        select
            s.sid,s.sname,c.cid,c.cname
        from
            t_stu s left join t_clazz c on s.cid = c.cid
        where
            s.sid = #{sid}
    </select>
```



### 💦 第二种方式：association


```java
    /**
     * 一条SQL语句，association
     * @param id
     * @return
     */
    Student selectByIdAssociation(Integer id);
```



```xml
    <!--一条SQL语句，association。-->
    <resultMap id="studentResultMapAssociation" type="Student">
        <id property="sid" column="sid"/>
        <result property="sname" column="sname"/>
        <!--
            association：翻译为关联。一个Student对象关联一个Clazz对象
                property：提供要映射的POJO类的属性名。
                javaType：用来指定要映射的java类型。
        -->
        <association property="clazz" javaType="Clazz">
            <id property="cid" column="cid"/>
            <result property="cname" column="cname"/>
        </association>
    </resultMap>

    <select id="selectByIdAssociation" resultMap="studentResultMapAssociation">
        select
            s.sid,s.sname,c.cid,c.cname
        from
            t_stu s left join t_clazz c on s.cid = c.cid
        where
            s.sid = #{sid}
    </select>
```



### 💦 第三种方式：分步查询 & 多对一延迟加载


+ 分步优点： 
    - 第一个优点：代码复用性增强。
    - 第二个优点：支持延迟加载。【暂时访问不到的数据可以先不查询。提高程序的执行效率。】



```java
    /**
     * 分部查询第一步：先根据学生的sid查询学生的信息。
     * @param sid
     * @return
     */
    Student selectByIdStep1(Integer sid);
```



```xml
    <!--
        分步查询的优点：
            第一：复用性增强。可以重复利用。（大步拆成N多个小碎步。每一个小碎步更加可以重复利用。）
            第二：采用这种分步查询，可以充分利用他们的延迟加载/懒加载机制。
        什么是延迟加载（懒加载），有什么用？
            延迟加载的核心原理是：用的时候再执行查询语句。不用的时候不查询。
            作用：提高性能。尽可能的不查，或者说尽可能的少查。来提高效率。
        在mybatis当中怎么开启延迟加载呢？
            association标签中添加fetchType="lazy"
            注意：默认情况下是没有开启延迟加载的。需要设置：fetchType="lazy"
            这种在association标签中配置fetchType="lazy"，是局部的设置，只对当前的association关联的sql语句起作用。

        在实际的开发中，大部分都是需要使用延迟加载的，所以建议开启全部的延迟加载机制：
            在mybatis核心配置文件中添加全局配置：lazyLoadingEnabled=true

        实际开发中的模式：
            把全局的延迟加载打开。
            如果某一步不需要使用延迟加载，请设置：fetchType="eager"
    -->
    <!--两条SQL语句，完成多对一的分步查询。-->
    <!--这里是第一步：根据学生的id查询学生的所有信息。这些信息当中含有班级id（cid）-->
    <resultMap id="studentResultMapByStep" type="Student">
        <id property="sid" column="sid"/>
        <result property="sname" column="sname"/>
        <association property="clazz"
                     select="com.powernode.mybatis.mapper.ClazzMapper.selectByIdStep2"
                     column="cid"
                     fetchType="eager"/>
    </resultMap>

    <select id="selectByIdStep1" resultMap="studentResultMapByStep">
        select sid,sname,cid from t_stu where sid = #{sid}
    </select>
```



```java
    /**
     * 分步查询第二步：根据cid获取班级信息。
     * @param cid
     * @return
     */
    Clazz selectByIdStep2(Integer cid);
```



```xml
    <!--分步查询第二步：根据cid获取班级信息。-->
    <select id="selectByIdStep2" resultType="Clazz">
        select cid,cname from t_clazz where cid = #{cid}
    </select>
```



全局开启延迟加载：



```xml
    <settings>
        <!--延迟加载的全局开关。默认值false不开启。-->
        <!--什么意思：所有只要但凡带有分步的，都采用延迟加载。-->
        <setting name="lazyLoadingEnabled" value="true"/>
    </settings>
```



## 🌊 一对多


多对一的映射实体类设计：  
一对多的实现，通常是在一的一方中有List集合属性。



![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851540743-d938123f-829f-4970-954f-ce645b90c38c.png)



在Clazz类中添加`List<Student> stus;`属性。



```java
/**
 * 班级信息
 */
public class Clazz {
    private Integer cid;
    private String cname;
    private List<Student> stus;
	......
}
```



```java
/**
 * 学生信息
 */
public class Student { // Student是多的一方
    private Integer sid;
    private String sname;
    private Clazz clazz; // Clazz是一的一方。
    ......
}
```



+ 一对多的实现通常包括两种实现方式： 
    - 第一种方式：collection
    - 第二种方式：分步查询



### 💦 第一种方式：collection


```java
    /**
     * 根据班级编号查询班级信息。
     * @param cid
     * @return
     */
    Clazz selectByCollection(Integer cid);
```



```xml
    <resultMap id="clazzResultMap" type="Clazz">
        <id property="cid" column="cid"/>
        <result property="cname" column="cname"/>
        <!--一对多，这里是collection。collection是集合的意思。-->
        <!--ofType 属性用来指定集合当中的元素类型。-->
        <collection property="stus" ofType="Student">
            <id property="sid" column="sid"/>
            <result property="sname" column="sname"/>
        </collection>
    </resultMap>

    <select id="selectByCollection" resultMap="clazzResultMap">
        select c.cid,c.cname,s.sid,s.sname from t_clazz c left join t_stu s on c.cid = s.cid where c.cid = #{cid}
    </select>
```



### 💦 第二种方式：分步查询 & 一对多延迟加载


```java
    /**
     * 分步查询。第一步：根据班级编号获取班级信息。
     * @param cid 班级编号
     * @return
     */
    Clazz selectByStep1(Integer cid);
```



```xml
    <!--分步查询第一步：根据班级的cid获取班级信息。-->
    <resultMap id="clazzResultMapStep" type="Clazz">
        <id property="cid" column="cid"/>
        <result property="cname" column="cname"/>
        <collection property="stus"
                    select="com.powernode.mybatis.mapper.StudentMapper.selectByCidStep2"
                    column="cid" fetchType="eager" />
    </resultMap>

    <select id="selectByStep1" resultMap="clazzResultMapStep">
        select cid,cname from t_clazz where cid = #{cid}
    </select>
```



```java
    /**
     * 根据班级编号查询学生信息。
     * @param cid
     * @return
     */
    List<Student> selectByCidStep2(Integer cid);
```



```xml
    <select id="selectByCidStep2" resultType="Student">
        select * from t_stu where cid = #{cid}
    </select>
```



+ 一对多延迟加载机制和多对一是一样的。同样是通过两种方式： 
    - 第一种：fetchType="lazy"
    - 第二种：修改全局的配置setting，lazyLoadingEnabled=true，如果开启全局延迟加载，想让某个sql不使用延迟加载：fetchType="eager"



# 🥽 MyBatis的缓存


![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851540348-94997b33-30f8-4712-9ff4-2ae2863a6652.png)



+ 缓存：cache
+ 缓存的作用：通过减少IO的方式，来提高程序的执行效率。
+ mybatis的缓存：将select语句的查询结果放到缓存（内存）当中，下一次还是这条select语句的话，直接从缓存中取，不再查数据库。一方面是减少了IO。另一方面不再执行繁琐的查找算法。效率大大提升。
+ mybatis缓存包括： 
    - 一级缓存：将查询到的数据存储到SqlSession中。
    - 二级缓存：将查询到的数据存储到SqlSessionFactory中。
    - 或者集成其它第三方的缓存：比如EhCache【Java语言开发的】、Memcache【C语言开发的】等。
+ 缓存只针对于DQL语句，也就是说缓存机制只对应select语句。



## 🌊 一级缓存


+ 一级缓存默认是开启的。不需要做任何配置。
+ 原理：只要使用同一个SqlSession对象执行同一条SQL语句，就会走缓存。
+ 什么情况下不走缓存？ 
    - 第一种：不同的SqlSession对象。
    - 第二种：查询条件变化了。
+ 一级缓存失效情况包括两种： 
    - 第一种：第一次查询和第二次查询之间，手动清空了一级缓存。`sqlSession.clearCache();`
    - 第二种：第一次查询和第二次查询之间，执行了增删改操作。【这个增删改和哪张表没有关系，只要有insert delete update操作，一级缓存就失效。】



## 🌊 二级缓存


+ 二级缓存的范围是SqlSessionFactory。
+ 使用二级缓存需要具备以下几个条件： 
    1. `<setting name="cacheEnabled" value="true">` 全局性地开启或关闭所有映射器配置文件中已配置的任何缓存。默认就是true，无需设置。
    2. 在需要使用二级缓存的SqlMapper.xml文件中添加配置：`<cache />`

```xml
<!--
    默认情况下，二级缓存机制是开启的。
    只需要在对应的SqlMapper.xml文件中添加以下标签。用来表示“我”使用该二级缓存。
-->
<cache/>
```

 

    3. 使用二级缓存的实体类对象必须是可序列化的，也就是必须实现java.io.Serializable接口
    4. SqlSession对象关闭或提交之后，一级缓存中的数据才会被写入到二级缓存当中。此时二级缓存才可用。



```java
public class Car implements Serializable {}
```



```java
    @Test
    public void testSelectById2() throws Exception{
        // 这里只有一个SqlSessionFactory对象。二级缓存对应的就是SqlSessionFactory。
        SqlSessionFactory sqlSessionFactory = new SqlSessionFactoryBuilder().build(Resources.getResourceAsStream("mybatis-config.xml"));
        SqlSession sqlSession1 = sqlSessionFactory.openSession();
        SqlSession sqlSession2 = sqlSessionFactory.openSession();
        CarMapper mapper1 = sqlSession1.getMapper(CarMapper.class);
        CarMapper mapper2 = sqlSession2.getMapper(CarMapper.class);

        // 这行代码执行结束之后，实际上数据是缓存到一级缓存当中了。（sqlSession1是一级缓存。）
        Car car1 = mapper1.selectById2(164L);
        System.out.println(car1);

        // 如果这里不关闭SqlSession1对象的话，二级缓存中还是没有数据的。

        // 如果执行了这行代码，sqlSession1的一级缓存中的数据会放到二级缓存当中。
        sqlSession1.close();

        // 这行代码执行结束之后，实际上数据会缓存到一级缓存当中。（sqlSession2是一级缓存。）
        Car car2 = mapper2.selectById2(164L);
        System.out.println(car2);

        // 程序执行到这里的时候，会将sqlSession1这个一级缓存中的数据写入到二级缓存当中。
        //sqlSession1.close();
        // 程序执行到这里的时候，会将sqlSession2这个一级缓存中的数据写入到二级缓存当中。
        sqlSession2.close();
    }
```



+ 二级缓存的失效：只要两次查询之间出现了增删改操作。二级缓存就会失效。【一级缓存也会失效】
+ 二级缓存的相关配置：  
![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851540642-cd602867-36ed-448d-8ffb-efb2dce682d8.png) 
    1. eviction：指定从缓存中移除某个对象的淘汰算法。默认采用LRU策略。 
        * LRU：Least Recently Used。最近最少使用。优先淘汰在间隔时间内使用频率最低的对象。(其实还有一种淘汰算法LFU，最不常用。)
        * FIFO：First In First Out。一种先进先出的数据缓存器。先进入二级缓存的对象最先被淘汰。
        * SOFT：软引用。淘汰软引用指向的对象。具体算法和JVM的垃圾回收算法有关。
        * WEAK：弱引用。淘汰弱引用指向的对象。具体算法和JVM的垃圾回收算法有关。
    2. flushInterval： 
        * 二级缓存的刷新时间间隔。单位毫秒。如果没有设置。就代表不刷新缓存，只要内存足够大，一直会向二级缓存中缓存数据。除非执行了增删改。
    3. readOnly： 
        * true：多条相同的sql语句执行之后返回的对象是共享的同一个。性能好。但是多线程并发可能会存在安全问题。
        * false：多条相同的sql语句执行之后返回的对象是副本，调用了clone方法。性能一般。但安全。
    4. size： 
        * 设置二级缓存中最多可存储的java对象数量。默认值1024。



## 🌊 MyBatis集成EhCache


[【https://www.yuque.com/zuihoudewu/java_note/mt2812#IB2eW】](https://www.yuque.com/zuihoudewu/java_note/mt2812#IB2eW)



+ 集成EhCache是为了代替mybatis自带的二级缓存。一级缓存是无法替代的。
+ mybatis对外提供了接口，也可以集成第三方的缓存组件。比如EhCache、Memcache等。都可以。
+ EhCache是Java写的。Memcache是C语言写的。所以mybatis集成EhCache较为常见，按照以下步骤操作，就可以完成集成：



第一步：引入mybatis整合ehcache的依赖。



```xml
<!--mybatis集成ehcache的组件-->
<dependency>
  <groupId>org.mybatis.caches</groupId>
  <artifactId>mybatis-ehcache</artifactId>
  <version>1.2.2</version>
</dependency>
```



第二步：在类的根路径下新建echcache.xml文件，并提供以下配置信息。



```xml
<?xml version="1.0" encoding="UTF-8"?>
<ehcache xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:noNamespaceSchemaLocation="http://ehcache.org/ehcache.xsd"
         updateCheck="false">
    <!--磁盘存储:将缓存中暂时不使用的对象,转移到硬盘,类似于Windows系统的虚拟内存-->
    <diskStore path="e:/ehcache"/>
  
    <!--defaultCache：默认的管理策略-->
    <!--eternal：设定缓存的elements是否永远不过期。如果为true，则缓存的数据始终有效，如果为false那么还要根据timeToIdleSeconds，timeToLiveSeconds判断-->
    <!--maxElementsInMemory：在内存中缓存的element的最大数目-->
    <!--overflowToDisk：如果内存中数据超过内存限制，是否要缓存到磁盘上-->
    <!--diskPersistent：是否在磁盘上持久化。指重启jvm后，数据是否有效。默认为false-->
    <!--timeToIdleSeconds：对象空闲时间(单位：秒)，指对象在多长时间没有被访问就会失效。只对eternal为false的有效。默认值0，表示一直可以访问-->
    <!--timeToLiveSeconds：对象存活时间(单位：秒)，指对象从创建到失效所需要的时间。只对eternal为false的有效。默认值0，表示一直可以访问-->
    <!--memoryStoreEvictionPolicy：缓存的3 种清空策略-->
    <!--FIFO：first in first out (先进先出)-->
    <!--LFU：Less Frequently Used (最少使用).意思是一直以来最少被使用的。缓存的元素有一个hit 属性，hit 值最小的将会被清出缓存-->
    <!--LRU：Least Recently Used(最近最少使用). (ehcache 默认值).缓存的元素有一个时间戳，当缓存容量满了，而又需要腾出地方来缓存新的元素的时候，那么现有缓存元素中时间戳离当前时间最远的元素将被清出缓存-->
    <defaultCache eternal="false" maxElementsInMemory="1000" overflowToDisk="false" diskPersistent="false"
                  timeToIdleSeconds="0" timeToLiveSeconds="600" memoryStoreEvictionPolicy="LRU"/>

</ehcache>
```



第三步：修改SqlMapper.xml文件中的标签，添加type属性。



```xml
<cache type="org.mybatis.caches.ehcache.EhcacheCache"/>
```



第四步：编写测试程序使用。



```java
@Test
public void testSelectById2() throws Exception{
    SqlSessionFactory sqlSessionFactory = new SqlSessionFactoryBuilder().build(Resources.getResourceAsStream("mybatis-config.xml"));
    
    SqlSession sqlSession1 = sqlSessionFactory.openSession();
    CarMapper mapper1 = sqlSession1.getMapper(CarMapper.class);
    Car car1 = mapper1.selectById(83L);
    System.out.println(car1);
    
    sqlSession1.close();
    
    SqlSession sqlSession2 = sqlSessionFactory.openSession();
    CarMapper mapper2 = sqlSession2.getMapper(CarMapper.class);
    Car car2 = mapper2.selectById(83L);
    System.out.println(car2);
}
```



# 🥽 MyBatis的逆向工程


+ 所谓的逆向工程是：根据数据库表逆向生成Java的pojo类，SqlMapper.xml文件，以及Mapper接口类等。
+ 要完成这个工作，需要借助别人写好的逆向工程插件。
+ 思考：使用这个插件的话，需要给这个插件配置哪些信息？ 
    - pojo类名、包名以及生成位置。
    - SqlMapper.xml文件名以及生成位置。
    - Mapper接口名以及生成位置。
    - 连接数据库的信息。
    - 指定哪些表参与逆向工程。
    - ......



## 🌊 逆向工程的使用(基础版)


第一步：基础环境准备  
新建模块：mybatis-011-generator  
打包方式：jar



第二步：在pom中添加逆向工程插件（project标签下）



```xml
<!--定制构建过程-->
<build>
  <!--可配置多个插件-->
  <plugins>
    <!--其中的一个插件：mybatis逆向工程插件-->
    <plugin>
      <!--插件的GAV坐标-->
      <groupId>org.mybatis.generator</groupId>
      <artifactId>mybatis-generator-maven-plugin</artifactId>
      <version>1.4.1</version>
      <!--允许覆盖-->
      <configuration>
        <overwrite>true</overwrite>
      </configuration>
      <!--插件的依赖-->
      <dependencies>
        <!--mysql驱动依赖-->
        <dependency>
          <groupId>mysql</groupId>
          <artifactId>mysql-connector-java</artifactId>
          <version>8.0.30</version>
        </dependency>
      </dependencies>
    </plugin>
  </plugins>
</build>
```



第三步：配置generatorConfig.xml  
该文件名必须叫做：generatorConfig.xml  
该文件必须放在类的根路径下。



```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE generatorConfiguration
        PUBLIC "-//mybatis.org//DTD MyBatis Generator Configuration 1.0//EN"
        "http://mybatis.org/dtd/mybatis-generator-config_1_0.dtd">

<generatorConfiguration>
    <!--
        targetRuntime有两个值：
            MyBatis3Simple：生成的是基础版，只有基本的增删改查。
            MyBatis3：生成的是增强版，除了基本的增删改查之外还有复杂的增删改查。
    -->
    <context id="DB2Tables" targetRuntime="MyBatis3Simple">
        <!--防止生成重复代码-->
        <plugin type="org.mybatis.generator.plugins.UnmergeableXmlMappersPlugin"/>
        <!-- 注释信息的生成 -->
        <commentGenerator>
            <!--是否去掉生成日期-->
            <property name="suppressDate" value="true"/>
            <!--是否去除注释-->
            <property name="suppressAllComments" value="true"/>
        </commentGenerator>

        <!--连接数据库信息-->
        <jdbcConnection driverClass="com.mysql.cj.jdbc.Driver"
                        connectionURL="jdbc:mysql://localhost:3306/powernode"
                        userId="root"
                        password="root">
        </jdbcConnection>

        <!-- 生成pojo包名和位置 -->
        <javaModelGenerator targetPackage="com.powernode.mybatis.pojo" targetProject="src/main/java">
            <!--是否开启子包-->
            <property name="enableSubPackages" value="true"/>
            <!--是否去除字段名的前后空白-->
            <property name="trimStrings" value="true"/>
        </javaModelGenerator>

        <!-- 生成SQL映射文件的包名和位置 -->
        <sqlMapGenerator targetPackage="com.powernode.mybatis.mapper" targetProject="src/main/resources">
            <!--是否开启子包-->
            <property name="enableSubPackages" value="true"/>
        </sqlMapGenerator>

        <!-- 生成Mapper接口的包名和位置 -->
        <javaClientGenerator
                type="xmlMapper"
                targetPackage="com.powernode.mybatis.mapper"
                targetProject="src/main/java">
            <property name="enableSubPackages" value="true"/>
        </javaClientGenerator>

        <!-- 表名和对应的实体类名-->
        <table tableName="t_car" domainObjectName="Car"/>

    </context>
</generatorConfiguration>
```



第四步：运行插件



![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851541039-38274df6-5faf-4875-8bf8-792c10b7c490.png)



## 🌊 逆向工程的使用(增强版)


generatorConfig.xml配置文件中targetRuntime的值选择MyBatis3，生成的是增强版，除了基本的增删改查之外还有复杂的增删改查。



```xml
    <!--
        targetRuntime有两个值：
            MyBatis3Simple：生成的是基础版，只有基本的增删改查。
            MyBatis3：生成的是增强版，除了基本的增删改查之外还有复杂的增删改查。
    -->
    <context id="DB2Tables" targetRuntime="MyBatis3">
```



生成的XxxxExample类负责封装查询条件



```java
public class CarMapperTest {

    // CarExample类负责封装查询条件的。
    @Test
    public void testSelect(){
        SqlSession sqlSession = SqlSessionUtil.openSession();
        CarMapper mapper = sqlSession.getMapper(CarMapper.class);
        // 执行查询
        // 1. 查询一个
        Car car = mapper.selectByPrimaryKey(165L);
        System.out.println(car);
        // 2. 查询所有（selectByExample，根据条件查询，如果条件是null表示没有条件。）
        List<Car> cars = mapper.selectByExample(null);
        cars.forEach(car1 -> System.out.println(car1));
        System.out.println("=========================================");
        // 3. 按照条件进行查询
        // QBC 风格：Query By Criteria 一种查询方式，比较面向对象，看不到sql语句。
        // 封装条件，通过CarExample对象来封装查询条件
        CarExample carExample = new CarExample();
        // 调用carExample.createCriteria()方法来创建查询条件
        // 继续向后调用方法追加查询条件
        carExample.createCriteria()
                   .andBrandLike("帕萨特")
                   .andGuidePriceGreaterThan(new BigDecimal(20.0));
        // 添加or
        // 上面添加的为and条件，or()开始添加or条件
        // (... and ... 前面的查询条件) or (...) 生成后的查询条件
        carExample.or().andCarTypeEqualTo("燃油车");
        // 执行查询
        List<Car> cars2 = mapper.selectByExample(carExample);
        cars2.forEach(car2 -> System.out.println(car2));

        sqlSession.close();

    }

}
```



# 🥽 MyBatis使用PageHelper


## 🌊 limit分页


+ mysql的limit后面两个数字： 
    - 第一个数字：startIndex（起始下标。下标从0开始。）
    - 第二个数字：pageSize（每页显示的记录条数）
+ 假设已知页码pageNum，还有每页显示的记录条数pageSize，第一个数字可以动态的获取吗？ 
    - startIndex = (pageNum - 1) * pageSize



![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851540574-1414b95a-cffe-463e-8b96-f032a482242a.png)



所以，标准通用的mysql分页SQL：



```sql
select 
  * 
from 
  tableName ...... 
limit 
  (pageNum - 1) * pageSize, pageSize
```



使用mybatis应该怎么做？



```java
    /**
     * 分页查询
     * @param startIndex 起始下标。
     * @param pageSize 每页显示的记录条数
     * @return
     */
    List<Car> selectByPage(@Param("startIndex") int startIndex, @Param("pageSize") int pageSize);
```



```xml
    <select id="selectByPage" resultType="Car">
        select * from t_car limit #{startIndex},#{pageSize}
    </select>
```



```java
    @Test
    public void testSelectByPage(){
        // 获取每页显示的记录条数
        int pageSize = 3;
        // 显示第几页：页码
        int pageNum = 3;
        // 计算开始下标
        int startIndex = (pageNum - 1) * pageSize;

        SqlSession sqlSession = SqlSessionUtil.openSession();
        CarMapper mapper = sqlSession.getMapper(CarMapper.class);
        List<Car> cars = mapper.selectByPage(startIndex, pageSize);
        cars.forEach(car -> System.out.println(car));
        sqlSession.close();
    }
```



## 🌊 PageHelper插件


获取数据不难，难的是获取分页相关的数据比较难(是否还有下一页等)。可以借助mybatis的PageHelper插件。



使用PageHelper插件进行分页，更加的便捷。



第一步：引入依赖



```xml
<dependency>
  <groupId>com.github.pagehelper</groupId>
  <artifactId>pagehelper</artifactId>
  <version>5.3.1</version>
</dependency>
```



第二步：在mybatis-config.xml文件中配置插件  
typeAliases标签下面进行配置：



```xml
<plugins>
  <plugin interceptor="com.github.pagehelper.PageInterceptor"></plugin>
</plugins>
```



第三步：编写Java代码



```java
    /**
     * 查询所有的Car，通过分页查询插件PageHelper完成。
     * @return
     */
    List<Car> selectAll();
```



```xml
    <select id="selectAll" resultType="Car">
        select * from t_car
    </select>
```



```java
    @Test
    public void testSelectAll(){
        SqlSession sqlSession = SqlSessionUtil.openSession();
        CarMapper mapper = sqlSession.getMapper(CarMapper.class);

        // 一定一定一定要注意：在执行DQL语句之前。开启分页功能。
        int pageNum = 2;
        int pageSize = 3;
        PageHelper.startPage(pageNum, pageSize);

        List<Car> cars = mapper.selectAll();
        //cars.forEach(car -> System.out.println(car));

		// 查询完之后创建PageInfo对象获取分页的相关信息
        // 封装分页信息对象new PageInfo()
        // PageInfo对象是PageHelper插件提供的，用来封装分页相关的信息的对象。
        // 第一个参数为查询出来的数据，第二个参数为导航的页数(导航有几页)
        // navigatePages=3, navigateFirstPage=1, navigateLastPage=3, navigatepageNums=[1, 2, 3]
        PageInfo<Car> carPageInfo = new PageInfo<>(cars, 3);

        System.out.println(carPageInfo);

        sqlSession.close();

        /*
        PageInfo{pageNum=2, pageSize=3, size=3, startRow=4, endRow=6, total=7, pages=3,
        list=Page{count=true, pageNum=2, pageSize=3, startRow=3, endRow=6, total=7, pages=3, reasonable=false, pageSizeZero=false}
        [Car{id=168, carNum='1204', brand='奥迪Q7', guidePrice=3.0, produceTime='2009-10-11', carType='燃油车'},
        Car{id=169, carNum='1205', brand='朗逸', guidePrice=4.0, produceTime='2001-10-11', carType='新能源'},
        Car{id=170, carNum='1206', brand='奔驰E300L', guidePrice=50.0, produceTime='2003-02-03', carType='新能源'}],
        prePage=1, nextPage=3, isFirstPage=false, isLastPage=false, hasPreviousPage=true, hasNextPage=true,
        navigatePages=3, navigateFirstPage=1, navigateLastPage=3, navigatepageNums=[1, 2, 3]}
         */
    }
```



# 🥽 MyBatis的注解式开发


+ mybatis中也提供了注解式开发方式，采用注解可以减少Sql映射文件的配置。
+ 当然，使用注解式开发的话，sql语句是写在java程序中的，这种方式也会给sql语句的维护带来成本。
+ 官方是这么说的： 
    - 使用注解来映射简单语句会使代码显得更加简洁，但对于稍微复杂一点的语句，Java 注解不仅力不从心，还会让你本就复杂的 SQL 语句更加混乱不堪。 因此，如果你需要做一些很复杂的操作，最好用 XML 来映射语句。
+ 使用注解编写复杂的SQL是这样的：  
![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762851540915-815f9752-44bc-4827-831c-22cb19b6c3f0.png)
+ 原则：简单sql可以注解。复杂sql使用xml。



## 🌊 [@Insert ](/Insert ) 


```java
@Insert("insert into t_car values(null,#{carNum},#{brand},#{guidePrice},#{produceTime},#{carType})")
int insert(Car car);
```



## 🌊 [@Delete ](/Delete ) 


```java
@Delete("delete from t_car where id = #{id}")
int deleteById(Long id);
```



## 🌊 [@Update ](/Update ) 


```java
@Update("update t_car set car_num=#{carNum},brand=#{brand},guide_price=#{guidePrice},produce_time=#{produceTime},car_type=#{carType} where id=#{id}")
int update(Car car);
```



## 🌊 [@Select ](/Select ) 


```java
@Select("select * from t_car where id = #{id}")
Car selectById(Long id);
```



## 🌊 [@Results ](/Results ) 


```java
@Select("select * from t_car where id = #{id}")
// 定义属性名与字段名的对应关系
@Results({
        @Result(property = "id", column = "id"),
        @Result(property = "carNum", column = "car_num"),
        @Result(property = "brand", column = "brand"),
        @Result(property = "guidePrice", column = "guide_price"),
        @Result(property = "produceTime", column = "produce_time"),
        @Result(property = "carType", column = "car_type")
})
Car selectById(Long id);
```







# MyBatis 速查笔记
## MyBatis 工具类 SqlSessionUtil 的编写
```java
package cw.mybatis.utils;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

import java.io.IOException;

/**
 * Mybatis工具类
 */
public class SqlSessionUtils {
    // 工具类的构造方法一般为私有，防止实例化对象
    // 工具类中的方法都是静态的，可以直接采用类名进行调用，不需要new对象，方便调用
    private SqlSessionUtils() {}
    
    private static SqlSessionFactory sqlSessionFactory;
    
    // 类加载时执行
    // SqlSessionUtil工具类在进行第一次加载的时候，解析mybatis-config.xml文件。创建SqlSessionFactory对象。
    static {
        SqlSessionFactoryBuilder sqlSessionFactoryBuilder = new SqlSessionFactoryBuilder();
        // SqlSessionFactory对象：一个SqlSessionFactory对应一个environment，一个environment通常是一个数据库。
        try {
            sqlSessionFactory = sqlSessionFactoryBuilder.build(Resources.getResourceAsStream("mybatis-config.xml"));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
    
    /**
     * 获取数据库会话对象
     * @return 数据库会话对象
     */
    public static SqlSession openSession() {
        // SqlSessionFactoryBuilder sqlSessionFactoryBuilder = new SqlSessionFactoryBuilder();
        // SqlSessionFactory对象：一个SqlSessionFactory对应一个environment，一个environment通常是一个数据库。
        // 所以一个数据库只需要一个SqlSessionFactory对象
        // SqlSessionFactory sqlSessionFactory = sqlSessionFactoryBuilder.build(Resources.getResourceAsStream("mybatis-config.xml"));
        SqlSession sqlSession = sqlSessionFactory.openSession();
        return sqlSession;
    }
}
```

## MyBatis 实现 CRUD
+ 在 MyBatis 中，使用 `#{}` 充当占位符

### insert
#### 使用 Map 传参
```java
/**
 * ClassName: Test01
 * Package: cw.mybatis
 * Description:
 *
 * @Author tcw
 * @Create 2023-05-10 19:17
 * @Version 1.0
 */
public class Test01 {
    @Test
    public void test01() {
        // 封装数据
        Map<String, Object> map = new HashMap<>();
        map.put("k1", "1333");
        map.put("k2", "比亚迪汉");
        map.put("k3", 10.0);
        map.put("k4", "2020-11-11");
        map.put("k5", "电车");
        
        SqlSession sqlSession = SqlSessionUtil.openSession();
        // sqlSession.insert(SQL语句的ID, 封装数据的对象)
        sqlSession.insert("insertCar", map);
        sqlSession.commit();
        sqlSession.close();
    }
}
```

+ <font style="color:rgb(77, 77, 77);">注意：</font>
    - <u><font style="color:rgb(77, 77, 77);">占位符中写map集合的key</font></u><font style="color:rgb(77, 77, 77);">，</font><font style="color:rgb(77, 77, 77);background-color:#FBDE28;">如果key不存在，则获取的是null，即向数据库中插入的数据为空</font>
    - <font style="color:rgb(77, 77, 77);">一般map集合的key起名的时候要见名知意。</font>

```xml
<mapper namespace="org.mybatis.example.BlogMapper">
	<select id="insertCar">
 		<!-- 
    insert into t_car 
    values(null, #{map集合的key}, #{map集合的key}, #{map集合的key}, #{map集合的key}, #{map集合的key}); 
    -->
		insert into t_car values(null, #{k1}, #{k2}, #{k3}, #{k4}, #{k5});
	</select>
</mapper>
```

#### <font style="color:rgb(77, 77, 77);">使用 POJO 传参</font>
```java
package cw.mybatis.pojo;

/**
 * ClassName: Car
 * Package: cw.mybatis.pojo
 * Description:
 * 封装汽车信息的 pojo 类
 *
 * @Author tcw
 * @Create 2023-05-10 20:48
 * @Version 1.0
 */
public class Car {
    // 数据库表当中的字段应该和pojo类的属性一一对应。
    // 建议使用包装类，这样可以防止null的问题。
    private Long id;
    private String carNum;
    private String brand;
    private Double guidePrice;
    private String produceTime;
    private String carTye;
    
    public Car(Long id, String carNum, String brand, Double guidePrice, String produceTime, String carTye) {
        this.id = id;
        this.carNum = carNum;
        this.brand = brand;
        this.guidePrice = guidePrice;
        this.produceTime = produceTime;
        this.carTye = carTye;
    }

    ......
    
}
```

```java
@Test
public void test02() {
    // 封装数据
    Car car = new Car(null, "3333", "比亚迪", 30.0, "2020-11-11", "新能源");

    SqlSession sqlSession = SqlSessionUtil.openSession();
    sqlSession.insert("insertCar", car);
    sqlSession.commit();
    sqlSession.close();
}
```

+ 注意：
    - 占位符 `#{}` 中写POJO的属性名
    - 严格意义上来说，使用POJO对象传递值的话，`#{}`<font style="background-color:#FBDE28;"> 这个大括号中写 get 方法的方法名去掉 get，然后将剩下的单词首字母小写，然后放进去</font>。
    - MyBatis 底层<font style="background-color:#FBDE28;">调用了 pojo 对象的 get 方法</font>。 

```xml
<mapper namespace="org.mybatis.example.BlogMapper">
	<select id="insertCar">
		insert into t_car 
    values(#{id}, #{carNum}, #{brand}, #{guidePrice}, #{produceTime}, #{carTye});
	</select>
</mapper>
```

### delete
```java
@Test
public void test03() {
    SqlSession sqlSession = SqlSessionUtil.openSession();
    // 删除数据
    sqlSession.delete("deleteCarById", 19);
    sqlSession.commit();
    sqlSession.close();
}
```

+ 注意：
    - 如果占位符只有一个，那么 `#{}` 的大括号里可以随意写。
    - 最好见名知意。

```xml
<delete id="deleteCarById">
  delete from t_car where id = #{id};
</delete>
```

### update
```java
@Test
public void tset04() {
    // 封装数据
    Car car = new Car(5L, "9999", "凯美瑞123", 30.3, "1999-11-10", "燃油车");

    SqlSession sqlSession = SqlSessionUtil.openSession();
    sqlSession.update("updateCarById", car);
    sqlSession.commit();
    sqlSession.close();
}
```

```xml
<update id="updateCarById">
  update t_car
  set car_num = #{carNum},
      brand = #{brand},
      guide_price = #{guidePrice}, 
      produce_time = #{produceTime}, 
      car_type = #{carTye}
  where id = #{id}
</update>
```

### select
#### 查一个
+ 根据 id (主键) 查询

```xml
<!-- mybatis 底层执行了 select 语句之后，一定会返回一个结果集对象：ResultSet -->
<!-- select 标签中 resultType 属性用来告诉 mybatis 查询结果集封装成什么类型的 java 对象 -->
<!-- resultType 通常写的是：全限定类名 -->
<!-- sql 语句中，如果表的字段名与相应的 java 类的属性名不一致需要使用别名为查询语句的字段指定别名，否则对应字段的查询为 null -->
<select id="selectById" resultType="cw.mybatis.pojo.Car">
  select id,
         car_num as carNum,
         brand,
         guide_price as guidePrice,
         produce_time as produceTime,
         car_type as carTye
  from t_car
  where id = #{id};
</select>
```

```java
@Test
public void test05() {
    SqlSession sqlSession = SqlSessionUtil.openSession();
    // 查询一个数据
    Car car = (Car) sqlSession.selectOne("selectById", 1);
    System.out.println(car);
    sqlSession.close();
}
```

#### 查所有
```xml
<!-- 
  resultType 还是指定要封装的结果集的类型。
  不是指定 List 类型，是指定 List 集合中元素的类型。 
-->
<select id="selectAll" resultType="cw.mybatis.pojo.Car">
  select  id,
          car_num as carNum,
          brand,
          guide_price as guidePrice,
          produce_time as produceTime,
          car_type as carTye
  from t_car
</select>
```

```java
@Test
public void test06() {
    SqlSession sqlSession = SqlSessionUtil.openSession();
    // 查询多个数据
    // selectList 方法：
    // 		mybatis 通过这个方法就可以得知你需要一个 List 集合。
    // 		它会自动给你返回一个 List 集合，集合中元素的数据类型为通过 resultType 指定的类型
    List<Object> cars = sqlSession.selectList("selectAll");
    cars.forEach(car -> System.out.println(car));
    sqlSession.close();
}
```

### SQLMapper 映射文件中的 namespace
+ namespace 命名空间主要是<font style="background-color:#FBDE28;">为了防止 sqlId 冲突</font>
+ 当不同的 SQLMapper 映射文件中，存在 sqlId 相同的两个SQL语句，若使用SQL语句时不使用命名空间，则会报错
+ 命名空间的使用 `namespace.sqlId` （MyBatis中sqlId的完整写法）

## MyBatis 核心配置文件
### 文档类型说明
```xml
<!DOCTYPE configuration
        PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-config.dtd">
```

+ 文档类型说明中的 configuration，是根标签的名称，一个文档只有一个根标签
+ http://mybatis.org/dtd/mybatis-3-config.dtd 是xml文档的dtd约束，约束文档中可以出现什么标签、标签能有什么子标签、标签中可以有什么属性、标签属性可以具有的值以及标签出现的顺序

### 根标签
```xml
<configuration>
  ...
</configuration>
```

+ configuration：根标签，表示配置信息

### properties
+ java.util.Properties类，是一个Map集合，key和value都是String类型
+ property标签中的name属性为key，value属性为value
+ 在properties标签中可以配置很多属性
+ 在properties下面的标签中可以使用property配置的属性值，使用 `${property的name属性}` 取出相应的值

```xml
<properties>
		<!-- <property name="属性名" value="属性值"/> -->
    <property name="jdbc.driver" value="com.mysql.cj.jdbc.Driver"/>
    <property name="jdbc.url" value="jdbc:mysql://localhost:3306/powernode"/>
    <property name="jdbc.username" value="root"/>
    <property name="jdbc.password" value="root"/>
</properties>
```

```xml
<dataSource type="POOLED">
    <property name="driver" value="${jdbc.driver}"/>
    <property name="url" value="${jdbc.url}"/>
    <property name="username" value="${jdbc.username}"/>
    <property name="password" value="${jdbc.password}"/>
</dataSource>
```

#### 从指定路径下开始查找配置文件
+ properties中的property可以配置到配置文件中

```xml
<!-- resource，从类路径下开始查找资源 -->
<properties resource="jdbc.properties" />
```

```xml
<!-- 从绝对路径当中加载资源 -->
<!-- 绝对路径怎么写？file:///路径 -->
<properties url="file:///d:/jdbc.properties" />
```

### environments
```xml
<environments default="powernodeDB">
  ...
</environments>
```

+ 在 environments 标签中配置数据库环境，可以配置多个数据库环境
+ default 表示默认使用的数据库环境
    - 当你使用mybatis创建SqlSessionFactory对象的时候，没有指定数据库环境的话，默认使用 default 属性指定的数据库环境

#### environment
+ environments 的子标签，在 environment 标签中配置每一个数据库环境
+ 一般一个数据库会对应一个SqlSessionFactory对象，一个环境environment会对应一个SqlSessionFactory对象，所以一个数据库一般对应一个环境

```xml
<!-- 第一个数据库环境 -->
<environment id="powernodeDB">
    <transactionManager type="JDBC"/>
    <dataSource type="POOLED">
        <property name="driver" value="${jdbc.driver}"/>
        <property name="url" value="${jdbc.url}"/>
        <property name="username" value="${jdbc.username}"/>
        <property name="password" value="${jdbc.password}"/>
        <property name="poolMaximumActiveConnections" value="10"/>
        <property name="poolTimeToWait" value="2000"/>
        <property name="poolMaximumCheckoutTime" value="10000"/>
        <property name="poolMaximumIdleConnections" value="5"/>
    </dataSource>
</environment>

<!-- 第二个数据库环境 -->
<environment id="mybatisDB">
    <transactionManager type="JDBC"/>
    <dataSource type="POOLED">
        <property name="driver" value="com.mysql.cj.jdbc.Driver"/>
        <property name="url" value="jdbc:mysql://localhost:3306/mybatis"/>
        <property name="username" value="root"/>
        <property name="password" value="root"/>
    </dataSource>
</environment>
```

##### 默认方式获取 SqlSessionFactory 对象
```java
SqlSessionFactory sqlSessionFactory = 
	sqlSessionFactoryBuilder.build(Resources.getResourceAsStream("mybatis-config.xml"));
```

+ 这种方式就是获取默认数据库环境
+ 该 SqlSessionFactory 对象对应在 environments 标签的 default 属性中指定的数据库环境

##### 通过数据库环境id获取 SqlSessionFactory 对象
```java
SqlSessionFactory sqlSessionFactory1 =
	sqlSessionFactoryBuilder.build(Resources.getResourceAsStream("mybatis-config.xml"), "powernodeDB");
```

+ 第二个参数为数据库环境id
+ 这种方式就是通过数据库环境id来使用指定的数据库环境
+ 通过该方式获取的 SqlSessionFactory 对象对应 id 相应的数据库环境

##### transactionManager
```xml
<transactionManager type="JDBC"/>
```

+ 作用：配置事务管理器，指定mybatis具体使用什么方式去管理事务。
+ type属性有两个值：
    - 第一个：JDBC: 使用原生的JDBC代码来管理事务。
    - `conn.setAutoCommit(false);`
    - `...`
    - `conn.commit();`
    - 第二个：MANAGED：mybatis不再负责事务的管理，将事务管理交给其它的JEE(JavaEE)容器来管理。
        * 例如：spring
    - 大小写无所谓。不缺分大小写。但是不能写其他值。只能是二选一： jdbc、managed
+ 在mybatis中提供了一个事务管理器接口：Transaction
    - 该接口下有两个实现类：
        * JdbcTransaction
        * ManagedTransaction
+ 如果type="JDBC"，那么底层会实例化JdbcTransaction对象。
+ 如果type="MANAGED"，那么底层会实例化ManagedTransaction

##### dataSource
```xml
<dataSource type="POOLED">
    <property name="driver" value="${jdbc.driver}"/>
    <property name="url" value="${jdbc.url}"/>
    <property name="username" value="${jdbc.username}"/>
    <property name="password" value="${jdbc.password}"/>
</dataSource>
```

+ dataSource被称为数据源。
+ dataSource的作用：为程序提供Connection对象。
    - 凡是给程序提供Connection对象的，都叫做数据源。
+ 数据源实际上是一套规范。
    - JDK中有这套规范：javax.sql.DataSource，这个数据源的规范，这套接口是JDK规定的。
    - 我们自己也可以编写数据源组件，只要实现javax.sql.DataSource接口就行，实现接口当中所有的方法。
+ 常见的数据源组件有哪些呢【常见的数据库连接池有哪些呢】？
    - 阿里巴巴的德鲁伊连接池：druid
    - c3p0
    - dbcp
    - ....
+ type属性用来指定数据源的类型，就是指定具体使用什么方式来获取Connection对象：
    - type属性有三个值：必须是三选一。
    - type="[UNPOOLED|POOLED|JNDI]"
    - UNPOOLED：不使用数据库连接池技术。每一次请求过来之后，都是创建新的Connection对象。
    - POOLED：使用mybatis自己实现的数据库连接池。
    - JNDI：集成其它第三方的数据库连接池。
        * JNDI是一套规范，大部分的web容器都实现了JNDI规范，例如：Tomcat、Jetty、WebLogic、WebSphere，这些服务器(容器)都实现了JNDI规范。
        * JNDI是：java命名目录接口。Tomcat服务器实现了这个规范。
    - 数据源的type属性指定不同的值，可以配置不同的属性 [https://mybatis.net.cn/configuration.html#environments](https://mybatis.net.cn/configuration.html#environments)

```xml
<dataSource type="POOLED">
    <property name="driver" value="${jdbc.driver}"/>
    <property name="url" value="${jdbc.url}"/>
    <property name="username" value="${jdbc.username}"/>
    <property name="password" value="${jdbc.password}"/>
    <!-- 以下配置数据库连接池的参数 -->
    <!--提醒：正常使用连接池的话，池中有很多参数是需要设置的。设置好参数，可以让连接池发挥的更好。事半功倍的效果。-->
    <!--具体连接池当中的参数如何配置呢？需要反复的根据当前业务情况进行测试。-->
    <!--poolMaximumActiveConnections：连接池当中最多的正在使用的连接对象的数量上限。最多有多少个连接可以活动。默认值10-->
    <property name="poolMaximumActiveConnections" value="10"/>
    <!--每隔2秒打印日志，并且尝试获取连接对象-->
    <property name="poolTimeToWait" value="2000"/>
    <!--强行让某个连接空闲，超时时间的设置-->
    <property name="poolMaximumCheckoutTime" value="10000"/>
    <!--最多的空闲数量-->
    <!--
        假设最多的连接数量为10个，最多空闲数量为5个，现在已经空闲5个了，马上第六个也要空闲了
        如果第六个空闲下来，连接池为了保证空闲的数量最多5个，会真正关闭多余的空闲连接对象
        可以节省系统资源
    -->
    <property name="poolMaximumIdleConnections" value="5"/>
</dataSource>
```

### mappers
+ 在mappers标签中可以配置多个sql映射文件的路径

```xml
<mappers>
    <!-- mapper：配置某个sql映射文件的路径 -->
    <!-- resource属性：使用相对于类路径的资源引用方式 -->
    <!-- url属性：使用完全限定资源定位符（URL）方式 -->
    <mapper resource="CarMapper.xml"/>
</mappers>
```





