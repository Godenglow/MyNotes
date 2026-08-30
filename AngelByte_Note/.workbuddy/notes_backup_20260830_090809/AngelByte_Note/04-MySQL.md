# 数据库概述
## 1.1 聊聊数据库
---

- 数据库是一门独立的学科，只要是做软件开发的，数据库都要学。
- 数据库（电子化的文件柜）是“按照数据结构来组织、存储和管理数据的仓库”。是一个长期存储在计算机内的、有组织的、可共享的、统一管理的大量数据的集合。
- 它的存储空间很大，可以存放百万条、千万条、上亿条数据。
- 数据库并不是随意地将数据进行存放，是有一定的规则的，否则查询的效率会很低。
- 当今世界是一个充满着数据的互联网世界，充斥着大量的数据。即这个互联网世界就是数据世界。数据的来源有很多，比如出行记录、消费记录、浏览的网页、发送的消息等等。除了文本类型的数据，图像、音乐、声音都是数据。
- 数据库对应的英文单词是DataBase，简称DB。

## 1.2 数据库类型
---

- 关系型数据库
    - 关系型数据库是依据关系模型来创建的数据库。所谓关系模型就是“一对一、一对多、多对多”等关系模型，关系模型就是指二维表格模型，因而一个关系型数据库就是由二维表及其之间的联系组成的一个数据组织。
    - 关系型数据可以很好地存储一些关系模型的数据，比如一个老师对应多个学生的数据（“多对多”），一本书对应多个作者（“一对多”），一本书对应一个出版日期（“一对一”）。
    - 关系模型包括数据结构（数据存储的问题，二维表）、操作指令集合（SQL语句）、完整性约束(表内数据约束、表与表之间的约束)。
- 非关系型数据库（NoSQL）
    - NoSQL，泛指非关系型的数据库。随着互联网web2.0网站的兴起，传统的关系数据库在处理web2.0网站，特别是超大规模和高并发的SNS类型的web2.0纯动态网站已经显得力不从心，出现了很多难以克服的问题，而非关系型的数据库则由于其本身的特点得到了非常迅速的发展。
    - NoSQL数据库的产生就是为了解决大规模数据集合多重数据种类带来的挑战，特别是大数据应用难题。NoSQL最常见的解释是“non-relational”， “Not Only SQL”也被很多人接受。
    - NoSQL仅仅是一个概念，泛指非关系型的数据库，区别于关系数据库，它们不保证关系数据的ACID特性。NoSQL是一项全新的数据库革命性运动，其拥护者们提倡运用非关系型的数据存储，相对于铺天盖地的关系型数据库运用，这一概念无疑是一种全新的思维的注入。
    - NoSQL有如下优点：易扩展，NoSQL数据库种类繁多，但是一个共同的特点都是去掉关系数据库的关系型特性。数据之间无关系，这样就非常容易扩展。无形之间也在架构的层面上带来了可扩展的能力。大数据量，高性能，NoSQL数据库都具有非常高的读写性能，尤其在大数据量下，同样表现优秀。这得益于它的无关系性，数据库的结构简单。

## 1.3 数据库管理系统
---

- 数据库管理系统（Database Management System，简称DBMS）是为管理数据库而设计的电脑软件系统，一般具有存储、截取、安全保障、备份等基础功能。
- 数据库管理系统是数据库系统的核心组成部分，主要完成对数据库的操作与管理功能，实现数据库对象的创建、数据库存储数据的查询、添加、修改与删除操作和数据库的用户管理、权限管理等。
- 常见的数据库管理系统有：MySQL、Oracle、DB2、MS SQL Server、SQLite、PostgreSQL、Sybase等。

## 1.4 什么是SQL
---

- 结构化查询语言（Structured Query Language）简称SQL，是一种特殊目的的编程语言，是一种数据库查询和程序设计语言，用于存取数据以及查询、更新和管理关系数据库系统。
- 结构化查询语言是高级的非过程化编程语言，允许用户在高层数据结构上工作。它不要求用户指定对数据的存放方法，也不需要用户了解具体的数据存放方式，所以具有完全不同底层结构的不同数据库系统, 可以使用相同的结构化查询语言作为数据输入与管理的接口。结构化查询语言语句可以嵌套，这使它具有极大的灵活性和强大的功能。
- SQL的分类
    - DQL
        * 数据查询语言（Data Query Language, DQL）是SQL语言中，负责进行数据查询而不会对数据本身进行修改的语句，这是最基本的SQL语句。保留字SELECT是DQL（也是所有SQL）用得最多的动词，其他DQL常用的保留字有FROM，WHERE，GROUP BY，HAVING和ORDER BY。这些DQL保留字常与其他类型的SQL语句一起使用。
    - DDL
        * 数据定义语言 (Data Definition Language, DDL) 是SQL语言集中，负责数据结构定义与数据库对象定义的语言，由CREATE、ALTER与DROP三个语法所组成，最早是由 Codasyl (Conference on Data Systems Languages) 数据模型开始，现在被纳入 SQL 指令中作为其中一个子集。
    - DML
        * 数据操纵语言（Data Manipulation Language, DML）是SQL语言中，负责对数据库对象运行数据访问工作的指令集，以INSERT、UPDATE、DELETE三种指令为核心，分别代表插入、更新与删除。
    - DCL
        * 数据控制语言 (Data Control Language) 在SQL语言中，是一种可对数据访问权进行控制的指令，它可以控制特定用户账户对数据表、查看表、预存程序、用户自定义函数等数据库对象的控制权。由 GRANT 和 REVOKE 两个指令组成。DCL以控制用户的访问权限为主，GRANT为授权语句，对应的REVOKE是撤销授权语句。
    - TPL
        * 数据事务管理语言（Transaction Processing Language）它的语句能确保被DML语句影响的表的所有行及时得以更新。TPL语句包括BEGIN TRANSACTION，COMMIT和ROLLBACK。
    - CCL
        * 指针控制语言（Cursor Control Language），它的语句，像DECLARE CURSOR，FETCH INTO和UPDATE WHERE CURRENT用于对一个或多个表单独行的操作。
- DBMS、SQL、DB之间的关系
    - DBMS通过执行SQL来操作DB中的数据。

# MySQL的安装与配置
## 2.1 MySQL概述
---

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1619752945028-dbcb73aa-50e2-4b1c-947d-21da8d742e6d.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_9%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

- MySQL是一个关系型数据库管理系统，由瑞典MySQL AB公司开发，MySQL AB公司被Sun公司收购，Sun公司又被Oracle公司收购，目前属于Oracle公司。
- MySQL是目前最流行的关系型数据库管理系统，在WEB应用方面MySQL是最好的RDBMS应用软件之一。 国内淘宝网站就使用的是MySQL集群。
- MySQL特点
    - MySQL有开源版本和收费版本，你使用开源版本是不收费的。
    - MySQL支持大型数据库，可以处理上千万记录的大型数据库。
    - MySQL使用标准的SQL数据库语言形式。
    - MySQL在很多系统上面都支持。
    - MySQL对Java，C都有很好的支持，当然其他的语言也支持比如Python、PHP。
    - MySQL是可以定制的，采用了GPL协议，你可以修改源码来开发自己的MySQL系统。

## 2.2 MySQL的下载
---

- 第一种下载方式：官网下载
    - 第一步：打开MySQL官网[https://www.mysql.com/](https://www.mysql.com/)

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1619753207824-f47a5a2c-3ee1-4d73-881d-be1bb67a8019.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_53%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

    - 第二步：点击"DOWNLOADS"

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1619754075151-2e1900d9-0ee0-4905-b3dc-97b5598061f1.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_31%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

    - 第三步：当前页继续下拉，直到找到下图链接

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1619754206255-ee47b52c-e183-4401-a8e7-7b0e51452a00.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_28%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

    - 第四步：点击上图链接，进入下面页面，其中“MySQL Community Server”是解压版mysql，“MySQL Installer for Windows”是安装版，这里我们选择解压版

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1619754239811-b4151058-268c-406b-bcd3-72a6d5771e4b.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_29%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

    - 第五步：点击上图“MySQL Community Server”

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620375449949-470a5fb1-8af6-4130-a424-129b8961cb8c.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_35%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

    - 第六步：点击上图第1个“Download”

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1619754349149-75c6289e-0461-4c82-bf0b-388471535683.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_29%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

    - 第七步：点击上图“No thanks, just start my download.”开始下载，直到下载完毕。

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620375547996-62d248ee-f33d-41a5-ba14-50cf38405d9b.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_11%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

- 第二种下载方式：百度网盘
    - 链接：[https://pan.baidu.com/s/1Oxy4_X2VnuX5Gb3Vh0Cctg](https://pan.baidu.com/s/1Oxy4_X2VnuX5Gb3Vh0Cctg) 提取码：ho17 

## 2.3 MySQL安装与配置
---

- 将下载的zip压缩包解压，我这里直接解压到C盘的根目录下

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620375547996-62d248ee-f33d-41a5-ba14-50cf38405d9b.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_11%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620376986790-01106d3e-b89f-453a-98cb-f2a86d4b2544.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_14%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

mysql的根目录为：C:\mysql-8.0.24-winx64

- 将C:\mysql-8.0.24-winx64\bin目录配置到环境变量path当中

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620377142769-f797dd2c-4f82-4c8f-b5a2-d97bfbe52225.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

- 初始化data目录
    - 使用管理员身份打开dos命令窗口（按win键，输入cmd，点击管理员身份运行）

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620377404683-4ed7c1d7-c8f1-44a3-ae32-0005183fcd09.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_22%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

    - cd命令切换到mysql的bin目录下，执行mysqld --initialize --console进行data目录初始化，此时会在控制台生成一个随机密码，下图红框中就是随机密码

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620379266865-b043168d-8825-44e9-99ab-35ce6f8c8e25.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_29%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

技巧：左键选中密码，直接点击右键，此时密码已经复制到剪贴板中了，

然后随便找一个文件，将密码粘贴到文件中保存起来。

- 安装MySQL服务：cd命令切换到bin目录下，执行命令mysqld -install

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620379567159-f63f3527-3ba9-48fe-8a19-57e4c3767662.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_10%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

- 查看mysql服务名称：此电脑-右键-管理-服务和应用程序-服务-找MySQL服务，如下图mysql服务名称：MySQL

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620379678662-4b14e7a5-d17c-4c2b-917d-cc4d73b94ae5.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_23%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

- 启动MySQL服务：net start mysql，注意start后面是mysql服务的名称

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620379806288-826de76c-2827-419e-ab16-b6fc72afdbca.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_10%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

停止mysql服务的命令：net stop mysql

注意：启停mysql服务也可以在上一步的图中点击右键进行启停服务。

- 登录mysql：输入mysql -uroot -p，然后回车，输入刚才的随机密码，然后回车，看到下图表示成功登录mysql

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620379936249-1bfaef7c-9ca7-4ddd-978a-b518acd834b0.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_18%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

- 修改MySQL的root账户密码：ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '新密码';

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620382836782-5a7fef8d-15ce-4dca-a5d0-831b6f60f56e.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_22%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

- 使用新密码登录mysql

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620382883258-875c0c1a-00c7-40f8-a8dd-edb1d39e94e0.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_20%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

## 2.4 MySQL卸载
---

- 停止mysql的服务

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620383089030-497a3bfc-74d5-43a6-9689-8f9e0b24dd73.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_10%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

- 删除mysql服务

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620383158420-3d5117c6-0c0f-421c-9570-407dac8c6612.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_12%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

- 删除mysql的目录

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620383199727-89d46dc3-b4cf-4883-9a18-b0ee0c0fe6e8.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

## 2.5 登录MySQL
---

- 本地登录
    - 如果mysql的服务是启动的，打开dos命令窗口，输入：mysql -uroot -p，回车，然后输入root账户的密码

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620389190451-81319065-6d04-4094-97d0-13236236ad32.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_30%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

解释“mysql -uroot -p”：

mysql是一个命令，在bin目录下，对应的命令文件是mysql.exe，如果将bin目录配置到环境

变量path中，才可以在以上位置使用该命令。

-uroot 表示登录的用户是root，u实际上是user单词的首字母。

-p 表示登录时使用密码，p实际上是password单词的首字母。

    - 也可以将密码以明文的形式写到-p后面，这样做可能会导致你的密码泄露

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620389582655-74210644-318a-4e71-a242-192d61ef9fd9.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_29%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

- 远程登录
    - 假设mysql安装在A机器上，现在你要在B机器上连接mysql数据库，此时需要使用远程登录，远程登录时加上远程机器的ip地址即可

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620389951870-e1585ee0-d1cd-4b89-973b-b3e6c4a20539.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_28%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

-h中的h实际上是host单词的首字母。在-h后面的是远程计算机的ip地址。

127.0.0.1是计算机默认的本机IP地址。

127.0.0.1又可以写作：localhost，他们是等效的。

注意：mysql默认情况下root账户是不支持远程登录的，其实这是一种安全策略，

为了保护root账户的安全。如果希望root账户支持远程登录，这是需要进行设置的。

# 初始化测试数据
## 3.1 MySQL命令行基本命令
---

1. 列出当前数据库管理系统中有哪些数据库。

```sql
show databases;
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620402104809-379ae418-d997-4758-9a02-45bbfad7178e.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_10%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

2. 创建数据库，起名bjpowernode。

```sql
create database bjpowernode;
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620402231403-ddd2c76f-3b9f-4477-9504-502328fe64fc.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

3.  使用bjpowernode数据库。

```sql
use bjpowernode;
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620402295297-4dbb2d54-4210-44c9-bc8f-c887327bfb8c.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_10%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

4. 查看当前用的是哪个数据库。

```sql
select database();
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620402349349-2786c9cb-8683-4d17-bd26-c73a7b451847.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_12%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

5.  查看当前数据库中有哪些表。

```sql
show tables;
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620402397890-84d73980-1046-4e83-b6cb-bdcc68ba7b57.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_9%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620402645490-1cd5d42e-5735-4c0a-8723-e4fb81c96b8a.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

6.  删除数据库bjpowernode。

```sql
drop database bjpowernode;
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620402497021-d7ff9bf3-3c9a-4c9c-bc5d-f5dece31188f.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_10%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

7. 退出mysql
    1. exit
    2. quit
    3. ctrl + c
8. 查看当前mysql版本

```sql
select version();
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620468380301-0c326efb-a538-4271-b75d-ff5add0e453a.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_13%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

还可以使用mysql.exe命令来查看版本信息（在没有登录mysql之前使用）：mysql --version

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620468207568-77aa05ff-8d65-47f6-b90d-2c176893a52f.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_18%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

## 3.2 数据库表的概述
---

| name | age | gender |
| --- | --- | --- |
| 张三 | 20 | 男 |
| 李四 | 22 | 女 |

- 以上就是数据库表格的直观展示形式。
- 表格英文单词table。
- 表是数据库存储数据的基本单元，数据库存储数据的时候，是将数据存储在表对象当中的。为什么将数据存储在表中呢？因为表存储数据非常直观。
- 任何一张表都有行和列：
    - 行：记录（一行就是一条数据）
    - 列：字段（name字段、age字段、gender字段）
- 每个字段包含以下属性：
    - 字段名：name、age、gender都是字段的名字
    - 字段的数据类型：每个字段都有数据类型，比如：字符类型、数字类型、日期类型
    - 字段的数据长度：每个字段有可能会有长度的限制
    - 字段的约束：比如某些字段要求该字段下的数据不能重复、不能为空等，用来保证表格中数据合法有效

## 3.3 初始化测试数据
---

为了方便后面内容的学习，老师提前准备了表以及表中的测试数据，以下是建表并且初始化数据的sql脚本

```sql
DROP TABLE IF EXISTS EMP;
DROP TABLE IF EXISTS DEPT;
DROP TABLE IF EXISTS SALGRADE;

CREATE TABLE DEPT(DEPTNO int(2) not null ,
	DNAME VARCHAR(14) ,
	LOC VARCHAR(13),
	primary key (DEPTNO)
);
CREATE TABLE EMP(EMPNO int(4)  not null ,
	ENAME VARCHAR(10),
	JOB VARCHAR(9),
	MGR INT(4),
	HIREDATE DATE  DEFAULT NULL,
	SAL DOUBLE(7,2),
	COMM DOUBLE(7,2),
	primary key (EMPNO),
	DEPTNO INT(2) 
);

CREATE TABLE SALGRADE( GRADE INT,
	LOSAL INT,
	HISAL INT
);

INSERT INTO DEPT ( DEPTNO, DNAME, LOC ) VALUES ( 10, 'ACCOUNTING', 'NEW YORK'); 
INSERT INTO DEPT ( DEPTNO, DNAME, LOC ) VALUES ( 20, 'RESEARCH', 'DALLAS'); 
INSERT INTO DEPT ( DEPTNO, DNAME, LOC ) VALUES ( 30, 'SALES', 'CHICAGO'); 
INSERT INTO DEPT ( DEPTNO, DNAME, LOC ) VALUES ( 40, 'OPERATIONS', 'BOSTON'); 
 
INSERT INTO EMP ( EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM,DEPTNO ) VALUES ( 7369, 'SMITH', 'CLERK', 7902,  '1980-12-17', 800, NULL, 20); 
INSERT INTO EMP ( EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM,DEPTNO ) VALUES ( 7499, 'ALLEN', 'SALESMAN', 7698,  '1981-02-20', 1600, 300, 30); 
INSERT INTO EMP ( EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM,DEPTNO ) VALUES ( 7521, 'WARD', 'SALESMAN', 7698,  '1981-02-22', 1250, 500, 30); 
INSERT INTO EMP ( EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM,DEPTNO ) VALUES ( 7566, 'JONES', 'MANAGER', 7839,  '1981-04-02', 2975, NULL, 20); 
INSERT INTO EMP ( EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM,DEPTNO ) VALUES ( 7654, 'MARTIN', 'SALESMAN', 7698,  '1981-09-28', 1250, 1400, 30); 
INSERT INTO EMP ( EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM,DEPTNO ) VALUES ( 7698, 'BLAKE', 'MANAGER', 7839,  '1981-05-01', 2850, NULL, 30); 
INSERT INTO EMP ( EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM,DEPTNO ) VALUES ( 7782, 'CLARK', 'MANAGER', 7839,  '1981-06-09', 2450, NULL, 10); 
INSERT INTO EMP ( EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM,DEPTNO ) VALUES ( 7788, 'SCOTT', 'ANALYST', 7566,  '1987-04-19', 3000, NULL, 20); 
INSERT INTO EMP ( EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM,DEPTNO ) VALUES ( 7839, 'KING', 'PRESIDENT', NULL,  '1981-11-17', 5000, NULL, 10); 
INSERT INTO EMP ( EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM,DEPTNO ) VALUES ( 7844, 'TURNER', 'SALESMAN', 7698,  '1981-09-08', 1500, 0, 30); 
INSERT INTO EMP ( EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM,DEPTNO ) VALUES ( 7876, 'ADAMS', 'CLERK', 7788,  '1987-05-23', 1100, NULL, 20); 
INSERT INTO EMP ( EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM,DEPTNO ) VALUES ( 7900, 'JAMES', 'CLERK', 7698,  '1981-12-03', 950, NULL, 30); 
INSERT INTO EMP ( EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM,DEPTNO ) VALUES ( 7902, 'FORD', 'ANALYST', 7566,  '1981-12-03', 3000, NULL, 20); 
INSERT INTO EMP ( EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM,DEPTNO ) VALUES ( 7934, 'MILLER', 'CLERK', 7782,  '1982-01-23', 1300, NULL, 10); 
 
INSERT INTO SALGRADE ( GRADE, LOSAL, HISAL ) VALUES ( 1, 700, 1200); 
INSERT INTO SALGRADE ( GRADE, LOSAL, HISAL ) VALUES ( 2, 1201, 1400); 
INSERT INTO SALGRADE ( GRADE, LOSAL, HISAL ) VALUES ( 3, 1401, 2000); 
INSERT INTO SALGRADE ( GRADE, LOSAL, HISAL ) VALUES ( 4, 2001, 3000); 
INSERT INTO SALGRADE ( GRADE, LOSAL, HISAL ) VALUES ( 5, 3001, 9999); 
commit;
```

- 什么是sql脚本：文件名是.sql，并且该文件中编写了大量的SQL语句，执行sql脚本程序就相当于批量执行SQL语句。
- 你入职的时候，项目一般都是进展了一部分，多数情况下你进项目组的时候数据库的表以及数据都是有的，项目经理第一天可能会给你一个较大的sql脚本文件，你需要执行这个脚本文件来初始化你的本地数据库。（当然，也有可能数据库是共享的。）
- 创建文件：bjpowernode.sql，把以上SQL语句全部复制到sql脚本文件中。
- 执行SQL脚本文件，初始化数据库
    - 第一步：命令窗口登录mysql
    - 第二步：创建数据库bjpowernode（如果之前已经创建就不需要再创建了）：create database bjpowernode;
    - 第三步：使用数据库bjpowernode：use bjpowernode;
    - 第四步：source命令执行sql脚本，注意：source命令后面是sql脚本文件的绝对路径。

        ![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620435073900-d9e19c5e-9b0e-4d09-a3ee-74471ec9ebb8.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_13%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

    - 第五步：查看是否初始化成功，执行：show tables;

        ![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620435161519-44d66617-3323-4834-8f57-5db6cc4c8cf3.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_11%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

- 使用其他的mysql客户端工具也可以执行sql脚本，比如navicat。使用source命令执行sql脚本的优点：**<font style="color:#F5222D;">可支持大文件</font>**。

## 3.4 熟悉测试数据
---

emp dept salgrade三张表分别存储什么信息

- emp：员工信息
- dept：部门信息
- salgrade：工资等级信息

查看表结构：desc或describe，语法格式：desc或describe +表名

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620441048844-4e9e7687-f9a2-4014-a014-f5a2c267b422.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_16%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

以上的结果展示的不是表中的数据，而是表的结构。

- Field是字段名
- Type是这个字段的数据类型
- Null是这个字段是否允许为空
- Key是这个字段是否为主键或外键
- Default是这个字段的默认值

对以上表结构进行解释说明：

- emp表
    - empno：员工编号，int类型（整数），不能为空，主键（主键后期学习约束时会进行说明）
    - ename：员工姓名，varchar类型（字符串）
    - job：工作岗位，varchar类型
    - mgr：上级领导编号，int类型
    - hiredate：雇佣日期，date类型（日期类型）
    - sal：月薪，double类型（带有浮点的数字）
    - comm：补助津贴，double类型
    - deptno：部门编号，int类型
- dept表
    - deptno：部门编号，int类型，主键
    - dname：部门名称，varchar类型
    - loc：位置，varchar类型
- salgrade表
    - grade：等级，int类型
    - losal：最低工资，int类型
    - hisal：最高工资，int类型

对于以上表结构要提前了解，后面学习的内容需要你马上反应出：哪个字段是什么意思。

查看一下表中的数据，来加深一下印象（以下SQL语句会在后面课程中学习）：

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620442749316-53eb0de4-bc2f-4af4-b6fa-a39eafc5265e.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_21%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

# 查询DQL专题
## 4.1 简单查询
---

查询是SQL语言的核心，用于表达SQL查询的select查询命令是功能最强也是最为复杂的SQL语句，它的作用就是从数据库中检索数据，并将查询结果返回给用户。 select语句由：select子句(查询内容)、from子句(查询对象)、where子句(查询条件)、order by子句(排序方式)、group by子句(分组方式)等组成。查询语句属于SQL语句中的DQL语句，是所有SQL语句中最为复杂也是最重要的语句，所以必须掌握。接下来我们先从简单查询语句开始学习。

### 4.1.1 查一个字段
---

查询一个字段说的是：一个表有多列，查询其中的一列。

语法格式：select 字段名 from 表名;

- select和from是关键字，不能随便写
- **<font style="color:#F5222D;">一条SQL语句必须以“;”结尾</font>**
- **<font style="color:#F5222D;">对于SQL语句来说，大小写都可以</font>**
- 字段名和表名属于标识符，按照表的实际情况填写，不知道字段名的，可以使用desc命令查看表结构

案例1：查询公司中所有员工编号

```sql
select empno from emp; 
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620444005101-f8b17d19-7943-42da-868a-4353bbc39d72.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

案例2：查询公司中所有员工姓名

```sql
SELECT ENAME FROM EMP;
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620444051586-c22b328d-726d-43a1-84c5-b61b053e4c76.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

在mysql命令行客户端中，sql语句没有分号是不会执行的：

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620444166592-310dfb98-9eed-43ed-afa5-b479e03e0a79.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_9%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

末尾加上“;”就执行了：

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620444251765-5d3f1b6c-a491-4382-92a8-8ebb31a40b45.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_27%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

以上sql虽然以分号结尾之后执行了，但是报错了，错误信息显示：语法错误。

假设一个SQL语句在书写过程中出错了，怎么终止这条SQL呢？\c

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620444994820-7b03fb95-5097-418c-bc6f-75e3613c7d17.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_9%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

- [ ] 任务1：查询所有部门名称。
- [ ] 任务2：查询所有薪资等级。

### 4.1.2 查多个字段
---

查询多个字段时，在字段名和字段名之间添加“,”即可。

语法格式：select 字段名1,字段名2,字段名3 from 表名;

案例1：查询员工编号以及员工姓名。

```sql
select empno, ename from emp;
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620445192077-e454043b-9203-4ca0-83f3-7e7d991187c5.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_11%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

字段的前后顺序无所谓（只是显示结果列的时候顺序变了）：

```sql
select ename, empno from emp;
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620445262526-49d81087-7e1b-44f2-afe7-e8bad59dc21d.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_10%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

- [ ] 任务1：查询部门编号、部门名称以及位置。
- [ ] 任务2：查询员工的名字以及工作岗位。

### 4.1.3 查所有字段
---

查询所有字段的可以将每个字段都列出来查询，也可以采用“*”来代表所有字段

案例1：查询员工的所有信息

```sql
select * from emp;
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620446156182-c5776f47-0d54-45e1-b0a6-af8196b3cbcd.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_21%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

案例2：查询所有部门信息

```sql
select * from dept;
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620452731531-c4b03af4-9f9f-46d8-acf5-7132317f89ae.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

采用“*”进行查询存在的缺点：

- select * from dept; 在执行的时候会被解析为 select DEPTNO, DNAME, LOC from dept; 再执行，所以这种效率方面弱一些。
- 采用“*”的可读性较差，通过“*”很难看出都有哪些具体的字段。

什么时候使用“*”？

- 这个SQL语句不在项目编码中使用，如果平时自己想快速查看表中所有数据的话，这种写法还是很给力的。

- [ ] 任务1：查询所有的薪资等级以及每个薪资等级的最低工资和最高工资。

### 4.1.4 查询时字段可参与数学运算
---

在进行查询操作的时候，字段是可以参与数学运算的，例如加减乘除等。

案例1：查询每个员工的月薪

```sql
select ename, sal from emp;
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620453626714-46aed4db-e9fb-49be-a9be-ce9662dbc962.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_11%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

案例2：查询每个员工的年薪（月薪 * 12）

```sql
select ename, sal * 12 from emp;
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620453661204-ca783845-5f31-49fc-90d8-0f4426598cde.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_11%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

- [ ] 任务1：查询每个员工月薪加1000之后的月薪
- [ ] 任务2：查询每个员工月薪加1000之后的年薪

### 4.1.5 查询时字段可起别名
---

我们借用一下之前的SQL语句

```sql
select ename, sal * 12 from emp;
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620453661204-ca783845-5f31-49fc-90d8-0f4426598cde.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_11%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

以上的查询结果列名“sal * 12”可读性较差，是否可以给查询结果的列名进行重命名呢？

- 使用as关键字

```sql
select ename, sal * 12 as yearsal from emp;
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620454420847-c739365b-440e-4cf7-b1e2-2bcf6d5cdb8b.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_13%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

通过as关键字起别名后，查询结果列显示yearsal，可读性增强。

- 其实as关键字可以省略，只要使用空格即可

```sql
select ename, sal * 12 yearsal from emp;
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620466356467-fb4612f8-72f6-4506-b2bc-1744846c171d.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_13%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

- 通过以上测试，得知as可以省略，可以使用空格代替as，但如果别名中有空格呢？

```sql
select ename, sal * 12 year sal from emp;
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620466540145-98adb10e-15a2-46df-9179-7e41ae1fc322.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_27%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

可以看出，执行报错了，说语法有问题，这是为什么？分析一下：SQL语句编译器在检查该语句的时候，在year后面遇到了空格，会继续找from关键字，但year后面不是from关键字，所以编译器报错了。怎么解决这个问题？记住：如果别名中有空格的话，可以将这个别名使用双引号或者单引号将其括起来。

```sql
select ename, sal * 12 "year sal" from emp;
select ename, sal * 12 'year sal' from emp;
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620467027246-b5cce57e-3ca3-4b3f-9298-a21fc3bb77c3.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_16%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

**<font style="color:#F5222D;">在mysql中，字符串既可以使用双引号也可以使用单引号，但还是建议使用单引号，因为单引号属于标准SQL。</font>**

- 如果别名采用中文呢？

```sql
select ename, sal * 12 年薪 from emp;
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1620467760618-b5df74f5-c8ee-4e39-88a9-e10fde59bb56.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_13%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

**<font style="color:#F5222D;">别名是中文是可以的，但是对于低版本的mysql来说会报错，需要添加双引号或单引号。</font>**我们当前使用的mysql版本是：8.0.24

- [ ] 任务：查询所有员工的信息，要求每个字段名采用中文显示。

## 4.2 条件查询
---

通常在进行查询操作的时候，都是查询符合某些条件的数据，很少将表中所有数据都取出来。怎么取出表的部分数据？需要在查询语句中添加条件进行数据的过滤。常见的过滤条件如下：

| **条件** | **说明** |
| --- | --- |
| = | 等于 |
| <>或!= | 不等于 |
| >= | 大于等于 |
| <= | 小于等于 |
| > | 大于 |
| < | 小于 |
| between...and... | 等同于 >= and <= |
| is null | 为空 |
| is not null | 不为空 |
| <=> | 安全等于（可读性差，很少使用了）。 |
| and 或 && | 并且 |
| or 或 || | 或者 |
| in | 在指定的值当中 |
| not in | 不在指定的值当中 |
| exists |  |
| not exists |  |
| like | 模糊查询 |

### 4.2.1 条件查询语法格式
---

```sql
select 
  ...
from
  ...
where
  过滤条件;
```

过滤条件放在where子句当中，以上语句的执行顺序是：

    第一步：先执行from

    第二步：再通过where条件过滤

    第三步：最后执行select，查询并将结果展示到控制台

### 4.2.2 等于、不等于
---

- =

判断等量关系，支持多种数据类型，比如：数字、字符串、日期等。

案例1：查询月薪3000的员工编号及姓名

```sql
select 
  empno,ename
from
  emp
where
  sal = 3000;
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621907694609-eea9c573-f409-4291-b065-afdbf568e8c7.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_14%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

案例2：查询员工FORD的岗位及月薪

```sql
select
	job, sal
from
	emp
where
	ename = 'FORD';
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621907754724-3f628fe9-0c56-4057-8be7-60d0bf968b6c.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_14%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

存储在表emp中的员工姓名是FORD，全部大写，如果在查询的时候，写成全部小写会怎样呢？

```sql
select
	job, sal
from
	emp
where
	ename = 'ford';
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621907908980-acfef2ac-247a-434a-846d-aebe132c534b.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_12%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

通过测试发现，即使写成小写ford，也是可以查询到结果的，**<font style="color:#F5222D;">不过这里需要注意的是：在Oracle数据库当中是查询不到数据的，Oracle的语法要比MySQL的语法严谨。对于SQL语句本身来说是不区分大小写的，但是对于表中真实存储的数据，大写A和小写a还是不一样的，这一点Oracle做的很好。MySQL的语法更随性。另外在Oracle当中，字符串是必须使用单引号括起来的，但在MySQL当中，字符串可以使用单引号，也可以使用双引号</font>**，如下：

```sql
select
	job, sal
from
  emp
where
  ename = "FORD";
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621908335672-ce3770ed-b906-44ad-8e6a-1255e620f77c.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_16%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

案例3：查询岗位是MANAGER的员工编号及姓名

```sql
select
  empno, ename
from
  emp
where
  job = 'MANAGER';
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621908485311-e63dfa85-7530-4d2e-8652-f5885287dda7.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_17%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

- [ ] 任务：查询工资级别是1的最低工资以及最高工资
- <> 或 !=

判断非等量关系，支持字符串、数字、日期类型等。不等号有两种写法，第一种<>，第二种!=，第二种写法和Java程序中的不等号相同，第一种写法比较诡异，不过也很好理解，比如<>3，表示小于3、大于3，就是不等于3。你get到了吗？

案例1：查询工资不是3000的员工编号、姓名、薪资

```sql
select
  empno,ename,sal
from
  emp
where
  sal <> 3000;
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621909279969-92f574b8-825b-4774-ab25-b5ccb058ebd5.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_16%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

案例2：查询工作岗位不是MANAGER的员工姓名和岗位

```sql
select
  ename,job
from
	emp
where
	job <> 'MANAGER';
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621909394164-d589f9f5-30a1-477c-aef6-b659ae36d9e8.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_16%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

- [ ] 任务：查询不在部门编号为10的部门工作的员工信息

### 4.2.3 大于、大于等于、小于、小于等于
---

- 大于 >

案例：找出薪资大于3000的员工姓名、薪资

```sql
select 
  ename, sal
from
  emp
where
  sal > 3000;
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621909653019-47b3d57f-3690-46fb-9f47-7906f0fd3245.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

- 大于等于 >=

案例：找出薪资大于等于3000的员工姓名、薪资

```sql
select 
  ename, sal
from
  emp
where
  sal >= 3000;
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621909723383-d1a6872b-5790-4d89-875b-e1116ea539cf.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

- 小于 <

案例：找出薪资小于3000的员工姓名、薪资

```sql
select 
  ename, sal
from
  emp
where
  sal < 3000;
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621909833614-f9d57a1f-1d48-4d14-aaef-83c5bddb89a8.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

- 小于等于 <=

案例：找出薪资小于等于3000的员工姓名、薪资

```sql
select 
  ename, sal
from
  emp
where
  sal <= 3000;
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621909895715-9af5ab2f-b445-4b44-a643-fd2a312cac2c.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

### 4.2.4 and
---

and表示并且，还有另一种写法：&&

案例：找出薪资大于等于3000并且小于等于5000的员工姓名、薪资。

```sql
select
  ename,sal
from
  emp
where
  sal >= 3000 and sal <= 5000;
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621910545661-438867ac-b8d0-4a80-929e-5a758b44add4.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_19%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621910577682-f852440b-94f8-4299-89ad-c0a88fefc0d1.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_19%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

- [ ] 任务：找出工资级别为2~4（包含2和4）的最低工资和最高工资。

### 4.2.5 or
---

or表示或者，还有另一种写法：||

案例：找出工作岗位是MANAGER和SALESMAN的员工姓名、工作岗位

```sql
select 
  ename, job
from
  emp
where
  job = 'MANAGER' or job = 'SALESMAN';
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621910850853-c7030458-0c8f-4040-bc29-c6fa66caca7c.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_14%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621910943353-4a9fb152-67b9-4044-a2b4-b90a2fbf3f57.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_13%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

注意：这个题目描述中有这样一句话：MANAGER和SALESMAN，有的同学一看到“和”，就直接使用“and”了，因为“和”对应的英文单词是“and”，如果是这样的话，就大错特错了，因为and表示并且，使用and表示工作岗位既是MANAGER又是SALESMAN的员工，这样的员工是不存在的，因为每一个员工只有一个岗位，不可能同时从事两个岗位。所以使用and是查询不到任何结果的。如下

```sql
select 
  ename, job
from
  emp
where
  job = 'MANAGER' and job = 'SALESMAN';
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621911189669-be42f087-b388-4eb2-80b7-602766996b82.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_13%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

- [ ] 任务：查询20和30部门的员工信息。

### 4.2.6 and和or的优先级问题
---

and和or同时出现时，and优先级较高，会先执行，如果希望or先执行，这个时候需要给or条件添加小括号。另外，以后遇到不确定的优先级时，可以通过添加小括号的方式来解决。对于优先级问题没必要记忆。

案例：找出薪资小于1500，并且部门编号是20或30的员工姓名、薪资、部门编号。

先来看一下错误写法：

```sql
select
  ename,sal,deptno
from
  emp
where
  sal < 1500 and deptno = 20 or deptno = 30;
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621912213872-f2b1fe9e-384c-404e-bf24-d81bd895ae23.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

认真解读题意得知：薪资小于1500是一个大前提，要找出的是薪资小于1500的，满足这个条件的前提下，再找部门编号是20或30的，显然以上的运行结果中出现了薪资为1600的，为什么1600的会出现呢？这是因为“sal < 1500 and deptno = 20”结合在一起了，“depnto = 30”成了一个独立的条件。会导致部门编号为30的所有员工全部查询出来。我们应该让“deptno = 20 or deptno = 30”结合在一起，正确写法如下：

```sql
select
  ename,sal,deptno
from
  emp
where
  sal < 1500 and (deptno = 20 or deptno = 30);
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621912713447-a9b7aeee-4998-4eae-8e53-71353a405890.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

- [ ] 任务：找出薪资小于1500的，并且工作岗位是CLERK和SALESMAN的员工姓名、薪资、岗位。

### 4.2.7 between...and...
---

between...and...等同于 >= and <=

做区间判断的，包含左右两个边界值。

它支持数字、日期、字符串等数据类型。

between...and...在使用时一定是**<font style="color:#F5222D;">左小右大</font>**。左大右小时无法查询到数据。

between...and... 和 >= and <=只是在写法结构上有区别，执行原理和效率方面没有区别。

案例：找出薪资在1600到3000的员工姓名、薪资

```sql
select 
  ename,sal
from
  emp
where
	sal between 1600 and 3000;
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621913942714-15a74832-d5da-4215-8991-35a3d48f7061.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_11%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

采用左大右小的方式：

```sql
select 
  ename,sal
from
  emp
where
	sal between 3000 and 1600;
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621914030809-2ebf83da-aba0-429d-970e-2f6906611f11.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_10%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

没有查询到任何数据，所以在使用的时候一定要注意：**<font style="color:#F5222D;">左小右大</font>**。

- [ ] 任务：查询在1982-01-23到1987-04-19之间入职的员工

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621914250873-25bff9ba-b4e6-4145-a5f8-9036fba35627.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_22%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

注意：以上SQL语句中日期需要加上单引号。

### 4.2.8 is null、is not null
---

判断某个数据是否为null，不能使用等号，只能使用 is null

判断某个数据是否不为null，不能使用不等号，只能使用 is not null

在数据库中null不是一个值，不能用等号和不等号衡量，null代表什么也没有，没有数据，没有值

案例1：找出津贴为空的员工姓名、薪资、津贴。

```sql
select
  ename,sal,comm
from
  emp
where
  comm is null;
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621914737738-74345239-9ea8-4afa-a4bf-68fb0bb26e98.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_13%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

我们使用等号，尝试一下：

```sql
select
  ename,sal,comm
from
  emp
where
  comm = null;
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621914817611-97c0858b-a248-4a10-9fba-e5152283b553.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_11%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

查询不到任何数据，所以判断是否为空，不能用等号。

案例2：找出津贴不为空的员工姓名、薪资、津贴

```sql
select
  ename,sal,comm
from
  emp
where
  comm is not null;
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621914906515-cfd5351e-22bc-4184-b6d5-785f27049020.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_14%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

### 4.2.9 安全等于（了解）
---

<=>安全等于，用的很少，因为它的缺点是可读性差，了解即可。

<=>安全等于可作为普通运算符=，安全等于除了可以达到等号=的效果之外，还可以使用comm<=>null 代替comm is null。使用!(comm<=>null)代替comm is not null

案例1：找出薪资3000的员工姓名、岗位

```sql
select
  ename,job
from
  emp
where
  sal <=> 3000;
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621948917056-c56bb7df-9764-4991-98ea-215bf224a1c4.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_14%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

案例2：查找津贴是空的员工姓名、薪资、津贴

```sql
select
  ename, sal, comm
from
  emp
where
  comm <=> null;
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621949017900-f5dede8a-abe2-4604-b284-44908345eeec.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_10%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

案例3：查找津贴不是空的员工姓名、薪资、津贴

```sql
select
  ename, sal, comm
from
  emp
where
  !(comm <=> null);
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621949205597-28ad68b8-396d-4051-a313-0b695e918c64.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_12%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

### 4.2.10 in、not in
---

- in

job in('MANAGER','SALESMAN','CLERK') 等同于 job = 'MANAGER' or job = 'SALESMAN' or job = 'CLERK'

sal in(1600, 3000, 5000) 等同于 sal = 1600 or sal = 3000 or sal = 5000

in后面有一个小括号，小括号当中有多个值，值和值之间采用逗号隔开

sal in(1500, 5000)，需要注意的是：这个并不是说薪资在1500到5000之间，in不代表区间，表示sal是1500的和sal是5000的

案例1：找出工作岗位是MANAGER和SALESMAN的员工姓名、薪资、工作岗位

第一种：使用or

```sql
select
  ename,sal,job
from
  emp
where
  job = 'MANAGER' or job = 'SALESMAN';
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621979207586-14dece4a-ce7f-4db8-a43f-bbfee6fd6133.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_16%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

第二种：使用in

```sql
select
  ename,sal,job
from
  emp
where
  job in('MANAGER', 'SALESMAN');
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621979288013-a6975d0e-46f9-43d8-a226-6df047e6490e.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_13%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

案例2：找出薪资是1500/1600/3000的员工姓名、工作岗位

```sql
select
  ename,job
from
  emp
where
  sal in(1500, 1600, 3000);
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621979430766-b7dc80d4-568a-4216-a173-6ec7c49d1f9c.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_12%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

- [ ] 任务：找出部门编号是10和20的员工编号、姓名。（要求使用两种方案）

- not in

job not in('MANAGER','SALESMAN') 等同于 job <> 'MANAGER' and job <> 'SALESMAN'

sal not in(1600, 5000) 等同于 sal <> 1600 and sal <> 5000

案例：找出工作岗位不是MANAGER和SALESMAN的员工姓名、工作岗位

第一种：使用and

```sql
select 
  ename,job
from
  emp
where
  job <> 'MANAGER' and job <> 'SALESMAN';
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621980958567-7c01fd48-a1ec-4392-85e1-120b86865b99.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_17%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

第二种：使用not in

```sql
select 
  ename,job
from
  emp
where
  job not in('MANAGER', 'SALESMAN');
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621981036376-d6cecc7a-b7b8-4342-a83e-19ee49d77697.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

- [ ] 任务：找出薪资不是1600和3000的员工姓名、薪资。

- **<font style="color:#F5222D;">in、not in 与 NULL</font>**

先来看一下emp表中的数据

```sql
select * from emp;
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621981605595-632500b0-a2a0-401c-8995-1573468ae1f1.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_28%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

通过表中数据观察到，有4个员工的津贴不为NULL，剩下10个员工的津贴都是NULL。

写这样一条SQL语句：

```sql
select * from emp where comm in(NULL, 300);
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621981810022-80718321-ffdd-496b-af1d-620cf268c993.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_26%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

为什么以上执行结果只有一条记录呢？分析一下：

首先你要知道in的执行原理实际上是采用=和or的方式，也就是说，以上SQL语句实际上是：

```sql
select * from emp where comm = NULL or comm = 300;
```

其中NULL不能用等号=进行判断，所以comm = NULL结果是false，然而中间使用的是or，所以comm = NULL被忽略了。所以查询结果就以上一条数据。

通过以上的测试得知：**<font style="color:#F5222D;">in是自动忽略NULL的</font>**。

再写这样一条SQL语句：

```sql
select * from emp where comm not in(NULL, 300);
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1621982073198-d77677ed-77de-4086-aba9-4eaeda923a51.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_19%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

以上的执行结果奇怪了，为什么没有查到任何数据呢？我们分析一下：

首先你要知道not in的执行原理实际上是采用<>和and的方式，也就是说，以上SQL语句实际上是：

```sql
select * from emp where comm <> NULL and comm <> 300;
```

其中NULL的判断不能使用<>，所以comm <> NULL结果是false，由于后面是and，and表示并且，comm <> NULL已经是false了，所以and右边的就没必要运算了，comm <> NULL and comm <> 300的整体运算结果就是false。所以查询不到任何数据。

通过以上测试得知，**<font style="color:#F5222D;">not in是不会自动忽略NULL的</font>**，所以在使用not in的时候一定要提前过滤掉NULL。

### 4.2.11 in和or的效率比拼
---

在MySQL当中，如何统计一个SQL语句的执行时长？

- 可以使用这个命令：show profiles;  这个命令可以查看在mysql中执行的所有SQL以及命令的耗费时长。
- show profiles; 是在mysql5.0.37之后添加的。所以要确保你的mysql版本没问题。
- 如何开启时长统计功能：set profiling = 1;
- 查看时长统计功能是否开启：show variables like '%pro%';
- 查看每条SQL的耗时：show profiles;
- 查看其中某条SQL耗时明细：show profile for query query_id;
- 查看最新一条SQL的耗时明细：show profile;
- 查看cpu，io等信息：show profile block io, cpu for query query_id; 

or的效率为O(n)，而in的效率为O(logn), 当n越大的时候效率相差越明显。以下是测试过程：

第一步，创建测试表，并生成测试数据，测试数据为1000万条记录。数据库中关闭了query cache，因此数据库缓存不会对查询造成影响。具体的代码如下：

```sql
#创建测试的test表
DROP TABLE IF EXISTS test; 
CREATE TABLE test( 
    ID INT(10) NOT NULL, 
    `Name` VARCHAR(20) DEFAULT '' NOT NULL, 
    PRIMARY KEY( ID ) 
)ENGINE=INNODB DEFAULT CHARSET utf8; 

#创建生成测试数据的存储过程
DROP PROCEDURE IF EXISTS pre_test; 
DELIMITER //
CREATE PROCEDURE pre_test() 
BEGIN 
DECLARE i INT DEFAULT 0; 
SET autocommit = 0; 
WHILE i<10000000 DO 
INSERT INTO test ( ID,`Name` ) VALUES( i, CONCAT( 'Carl', i ) ); 
SET i = i+1; 
IF i%2000 = 0 THEN 
COMMIT; 
END IF; 
END WHILE; 
END; //
DELIMITER ;

#执行存储过程生成测试数据
CALL pre_test();
```

以上SQL看不懂没关系，先执行它，进行数据初始化准备工作。

第二步：分三种情况进行测试，分别是：

第1种情况：in和or所在列为主键的情形。

第2种情况：in和or所在列创建有索引的情形。

第3种情况：in和or所在列没有索引的情形。

每种情况又采用不同的in和or的数量进行测试。由于测试语句的数据量有4种情况，我这里就称为A组、B组、C组、D组，其中A组为3个值，B组为150个值，C组为300个值，D组为1000个值。具体的测试语句如下：

```sql
#A组
#in和or中有3条数据的情况
SELECT * FROM test WHERE id IN (1,23,48);
SELECT * FROM test WHERE id =1 OR id=23 OR id=48;

#B组
#in和or中有150条数据的情况
SELECT * FROM test WHERE id IN (59617932,98114476,89047409,26968186,56586105,35488201,53251989,18182139,71164231,57655852,7948544,60658339,50758185,66667117,34771253,68699137,27877290,44275282,1585444,71219424,90937482,83928635,24588528,81933207,9607562,12013895,84640278,85549596,53249244,8567444,85402877,15040223,54266509,17718135,91687882,22930500,94756430,66031097,13084573,18137443,89917778,46845456,43939093,35943480,18213703,46362815,49835919,83137546,2101409,74932951,11984477,93113331,77848222,68546065,33728734,90793684,44975642,61387237,52483391,97716233,49449060,22411182,30776331,60597240,6911731,45789095,62075344,8379933,97910423,86861971,81342386,93423963,83852896,18566482,22747687,51420625,75862064,26402882,93958561,85202979,97049369,67674725,9475653,92302381,78133617,49295001,36517340,81387142,15707241,60832834,93157830,64171432,58537826,70141767,7326025,36632075,9639624,8900056,99702164,35108945,87820933,57302965,16652391,41845132,62184393,70136913,79574630,32562398,94616790,61258220,73162018,81644480,19453596,97380163,1204733,33357040,84854495,13888863,49041868,89272326,38405345,571248,6349029,70755321,79307694,60619684,92624181,73135306,23279848,95612954,55845916,6223606,43836918,37459781,67969314,99398872,7616960,37189193,50151920,62881879,12364637,33204320,27135672,28441504,47373461,87967926,30631796,20053540,18735984,83406724);
SELECT * FROM test WHERE id=59617932 OR id=98114476 OR id=89047409 OR id=26968186 OR id=56586105 OR id=35488201 OR id=53251989 OR id=18182139 OR id=71164231 OR id=57655852 OR id=7948544 OR id=60658339 OR id=50758185 OR id=66667117 OR id=34771253 OR id=68699137 OR id=27877290 OR id=44275282 OR id=1585444 OR id=71219424 OR id=90937482 OR id=83928635 OR id=24588528 OR id=81933207 OR id=9607562 OR id=12013895 OR id=84640278 OR id=85549596 OR id=53249244 OR id=8567444 OR id=85402877 OR id=15040223 OR id=54266509 OR id=17718135 OR id=91687882 OR id=22930500 OR id=94756430 OR id=66031097 OR id=13084573 OR id=18137443 OR id=89917778 OR id=46845456 OR id=43939093 OR id=35943480 OR id=18213703 OR id=46362815 OR id=49835919 OR id=83137546 OR id=2101409 OR id=74932951 OR id=11984477 OR id=93113331 OR id=77848222 OR id=68546065 OR id=33728734 OR id=90793684 OR id=44975642 OR id=61387237 OR id=52483391 OR id=97716233 OR id=49449060 OR id=22411182 OR id=30776331 OR id=60597240 OR id=6911731 OR id=45789095 OR id=62075344 OR id=8379933 OR id=97910423 OR id=86861971 OR id=81342386 OR id=93423963 OR id=83852896 OR id=18566482 OR id=22747687 OR id=51420625 OR id=75862064 OR id=26402882 OR id=93958561 OR id=85202979 OR id=97049369 OR id=67674725 OR id=9475653 OR id=92302381 OR id=78133617 OR id=49295001 OR id=36517340 OR id=81387142 OR id=15707241 OR id=60832834 OR id=93157830 OR id=64171432 OR id=58537826 OR id=70141767 OR id=7326025 OR id=36632075 OR id=9639624 OR id=8900056 OR id=99702164 OR id=35108945 OR id=87820933 OR id=57302965 OR id=16652391 OR id=41845132 OR id=62184393 OR id=70136913 OR id=79574630 OR id=32562398 OR id=94616790 OR id=61258220 OR id=73162018 OR id=81644480 OR id=19453596 OR id=97380163 OR id=1204733 OR id=33357040 OR id=84854495 OR id=13888863 OR id=49041868 OR id=89272326 OR id=38405345 OR id=571248 OR id=6349029 OR id=70755321 OR id=79307694 OR id=60619684 OR id=92624181 OR id=73135306 OR id=23279848 OR id=95612954 OR id=55845916 OR id=6223606 OR id=43836918 OR id=37459781 OR id=67969314 OR id=99398872 OR id=7616960 OR id=37189193 OR id=50151920 OR id=62881879 OR id=12364637 OR id=33204320 OR id=27135672 OR id=28441504 OR id=47373461 OR id=87967926 OR id=30631796 OR id=20053540 OR id=18735984 OR id=83406724;

#C组
#in和or中有300条数据的情况
SELECT * FROM test WHERE id IN (37092877,94859722,74276090,8763830,38727241,95732954,93414819,55070016,3591352,73857925,92290525,15210159,83905516,54934589,83004136,31442143,6060569,22209206,27649629,11464943,77822402,28714780,10058522,62252663,13751461,38997875,47320577,64507359,36137908,54297630,97411161,56542672,22017966,55190708,70072386,24300664,93413617,23621629,74772508,62774612,43001947,46161388,85563006,70177147,63960440,18001207,81734850,10635060,6551152,54877885,44426798,73950635,18713144,21690065,82153543,26048520,79954773,22411093,97307339,74193176,1413532,88006544,36062746,24043946,17132007,95958217,26112542,27303972,17247403,56778979,60928031,69369613,90584759,86234538,41726089,25315005,27568726,25091624,15307765,83130887,42726438,75872353,18991223,47819224,75457713,54659391,54889687,65229322,17124556,38376043,1989975,45973571,48597804,58632319,43388664,97010450,94745635,13217373,40472912,40220510,58319808,48228318,48936085,86281500,65466706,96815281,11751559,50188155,76649755,35315411,20360954,17739218,10918461,51429591,41447650,65170472,26810295,80912347,17157209,75851858,61150903,4408208,61200404,6655467,66863737,51549112,61951371,14368308,14663119,8762531,31765056,30560647,41048147,95526521,94929131,56881239,79014587,62705983,15892901,66151473,98846144,79336731,35949035,26250054,97536202,40575682,6965144,91059908,97939380,30854180,1965937,17193347,76584991,70467475,6559872,97386594,13939914,20379091,84906436,45989448,17337270,4949675,96963499,12561575,77153018,73213368,68283041,33977574,86290771,70381017,73095085,454900,44614195,48171334,49603342,7430998,29447060,47643508,82393912,83169846,94256496,35275444,40024984,25377535,46571333,32510994,70927802,92017916,97302502,22859741,32726786,79071601,93977472,47409421,49311618,77366144,84838598,59401507,67110877,42075938,76962007,27984930,72982484,81363683,75017478,88624177,67220235,88290070,26311443,87681081,77960250,4996033,68448074,67762279,99650583,36766422,27233152,71436659,25428777,81481679,51070397,88351803,78755075,26783938,83610840,45650662,86305644,1717314,66176062,6507047,45084786,74402982,55661367,35721238,40424913,24294239,30223531,55367671,56777532,12604154,4870493,14750488,74039611,42549918,70710424,56247316,63002053,71117605,16510883,67417211,34057637,74185092,58603491,66987830,73584171,9178319,47096502,1554825,37756804,85168245,92690138,6120773,99586029,74696745,61803307,56631845,42681796,58965644,68703695,69660559,15879062,26713059,85186928,63117471,53007808,74576547,32187857,13701205,88645881,24507258,87453800,39624977,75862710,62419627,70804059,10461373,18265782,56366177,68093007,75760763,43931574,65808002,49148775,98019987,71183123,53762434,78851856,37767085,89124453,47566746);

SELECT * FROM test WHERE id=37092877 OR id=94859722 OR id=74276090 OR id=8763830 OR id=38727241 OR id=95732954 OR id=93414819 OR id=55070016 OR id=3591352 OR id=73857925 OR id=92290525 OR id=15210159 OR id=83905516 OR id=54934589 OR id=83004136 OR id=31442143 OR id=6060569 OR id=22209206 OR id=27649629 OR id=11464943 OR id=77822402 OR id=28714780 OR id=10058522 OR id=62252663 OR id=13751461 OR id=38997875 OR id=47320577 OR id=64507359 OR id=36137908 OR id=54297630 OR id=97411161 OR id=56542672 OR id=22017966 OR id=55190708 OR id=70072386 OR id=24300664 OR id=93413617 OR id=23621629 OR id=74772508 OR id=62774612 OR id=43001947 OR id=46161388 OR id=85563006 OR id=70177147 OR id=63960440 OR id=18001207 OR id=81734850 OR id=10635060 OR id=6551152 OR id=54877885 OR id=44426798 OR id=73950635 OR id=18713144 OR id=21690065 OR id=82153543 OR id=26048520 OR id=79954773 OR id=22411093 OR id=97307339 OR id=74193176 OR id=1413532 OR id=88006544 OR id=36062746 OR id=24043946 OR id=17132007 OR id=95958217 OR id=26112542 OR id=27303972 OR id=17247403 OR id=56778979 OR id=60928031 OR id=69369613 OR id=90584759 OR id=86234538 OR id=41726089 OR id=25315005 OR id=27568726 OR id=25091624 OR id=15307765 OR id=83130887 OR id=42726438 OR id=75872353 OR id=18991223 OR id=47819224 OR id=75457713 OR id=54659391 OR id=54889687 OR id=65229322 OR id=17124556 OR id=38376043 OR id=1989975 OR id=45973571 OR id=48597804 OR id=58632319 OR id=43388664 OR id=97010450 OR id=94745635 OR id=13217373 OR id=40472912 OR id=40220510 OR id=58319808 OR id=48228318 OR id=48936085 OR id=86281500 OR id=65466706 OR id=96815281 OR id=11751559 OR id=50188155 OR id=76649755 OR id=35315411 OR id=20360954 OR id=17739218 OR id=10918461 OR id=51429591 OR id=41447650 OR id=65170472 OR id=26810295 OR id=80912347 OR id=17157209 OR id=75851858 OR id=61150903 OR id=4408208 OR id=61200404 OR id=6655467 OR id=66863737 OR id=51549112 OR id=61951371 OR id=14368308 OR id=14663119 OR id=8762531 OR id=31765056 OR id=30560647 OR id=41048147 OR id=95526521 OR id=94929131 OR id=56881239 OR id=79014587 OR id=62705983 OR id=15892901 OR id=66151473 OR id=98846144 OR id=79336731 OR id=35949035 OR id=26250054 OR id=97536202 OR id=40575682 OR id=6965144 OR id=91059908 OR id=97939380 OR id=30854180 OR id=1965937 OR id=17193347 OR id=76584991 OR id=70467475 OR id=6559872 OR id=97386594 OR id=13939914 OR id=20379091 OR id=84906436 OR id=45989448 OR id=17337270 OR id=4949675 OR id=96963499 OR id=12561575 OR id=77153018 OR id=73213368 OR id=68283041 OR id=33977574 OR id=86290771 OR id=70381017 OR id=73095085 OR id=454900 OR id=44614195 OR id=48171334 OR id=49603342 OR id=7430998 OR id=29447060 OR id=47643508 OR id=82393912 OR id=83169846 OR id=94256496 OR id=35275444 OR id=40024984 OR id=25377535 OR id=46571333 OR id=32510994 OR id=70927802 OR id=92017916 OR id=97302502 OR id=22859741 OR id=32726786 OR id=79071601 OR id=93977472 OR id=47409421 OR id=49311618 OR id=77366144 OR id=84838598 OR id=59401507 OR id=67110877 OR id=42075938 OR id=76962007 OR id=27984930 OR id=72982484 OR id=81363683 OR id=75017478 OR id=88624177 OR id=67220235 OR id=88290070 OR id=26311443 OR id=87681081 OR id=77960250 OR id=4996033 OR id=68448074 OR id=67762279 OR id=99650583 OR id=36766422 OR id=27233152 OR id=71436659 OR id=25428777 OR id=81481679 OR id=51070397 OR id=88351803 OR id=78755075 OR id=26783938 OR id=83610840 OR id=45650662 OR id=86305644 OR id=1717314 OR id=66176062 OR id=6507047 OR id=45084786 OR id=74402982 OR id=55661367 OR id=35721238 OR id=40424913 OR id=24294239 OR id=30223531 OR id=55367671 OR id=56777532 OR id=12604154 OR id=4870493 OR id=14750488 OR id=74039611 OR id=42549918 OR id=70710424 OR id=56247316 OR id=63002053 OR id=71117605 OR id=16510883 OR id=67417211 OR id=34057637 OR id=74185092 OR id=58603491 OR id=66987830 OR id=73584171 OR id=9178319 OR id=47096502 OR id=1554825 OR id=37756804 OR id=85168245 OR id=92690138 OR id=6120773 OR id=99586029 OR id=74696745 OR id=61803307 OR id=56631845 OR id=42681796 OR id=58965644 OR id=68703695 OR id=69660559 OR id=15879062 OR id=26713059 OR id=85186928 OR id=63117471 OR id=53007808 OR id=74576547 OR id=32187857 OR id=13701205 OR id=88645881 OR id=24507258 OR id=87453800 OR id=39624977 OR id=75862710 OR id=62419627 OR id=70804059 OR id=10461373 OR id=18265782 OR id=56366177 OR id=68093007 OR id=75760763 OR id=43931574 OR id=65808002 OR id=49148775 OR id=98019987 OR id=71183123 OR id=53762434 OR id=78851856 OR id=37767085 OR id=89124453 OR id=47566746;

#D组
#in和or中有1000条数据的情况
SELECT * FROM test WHERE id IN (93674701,9720356,31732184,53855095,33144472,71864888,27541768,27238726,83648428,12942332,26918445,19781953,81861032,74800064,12286132,6624397,64942581,70512799,46356598,88292448,87069909,38175756,98121997,62570414,15900806,51527968,89092372,8084203,53772848,78871524,3608561,85909562,41702172,61800503,57877634,93407278,30824340,13159046,49055339,73058078,983603,73571456,51694978,75136628,82716874,83551181,7964224,47505945,92695321,15885152,79282709,18572099,27392970,14552787,19848227,4518183,11773920,22285326,71605145,2402625,63365854,70973600,10584706,83688869,84268419,6026005,36545233,24462648,19293921,17561083,52105483,59243514,35230465,34650779,30053489,24225251,59642405,81933853,94495716,26364324,25980634,5579237,14569289,89417845,71178959,4143920,20467990,53316808,21288525,82249537,37737589,44712689,36788133,15668654,4697556,63785060,11555169,36401204,92276179,4135929,75453019,28231031,8649240,11576980,20262028,56242424,11305608,5655216,90240601,28569373,5296027,10739594,72751648,22531251,12535926,36347415,19740655,69125465,7523885,88128548,88830806,25010302,29411467,99614288,32646290,16592563,69036910,32604729,88737786,90169676,57646877,72105460,40027541,70362483,37221415,25284914,69691185,17972978,1544661,47324366,25337670,91133621,63697117,48652228,18538437,79966496,26066529,65334307,8305141,86289387,20178085,88836090,74948034,14101728,7837868,83548120,65602502,83129211,24785681,65000269,49140174,62636621,31096695,52276400,28546681,83631937,57100225,42531528,28326396,38641032,93055463,20525612,66073509,35154065,29007664,12600294,76829494,73917074,67226149,12478806,39842542,70312958,82792046,49668650,46280815,96555182,22966062,83158116,87566530,66277804,7944142,90649884,64342810,9881875,14833854,82959569,50523207,48788762,3801076,14677723,63080506,96215352,36302231,35067168,11695282,19447382,66401373,40822285,41406321,48630216,78955925,57194625,52097877,16169037,44834346,2593695,29948466,41842778,50510473,39669493,64590865,26160800,94882286,2703212,41243905,89363549,82819429,25565895,86836890,58385785,55898457,99305620,43332680,98223672,4494624,25408421,28054121,48197701,90633404,25825550,90631154,24867226,61846156,38911183,67826056,10676975,57116645,474292,82387517,56211477,46555785,49282428,99468990,81172472,26720330,38692582,96073680,88412290,28829489,1816508,75321051,81650509,23175973,42008725,60743468,52532114,731909,77811415,86804961,29675484,33584929,180367,93687804,41093066,5987495,27291494,78229979,63194139,34357776,9992084,22643334,22407822,69740170,29581361,50036776,88768091,82537322,83709895,55361776,90616169,44595355,9468440,54552233,73496954,46104486,92947715,38522993,88515232,57725249,48507967,25309486,91597013,85635814,69579638,68775627,57556546,77900275,95965693,9601780,5448068,54075952,64335883,80114875,14793294,21016639,1959922,93176996,7893733,51407895,45849129,33857790,30096194,78021982,66555961,15842998,77678123,56648395,8171848,80152264,78616680,80098122,22882409,77242219,3124519,60865422,43164198,43256621,73261157,12541949,49780175,23167183,10509251,41809106,25655902,6752559,39850293,50992519,40061483,84526968,93056718,53267125,53914467,39404926,83672449,21484465,34147538,13437853,74079093,50400032,85705998,7557614,10300505,79264856,65669946,23899714,53506926,36081544,11113765,65755643,5826515,60392667,55562374,98132987,80904530,92663352,7283593,3709276,52078745,84847057,34235334,63889320,70036669,58603533,27394053,54766781,50920854,80202681,67618417,82912294,20150728,20042189,86403320,38738266,58393070,50887299,12170654,16212895,37361223,13677457,19503506,20213757,84240441,39618969,26401150,47937678,55871130,79189571,5717133,12444503,95283334,14827147,22008485,56345882,43237192,56980197,68699371,46407250,72120555,70694039,46438829,17774982,36484024,138767,89563532,54847019,7815592,44909604,50479084,17462504,96594465,58317102,92426225,91894699,4501659,43315607,9442814,19705166,87751308,95588126,92372510,20281564,19251355,10321183,34573093,19074704,84678191,24383998,27670253,50223562,34091936,99304371,32477827,54273037,86525073,73253547,33316827,6724062,76707318,78171148,44729510,16697684,68966388,57448392,51380186,35344477,98153122,51825492,27202774,26901641,37527637,88241695,15100257,30418000,21821200,95511035,9289513,83870196,54628801,39402988,88345504,84232433,13925255,70816934,6822742,14400466,430652,87397095,89773413,10883914,89939310,39597573,49356789,62857680,93292662,55644642,81922551,94304087,63705961,137763,22392805,65195561,39498904,22576234,59467794,46389072,66341462,44602153,18204976,45366397,3880945,98231882,27999162,38209350,10599910,77139550,35114264,57109708,93064441,34801782,24938667,84955486,53018874,37969943,64372852,69596670,21288762,12774121,97588451,23575359,10954061,50363988,56263940,61520763,85096643,36250068,19807406,20984386,24520668,44631794,62587890,44963362,7663521,78505677,98442373,90280978,14494324,16069861,11397153,87726305,26133866,42024935,93393929,72575268,76384597,42272046,81658814,40811718,86054463,35997739,51075676,62839927,68179261,19292480,10464999,6342696,75842285,28671096,30029838,19617648,94667632,75855376,83477767,456684,81197213,1961395,79590898,470693,64786459,90138714,30486571,75566704,64467558,21380112,17742907,7733647,92017,64615799,72272722,66873854,77198963,35594848,42694993,12431322,2247181,11020746,42416726,19127785,95444937,36842133,4203521,48149533,45322440,59710953,38250773,31370132,26889920,45927952,55298246,31197238,44744953,35531670,38850041,29759177,76433451,33696500,2823716,68574340,68889919,35744793,64772909,41562277,72606631,54617176,76086087,61060196,1593669,4666059,44201567,97015910,51039786,47534369,36899420,95163693,34278055,24361819,93200909,29991418,63172824,53644148,61454424,44726508,64910883,31088636,14005026,83267869,28497493,12406441,34686539,70646963,7687253,23115957,64556990,49701688,76843379,22370877,11199132,15492661,72101877,47154152,54969058,96696025,33567129,95788960,13301506,38695877,52992551,37817234,82136809,28111091,84977065,93404791,56350318,27576451,84170153,37381626,22432144,35119973,23922989,98961080,14336913,49612713,47410677,41559348,64216475,75502736,16203656,81726720,64541981,82181762,95869963,1086041,76856852,99484886,47292021,99746735,79082859,67416188,46391963,58631281,80994168,9464550,5851058,16534935,63307701,91875109,18716507,15870646,6003995,836024,35610568,39574140,76244639,83403189,51252728,6516065,94907007,81605606,40398075,40258386,6692981,50852074,2869416,97682971,44427361,9608914,58464559,81806036,20047387,66264452,58063775,54179837,48463792,17877188,31718426,64192249,35574859,3671766,88905164,78137697,46929619,21063327,83078770,93293821,41618319,3832324,91310612,79854291,68734227,8826717,80881657,95208907,7079422,30037415,5494004,44809486,97620027,35689182,13120783,26108678,1537176,16538727,50841024,36515680,82635278,11112660,16276555,72997511,93487848,88201238,53997085,15198916,61214583,78412499,3585265,1402827,56445518,47661453,25615629,58263458,62155263,46608555,15822703,82285214,76021596,84571697,45999350,40074628,8219220,5429523,74024203,22354037,17605466,60436920,52777032,65801717,43656316,10424270,48035786,29493228,83897372,62101275,84793857,56894828,70636689,72497148,67388694,68146510,64298548,97117498,25553211,54226533,90395845,24172623,91712292,98280822,54042497,25032894,6833135,39011254,9837753,63507766,26747954,45941264,99955245,80051546,78510759,71322333,92407609,95809491,18999217,23430377,11861293,42583098,24163209,11358738,3237302,3176665,87151132,2789150,63905882,59864282,3673596,19570439,22883042,72375525,51614404,47526636,98443133,99140135,33855918,28333489,81416033,2670097,4897577,24439616,36643479,40817600,76022791,40072872,95193435,96967607,24983145,49883271,94602753,83555050,85455145,34563229,72328311,12002151,71481181,72998351,1489188,38426973,91893116,61594591,89693630,6268166,20056665,62169880,17143472,35103925,22452590,54272289,34236829,78028543,84474414,40386926,50550952,49413559,48781941,22927237,44447815,29960478,47578119,10192558,87733936,88699383,38808712,79944807,84014713,31865463,72617685,19557568,47865990,39069638,20086122,1777562,29018078,78358083,94561719,46281152,99789008,86929490,16534451,55989144,52455669,54561585,97379646,20416183,87617750,76115505,3282482,8383619,45456319,29576432,67750627,61736333,33745442,51502165,35349384,78106651,23232822,94851387,78254073,82406754,10317954,70125940,45067526,27061875,25640164,52574899,93819227,93789607,96122951,31673246,70431904,54067896,37146857,37817889,14058940,60710246,64844350,91604383,71972005,13888349,19093493,27397281,61085409,66529387,82761299,72236310,19277077,96599501,68304096,48292937,97503321,88011133,29224803,79782945,79965966,83716914,90432214,48938902,12498489,30246261,91624049,68652396,23677785,44084687,3865123,37823170,45287730,38784682,28058351,68226368,61569897,44737876,70575908,25568463,24668386,88650569,35559584,1897737,77844785,29780669,84004602,29029776,91003545,48058106,9463847);

SELECT * FROM test WHERE id=93674701 OR id=9720356 OR id=31732184 OR id=53855095 OR id=33144472 OR id=71864888 OR id=27541768 OR id=27238726 OR id=83648428 OR id=12942332 OR id=26918445 OR id=19781953 OR id=81861032 OR id=74800064 OR id=12286132 OR id=6624397 OR id=64942581 OR id=70512799 OR id=46356598 OR id=88292448 OR id=87069909 OR id=38175756 OR id=98121997 OR id=62570414 OR id=15900806 OR id=51527968 OR id=89092372 OR id=8084203 OR id=53772848 OR id=78871524 OR id=3608561 OR id=85909562 OR id=41702172 OR id=61800503 OR id=57877634 OR id=93407278 OR id=30824340 OR id=13159046 OR id=49055339 OR id=73058078 OR id=983603 OR id=73571456 OR id=51694978 OR id=75136628 OR id=82716874 OR id=83551181 OR id=7964224 OR id=47505945 OR id=92695321 OR id=15885152 OR id=79282709 OR id=18572099 OR id=27392970 OR id=14552787 OR id=19848227 OR id=4518183 OR id=11773920 OR id=22285326 OR id=71605145 OR id=2402625 OR id=63365854 OR id=70973600 OR id=10584706 OR id=83688869 OR id=84268419 OR id=6026005 OR id=36545233 OR id=24462648 OR id=19293921 OR id=17561083 OR id=52105483 OR id=59243514 OR id=35230465 OR id=34650779 OR id=30053489 OR id=24225251 OR id=59642405 OR id=81933853 OR id=94495716 OR id=26364324 OR id=25980634 OR id=5579237 OR id=14569289 OR id=89417845 OR id=71178959 OR id=4143920 OR id=20467990 OR id=53316808 OR id=21288525 OR id=82249537 OR id=37737589 OR id=44712689 OR id=36788133 OR id=15668654 OR id=4697556 OR id=63785060 OR id=11555169 OR id=36401204 OR id=92276179 OR id=4135929 OR id=75453019 OR id=28231031 OR id=8649240 OR id=11576980 OR id=20262028 OR id=56242424 OR id=11305608 OR id=5655216 OR id=90240601 OR id=28569373 OR id=5296027 OR id=10739594 OR id=72751648 OR id=22531251 OR id=12535926 OR id=36347415 OR id=19740655 OR id=69125465 OR id=7523885 OR id=88128548 OR id=88830806 OR id=25010302 OR id=29411467 OR id=99614288 OR id=32646290 OR id=16592563 OR id=69036910 OR id=32604729 OR id=88737786 OR id=90169676 OR id=57646877 OR id=72105460 OR id=40027541 OR id=70362483 OR id=37221415 OR id=25284914 OR id=69691185 OR id=17972978 OR id=1544661 OR id=47324366 OR id=25337670 OR id=91133621 OR id=63697117 OR id=48652228 OR id=18538437 OR id=79966496 OR id=26066529 OR id=65334307 OR id=8305141 OR id=86289387 OR id=20178085 OR id=88836090 OR id=74948034 OR id=14101728 OR id=7837868 OR id=83548120 OR id=65602502 OR id=83129211 OR id=24785681 OR id=65000269 OR id=49140174 OR id=62636621 OR id=31096695 OR id=52276400 OR id=28546681 OR id=83631937 OR id=57100225 OR id=42531528 OR id=28326396 OR id=38641032 OR id=93055463 OR id=20525612 OR id=66073509 OR id=35154065 OR id=29007664 OR id=12600294 OR id=76829494 OR id=73917074 OR id=67226149 OR id=12478806 OR id=39842542 OR id=70312958 OR id=82792046 OR id=49668650 OR id=46280815 OR id=96555182 OR id=22966062 OR id=83158116 OR id=87566530 OR id=66277804 OR id=7944142 OR id=90649884 OR id=64342810 OR id=9881875 OR id=14833854 OR id=82959569 OR id=50523207 OR id=48788762 OR id=3801076 OR id=14677723 OR id=63080506 OR id=96215352 OR id=36302231 OR id=35067168 OR id=11695282 OR id=19447382 OR id=66401373 OR id=40822285 OR id=41406321 OR id=48630216 OR id=78955925 OR id=57194625 OR id=52097877 OR id=16169037 OR id=44834346 OR id=2593695 OR id=29948466 OR id=41842778 OR id=50510473 OR id=39669493 OR id=64590865 OR id=26160800 OR id=94882286 OR id=2703212 OR id=41243905 OR id=89363549 OR id=82819429 OR id=25565895 OR id=86836890 OR id=58385785 OR id=55898457 OR id=99305620 OR id=43332680 OR id=98223672 OR id=4494624 OR id=25408421 OR id=28054121 OR id=48197701 OR id=90633404 OR id=25825550 OR id=90631154 OR id=24867226 OR id=61846156 OR id=38911183 OR id=67826056 OR id=10676975 OR id=57116645 OR id=474292 OR id=82387517 OR id=56211477 OR id=46555785 OR id=49282428 OR id=99468990 OR id=81172472 OR id=26720330 OR id=38692582 OR id=96073680 OR id=88412290 OR id=28829489 OR id=1816508 OR id=75321051 OR id=81650509 OR id=23175973 OR id=42008725 OR id=60743468 OR id=52532114 OR id=731909 OR id=77811415 OR id=86804961 OR id=29675484 OR id=33584929 OR id=180367 OR id=93687804 OR id=41093066 OR id=5987495 OR id=27291494 OR id=78229979 OR id=63194139 OR id=34357776 OR id=9992084 OR id=22643334 OR id=22407822 OR id=69740170 OR id=29581361 OR id=50036776 OR id=88768091 OR id=82537322 OR id=83709895 OR id=55361776 OR id=90616169 OR id=44595355 OR id=9468440 OR id=54552233 OR id=73496954 OR id=46104486 OR id=92947715 OR id=38522993 OR id=88515232 OR id=57725249 OR id=48507967 OR id=25309486 OR id=91597013 OR id=85635814 OR id=69579638 OR id=68775627 OR id=57556546 OR id=77900275 OR id=95965693 OR id=9601780 OR id=5448068 OR id=54075952 OR id=64335883 OR id=80114875 OR id=14793294 OR id=21016639 OR id=1959922 OR id=93176996 OR id=7893733 OR id=51407895 OR id=45849129 OR id=33857790 OR id=30096194 OR id=78021982 OR id=66555961 OR id=15842998 OR id=77678123 OR id=56648395 OR id=8171848 OR id=80152264 OR id=78616680 OR id=80098122 OR id=22882409 OR id=77242219 OR id=3124519 OR id=60865422 OR id=43164198 OR id=43256621 OR id=73261157 OR id=12541949 OR id=49780175 OR id=23167183 OR id=10509251 OR id=41809106 OR id=25655902 OR id=6752559 OR id=39850293 OR id=50992519 OR id=40061483 OR id=84526968 OR id=93056718 OR id=53267125 OR id=53914467 OR id=39404926 OR id=83672449 OR id=21484465 OR id=34147538 OR id=13437853 OR id=74079093 OR id=50400032 OR id=85705998 OR id=7557614 OR id=10300505 OR id=79264856 OR id=65669946 OR id=23899714 OR id=53506926 OR id=36081544 OR id=11113765 OR id=65755643 OR id=5826515 OR id=60392667 OR id=55562374 OR id=98132987 OR id=80904530 OR id=92663352 OR id=7283593 OR id=3709276 OR id=52078745 OR id=84847057 OR id=34235334 OR id=63889320 OR id=70036669 OR id=58603533 OR id=27394053 OR id=54766781 OR id=50920854 OR id=80202681 OR id=67618417 OR id=82912294 OR id=20150728 OR id=20042189 OR id=86403320 OR id=38738266 OR id=58393070 OR id=50887299 OR id=12170654 OR id=16212895 OR id=37361223 OR id=13677457 OR id=19503506 OR id=20213757 OR id=84240441 OR id=39618969 OR id=26401150 OR id=47937678 OR id=55871130 OR id=79189571 OR id=5717133 OR id=12444503 OR id=95283334 OR id=14827147 OR id=22008485 OR id=56345882 OR id=43237192 OR id=56980197 OR id=68699371 OR id=46407250 OR id=72120555 OR id=70694039 OR id=46438829 OR id=17774982 OR id=36484024 OR id=138767 OR id=89563532 OR id=54847019 OR id=7815592 OR id=44909604 OR id=50479084 OR id=17462504 OR id=96594465 OR id=58317102 OR id=92426225 OR id=91894699 OR id=4501659 OR id=43315607 OR id=9442814 OR id=19705166 OR id=87751308 OR id=95588126 OR id=92372510 OR id=20281564 OR id=19251355 OR id=10321183 OR id=34573093 OR id=19074704 OR id=84678191 OR id=24383998 OR id=27670253 OR id=50223562 OR id=34091936 OR id=99304371 OR id=32477827 OR id=54273037 OR id=86525073 OR id=73253547 OR id=33316827 OR id=6724062 OR id=76707318 OR id=78171148 OR id=44729510 OR id=16697684 OR id=68966388 OR id=57448392 OR id=51380186 OR id=35344477 OR id=98153122 OR id=51825492 OR id=27202774 OR id=26901641 OR id=37527637 OR id=88241695 OR id=15100257 OR id=30418000 OR id=21821200 OR id=95511035 OR id=9289513 OR id=83870196 OR id=54628801 OR id=39402988 OR id=88345504 OR id=84232433 OR id=13925255 OR id=70816934 OR id=6822742 OR id=14400466 OR id=430652 OR id=87397095 OR id=89773413 OR id=10883914 OR id=89939310 OR id=39597573 OR id=49356789 OR id=62857680 OR id=93292662 OR id=55644642 OR id=81922551 OR id=94304087 OR id=63705961 OR id=137763 OR id=22392805 OR id=65195561 OR id=39498904 OR id=22576234 OR id=59467794 OR id=46389072 OR id=66341462 OR id=44602153 OR id=18204976 OR id=45366397 OR id=3880945 OR id=98231882 OR id=27999162 OR id=38209350 OR id=10599910 OR id=77139550 OR id=35114264 OR id=57109708 OR id=93064441 OR id=34801782 OR id=24938667 OR id=84955486 OR id=53018874 OR id=37969943 OR id=64372852 OR id=69596670 OR id=21288762 OR id=12774121 OR id=97588451 OR id=23575359 OR id=10954061 OR id=50363988 OR id=56263940 OR id=61520763 OR id=85096643 OR id=36250068 OR id=19807406 OR id=20984386 OR id=24520668 OR id=44631794 OR id=62587890 OR id=44963362 OR id=7663521 OR id=78505677 OR id=98442373 OR id=90280978 OR id=14494324 OR id=16069861 OR id=11397153 OR id=87726305 OR id=26133866 OR id=42024935 OR id=93393929 OR id=72575268 OR id=76384597 OR id=42272046 OR id=81658814 OR id=40811718 OR id=86054463 OR id=35997739 OR id=51075676 OR id=62839927 OR id=68179261 OR id=19292480 OR id=10464999 OR id=6342696 OR id=75842285 OR id=28671096 OR id=30029838 OR id=19617648 OR id=94667632 OR id=75855376 OR id=83477767 OR id=456684 OR id=81197213 OR id=1961395 OR id=79590898 OR id=470693 OR id=64786459 OR id=90138714 OR id=30486571 OR id=75566704 OR id=64467558 OR id=21380112 OR id=17742907 OR id=7733647 OR id=92017 OR id=64615799 OR id=72272722 OR id=66873854 OR id=77198963 OR id=35594848 OR id=42694993 OR id=12431322 OR id=2247181 OR id=11020746 OR id=42416726 OR id=19127785 OR id=95444937 OR id=36842133 OR id=4203521 OR id=48149533 OR id=45322440 OR id=59710953 OR id=38250773 OR id=31370132 OR id=26889920 OR id=45927952 OR id=55298246 OR id=31197238 OR id=44744953 OR id=35531670 OR id=38850041 OR id=29759177 OR id=76433451 OR id=33696500 OR id=2823716 OR id=68574340 OR id=68889919 OR id=35744793 OR id=64772909 OR id=41562277 OR id=72606631 OR id=54617176 OR id=76086087 OR id=61060196 OR id=1593669 OR id=4666059 OR id=44201567 OR id=97015910 OR id=51039786 OR id=47534369 OR id=36899420 OR id=95163693 OR id=34278055 OR id=24361819 OR id=93200909 OR id=29991418 OR id=63172824 OR id=53644148 OR id=61454424 OR id=44726508 OR id=64910883 OR id=31088636 OR id=14005026 OR id=83267869 OR id=28497493 OR id=12406441 OR id=34686539 OR id=70646963 OR id=7687253 OR id=23115957 OR id=64556990 OR id=49701688 OR id=76843379 OR id=22370877 OR id=11199132 OR id=15492661 OR id=72101877 OR id=47154152 OR id=54969058 OR id=96696025 OR id=33567129 OR id=95788960 OR id=13301506 OR id=38695877 OR id=52992551 OR id=37817234 OR id=82136809 OR id=28111091 OR id=84977065 OR id=93404791 OR id=56350318 OR id=27576451 OR id=84170153 OR id=37381626 OR id=22432144 OR id=35119973 OR id=23922989 OR id=98961080 OR id=14336913 OR id=49612713 OR id=47410677 OR id=41559348 OR id=64216475 OR id=75502736 OR id=16203656 OR id=81726720 OR id=64541981 OR id=82181762 OR id=95869963 OR id=1086041 OR id=76856852 OR id=99484886 OR id=47292021 OR id=99746735 OR id=79082859 OR id=67416188 OR id=46391963 OR id=58631281 OR id=80994168 OR id=9464550 OR id=5851058 OR id=16534935 OR id=63307701 OR id=91875109 OR id=18716507 OR id=15870646 OR id=6003995 OR id=836024 OR id=35610568 OR id=39574140 OR id=76244639 OR id=83403189 OR id=51252728 OR id=6516065 OR id=94907007 OR id=81605606 OR id=40398075 OR id=40258386 OR id=6692981 OR id=50852074 OR id=2869416 OR id=97682971 OR id=44427361 OR id=9608914 OR id=58464559 OR id=81806036 OR id=20047387 OR id=66264452 OR id=58063775 OR id=54179837 OR id=48463792 OR id=17877188 OR id=31718426 OR id=64192249 OR id=35574859 OR id=3671766 OR id=88905164 OR id=78137697 OR id=46929619 OR id=21063327 OR id=83078770 OR id=93293821 OR id=41618319 OR id=3832324 OR id=91310612 OR id=79854291 OR id=68734227 OR id=8826717 OR id=80881657 OR id=95208907 OR id=7079422 OR id=30037415 OR id=5494004 OR id=44809486 OR id=97620027 OR id=35689182 OR id=13120783 OR id=26108678 OR id=1537176 OR id=16538727 OR id=50841024 OR id=36515680 OR id=82635278 OR id=11112660 OR id=16276555 OR id=72997511 OR id=93487848 OR id=88201238 OR id=53997085 OR id=15198916 OR id=61214583 OR id=78412499 OR id=3585265 OR id=1402827 OR id=56445518 OR id=47661453 OR id=25615629 OR id=58263458 OR id=62155263 OR id=46608555 OR id=15822703 OR id=82285214 OR id=76021596 OR id=84571697 OR id=45999350 OR id=40074628 OR id=8219220 OR id=5429523 OR id=74024203 OR id=22354037 OR id=17605466 OR id=60436920 OR id=52777032 OR id=65801717 OR id=43656316 OR id=10424270 OR id=48035786 OR id=29493228 OR id=83897372 OR id=62101275 OR id=84793857 OR id=56894828 OR id=70636689 OR id=72497148 OR id=67388694 OR id=68146510 OR id=64298548 OR id=97117498 OR id=25553211 OR id=54226533 OR id=90395845 OR id=24172623 OR id=91712292 OR id=98280822 OR id=54042497 OR id=25032894 OR id=6833135 OR id=39011254 OR id=9837753 OR id=63507766 OR id=26747954 OR id=45941264 OR id=99955245 OR id=80051546 OR id=78510759 OR id=71322333 OR id=92407609 OR id=95809491 OR id=18999217 OR id=23430377 OR id=11861293 OR id=42583098 OR id=24163209 OR id=11358738 OR id=3237302 OR id=3176665 OR id=87151132 OR id=2789150 OR id=63905882 OR id=59864282 OR id=3673596 OR id=19570439 OR id=22883042 OR id=72375525 OR id=51614404 OR id=47526636 OR id=98443133 OR id=99140135 OR id=33855918 OR id=28333489 OR id=81416033 OR id=2670097 OR id=4897577 OR id=24439616 OR id=36643479 OR id=40817600 OR id=76022791 OR id=40072872 OR id=95193435 OR id=96967607 OR id=24983145 OR id=49883271 OR id=94602753 OR id=83555050 OR id=85455145 OR id=34563229 OR id=72328311 OR id=12002151 OR id=71481181 OR id=72998351 OR id=1489188 OR id=38426973 OR id=91893116 OR id=61594591 OR id=89693630 OR id=6268166 OR id=20056665 OR id=62169880 OR id=17143472 OR id=35103925 OR id=22452590 OR id=54272289 OR id=34236829 OR id=78028543 OR id=84474414 OR id=40386926 OR id=50550952 OR id=49413559 OR id=48781941 OR id=22927237 OR id=44447815 OR id=29960478 OR id=47578119 OR id=10192558 OR id=87733936 OR id=88699383 OR id=38808712 OR id=79944807 OR id=84014713 OR id=31865463 OR id=72617685 OR id=19557568 OR id=47865990 OR id=39069638 OR id=20086122 OR id=1777562 OR id=29018078 OR id=78358083 OR id=94561719 OR id=46281152 OR id=99789008 OR id=86929490 OR id=16534451 OR id=55989144 OR id=52455669 OR id=54561585 OR id=97379646 OR id=20416183 OR id=87617750 OR id=76115505 OR id=3282482 OR id=8383619 OR id=45456319 OR id=29576432 OR id=67750627 OR id=61736333 OR id=33745442 OR id=51502165 OR id=35349384 OR id=78106651 OR id=23232822 OR id=94851387 OR id=78254073 OR id=82406754 OR id=10317954 OR id=70125940 OR id=45067526 OR id=27061875 OR id=25640164 OR id=52574899 OR id=93819227 OR id=93789607 OR id=96122951 OR id=31673246 OR id=70431904 OR id=54067896 OR id=37146857 OR id=37817889 OR id=14058940 OR id=60710246 OR id=64844350 OR id=91604383 OR id=71972005 OR id=13888349 OR id=19093493 OR id=27397281 OR id=61085409 OR id=66529387 OR id=82761299 OR id=72236310 OR id=19277077 OR id=96599501 OR id=68304096 OR id=48292937 OR id=97503321 OR id=88011133 OR id=29224803 OR id=79782945 OR id=79965966 OR id=83716914 OR id=90432214 OR id=48938902 OR id=12498489 OR id=30246261 OR id=91624049 OR id=68652396 OR id=23677785 OR id=44084687 OR id=3865123 OR id=37823170 OR id=45287730 OR id=38784682 OR id=28058351 OR id=68226368 OR id=61569897 OR id=44737876 OR id=70575908 OR id=25568463 OR id=24668386 OR id=88650569 OR id=35559584 OR id=1897737 OR id=77844785 OR id=29780669 OR id=84004602 OR id=29029776 OR id=91003545 OR id=48058106 OR id=9463847;
```

测试结果如下：

第一种情况，ID列为主键的情况，4组测试执行计划一样，执行的时间也基本没有区别。

A组or和in的执行时间： or的执行时间为：0.002s     in的执行时间为：0.002s

B组or和in的执行时间： or的执行时间为：0.004s     in的执行时间为：0.004s

C组or和in的执行时间： or的执行时间为：0.006s     in的执行时间为：0.005s

D组or和in的执行时间： or的执行时间为：0.018s     in的执行时间为：0.014s

第二种情况，ID列为一般索引的情况，4组测试执行计划一样，执行的时间也基本没有区别。

A组or和in的执行时间： or的执行时间为：0.002s     in的执行时间为：0.002s

B组or和in的执行时间： or的执行时间为：0.006s     in的执行时间为：0.005s  

C组or和in的执行时间： or的执行时间为：0.008s     in的执行时间为：0.008s

D组or和in的执行时间： or的执行时间为：0.021s     in的执行时间为：0.020s  

第三种情况，ID列没有索引的情况，4组测试执行计划一样，执行的时间有很大的区别。

A组or和in的执行时间： or的执行时间为：5.016s      in的执行时间为：5.071s

B组or和in的执行时间： or的执行时间为：1min 02s     in的执行时间为：5.018s

C组or和in的执行时间： or的执行时间为：1min 55s     in的执行时间为：5.018s

D组or和in的执行时间： or的执行时间为：6min 17s     in的执行时间为：5.057s

结论：从上面的测试结果，可以看出如果in和or所在列有索引或者主键的话，or和in没啥差别，执行计划和执行时间都几乎一样。如果in和or所在列没有索引的话，性能差别就很大了。在没有索引的情况下，随着in或者or后面的数据量越多，in的效率不会有太大的下降，但是or会随着记录越多的话性能下降非常厉害，从第三种测试情况中可以很明显地看出了，基本上是指数级增长。因此在给in和or的效率下定义的时候，应该再加上一个条件，就是所在的列是否有索引或者是否是主键。如果有索引或者主键性能没啥差别，如果没有索引，性能差别不是一点点！ 

### 4.2.12 exists、not exists
---

### 4.2.13 in和exists的区别
---

### 4.2.14 模糊查询like
---

模糊查询又被称为模糊匹配，在实际开发中使用较多，比如：查询公司中所有姓张的，查询岗位中带有经理两个字的职位等等，这些都需要使用模糊查询。

模糊查询的语法格式如下：

```sql
select .. from .. where 字段 like '通配符表达式';
```

在模糊查询中，通配符主要包括两个：一个是%，一个是下划线_。其中%代表任意多个字符。下划线_代表任意一个字符。

案例1：查询员工名字以'S'开始的员工姓名

```sql
select ename from emp where ename like 'S%';
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1622000884924-f3303ff0-cb9a-4393-831c-01d3e705606d.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_18%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

案例2：查询员工名字以'T'结尾的员工姓名

```sql
select ename from emp where ename like '%T';
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1622000970235-0265da36-1e10-4da5-abb8-c651452fad21.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_18%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

案例3：查询员工名字中含有'O'的员工姓名

```sql
select ename from emp where ename like '%O%';
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1622001027995-71da44df-e3b1-4e56-a6e2-922a50ccc2b7.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_18%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

案例4：查询员工名字中第二个字母是'A'的员工姓名

```sql
select ename from emp where ename like '_A%';
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1622001108864-1abbac56-669f-4c35-9b48-6d80452ad8ce.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_18%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

案例5：查询学员名字中含有下划线的。

执行以下SQL语句，先准备测试数据：

```sql
drop table if exists student;
create table student(
  id int,
  name varchar(255)
);
insert into student(id,name) values(1, 'susan');
insert into student(id,name) values(2, 'lucy');
insert into student(id,name) values(3, 'jack_son');
select * from student;
```

![](https://cdn.nlark.com/yuque/0/2021/png/21376908/1622001536746-e0d05c73-f941-4f28-9190-bbfcf248c41b.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_11%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

查询学员名字中含有下划线的，执行以下SQL试试：

```sql
select * from student where name like '%_%';
```

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1667523151909-c112a3cb-9968-4b4a-8bee-5a75c4b6a9f2.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_19%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

显然这个查询结果不是我们想要的，以上SQL之所以将所有数据全部显示了，因为下划线代表任意单个字符，如果你想让这个下划线变成一个普通的下划线字符，就要使用转义字符了，在mysql当中转义字符是“\”，这个和java语言中的转义字符是一样的：

```sql
select * from student where name like '%\_%';
```

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1667523291579-62dc328f-17ef-4e97-a22a-374ade19e797.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_18%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

## 4.3 排序操作
---

排序操作很常用，比如查询学员成绩，按照成绩降序排列。排序的SQL语法：

```sql
select .. from .. order by 字段 asc/desc
```

### 4.3.1 单一字段升序
查询员工的编号、姓名、薪资，按照薪资升序排列。

```sql
select empno,ename,sal from emp order by sal asc;
```

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1667524015631-e1f1b6c3-0a5b-4f04-91d1-7a11df8fc7ff.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_20%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

### 4.3.2 单一字段降序
查询员工的编号、姓名、薪资，按照薪资降序排列。

```sql
select empno,ename,sal from emp order by sal desc;
```

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1667524068322-84c1f716-5b7a-4b72-8a41-c0f8ec433d57.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_21%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

### 4.3.3 默认采用升序
查询员工的编号、姓名、薪资，按照薪资升序排列。

```sql
select empno,ename,sal from emp order by sal;
```

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1667524117390-bd4560ff-accf-45ee-97f1-d098f86fd31f.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_19%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

查询员工的编号、姓名，按照姓名升序排列。

```sql
select empno,ename from emp order by ename;
```

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1667524169552-6abc923e-3638-4a65-ab97-741c22f885fa.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_18%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

### 4.3.4 多个字段排序
查询员工的编号、姓名、薪资，按照薪资升序排列，如果薪资相同的，再按照姓名升序排列。

```sql
select empno,ename,sal from emp order by sal asc, ename asc;
```

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1667524337952-bbef44e7-488e-4c3e-9317-1fda80054c92.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_23%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

### 4.3.5 where和order by的位置
找出岗位是MANAGER的员工姓名和薪资，按照薪资升序排列。

```sql
select ename,sal from emp where job = 'MANAGER' order by sal asc;
```

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1667524386864-8d24513b-85f9-4f31-9462-4fe094cb0843.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_25%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

**<font style="color:#E8323C;">通过这个例子主要是想告诉大家：where先执行，order by语句是最后执行的。</font>**

## 4.4 distinct去重
查询工作岗位

```sql
select job from emp;
```

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668570471000-b0d2c628-c149-4b13-b44c-ae6f5edefcf6.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_13%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

可以看到工作岗位中有重复的记录，如何在显示的时候去除重复记录呢？在字段前添加distinct关键字。

```sql
select distinct job from emp;
```

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668570545279-ba8dcff3-533d-4ca8-9cc9-4b544ae47e8c.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

注意：这个去重只是将显示的结果去重，原表数据不会被更改。

接下来测试一下，在distinct关键字前添加其它字段是否可以？

```sql
select ename, distinct job from emp;
```

分析一下：ename是14条记录，distinct job是5条记录，可以同时显示吗？

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668570696423-05844698-00b1-4e9e-aa98-1a53f465cff4.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_27%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

报错了，通过测试得知，distinct只能出现在所有字段的最前面。

当distinct出现后，后面多个字段一定是联合去重的，我们来做两个练习就知道了：

练习1：找出公司中所有的工作岗位。

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668570864793-732f34aa-5b7d-4389-b4af-51cbd964215f.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

练习2：找出公司中不同部门的不同工作岗位。

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668570891921-9c547b9b-d20e-4695-9704-051863b5e868.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_18%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

## 4.5 数据处理函数
---

关于select语句，我们之前都是这样写：select 字段名 from 表名; 其实，这里的字段名可以看做“变量”，select后面既然可以跟变量，那么可以跟常量吗，尝试一下：

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668568118423-c5b5d189-4d32-41ab-a189-3f155d0d0efa.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_25%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

通过以上sql的测试得知，select后面既可以跟变量，又可以跟常量。

以上三条SQL中前两条中100和'abc'都是常量，最后一条SQL的abc没有添加单引号，它会被当做某个表的字段名，因为没有这个字段所以报错。 

### 4.5.1 字符串相关
**转大写upper和ucase**

```sql
# 查询所有员工名字，以大写形式展现
select upper(ename) as ename from emp;
```

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668565912887-88d14d6c-707b-4e50-ac47-f8ad61b40d14.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_20%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

还有一个和upper函数功能相同的函数ucase，也可以转大写，了解一下即可：

```sql
# 查询所有员工姓名，以大写形式展现
select ucase(ename) as ename from emp;
```

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668566229563-55802f88-f6d6-436a-b478-18832d7a0342.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_19%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

```sql
# 查询员工smith的岗位、薪资（假如你不知道数据库表中的人名是大写、小写还是大小写混合）
select ename, job, sal from emp where upper(ename) = 'SMITH';
```

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668566360054-6e77882a-21fc-4b6e-9a04-3e0098606db8.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_28%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

**转小写lower和lcase，很简单，不再赘述，直接上代码：**

```sql
# 查询员工姓名，以小写形式展现
select lower(ename) as ename from emp;
select lcase(ename) as ename from emp;
```

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668566699289-0a479f71-ecf4-4a3f-ac4c-8516a4f0fee8.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_18%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668566716526-c8fac5f9-7079-4738-a3d1-2a5c3c5e1145.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_18%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

**截取字符串substr**

语法：substr('被截取的字符串', 起始下标, 截取长度)

有两种写法：

第一种：substr('被截取的字符串', 起始下标, 截取长度)

第二种：substr('被截取的字符串', 起始下标)，当第三个参数“截取长度”缺失时，截取到字符串末尾

注意：起始下标从1开始，不是从0开始。（1表示从左侧开始的第一个位置，-1表示从右侧开始的第一个位置。）

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668567142258-6748508c-c3bb-440f-8ad7-c64df6c0028d.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_19%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

练习：找出员工名字中第二个字母是A的

```sql
select ename from emp where substr(ename, 2, 1) = 'A';
```

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668567271612-710d3592-6111-4ab5-97c1-12f809ac7645.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_24%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

**获取字符串长度length**

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672736218451-70fddda1-2541-4c91-9f39-3f968a6b6e12.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

注意：一个汉字是2个长度。

**获取字符的个数char_length**

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672736125194-177317bd-f65c-4c05-bda7-f58961b78fd7.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_17%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

**字符串拼接**

语法：concat('字符串1', '字符串2', '字符串3'....)

拼接的字符串数量没有限制。

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668569810019-a8c939c4-518d-4ed9-961a-27d4440d13d0.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_25%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

注意：在mysql8之前，双竖线||也是可以完成字符串拼接的。但在mysql8之后，||只作为逻辑运算符，不能再进行字符串拼接了。

```sql
select 'abc' || 'def' || 'xyz';
```

mysql8之后，|| 只作为“或者”运算符，例如：找出工资高于3000或者低于900的员工姓名和薪资：

```sql
select ename, sal from emp where sal > 3000 || sal < 900;
```

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1669780282134-d3a16d8a-e0fc-4744-beff-83b3579f6161.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_27%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

mysql中可以使用+进行字符串的拼接吗？不可以，在mysql中+只作加法运算，在进行加法运算时，会将加号两边的数据尽最大的努力转换成数字再求和，如果无法转换成数字，最终运算结果通通是0

**去除字符串前后空白trim**

```sql
select concat(trim('    abc    '), 'def');
```

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668570023583-bcf0b431-c34c-486b-9ee0-e571ff3c158d.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_20%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

默认是去除前后空白，也可以去除指定的前缀后缀，例如：

去除前置0

```sql
select trim(leading '0' from '000111000');
```

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668570194415-8f78ced1-8f36-42d3-a829-b81fc4132c85.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_20%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

去除后置0

```sql
select trim(trailing '0' from '000111000');
```

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668570218215-c862c7d8-1ee3-4066-8e25-055767efee61.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_20%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

前置0和后置0全部去除

```sql
select trim(both '0' from '000111000');
```

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1668570238062-dff388d3-3106-457d-a9ae-819f41821792.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_19%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

### 4.5.2 数字相关
**rand()和rand(x)**

rand()生成0到1的随机浮点数。

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1669797997130-63b2c8d0-6169-4ee8-9b6b-c3087e9d733b.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_14%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

rand(x)生成0到1的随机浮点数，通过指定整数x来确定每次获取到相同的浮点值。

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1669798044104-7fc0b727-ff91-4d3e-be33-9954d556afe2.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_12%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1669798069147-75492782-759d-46d9-84c5-a83b3a63594c.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_12%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

**round(x)和round(x,y)四舍五入**

round(x) 四舍五入，保留整数位，舍去所有小数

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1669798450055-e26955bd-ea2d-445a-be98-721b54d3ca35.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_12%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

round(x,y) 四舍五入，保留y位小数

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1669798534269-9c494800-7878-4ccf-bacc-a8c4cdafbbe6.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_13%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

**truncate(x, y)舍去**

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1669798594158-7e51e7a5-27af-4f7f-8021-a751f425a316.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_14%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

以上SQL表示保留两位小数，剩下的全部舍去。

数字处理函数除了以上的之外，还有ceil和floor函数：

- ceil函数：返回大于或等于数值x的最小整数
- floor函数：返回小于或等于数值x的最大整数

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672735932932-f0dfc7de-1f77-4eb0-b6e9-b6c6c2ce7ae3.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_11%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

### 4.5.3 空处理
ifnull(x, y)，空处理函数，当x为NULL时，将x当做y处理。

ifnull(comm, 0)，表示如果员工的津贴是NULL时当做0处理。

在SQL语句中，凡是有NULL参与的数学运算，最终的计算结果都是NULL：

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1669798864111-5cffd59f-d15c-4f6c-a2d8-0b623ec1f16c.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_12%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

看这样一个需求：查询每个员工的年薪。（年薪 = (月薪 + 津贴) * 12个月。注意：有的员工津贴comm是NULL。）

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1669798945415-90bccaa6-1dda-4ebd-bc50-63ab5ba2b89a.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_24%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

以上查询结果中显示SMITH等人的年薪是NULL，这是为什么，这是因为SMITH等人的津贴comm是NULL，有NULL参与的数学运算，最终结果都是NULL，显然这个需要空处理，此时就用到了ifnull函数：

![](https://cdn.nlark.com/yuque/0/2022/png/21376908/1669799067232-4896fa47-5c64-409a-b970-dddc31e06050.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_28%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

### 4.5.4 日期和时间相关函数
1. **获取当前日期和时间**

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672707310711-3115e4af-385c-4565-89c7-25bad76e8a6a.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_12%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672707382021-d8d296b7-9d9a-4072-b714-c99da604ac12.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_11%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672707469394-4fe3f0fb-ca9e-4484-b939-db716f6ddd38.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_23%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

now()和sysdate()的区别：

- now()：获取的是执行select语句的时刻。
- sysdate()：获取的是执行sysdate()函数的时刻。
2. **获取当前日期**

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672707770762-e9723219-562f-4a53-9d8a-9055ee80c25d.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_13%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

获取当前日期有三种写法，掌握任意一种即可：

- curdate()
- current_date()
- current_date
3. **获取当前时间**

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672707856778-8eec2322-c3c8-4ddc-94c4-3e08eea430a8.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_12%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

获取档期时间有三种写法，掌握其中一种即可：

- curtime()
- current_time()
- current_time
4. **获取单独的年、月、日、时、分、秒**

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672708190559-a1d93032-699d-49dc-87cc-4ccb045bee28.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_13%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672708242288-89a20209-4ca2-4d1c-a1b0-5ad5f1179841.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_14%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

注意：这些函数在使用的时候，需要传递一个日期参数给它，它可以获取到你给定的这个日期相关的年、月、日、时、分、秒的信息。

一次性提取一个给定日期的“年月日”部分，可以使用date()函数，例如：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672713926559-d9c4257b-3536-4124-b4f4-3fd3626a293e.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_12%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

一次性提取一个给定日期的“时分秒”部分，可以使用time()函数，例如：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672721340191-9c568184-73b5-4c26-9035-95245016ba4f.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_12%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

5. **date_add函数**

date_add函数的作用：给指定的日期添加间隔的时间，从而得到一个新的日期。

date_add函数的语法格式：date_add(日期, interval expr 单位)，例如：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672709352877-e64de4c0-d776-4e30-908b-4a96c04bc186.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_22%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

以'2023-01-03'为基准，间隔3天之后的日期：'2023-01-06'

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672709436259-c6d671c6-ccc8-4109-9612-1f178801ef64.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_22%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

以'2023-01-03'为基准，间隔3个月之后的日期：'2023-04-03'

详细解释一下这个函数的相关参数：

- 日期：一个日期类型的数据
- interval：关键字，翻译为“间隔”，固定写法
- expr：指定具体的间隔量，一般是一个数字。**<font style="color:#E8323C;">也可以为负数，如果为负数，效果和date_sub函数相同</font>**。
- 单位：
    - year：年
    - month：月
    - day：日
    - hour：时
    - minute：分
    - second：秒
    - microsecond：微秒（1秒等于1000毫秒，1毫秒等于1000微秒）
    - week：周
    - quarter：季度

请分析下面这条SQL语句所表达的含义：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672710673500-8afb96ad-3aa5-4adb-9160-9aaac4b4ff83.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_30%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

以上SQL表示：以2022-10-01 10:10:10为基准，在这个时间基础上添加-1微秒，也就是减去1微秒。

以上SQL也可以采用date_sub函数完成，例如：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672710799157-9775a5b0-143f-493b-a6f0-cd8db5c6ca31.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_28%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

另外，单位也可以采用复合型单位，例如：

- SECOND_MICROSECOND
- MINUTE_MICROSECOND
- MINUTE_SECOND：几分几秒之后
- HOUR_MICROSECOND
- HOUR_SECOND
- HOUR_MINUTE：几小时几分之后
- DAY_MICROSECOND
- DAY_SECOND
- DAY_MINUTE
- DAY_HOUR：几天几小时之后
- YEAR_MONTH：几年几个月之后

如果单位采用复合型的话，expr该怎么写呢？例如单位采用：day_hour，假设我要表示3天2小时之后，怎么写？

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672711325140-0a281589-4bc2-4fc8-bd7f-9a5ff180ba71.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_29%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

'3,2'这个应该很好理解，表示3天2个小时之后。'3,2'和day_hour是对应的。

6. **date_format日期格式化函数**

将日期转换成具有某种格式的日期字符串，通常用在查询操作当中。（date类型转换成char类型）

语法格式：date_format(日期, '日期格式')

该函数有两个参数：

- 第一个参数：日期。这个参数就是即将要被格式化的日期。类型是date类型。
- 第二个参数：指定要格式化的格式字符串。
    - %Y：四位年份
    - %y：两位年份
    - %m：月份（1..12）
    - %d：日（1..30）
    - %H：小时（0..23）
    - %i：分（0..59）
    - %s：秒（0..59）

例如：获取当前系统时间，让其以这个格式展示：2000-10-11 20:15:30

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672716928881-badddb77-c670-43f3-8b25-8e2eb4952a04.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_23%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

注意：在mysql当中，默认的日期格式就是：%Y-%m-%d %H:%i:%s，所以当你直接输出日期数据的时候，会自动转换成该格式的字符串：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672717081322-e99bdff0-76df-4fcc-958a-463bf9e65d9d.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_11%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

7. **str_to_date函数**

该函数的作用是将char类型的日期字符串转换成日期类型date，通常使用在插入和修改操作当中。（char类型转换成date类型）

假设有一个学生表t_student，学生有一个生日的字段，类型是date类型：

```sql
drop table if exists t_student;
create table t_student(
  name varchar(255),
  birth date
);
desc t_student;
```

我们要给这个表插入一条数据：姓名zhangsan，生日85年10月1日，执行以下insert语句：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672718111465-698c085a-b3f1-4523-9f3f-d27ceb4410d5.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_33%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

错误原因：日期值不正确。意思是：birth字段需要一个日期，你给的这个字符串'10/01/1985'我识别不了。这种情况下，我们就可以使用str_to_date函数进行类型转换：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672718492868-58ab55ff-a4e7-481f-9c58-9c81014d1762.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_39%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672718610506-ec24a44e-7854-4037-8567-b42dfb9228c0.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

当然，如果你提供的日期字符串格式能够被mysql解析，str_to_date函数是可以省略的，底层会自动调用该函数进行类型转换：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672718807175-8b62c13a-e771-482d-a999-7548501da25e.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_31%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

如果日期格式符合以上的几种格式，mysql都会自动进行类型转换的。

8. **dayofweek、dayofmonth、dayofyear函数**

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672719401783-7ea51704-954a-4f96-aa81-3a8da4b34582.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_20%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

dayofweek：一周中的第几天（1~7），周日是1，周六是7。

dayofmonth：一个月中的第几天（1~31）

dayofyear：一年中的第几天（1~366）

9. **last_day函数**

获取给定日期所在月的最后一天的日期：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672719572099-bba462b8-da22-42b7-9a40-9c2c545596ef.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_14%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

10. **datediff函数**

计算两个日期之间所差天数：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672720897012-c5e7e6dd-29de-46b0-b2c1-e1de3e8d6e54.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_25%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

时分秒不算，只计算日期部分相差的天数。

11. **timediff函数**

计算两个日期所差时间，例如日期1和日期2所差10:20:30，表示差10小时20分钟30秒。

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672721193551-f65b470a-9060-4010-b172-b34eb1787e55.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_28%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

### 4.5.5 if函数
如果条件为TRUE则返回“YES”，如果条件为FALSE则返回“NO”：

```sql
SELECT IF(500<1000, "YES", "NO");
```

例如：如果工资高于3000，则输出1，反之则输出0

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672725980625-f929cbdc-41ec-49d4-a5de-bc753dfbe67e.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_21%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

再例如：如果名字是SMITH的，工资上调10%，其他员工工资正常显示。

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672726073468-51733168-6ebe-477d-9aba-267adcefd10a.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_28%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

再例如：工作岗位是MANAGER的工资上调10%，是SALESMAN的工资上调20%，其他岗位工资正常。

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672726371265-19128e1a-47cf-46b0-9b80-310d37010535.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_41%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

上面这个需求也可以使用：case.. when.. then.. when.. then.. else.. end来完成：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672726864928-8206091b-3bd3-4f12-b784-173aff775d6f.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_16%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

### 4.5.6 cast函数
cast函数用于将值从一种数据类型转换为表达式中指定的另一种数据类型

语法：cast(值 as 数据类型)

例如：cast('2020-10-11' as date)，表示将字符串'2020-10-11'转换成日期date类型。

在使用cast函数时，可用的数据类型包括：

- date：日期类型
- time：时间类型
- datetime：日期时间类型
- signed：有符号的int类型（有符号指的是正数负数）
- char：定长字符串类型
- decimal：浮点型

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672737293605-d7e38772-e9c3-40ab-a7ea-3311aa14a1a9.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_22%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672737634602-96cdd564-1220-445e-9b18-b3f0a2a55379.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_16%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672737720321-3812fd42-d3a4-4985-96d2-629947d9ce48.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_17%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672737802812-d04d581c-138c-4e4e-97d4-c979558e9b2e.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_20%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

### 4.5.7 加密函数
md5函数，可以将给定的字符串经过md5算法进行加密处理，字符串经过加密之后会生成一个固定长度32位的字符串，md5加密之后的密文通常是不能解密的：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1672737046172-5ee0458a-60c6-4bae-b075-94b7dee440ab.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_16%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

## 4.6 分组函数
分组函数的执行原则：先分组，然后对每一组数据执行分组函数。如果没有分组语句group by的话，整张表的数据自成一组。

分组函数包括五个：

- max：最大值
- min：最小值
- avg：平均值
- sum：求和
- count：计数

**找出员工的最高薪资**

select max(sal) from emp;

**找出员工的最低工资**

select min(sal) from emp;

**计算员工的平均薪资**

select avg(sal) from emp;

**计算员工的工资和**

select sum(sal) from emp;

**计算员工的津贴之和**

select sum(comm) from emp;

<font style="color:#DF2A3F;">重点：所有的分组函数都是自动忽略NULL的。</font>

**统计员工人数**

select count(ename) from emp;

select count(*) from emp;

select count(1) from emp;

count(*)和count(1)的效果一样，统计该组中总记录行数。

count(ename)统计的是这个ename字段中不为NULL个数总和。

例如：count(comm) 结果是 4，而不是14

**统计岗位数量**

select count(distinct job) from emp;

**分组函数组合使用**

select count(*),max(sal),min(sal),avg(sal),sum(sal) from emp;

**分组函数不能直接使用在where子句当中**

select ename,job from emp where sal > avg(sal); 这个会报错的

原因：分组的行为是在where执行之后才开始的。

## 4.7 分组查询
1. **group by**

按照某个字段分组，或者按照某些字段联合分组。注意：group by的执行是在where之后执行。

语法：

group by 字段

group by 字段1,字段2,字段3....

**找出每个岗位的平均薪资**

select job, avg(sal) from emp group by job;

**找出每个部门最高工资**

select deptno,max(sal) from emp group by deptno;

**找出每个部门不同岗位的平均薪资**

select deptno,job,avg(sal) from emp group by deptno,job;

**当select语句中有group by的话，select后面只能跟分组函数或参加分组的字段**

select ename,deptno,avg(sal) from emp group by deptno; // 这个SQL执行后会报错。

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1676866192155-44d23157-87d0-4a58-a9d5-2641619d74fe.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_33%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

2. **having**

having写在group by的后面，当你对分组之后的数据不满意，可以继续通过having对分组之后的数据进行过滤。

where的过滤是在分组前进行过滤。

使用原则：尽量在where中过滤，实在不行，再使用having。越早过滤效率越高。

**找出除20部分之外，其它部门的平均薪资。**

select deptno,avg(sal) from emp where deptno<>20 group by deptno; // 建议

select deptno,avg(sal) from emp group by deptno having deptno <> 20; // 不建议

**查询每个部门平均薪资，找出平均薪资高于2000的。**

select deptno,avg(sal) from emp group by deptno having avg(sal) > 2000;

3. **总结单表的DQL语句**

select ...5

from ...1

where ...2

group by ...3

having ...4

order by ...6

重点掌握一个完整的DQL语句执行顺序。

4. **行转列，列转行**
5. **组内排序**

案例：找出每个工作岗位的工资排名在前两名的。

substring_index函数的使用：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1678080182698-009c47d2-eb75-4f67-afaa-874c7904ed45.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_22%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

group_concat函数的使用：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1678082111760-02413f4e-a8b0-4837-8cb0-3b201151293f.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_26%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

## 4.9 连接查询
1. **什么是连接查询？**
    1. 从一张表中查询数据称为单表查询。
    2. 从两张或更多张表中联合查询数据称为多表查询，又叫做连接查询。
    3. 什么时候需要使用连接查询？
        1. 比如这样的需求：员工表中有员工姓名，部门表中有部门名字，要求查询每个员工所在的部门名字，这个时候就需要连接查询。
2. **连接查询的分类？**
    1. 根据语法出现的年代进行分类：
        1. SQL92（这种语法很少用，可以不用学。）
        2. SQL99（我们主要学习这种语法。）
    2. 根据连接方式的不同进行分类：
        1. 内连接
            1. 等值连接
            2. 非等值连接
            3. 自连接
        2. 外连接
            1. 左外连接（左连接）
            2. 右外连接（右连接）
        3. 全连接
3. **笛卡尔积现象？**
    1. 当两张表进行连接查询时，如果没有任何条件进行过滤，最终的查询结果条数是两张表条数的乘积。为了避免笛卡尔积现象的发生，需要添加条件进行筛选过滤。
    2. 需要注意：添加条件之后，虽然避免了笛卡尔积现象，但是匹配的次数没有减少。
    3. 为了SQL语句的可读性，为了执行效率，建议给表起别名。
4. **什么叫内连接？**

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677398804476-afbffad7-7d5a-4318-9e86-a3f8092dfcc8.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_14%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

满足条件的记录才会出现在结果集中。

5. **内连接之等值连接**

连接时，条件为等量关系。

案例：查询每个员工所在的部门名称，要求显示员工名、部门名。

```sql
select
	e.ename,d.dname
from
	emp e
inner join
	dept d
on
	e.deptno = d.deptno;
```

注意：inner可以省略。

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677401675659-04e46e96-9f00-4210-8beb-e8148807ae10.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_12%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

6. **内连接之非等值连接**

连接时，条件是非等量关系。

案例：查询每个员工的工资等级，要求显示员工名、工资、工资等级。

```sql
select
	e.ename,e.sal,s.grade
from
	emp e
join
	salgrade s
on
	e.sal between s.losal and s.hisal;
```

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677401628377-11f115a0-b961-4e10-b411-97ea04a89035.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_13%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

7. **内连接之自连接**

连接时，一张表看做两张表，自己和自己进行连接。

案例：找出每个员工的直属领导，要求显示员工名、领导名。

```sql
select
	e.ename 员工名, l.ename 领导名
from
	emp e
join
	emp l
on
	e.mgr = l.empno;
```

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677402107820-a3fc38cc-4e13-4a39-8bb4-f1d9de713cd9.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_12%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

思路：

将emp表当做员工表 e

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677401951879-b0967e07-82f4-41e3-861e-d61e7d679e71.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_12%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

将emp表当做领导表 l

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677401973338-4bc03ba9-815d-4fca-90fb-de34e5848da3.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_11%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

可以发现连接条件是：e.mgr = l.empno（员工的领导编号=领导的员工编号）

注意：KING这个员工没有查询出来。如果想将KING也查询出来，需要使用外连接。

8. **什么叫外连接？**

内连接是满足条件的记录查询出来。也就是两张表的交集。

外连接是除了满足条件的记录查询出来，再将其中一张表的记录全部查询出来，另一张表如果没有与之匹配的记录，自动模拟出NULL与其匹配。

左外连接：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677398828684-41b0bde2-1689-47a4-ae7b-3c5c4fb82ce6.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_14%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

右外连接：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677398837026-688ff40f-d74b-4da6-a2e4-9573f5ba1580.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_14%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

9. **外连接之左外连接（左连接）**

案例：查询所有部门信息，并且找出每个部门下的员工。

```sql
select
  d.*,e.ename
from
  dept d
left outer join
  emp e
on
  d.deptno = e.deptno;
```

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677402955987-bdcd956a-8dd4-481b-97de-c785b200e902.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_13%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

注意：outer可以省略。

任何一个左连接都可以写作右连接。

10. **外连接之右外连接（右连接）**

还是上面的案例，可以写作右连接。

```sql
select
  d.*,e.ename
from
  emp e
right outer join
  dept d
on
  d.deptno = e.deptno;
```

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677403445932-325502d5-b568-46a5-8f7a-d91030f3cac3.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_13%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

案例：找出所有员工的上级领导，要求显示员工名和领导名。

```sql
select 
  e.ename 员工名,l.ename 领导名 
from 
  emp e 
left join 
  emp l 
on
  e.mgr = l.empno;
```

```sql
select 
  e.ename 员工名,l.ename 领导名 
from 
  emp l 
right join 
  emp e 
on
  e.mgr = l.empno;
```

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677403569294-c9688076-61e2-4e33-bb40-06d4307c6b43.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_12%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

11. **什么是全连接？**

MySQL不支持full join。oracle数据库支持。

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677398846702-4a3f3e0f-16bb-4e00-8015-490dc44d114b.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_14%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

两张表数据全部查询出来，没有匹配的记录，各自为对方模拟出NULL进行匹配。

客户表：t_customer

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677405118434-d9979d32-5647-4b0a-8d65-1ff6b61c6d44.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_11%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

订单表：t_order

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677405287024-4df811ac-9216-47c3-98b2-20f5d7ce2886.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_12%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

案例：查询所有的客户和订单。

```sql
select 
 c.*,o.* 
from 
 t_customer c 
full join 
 t_order o 
on 
 c.cid = o.cid;
```

12. **三张表甚至更多张表如何进行表连接**

案例：找出每个员工的部门，并且要求显示每个员工的薪资等级。

```sql
select 
 e.ename,d.dname,s.grade 
from 
 emp e 
join 
 dept d 
on 
 e.deptno = d.deptno 
join 
 salgrade s 
on 
 e.sal between s.losal and s.hisal;
```

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677404511432-b8fe8eb2-c828-4913-8d7c-a7b47a0ee270.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

## 4.10 子查询
1. **什么是子查询？**
    1. select语句中嵌套select语句就叫做子查询。
    2. select语句可以嵌套在哪里？
        1. where后面、from后面、select后面都是可以的。
2. **where后面使用子查询**

案例：找出高于平均薪资的员工姓名和薪资。

错误的示范：

```sql
select ename,sal from emp where sal > avg(sal);
```

错误原因：where后面不能直接使用分组函数。

可以使用子查询：

```sql
select ename,sal from emp where sal > (select avg(sal) from emp);
```

3. **from后面使用子查询**

小窍门：from后面的子查询可以看做一张临时表。

案例：找出每个部门的平均工资的等级。

第一步：先找出每个部门平均工资。

```sql
select deptno, avg(sal) avgsal from emp group by deptno;
```

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677477788393-e2525a0a-2092-4a5e-80e7-7f8df04f6a6c.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_14%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

第二步：将以上查询结果当做临时表t，t表和salgrade表进行连接查询。条件：t.avgsal between s.losal and s.hisal

```sql
select t.*,s.grade from (select deptno, avg(sal) avgsal from emp group by deptno) t join salgrade s on t.avgsal between s.losal and s.hisal;
```

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1677477892811-ef9b366b-82be-4407-86f1-8dfa81492d8c.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_11%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

4. **select后面使用子查询**

```sql
select e.ename,(select d.dname from dept d where e.deptno = d.deptno) as dname from emp e;
```

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1678063689524-a204a93a-6454-4ff7-a1c6-ac5229edae91.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_12%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

5. **any子查询**

<font style="color:#DF2A3F;">和or、in类似，只不过any需要搭配比较符一起用。</font>

in可以完成的，例如：找出工资是3000和5000的：

```sql
select ename,sal from emp where sal in(3000,5000);
```

or也可以完成：

```sql
select ename,sal from emp where sal = 3000 or sal = 5000;
```

or可以完成的，例如：找出工资大于3000或大于5000的：

```sql
select ename,sal from emp where sal > 3000 or sal > 5000;
```

以上如果采用in就完成不了，但可以采用any来完成：

```sql
select ename,sal from emp where sal > any(3000, 5000);
```

但这里要注意，以上sql是无法执行的，<font style="color:#DF2A3F;">因为any后面只能跟子查询。</font>

案例：找出工资高于岗位是ANALYST或PRESIDENT的员工姓名和工资。

```sql
select ename,sal from emp where sal > any(select sal from emp where job in('ANALYST', 'PRESIDENT'));
```

6. **some子查询**

some和any的效果相同。

7. **all子查询**

类似于and，例如：找出工资大于等于岗位是ANALYST并且PRESIDENT的员工姓名和工资。如果使用and实现：

```sql
select ename,sal from emp where sal >= (select distinct sal from emp where job='ANALYST') and sal >= (select distinct sal from emp where job='PRESIDENT');
```

使用all进行实现：

```sql
select ename,sal from emp where sal >= all(select sal from emp where job='ANALYST' or job='PRESIDENT');
```

## 4.11 union&union all
不管是union还是union all都可以将两个查询结果集进行合并。

union会对合并之后的查询结果集进行去重操作。

union all是直接将查询结果集合并，不进行去重操作。（union all和union都可以完成的话，优先选择union all，union all因为不需要去重，所以效率高一些。）

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1678078225300-461e069f-0c80-4745-88a7-2969acccd076.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_12%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1678078278429-e97f96a1-7429-4b68-8df9-3bda3a890797.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_12%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

案例：查询工作岗位是MANAGER和SALESMAN的员工。

```sql
select ename,sal from emp where job='MANAGER'
union all
select ename,sal from emp where job='SALESMAN';
```

以上案例采用or也可以完成，那or和union all有什么区别？<font style="color:#DF2A3F;">考虑走索引优化之类的选择union all，其它选择or。</font>

两个结果集合并时，列数量要相同：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1678078078467-89b7ba88-52ae-4e70-b5cc-b4fe4a3daf76.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_28%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

## 4.12 limit
1. limit作用：查询第几条到第几条的记录。通常是因为表中数据量太大，需要分页显示。
2. limit语法格式：
    1. limit 开始下标, 长度
3. 案例：查询员工表前5条记录

```sql
select ename,sal from emp limit 0, 5;
```

如果下标是从0开始，可以简写为：

```sql
select ename,sal from emp limit 5;
```

4. 查询工资排名在前5名的员工（limit是在order by执行之后才会执行的）

```sql
select ename,sal from emp order by sal desc limit 5;
```

5. 通用的分页sql

假设每页显示3条记录：pageSize = 3

第1页：limit 0, 3

第2页：limit 3, 3

第3页：limit 6, 3

第pageNo页：limit (pageNo - 1)*pageSize, pageSize

## 4.13 SQL练手题
1. 取得每个部门最高薪水的人员名称
    1. 第一步：取得每个部门最高薪水

```sql
select deptno,max(sal) as maxsal from emp group by deptno;
```

    2. 第二步：将上面第一步的查询结果当做一张临时表t，进行表连接，条件是：t.deptno=e.deptno and t.maxsal=e.sal

```sql
select e.ename,t.* from emp e join (select deptno,max(sal) as maxsal from emp group by deptno) t on e.deptno = t.deptno and e.sal = t.maxsal;
```

2. 哪些人的薪水在部门的平均薪水之上
    1. 第一步：取得每个部门的平均薪水

```sql
select deptno,avg(sal) as avgsal from emp group by deptno;
```

    2. 第二步：将上面的查询结果当做临时表t，让t和emp e表进行表连接，条件是：t.deptno=e.deptno and e.sal>t.avgsal

```sql
select e.ename,e.sal,t.* from emp e join (select deptno,avg(sal) as avgsal from emp group by deptno) t on t.deptno=e.deptno and e.sal>t.avgsal;
```

3. 取得每个部门平均薪水的等级
    1. 第一步：取得每个部门的平均薪水

```sql
select deptno,avg(sal) as avgsal from emp group by deptno;
```

    2. 第二步：将上面的查询结果当做临时表t，然后t和salgrade s表进行连接，条件是：t.avgsal between s.losal and s.hisal

```sql
select t.*,s.grade from (select deptno,avg(sal) as avgsal from emp group by deptno) t join salgrade s on t.avgsal between s.losal and s.hisal;
```

4. 取得部门中（所有人的）平均的薪水等级
    1. 第一步：找出每个人的薪水等级

```sql
select e.ename,e.sal,s.grade from emp e join salgrade s on e.sal between s.losal and s.hisal;
```

    2. 第二步：在上面的查询结果当中继续按照部门编号进行分组，求平均值。（不需要将上面的查询结果当做临时表，继续基于它进行分组即可。）

```sql
select 
   e.deptno,avg(s.grade) 
from 
  emp e 
join 
  salgrade s 
on 
  e.sal between s.losal and s.hisal 
group by 
  e.deptno;
```

5. 不准用组函数（Max），取得最高薪水（给出两种解决方案）
    1.  第一种方案：按照薪资降序排列，取第一个。

```sql
select sal from emp order by sal desc limit 1;
```

    2. 第二种方案：采用表的自连接方式。

```sql
select ename,sal from emp where sal not in(select distinct a.sal from emp a join emp b on a.sal < b.sal);
```

6. 取得平均薪水最高的部门的部门编号（至少给出两种解决方案）
    1. 第一种方案：降序排列取第一个

```sql
select deptno,avg(sal) as avgsal from emp group by deptno order by avgsal desc limit 1;
```

    2. 第二种方案：max函数

```sql
select deptno,avg(sal) as avgsal from emp group by deptno having avg(sal)=(select max(t.avgsal) from (select avg(sal) as avgsal from emp group by deptno) t);
```

7. 取得平均薪水最高的部门的部门名称
    1. 比上面的题目多一个表连接，和dept表连接，按照部门名称进行分组。

```sql
select d.dname,avg(e.sal) as avgsal from emp e join dept d on e.deptno=d.deptno group by d.dname order by avgsal desc limit 1;
```

8. 求平均薪水的等级最低的部门的部门名称
    1. 第一步：求每个部门的平均薪水

```sql
select d.dname,avg(e.sal) as avgsal from emp e join dept d on e.deptno = d.deptno group by d.dname;
```

    2. 第二步：求每个部门的平均薪水等级（将以上的执行结果当做临时表t，t和salgrade s表进行连接，条件：t.avgsal between .s.losal and s.hisal）

```sql
select t.*,s.grade from (select d.dname,avg(e.sal) as avgsal from emp e join dept d on e.deptno = d.deptno group by d.dname) t join salgrade s on t.avgsal between s.losal and s.hisal;
```

    3. 第三步：找到最低的部门名称（以上结果继续按照grade进行升序，然后limit 1）

```sql
select t.*,s.grade from (select d.dname,avg(e.sal) as avgsal from emp e join dept d on e.deptno = d.deptno group by d.dname) t join salgrade s on t.avgsal between s.losal and s.hisal order by s.grade asc limit 1;
```

9. 取得比普通员工(员工代码没有在mgr字段上出现的)的最高薪水还要高的领导人姓名
    1. 第一步：找出所有的普通员工的最高薪水

```sql
select max(sal) from emp where empno not in(select mgr from emp where mgr is not null);
```

    2. 第二步：大于以上最高薪水的一定是要找的领导人。

```sql
select ename,sal from emp where sal > (select max(sal) from emp where empno not in(select mgr from emp where mgr is not null));
```

10. 取得薪水最高的前五名员工

```sql
select ename,sal from emp order by sal desc limit 5;
```

11. 取得薪水最高的第六到第十名员工

```sql
select ename,sal from emp order by sal desc limit 5, 5;
```

12. 取得最后入职的5名员工

```sql
select ename,sal,hiredate from emp order by hiredate desc limit 5;
```

13. 取得每个薪水等级有多少员工
    1. 第一步：找出每个员工的薪水等级

```sql
select e.ename,s.grade from emp e join salgrade s on e.sal between s.losal and s.hisal;
```

    2. 第二步：基于以上的记录继续根据等级分组，count即可。

```sql
select s.grade,count(*) from emp e join salgrade s on e.sal between s.losal and s.hisal group by s.grade;
```

14. 列出所有员工及领导的姓名

```sql
select e.ename 员工名, l.ename 领导名 from emp e left join emp l on e.mgr = l.empno;
```

15. 列出受雇日期早于其直接上级的所有员工的编号,姓名,部门名称

```sql
select e.ename 员工名,e.hiredate, l.ename 领导名,l.hiredate,d.dname from emp e join emp l on e.mgr = l.empno join dept d on e.deptno = d.deptno where e.hiredate < l.hiredate;
```

16. 列出部门名称和这些部门的员工信息,同时列出那些没有员工的部门

```sql
select d.dname,e.ename,e.sal from dept d left join emp e on d.deptno = e.deptno;
```

17. 列出至少有5个员工的所有部门

```sql
select deptno, count(*) from emp group by deptno having count(*) >= 5;
```

18. 列出薪金比"SMITH"多的所有员工信息

```sql
select ename,sal from emp where sal > (select sal from emp where ename = 'SMITH');
```

19. 列出所有"CLERK"(办事员)的姓名及其部门名称,部门的人数

```sql
select t1.ename,t1.dname,t2.total from (select e.ename,d.dname,d.deptno from emp e join dept d on e.deptno = d.deptno where e.job = 'CLERK') t1 join (select count(*) as total,deptno  from emp group by deptno) t2 on t1.deptno = t2.deptno;
```

20. 列出最低薪金大于1500的各种工作及从事此工作的全部雇员人数

```sql
select job,min(sal),count(*) from emp group by job having min(sal)>1500;
```

21. 列出在部门"SALES"<销售部>工作的员工的姓名,假定不知道销售部的部门编号

```sql
select e.ename,d.dname from emp e join dept d on e.deptno = d.deptno where d.dname='sales';
```

22. 列出薪金高于公司平均薪金的所有员工,所在部门,上级领导,雇员的工资等级

```sql
select e.ename 员工,l.ename 领导,d.dname,s.grade from 
emp e left join emp l on e.mgr = l.empno 
join dept d on e.deptno = d.deptno 
join salgrade s on e.sal between s.losal and s.hisal 
where e.sal > (select avg(sal) from emp);
```

23. 列出与"SCOTT"从事相同工作的所有员工及部门名称

```sql
select e.ename,d.dname,e.job from emp e join dept d on e.deptno=d.deptno where job=(select job from emp where ename ='scott');
```

24. 列出薪金等于部门30中员工的薪金的其他员工的姓名和薪金

```sql
select ename,sal,deptno from emp where sal in(select distinct sal from emp where deptno=30) and deptno <> 30;
```

25. 列出薪金高于在部门30工作的所有员工的薪金的员工姓名和薪金.部门名称

```sql
select e.ename,e.sal,d.dname from emp e join dept d on e.deptno = d.deptno where sal > (select max(sal) from emp where deptno=30);
```

26. 列出在每个部门工作的员工数量,平均工资和平均服务期限

```sql
select avg(sal),count(*),deptno,avg(datediff(now(),hiredate)) as avgtime from emp group by deptno;
```

27. 列出所有员工的姓名、部门名称和工资

```sql
select e.ename,e.sal,d.dname from emp e join dept d on e.deptno = d.deptno;
```

28. 列出所有部门的详细信息和人数

```sql
select d.deptno,d.dname,d.loc,count(e.deptno) from emp e right join dept d on e.deptno=d.deptno group by  d.deptno,d.dname,d.loc;
```

29. 列出各种工作的最低工资及从事此工作的雇员姓名

```sql
select t.job,t.minsal,e.ename from emp e join (select job,min(sal) as minsal from emp group by job) t on e.job=t.job and e.sal=t.minsal;
```

30. 列出各个部门的MANAGER(领导)的最低薪金

```sql
select deptno,min(sal) from emp where job='MANAGER' group by deptno
```

31. 列出所有员工的年工资,按年薪从低到高排序

```sql
select ename,(sal+ifnull(comm,0))*12 as yearsal from emp order by yearsal asc;
```

32. 求出员工领导的薪水超过3000的员工名称与领导名称

```sql
select e.ename 员工名, l.ename 领导名 from emp e join emp l on e.mgr = l.empno where l.sal>3000;
```

33. 求出部门名称中,带'S'字符的部门员工的工资合计、部门人数

```sql
select d.dname,ifnull(sum(sal),0) as sumsal,count(e.ename) from emp e right join dept d on e.deptno=d.deptno where d.dname like '%S%' group by d.dname;
```

34. 给任职日期超过30年的员工加薪10%

```sql
update emp set sal=sal*1.1 where datediff(now(),hiredate)/365 > 30;
```

35. 某公司面试题

有3个表S（学生表），C（课程表），SC（学生选课表）

S（SNO，SNAME）代表（学号，姓名）  

C（CNO，CNAME，CTEACHER）代表（课号，课名，教师）

SC（SNO，CNO，SCGRADE）代表（学号，课号，成绩）

```sql
CREATE TABLE SC
(
  SNO      VARCHAR(200),
  CNO      VARCHAR(200),
  SCGRADE  VARCHAR(200)
);

CREATE TABLE S
(
  SNO    VARCHAR(200 ),
  SNAME  VARCHAR(200)
);

CREATE TABLE C
(
  CNO       VARCHAR(200),
  CNAME     VARCHAR(200),
  CTEACHER  VARCHAR(200)
);

INSERT INTO C ( CNO, CNAME, CTEACHER ) VALUES ( '1', '语文', '张'); 
INSERT INTO C ( CNO, CNAME, CTEACHER ) VALUES ( '2', '政治', '王'); 
INSERT INTO C ( CNO, CNAME, CTEACHER ) VALUES ( '3', '英语', '李'); 
INSERT INTO C ( CNO, CNAME, CTEACHER ) VALUES ( '4', '数学', '赵'); 
INSERT INTO C ( CNO, CNAME, CTEACHER ) VALUES ( '5', '物理', '黎明'); 
commit;
 
INSERT INTO S ( SNO, SNAME ) VALUES ( '1', '学生1'); 
INSERT INTO S ( SNO, SNAME ) VALUES ( '2', '学生2'); 
INSERT INTO S ( SNO, SNAME ) VALUES ( '3', '学生3'); 
INSERT INTO S ( SNO, SNAME ) VALUES ( '4', '学生4'); 
commit;
 
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '1', '1', '40'); 
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '1', '2', '30'); 
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '1', '3', '20'); 
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '1', '4', '80'); 
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '1', '5', '60'); 
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '2', '1', '60'); 
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '2', '2', '60'); 
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '2', '3', '60'); 
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '2', '4', '60'); 
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '2', '5', '40'); 
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '3', '1', '60'); 
INSERT INTO SC ( SNO, CNO, SCGRADE ) VALUES ( '3', '3', '80'); 
commit;
```

问题：

1，找出没选过“黎明”老师的所有学生姓名。

```sql
select sname from s where sno not in(select sno from sc where cno=(select cno from c where cteacher='黎明'));
```

2，列出2门以上（含2门）不及格学生姓名及平均成绩。

```sql
select a.*,b.avgscore from (select s.sno,s.sname,count(sc.scgrade) as num from sc join s on sc.sno=s.sno where sc.scgrade < 60 group by s.sname,s.sno having count(sc.scgrade) >= 2) a join (select sno,avg(scgrade) avgscore from sc group by sno) b on a.sno = b.sno;
```

3，既学过1号课程又学过2号课所有学生的姓名。

```sql
select sc.sno,s.sname from sc join s on sc.sno=s.sno where sc.cno=1 and sc.sno in(select sno from sc where cno=2);
```

# 表
## 5.1 创建表
语法格式：

```sql
create table 表名(
  字段名1 数据类型,
  字段名2 数据类型,
  字段名3 数据类型,
  ......
);
```

例如：创建学生表

```sql
create table t_student(
  no int,
  name varchar,
  gender char(1) default '男'
);
```

## 5.2 插入数据
语法格式：

```sql
insert into 表名(字段名1, 字段名2, 字段名3,......) values (值1,值2,值3,......);
```

字段名和值要一一对应。类型要一一对应，数量要一一对应。

字段名也可以省略，如果字段名省略就表示把所有字段名都写上去了，并且顺序和建表时的顺序相同。

## 5.3 删除表
语法格式：

```sql
drop table 表名;
```

或者

```sql
drop table if exists 表名;
```

判断是否存在这个表，如果存在则删除。避免不存在时的报错。

## 5.4 MySQL数据类型
数据类型（data_type）是指系统中所允许的数据的类型。数据库中的每个列都应该有适当的数据类型，用于限制或允许该列中存储的数据。例如，列中存储的为数字，则相应的数据类型应该为数值类型。

如果使用错误的数据类型可能会严重影响应用程序的功能和性能，所以在设计表时，应该特别重视数据列所用的数据类型。更改包含数据的列不是一件小事，这样做可能会导致数据丢失。因此，在创建表时必须为每个列设置正确的数据类型和长度。

MySQL 的数据类型可以分为整数类型、浮点数类型、定点数类型、日期和时间类型、字符串类型、二进制类型等。

### 5.4.1 整数类型
tinyint：1个字节（微小整数）

smallint：2个字节（小整数）

mediumint：3个字节（中等大小的整数）

int（integer）：4个字节（普通大小整数）

bigint：8个字节（大整数）

### 5.4.2 浮点数类型
float：4个字节，单精度（最多5位小数）

double：8个字节，双精度（最多16位小数）

### 5.4.3 定点数类型
decimal：定点数类型。底层实际上采用字符串的形式存储数字。

语法：decimal(m, d)

例如：decimal(3, 2) 表示3个有效数字，2个小数。

### 5.4.4 日期和时间类型
year：1个字节，只存储年，格式YYYY

time：3个字节，只存储时间，格式HH:MM:SS / HHMMSS

date：3个字节，只存储年月日，格式：YYYY-MM-DD

datetime：8个字节，存储年月日+时分秒，格式：YYYY-MM-DD HH:MM:SS（从公元1000年~公元9999年）

timestamp：4个字节，存储年月日+时分秒，格式：YYYY-MM-DD HH:MM:SS（从公元1980年~公元2040年）或者格式为 <font style="color:#DF2A3F;">YYYYMMDDHHMMSS（采用这种格式不需要使用单引号，当然你使用单引号也可以）</font>

### 5.4.5 字符串类型
**char(m)：**m长度是0~255个字符。

固定长度字符串，在定义时指定字符串列长。当保存时，在右侧填充空格以达到指定的长度。m表示列的长度，范围是 0～255 个字符。

例如，CHAR(4) 定义了一个固定长度的字符串列，包含的字符个数最大为 4。当检索到 CHAR 值时，尾部的空格将被删除。

**varchar(m)：**m长度是0~16383个字符

长度可变的字符串。varchar 的最大实际长度由最长的行的大小和使用的字符集确定，而实际占用的空间为字符串的实际长度加 1。

例如，varchar(50) 定义了一个最大长度为 50 的字符串，如果插入的字符串只有 10 个字符，则实际存储的字符串为 10 个字符和一个字符串结束字符。varchar在值保存和检索时尾部的空格仍保留。

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1678606760951-7d88aef7-4f6a-47cb-bd13-88af106eabbe.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

**text类型：**

- tinytext 表示长度为 255字符的 TEXT 列。
- text 表示长度为 65535字符的 TEXT 列。
- mediumtext 表示长度为 16777215字符的 TEXT 列。
- longtext 表示长度为 4294967295 或 4GB 字符的 TEXT 列。

**enum类型：**

- 语法：<字段名> enum('值1','值2',...)
- 该字段插入值时，只能是指定的枚举值。

**set类型：**

- 语法：<字段名> set('值1','值2','值3',...)   <font style="color:#DF2A3F;">注意：值不可重复</font>。
- 该字段插入值时，只能是指定的值。

### 5.4.6 二进制类型
BLOB类型：二进制大对象，可以存储图片、声音、视频等文件。

- blob：小的，最大长度65535个字节
- mediumblob：中等的，最大长度16777215个字节
- longblob：大的，最大长度4GB的字节

## 5.5 增删改表结构DDL
### 创建一个学生表

```sql
create table t_student(
  no bigint,
  name varchar(255),
  age int comment '年龄'
);
```

### 查看建表语句

```sql
show create table 表名;
```

### 修改表名

```sql
alter table 表名 rename 新表名;
```

### 新增字段

```sql
alter table 表名 add 字段名 数据类型;
```

### 修改字段名

```sql
alter table 表名 change 旧字段名 新字段名 数据类型;
```

### 修改字段数据类型

```sql
alter table 表名 modify column 字段名 数据类型;
```

### 删除字段

```sql
alter table 表名 drop 字段名;
```

## 5.6 DML语句
当我们对表中的数据进行增删改的时候，称它为DML语句。（数据操纵语言），主要包括：insert、delete、update

### 5.6.1 insert 增
语法格式：

```sql
insert into 表名(字段名1,字段名2,字段名3,...) values(值1,值2,值3,...);
```

表名后面的小括号当中的字段名如果省略掉，表示自动将所有字段都列出来了，并且字段的顺序和建表时的顺序一致。

一般为了可读性强，建议把字段名写上。

```sql
insert into 表名 values(值1,值2,值3,...);
```

一次可以插入多条记录：

```sql
insert into t_stu(no,name,age) values(1,'jack',20),(2,'lucy',30);
```

### 5.6.2 delete 删
语法格式：

```sql
# 将所有记录全部删除
delete from 表名;

# 删除符合条件的记录
delete from 表名 where 条件;
```

以上的删除属于DML的方式删除，这种删除的数据是可以通过事务回滚的方式重新恢复的，但是删除的效率较低。（这种删除是支持事务的。）

另外还有一种删除表中数据的方式，但是这种方式不支持事务，不可以回滚，删了之后数据是永远也找不回来了。这种删除叫做：表被截断。

注意：这个语句删除效率非常高，巨大的表，瞬间干掉所有数据。但不可恢复。

```sql
truncate table 表名;
```

### 5.6.3 update 改
语法格式：

```sql
update 表名 set 字段名1=值1, 字段名2=值2, 字段名3=值3 where 条件;
```

如果没有更新条件的话，所有记录全部更新。

## 5.7 约束constraint
创建表时，可以给表的字段添加约束，可以保证数据的完整性、有效性。比如大家上网注册用户时常见的：用户名不能为空。对不起，用户名已存在。等提示信息。

约束通常包括：

- 非空约束：not null
- 检查约束：check
- 唯一性约束：unique
- 主键约束：primary key
- 外键约束：foreign key

### 5.7.1 非空约束
语法格式：

```sql
create table t_stu(
  no int,
  name varchar(255) not null,
  age int
);
```

name字段不能为空。插入数据时如果没有给name指定值，则报错。

### 5.7.2 检查约束

```sql
create table t_stu(
  no int,
  name varchar(255),
  age int,
  check(age > 18)
);
```

### 5.7.3 唯一性约束
语法格式：

```sql
create table t_stu(
  no int,
  name varchar(255),
  email varchar(255) unique
);
```

email字段设置为唯一性，唯一性的字段值是可以为NULL的。但不能重复。以上在字段后面添加的约束，叫做列级约束。

当然，添加约束还有另一种方式：表级约束：

```sql
create table t_stu(
  no int,
  name varchar(255),
  email varchar(255),
  unique(email)
);
```

使用表级约束可以为多个字段添加联合唯一。

```sql
create table t_stu(
  no int,
  name varchar(255),
  email varchar(255),
  unique(name,email)
);
```

创建约束时也可以给约束起名字，将来可以通过约束的名字来删除约束：

```sql
create table t_stu(
  no int,
  name varchar(255),
  email varchar(255),
  constraint t_stu_name_email_unique unique(name,email)
);
```

所有的约束都存储在一个系统表当中：table_constraints。这个系统表在这个数据库当中：information_schema

### 5.7.4 主键约束
1. 主键：primary key，简称PK
2. 主键约束的字段不能为NULL，并且不能重复。
3. 任何一张表都应该有主键，没有主键的表可以视为无效表。
4. 主键值是这行记录的身份证号，是唯一标识。在数据库表中即使两条数据一模一样，但由于主键值不同，我们也会认为是两条完全的不同的数据。
5. 主键分类：
    1. 根据字段数量分类：
        1. 单一主键（1个字段作为主键）<font style="color:#DF2A3F;">==>建议的</font>
        2. 复合主键（2个或2个以上的字段作为主键）
    2. 根据业务分类：
        1. 自然主键（主键和任何业务都无关，只是一个单纯的自然数据）<font style="color:#DF2A3F;">===>建议的</font>
        2. 业务主键（主键和业务挂钩，例如：银行卡账号作为主键）
6. 单一主键（建议使用这种方式）

```sql
create table t_student(
  id bigint primary key,
  sno varchar(255) unique,
  sname varchar(255) not null
)
```

7. 复合主键（很少用，了解）

```sql
create table t_user(
  no int,
  name varchar(255),
  age int,
  constraint t_user_pk_no_name primary key(no,name)
);
```

8. 主键自增：既然主键值是一个自然的数字，mysql为主键值提供了一种自增机制，不需要我们程序员维护，mysql自动维护该字段

```sql
create table t_vip(
  no int primary key auto_increment,
  name varchar(255)
);
```

### 5.7.5 外键约束
1. 有这样一个需求：要求设计表，能够存储学生以及学校信息。
    1. 第一种方案：一张表

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1679198700192-73c1c697-39a5-483e-b267-730fb808082d.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_25%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

这种方式会导致数据冗余，浪费空间。

    2. 第二种方案：两张表：一张存储学生，一张存储学校

t_school 表

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1679198814824-520944e2-5b83-49ba-97e7-b8830286127a.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_13%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

t_student 表

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1679198856678-a80be906-abc8-4bf7-ac5e-e6a59b11c48a.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

如果采用以上两张表存储数据，对于学生表来说，sno这个字段的值是不能随便填的，这个sno是学校编号，必须要求这个字段中的值来自学校表的sno。

为了达到要求，此时就必须要给t_student表的sno字段添加外键约束了。

2. 外键约束：foreign key，简称FK。
3. 添加了外键约束的字段中的数据必须来自其他字段，不能随便填。
4. 假设给a字段添加了外键约束，要求a字段中的数据必须来自b字段，b字段不一定是主键，但至少要有唯一性。
5. 外键约束可以给单个字段添加，叫做单一外键。也可以给多个字段联合添加，叫做复合外键。复合外键很少用。
6. a表如果引用b表中的数据，可以把b表叫做父表，把a表叫做子表。
    1. 创建表时，先创建父表，再创建子表。
    2. 插入数据时，先插入父表，在插入子表。
    3. 删除数据时，先删除子表，再删除父表。
    4. 删除表时，先删除子表，再删除父表。
7. 如何添加外键：

```sql
create table t_school( 
  sno int primary key, 
  sname varchar(255) 
); 
create table t_student( 
  no int primary key, 
  name varchar(255), 
  age int, 
  sno int, 
  constraint t_school_sno_fk foreign key(sno) references t_school(sno) 
);
```

8. 级联删除

创建子表时，外键可以添加：on delete cascade，这样在删除父表数据时，子表会级联删除。谨慎使用。

```sql
create table t_student( 
  no int primary key, 
  name varchar(255), 
  age int, 
  sno int, 
  constraint t_school_sno_fk foreign key(sno) references t_school(sno) on delete cascade 
);
```

```sql
###删除约束
alert table t_student drop foreign key t_student_sno_fk;
###添加约束
alert table t_student add constraint t_student_sno_fk foreign key(sno) references t_school(sno) on delete cascade;
```

9. 级联更新 

```sql
create table t_student( 
  no int primary key, 
  name varchar(255), 
  age int, 
  sno int, 
  constraint t_school_sno_fk foreign key(sno) references t_school(sno) on update cascade 
);
```

10. 级联置空

```sql
create table t_student( 
  no int primary key, 
  name varchar(255), 
  age int, 
  sno int, 
  constraint t_school_sno_fk foreign key(sno) references t_school(sno) on delete set null 
);
```

# 数据库设计三范式
1. 什么是数据库设计三范式？
    1. 数据库表设计的原则。教你怎么设计数据库表有效，并且节省空间。
2. 三范式
    1. 第一范式：任何一张表都应该有主键，每个字段是原子性的不能再分
        1. 以下表的设计不符合第一范式：无主键，并且联系方式可拆分。

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1679201425169-4ce0b510-2795-4ac8-a0ca-404ffcb6c044.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_12%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

        2. 应该这样设计：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1679201619568-bcb56e54-e4d5-4152-9833-49d97afa8d35.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_13%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

    2. 第二范式：建立在第一范式基础上的，另外要求所有非主键字段完全依赖主键，不能产生部分依赖
        1. 以下表存储了学生和老师的信息

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1679201885946-02cacd49-4288-4520-93fb-e4dae6cff5dc.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_13%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

虽然符合第一范式，但是违背了第二范式，学生姓名、老师姓名都产生了部分依赖。导致数据冗余。

        2. 以下这种设计方式就是符合第二范式的：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1679202122322-da28bdc0-703b-4975-8fe4-0a7b6a222fee.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_19%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

    3. 第三范式：建立在第二范式基础上的，非主键字段不能传递依赖于主键字段
        1. 以下设计方式就是违背第三范式的

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1679202299108-66198c2a-933d-4bea-9e67-51425c31be7c.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_12%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

以上因为产生了传递依赖，导致班级名称冗余。

        2. 以下这种方式就是符合第三范式的：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1679202402829-5040060c-c87f-4411-a599-6a60cc3836a0.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

3. 一对多怎么设计？
    1. 口诀：一对多两张表，多的表加外键。
    2. ![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1679200526299-5a9122fe-b7f6-423c-9fd8-5c28a960cb75.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_14%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)
    3. ![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1679200546241-3a0db05e-74e8-4452-92b9-721c5b3d36d5.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)
4. 多对多怎么设计？
    1. 多对多三张表，关系表添加外键。
    2. ![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1679200858013-26513a66-0af8-4b84-bd90-b52a240de65c.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_27%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)
5. 一对一怎么设计？
    1. 两种方案：
        1. 第一种：主键共享
            1. ![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1679201037367-a1b5661a-f127-42b0-87d9-609c61fa4839.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_14%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)
        2. 第二种：外键唯一
            1. ![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1679201084526-c5773a4e-75bf-4e6d-9ac4-f8b8272d1b46.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_20%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)
6. 最终的设计？
    1. 最终以满足客户需求为原则，有的时候会拿空间换速度。

# 视图
1. 只能将select语句创建为视图。
2. 创建视图

```sql
create or replace view v_emp as select e.ename,d.dname from emp e join dept d on e.deptno = d.deptno;
```

3. 视图作用
    1. 如果开发中有一条非常复杂的SQL，而这个SQL在多处使用，会给开发和维护带来成本。使用视图可以降低开发和维护的成本。
    2. 视图可以隐藏表的字段名。
4. 修改视图

```sql
alter view v_emp as select e.ename,d.dname,d.deptno from emp e join dept d on e.deptno = d.deptno;
```

5. 删除视图
    1. drop view if exists v_emp;
6. 对视图增删改可以影响到原表数据。

# 事务
1. 什么是事务？
    1. 事务是一个最小的工作单元。在数据库当中，事务表示一件完整的事儿。
    2. 一个业务的完成可能需要多条DML语句共同配合才能完成，例如转账业务，需要执行两条DML语句，先更新张三账户的余额，再更新李四账户的余额，为了保证转账业务不出现问题，就必须保证要么同时成功，要么同时失败，怎么保证同时成功或者同时失败呢？就需要使用事务机制。
    3. 也就是说用了事务机制之后，在同一个事务当中，多条DML语句会同时成功，或者同时失败，不会出现一半成功，一半失败的现象。
2. 事务只针对DML语句有效：因为只有这三个语句是改变表中数据的。
    1. insert
    2. delete
    3. update
3. 事务四大特性：ACID
    1. 原子性（Atomicity）：是指事务包含的所有操作要么全部成功，要么同时失败。
    2. 一致性（Consistency）：是指事务开始前，和事务完成后，数据应该是一致的。例如张三和李四的钱加起来是5000，中间不管进行过多少次的转账操作(update)，总量5000是不会变的。这就是事务的一致性。
    3. 隔离性（Isolation）：隔离性是当多个⽤户并发访问数据库时，⽐如操作同⼀张表时，数据库为每⼀个⽤户开启的事务，不能被其他事务的操作所⼲扰，多个并发事务之间要相互隔离。
    4. 持久性（Durability）：持久性是指⼀个事务⼀旦被提交了，那么对数据库中的数据的改变就是永久性的，即便是在数据库系统遇到故障的情况下也不会丢失提交事务的操作。
4. 演示MySQL事务
    1. 在dos命令窗口中开启MySQL事务：start transaction; 或者：begin;
    2. 回滚事务：rollback; 
    3. 提交事务：commit;

只要执行以上的rollback或者commit，事务都会结束。

MySQL默认情况下采用的事务机制是：自动提交。所谓自动提交就是只要执行一条DML语句则提交一次。

了解内容：

savepoint p1; 将事务保存在某个点。

rollback to savepoint p1; 将事务回滚到保存点。

5. 事务隔离级别：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1679213953232-4c17a795-8b1f-45d2-907b-c5c16aff672d.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_22%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

脏读：能够读取到别人没有提交的数据。

不可重复读：在同一个事务中，第一次读取到的数据可能和第二次读取到的数据不同。

幻读：读取到的数据不够真实。

6. mysql默认的隔离级别：可重复读。
    1. 查看当前会话的隔离级别：select @@transaction_isolation;
    2. 查看全局的隔离级别：select @@gobal.transaction_isolation;
7. 设置事务隔离级别：
    1. 会话级：set transaction isolation level read committed;
    2. 全局级：set global transaction isolation level read committed;
8. 演示事务隔离级别。

# DBA命令
## 1. 新建用户
创建一个用户名为java1，密码设置为123的本地用户：

```sql
create user 'java1'@'localhost' identified by '123';
```

创建一个用户名为java2，密码设置为123的外网用户：

```sql
create user 'java2'@'%' identified by '123';
```

采用以上方式新建的用户没有任何权限：系统表也只能看到以下两个

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1679813363625-10cc7c30-76b3-4a1a-a83f-a1727489a420.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_14%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

使用root用户查看系统中当前用户有哪些？

```sql
select user,host from mysql.user;
```

## 2. 给用户授权
授权语法：grant [权限1，权限2...] on 库名.表名 to '用户名'@'主机名/IP地址';

给本地用户授权：grant [权限1，权限2...] on 库名.表名 to '用户名'@'<font style="color:#DF2A3F;">localhost</font>';

给外网用户授权：grant [权限1，权限2...] on 库名.表名 to '用户名'@'<font style="color:#DF2A3F;">%</font>';

所有权限：all privileges

细粒度权限：select、insert、delete、update、alter、create、drop、index(索引)、usage(登录权限)......

库名可以使用 * ，它代表所有数据库

表名可以采用 * ，它代表所有表

也可以提供具体的数据库和表，例如：powernode.emp （powernode数据库的emp表）

```sql
# 将所有库所有表的查询权限赋予本地用户java1
grant select on *.* to 'java1'@'localhost';

# 将powernode库中所有表的所有权限赋予本地用户java1
grant all privileges on powernode.* to 'java1'@'localhost';
```

授权后必须刷新权限，才能生效：<font style="color:#DF2A3F;">flush privileges</font>

<font style="color:#000000;">查看某个用户拥有哪些权限？</font>

<font style="color:#000000;">show grants for 'java1'@'localhost'</font>

<font style="color:#000000;">show grants for 'java2'@'%'</font>

with grant option：

```sql
# with grant option的作用是：java2用户也可以给其他用户授权了。
grant select,insert,delete,update on powernode.* to 'java2'@'%' with grant option;
```

## 3. 撤销用户权限
revoke 权限 on 数据库名.表名 from '用户'@'IP地址';

```sql
# 撤销本地用户java1的insert、update、delete权限
revoke insert, update, delete on powernode.* from 'java1'@'localhost'

# 撤销外网用户java2的insert权限
revoke insert on powernode.* from 'java2'@'%'
```

撤销权限后也需要刷新权限：flush privileges

## 4. 修改用户的密码
具有管理用户权限的用户才能修改密码，例如root账户可以修改其他账户的密码：

```sql
# 本地用户修改密码
alter user 'java1'@'localhost' identified by '456';

# 外网用户修改密码
alter user 'java2'@'%' identified by '456';
```

修改密码后，也需要刷新权限才能生效：flush privileges

以上是MySQL8版本以后修改用户密码的方式。

## 5. 修改用户名

```sql
rename user '原始用户名'@'localhost' to '新用户名'@'localhost';
rename user '原始用户名'@'localhost' to '新用户名'@'%';

rename user 'java1'@'localhost' to 'java11'@'localhost';
rename user 'java11'@'localhost' to 'java123'@'%';
```

flush privileges;

## 6. 删除用户

```sql
drop user 'java123'@'localhost';
drop user 'java2'@'%';
```

flush privileges;

## 7. 数据备份
- 导出数据（请在登录mysql数据库之前进行）

```sql
# 导出powernode这个数据库中所有的表
mysqldump powernode > d:/powernode.sql -uroot -p123456

# 导出powernode中emp表的数据
mysqldump powernode emp > d:/powernode.sql -uroot -p123456
```

- 导入数据（请在登录mysql之后操作）

```sql
create  database powernode;
use powernode;
source d:/powernode.sql
```

# MySQL客户端工具
1. 对于后端开发人员来说，一个好的MySQL客户端工具可以大大提升开发效率。目前企业中使用最多的是以下三个：
    1. Navicat for MySQL

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1679825266467-a704f0ce-835d-48c6-ab37-4c7bf5a1be57.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_12%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

    2. SQLyog

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1679825351769-5a2abe9e-cabb-407f-87e5-1aafeada40bd.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_9%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

    3. MySQL Workbench

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1679825234020-fa921858-476d-44c8-8074-1c0b137f2eaf.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_9%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

2. 安装Navicat for MySQL
3. 使用Navicat for MySQL
    1. 客户端连接MySQL服务器
    2. 创建数据库（字符集的选择）
    3. 创建表，设置主键，并且主键自增
    4. 添加数据（开启事务提交事务）
    5. 删除数据
    6. 修改数据
    7. 导出SQL脚本，导入SQL脚本
    8. 执行查询（全部执行和选择执行）
    9. 事务
    10. 外键

# 企业真题
## 第一题
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1680103320228-5ed4903b-6a54-4ce8-81c6-e3f1738eac95.jpeg?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

```sql
# 第一步：找小于等于80分的学员姓名
select distinct name from t_student where fenshu <= 80

# 第二步：not in
select distinct name from t_student where name not in(select distinct name from t_student where fenshu <= 80)
```

## 第二题
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1680103877015-ca07133d-716e-4cce-82f3-52118ff4c9ad.jpeg?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_18%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1680104265213-8afaf5de-a962-47c6-a1cd-72aefe28f616.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_21%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

其中，两个表的关联字段为申请单号。

1）查询身份证号为440401430103082的申请日期。

2）查询同一个身份证号码有两条以上记录的身份证号码及记录个数。

3）将身份证号码为440401430103082的记录在两个表中的申请状态均改为07。 

4）删除g_cardapplydetail表中所有姓李的记录。

模拟数据：考试做这种题目最重要的是要冷静下来，只有静下来SQL才能写好。要模拟数据。看到数据SQL就好写了。

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1680105543048-1dd227b9-f2e8-4daf-8b1b-155db36db813.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_29%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

1）查询身份证号为440401430103082的申请日期。

bigint转date，可以使用from_unixtime函数。

```sql
select a.g_applydate from g_cardapply a join g_cardapplydetail b on a.g_applyno = b.g_applyno where b.g_idcard = '440401430103082'
```

2）查询同一个身份证号码有两条以上记录的身份证号码及记录个数。

```sql
select count(g_idcard),g_idcard from g_cardapplydetail group by g_idcard having count(g_idcard) >= 2
```

3）将身份证号码为440401430103082的记录在两个表中的申请状态均改为07。

```sql
UPDATE 
	g_cardapply
JOIN 
	g_cardapplydetail 
ON 
	g_cardapply.g_applyno = g_cardapplydetail.g_applyno 
AND
	g_cardapplydetail.g_idcard = '440401430103082'
SET g_cardapply.g_state = '07',
g_cardapplydetail.g_state = '07'
```

4）删除g_cardapplydetail表中所有姓李的记录。

```sql
delete t1,t2 from g_cardapply t1 join g_cardapplydetail t2 on t1.g_applyno=t2.g_applyno where t2.g_name like '李%';
```

## 第三题
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1680142491993-8e350bec-9af7-4304-b7d6-92f2f313997e.jpeg?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_24%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1680142491981-3d90f70c-a859-4937-bdb7-60988985ea54.jpeg?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_24%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

表名：stuscore

1）统计如下：课程不及格[0~59]的多少个，良[60~80]多少个，优[81-100]多少个。

2）计算科科及格的人的平均成绩。

## 第四题
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1680144969653-7096e822-b1e5-44d4-bc34-55dacc9322b4.jpeg?x-oss-process=image%2Fauto-orient%2C1%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_24%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

1）请用一条SQL语句查询出不同部门中担任“钳工”的职工平均工资。

2）请用一条SQL语句查询出不同部门中担任“钳工”的职工平均工资高于2000的部门。

## 第五题
![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1680398222140-816dc325-2887-46aa-96ba-57b6f1c52c25.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_35%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

Employee是雇员信息表：

雇员姓名（主键）：person-name

街道：street

城市：city

Company是公司信息表：

公司名称（主键）：company-name

城市：city

Works是雇员工作信息表：

雇员姓名（主键）：person-name

公司名称：company-name

年薪：salary

Manages是雇员工作关系表：

雇员姓名（主键）：person-name

经理姓名：manager-name

模拟数据：

员工表：employee

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1680402378306-a5369a92-0751-468b-8ef2-2e65aee24d31.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

公司表：company

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1680402457539-3684d5f1-8e7e-470b-95f7-56b3d48e4cee.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_16%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

雇员工作信息表：Works

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1680402493037-5384139c-9959-4e34-8ce8-d0be11ea4563.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_13%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

雇员工作关系表：Manages

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1680402526039-fe04bfb3-e33b-4cbb-bc94-f680f0ae2a8e.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_14%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

请给出下面每一个查询的SQL语句：

1. 找出所有居住地与工作的公司在同一城市的员工的姓名。
2. 找出比Small Bank Corporation的所有员工收入都高的所有员工的姓名。
3. 找出平均年薪在10000美元以上的公司及其平均年薪。

## 第六题
![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1680399293078-ccb0ac3b-7273-4308-8f01-12705c3ed1fd.jpeg?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_22%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)![](https://cdn.nlark.com/yuque/0/2023/jpeg/21376908/1680399293094-1a4ca298-63ad-48db-9e8b-27ce4a6846a2.jpeg?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_36%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

客户表Client

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1680399899003-07e5e8a6-78d4-4939-b914-bf9280dcc3eb.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_11%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

订单表Order

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1680400992647-08ba0bcf-1ff6-45c7-a82e-3918a9f9e950.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_11%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

客户订单表ClientOrder

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1680400979869-ea2a1837-751b-4744-98a5-e04c9808b568.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_10%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

图书表Book

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1680401007501-200e3826-48ed-4638-8095-7be52757bdf1.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_14%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

1. 请写出一条SQL语句，查询出每个客户的所有订单并按照地址排序，要求输出格式为：address client_name phone order_id
2. 请写出一条SQL语句，查询出每个客户订购的图书总价。要求输出格式为：client_name total_price
3. 如果要求每个订单可以包含多种图书，应该如何修改Order表的主键？为了保证每个订单只被一个客户拥有，应该在ClientOrder表上增加怎样的约束？

## 第七题
![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1680403317776-7cd6d3bc-b547-4d94-9521-186a89ab67df.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_19%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1680403354657-0faf25ca-bb17-44ea-ade0-8a4e386756f3.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_21%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

模拟数据：

学生表：student

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1680405687756-49b16a32-1f8b-42b5-b4a3-cd8c231e79f0.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

课程表：course

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1680405700061-a86b3354-1d10-4be5-96fe-63ba01c8d7b4.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_12%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

成绩表：sc

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1680405996312-907e4929-7d55-4d62-9e8d-1281bdafe91a.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_13%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

教师表：teacher

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1680406005728-731d61b6-02a6-448d-8a66-000b0aa3a9e6.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_9%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

1. 查询1号课比2号课成绩高的所有学生学号。
2. 查询平均成绩大于60分的学号和平均成绩。
3. 查询所有学生学号、姓名、选课数、总成绩。
4. 查询姓“李”的老师的个数。
5. 查询没学过“叶平”老师课的学号、姓名。

## 第八题
![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1680403650729-b44beed8-c599-4077-8f43-8f862b94bfcd.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_17%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

学生表：student

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1680406785079-9ec12300-6db8-48b8-ad77-7d64ebcf4292.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_9%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

课程表：class

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1680406801984-082cd575-80cc-432e-9c19-c247c194fa40.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_10%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

选课表：chosen_class

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1680406813282-256975bc-ab6c-49f9-8d83-e5f60d2a00ed.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

1. 没有选修课程编号为C1的学生姓名
2. 列出每门课程名称和平均成绩，并按照成绩排序
3. 选了2门课以上的学生姓名。

## 第九题
![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1680403903386-c1b30b13-93ed-4b1a-a331-e4107c17d411.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_16%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1688106505123-a5edeb3b-0cdb-4ee3-befd-4a462fccbddd.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_13%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

要转换成：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1688106694493-9f831520-223c-4904-963a-3df0a7edb66a.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_11%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

### MySQL行转列

MySQL行转列又叫做**<font style="color:#DF2A3F;">数据透视</font>**。什么叫做行转列？将原本横向排列的数据透视成纵向排列的数据，进而进行计算、分析、展示等操作。

假设有一个学生选课成绩表，包含学生姓名（stu_name）、课程名称（course_name）和分数（score）三个字段。在原始数据中，每个学生在不同的课程中都有自己的得分情况，数据样例如下：

| stu_name | course_name | score |
| --- | --- | --- |
| 张三 | 数学 | 80 |
| 张三 | 英语 | 85 |
| 张三 | 历史 | 90 |
| 李四 | 数学 | 75 |
| 李四 | 英语 | 92 |
| 李四 | 历史 | 85 |
| 王五 | 数学 | 88 |
| 王五 | 英语 | 90 |
| 王五 | 历史 | 95 |

可以使用行转列操作，将每个学生在不同课程中的分数拆分成多条记录，每条记录包含一个课程以及对应的分数。转换后的数据样例如下：

| stu_name | 数学 | 英语 | 历史 |
| --- | --- | --- | --- |
| 张三 | 80 | 85 | 90 |
| 李四 | 75 | 92 | 85 |
| 王五 | 88 | 90 | 95 |

从上表中可以看出，在行转列之后，每一行记录都表示了一个学生在不同课程中的分数。这样更便于对不同科目的分数进行比较、计算平均值等分析操作。

#### 使用case when+group by完成

```sql
drop table if exists t_student;
create table t_student(
  stu_name varchar(10),
  course_name varchar(10),
  score int
);
insert into t_student(stu_name, course_name, score) values('张三', '数学', 80);
insert into t_student(stu_name, course_name, score) values('张三', '英语', 85);
insert into t_student(stu_name, course_name, score) values('张三', '历史', 90);
insert into t_student(stu_name, course_name, score) values('李四', '数学', 75);
insert into t_student(stu_name, course_name, score) values('李四', '英语', 92);
insert into t_student(stu_name, course_name, score) values('李四', '历史', 85);
insert into t_student(stu_name, course_name, score) values('王五', '数学', 88);
insert into t_student(stu_name, course_name, score) values('王五', '英语', 90);
insert into t_student(stu_name, course_name, score) values('王五', '历史', 95);
commit;
select * from t_student;
```

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1688106054073-451f919c-a97a-4c49-af03-991c86d78107.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_10%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

行转列后的效果是：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1688106114109-3c583e45-5324-47f7-b53c-f90e31dcdc82.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

sql如下：

```sql
select
	stu_name,
	max(case course_name when '数学' then score else 0 end) as '数学',
	max(case course_name when '英语' then score else 0 end) as '英语', 
	max(case course_name when '历史' then score else 0 end) as '历史' 
from 
	t_student
group by 
	stu_name;
```

通过以上内容的学习，我们这个面试题就迎刃而解了：

```sql
select
	year,
	max(case season when '一季度' then count else 0 end) as '一季度',
	max(case season when '二季度' then count else 0 end) as '二季度',
	max(case season when '三季度' then count else 0 end) as '三季度',
	max(case season when '四季度' then count else 0 end) as '四季度'
from 
	t_temp 
group by 
	year;
```

#### 
## 第十题
![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1680403550525-8f28573a-a583-4aaa-9e91-b5dde5ffa2f3.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_16%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

```sql
select 
	x.a 开始数字, y.a 结束数字
from 
	(select m.a,row_number() over(order by m.a) as rownum from (select a, lag(a) over(order by a asc) as pre_a from t) m where m.a - m.pre_a != 1 or m.pre_a is null) x 
join 
	(select n.a,row_number() over(order by n.a) as rownum from (select a, lead(a) over(order by a asc) as next_a from t) n where n.next_a - n.a != 1 or n.next_a is null) y 
on 
	x.rownum = y.rownum;
```

解答上面这个题目需要具备以下知识点：

- lag函数
- lead函数
- row_number函数

**<font style="color:#DF2A3F;">lag函数</font>**：获取当前行的上一行数据

```sql
select empno,ename,sal,(lag(sal) over(order by sal asc)) as pre_sal from emp;
```

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1688354808296-69cf1cf1-34e3-4b99-b4a2-2c575b0e2378.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

注意：over函数用来指定“在.....范围内”，通常和lag函数联用。

**<font style="color:#DF2A3F;">lead函数</font>**：获取当前行的下一行数据

```sql
select empno,ename,sal,(lead(sal) over(order by sal asc)) as next_sal from emp;
```

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1688355552758-57bb77a0-65d4-4717-8410-35c1f6c13e0e.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

注意：over函数用来指定“在.....范围内”，通常和lead函数联用。

**<font style="color:#DF2A3F;">row_number函数</font>**：可以为查询结果集生成行号：

```sql
select empno,ename,sal,row_number() over(order by sal) as rownum from emp;
```

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1688372778734-b8b7d759-d86d-43d5-807a-8447c8de7da4.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_14%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

利用row_number函数，将两个不相关的列拼接在一起显示：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1688372898512-55c19a9b-401d-49db-8ad3-10e64b2fc161.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_14%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1688372915619-8c9bb2e9-7023-43e7-88f1-ca17090825f0.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_14%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

```sql
select 
	x.a, y.b 
from 
	(select a,row_number() over(order by a) as rownum from t1) x 
join 
	(select b,row_number() over(order by b) as rownum from t2) y 
on 
	x.rownum = y.rownum;
```

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1688373063344-4437fa76-e5b6-4747-b189-9c3ae2ace4c0.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_9%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

CTE语法（公用表表达式）：Common Table Expression。创建临时表的一种语法：

```sql
-- 查询每个部门平均工资的工资等级
-- 第一种写法
select 
	t.deptno,t.avgsal,s.grade 
from 
	(select deptno,avg(sal) as avgsal from emp group by deptno) t 
join 
	salgrade s 
on 
	t.avgsal between s.losal and s.hisal;

-- 第二种写法：使用CTE语法
with cte_exp as(select deptno,avg(sal) as avgsal from emp group by deptno)
select 
	cte_exp.deptno,cte_exp.avgsal,s.grade
from
	cte_exp
join
	salgrade s
on
	cte_exp.avgsal between s.losal and s.hisal;
```

partition by：将数据分区，和group by区别是：group by是分组，然后和分组函数一起用。partition by分区不需要和分组函数一起使用

```sql
select deptno, empno,ename,sal,(lag(sal) over(partition by deptno order by sal asc)) as pre_sal from emp;
```

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1688355470071-e5e90e50-2b69-4126-bd79-a2118fb80e66.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_12%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

MySQL 8.0及以上版本中支持如下常用的窗口函数：

1. ROW_NUMBER()：排名函数，返回当前结果集中每个行的行号；
2. RANK()：排名函数，计算分组结果中的排名，相同的行排名相同且没有空缺，下一个行排名跳过空缺；
3. DENSE_RANK()：排名函数，计算分组结果中的排名，相同的行排名相同，排名连续，没有空缺；
4. NTILE()：将分组结果等分为指定的组数，计算每组的大小；
5. LAG()：返回分组内前一行的值；
6. LEAD()：返回分组内后一行的值；
7. FIRST_VALUE()：返回分组内第一个值；
8. LAST_VALUE()：返回分组内最后一个值；
9. AVG()、SUM()、COUNT()、MIN()、MAX()：聚合函数，可以配合OVER()进行窗口操作。

需要注意的是，MySQL的窗口函数和其他DBMS中的窗口函数相比较，可能略有不同，需要根据MySQL的文档进行使用。 

# 存储过程
## 1. 什么是存储过程？
存储过程可称为过程化SQL语言，是在普通SQL语句的基础上增加了编程语言的特点，把数据操作语句(DML)和查询语句(DQL)组织在过程化代码中，通过逻辑判断、循环等操作实现复杂计算的程序语言。

换句话说，存储过程其实就是数据库内置的一种编程语言，这种编程语言也有自己的变量、if语句、循环语句等。在一个存储过程中可以将多条SQL语句以逻辑代码的方式将其串联起来，执行这个存储过程就是将这些SQL语句按照一定的逻辑去执行，所以一个存储过程也可以看做是一组为了完成特定功能的SQL 语句集。

每一个存储过程都是一个数据库对象，就像table和view一样，存储在数据库当中，一次编译永久有效。并且每一个存储过程都有自己的名字。客户端程序通过存储过程的名字来调用存储过程。

在数据量特别庞大的情况下利用存储过程能达到倍速的效率提升。 

## 2. 存储过程的优点和缺点？
优点：速度快。

        * 降低了**应用服务器**和**数据库服务器**之间网络通讯的开销。尤其在数据量庞大的情况下效果显著。

缺点：移植性差。编写难度大。维护性差。

        * 每一个数据库都有自己的存储过程的语法规则，这种语法规则不是通用的。一旦使用了存储过程，则数据库产品很难更换，例如：编写了mysql的存储过程，这段代码只能在mysql中运行，无法在oracle数据库中运行。
        * 对于数据库存储过程这种语法来说，没有专业的IDE工具（集成开发环境），所以编码速度较低。自然维护的成本也会较高。

在实际开发中，存储过程还是很少使用的。只有在系统遇到了性能瓶颈，在进行优化的时候，对于大数量的应用来说，可以考虑使用一些。

## 3. 第一个存储过程
### 存储过程的创建

```plsql
create procedure p1()
begin
	select empno,ename from emp;
end;
```

### 存储过程的调用

```plsql
call p1();
```

### 存储过程的查看

```plsql
show create procedure p1;
```

```sql
select * from information_schema.routines where routine_name = 'p1';
```

information_schema.ROUTINES 是 MySQL 数据库中一个系统表，存储了所有存储过程和函数的详细信息，包括它们的名称、类型、定义文件、创建时间、修改时间等。这个系统表的信息是基于当前连接到的 MySQL 服务器上的所有数据库。

information_schema.ROUTINES 表中的一些重要的列包括：

- ROUTINE_SCHEMA：存储过程或函数所在的数据库名称。
- ROUTINE_NAME：存储过程或函数的名称。
- ROUTINE_TYPE：存储过程或函数的类型，可以是 PROCEDURE 或 FUNCTION。
- ROUTINE_DEFINITION：存储过程或函数的定义语句。
- CREATED：存储过程或函数的创建时间。
- LAST_ALTERED：存储过程或函数的最后修改时间。

通过查询 information_schema.ROUTINES，可以获取存储过程和函数的详细元数据信息，并对它们进行管理和维护。比如，可以使用该表来获取数据库中所有的存储过程和函数，并查找特定的对象，以便对它们进行修改或删除。

需要注意的是，information_schema.ROUTINES 表中的信息是只读的，不允许直接更新数据。如果需要修改存储过程或函数，需要使用 ALTER PROCEDURE 或 ALTER FUNCTION 等语句进行修改。

### 存储过程的删除

```plsql
drop procedure if exists p1;
```

### delimiter命令
在 MySQL 中，`delimiter` 命令用于改变 MySQL 解释语句的定界符。MySQL 默认使用分号 `;` 作为语句的定界符。而使用 `delimiter` 命令可以将分号 `;` 更改为其他字符，从而可以在 SQL 语句中使用分号 `;`。

例如，假设需要创建一个存储过程。在存储过程中通常会包括多条 SQL 语句，而这些语句都需要以分号 `;` 结尾。但默认情况下，执行到第一条语句的分号 `;` 后，MySQL 就会停止解释，导致后续的语句无法执行。解决方式就是使用 `delimiter` 命令将分号改为其他字符，使分号 `;` 不再是语句定界符。例如：

```sql
delimiter //

CREATE PROCEDURE my_proc ()
BEGIN
SELECT * FROM my_table;
INSERT INTO my_table (col1, col2) VALUES ('value1', 'value2');
END //

delimiter ;
```

在这个例子中，我们使用 `delimiter //` 命令将定界符改为两个斜线 `//`。在存储过程中，以分号 `;` 结尾的语句不再被解释为语句的结束。而使用 `delimiter ;` 可以将分号恢复为语句定界符。

总之，`delimiter` 命令可以改变 MySQL 数据库系统中 SQL 查询语句的分隔符，从而可使一条 SQL 查询语句包含多个 SQL 语句。这样的话，就方便了我们在一个语句里面加入多个语句，而且不会被错

## 4. MySQL的变量
mysql中的变量包括：系统变量、用户变量、局部变量。

### 系统变量
MySQL 系统变量是指在 MySQL 服务器运行时控制其行为的参数。这些变量可以被设置为特定的值来改变服务器的默认设置，以满足不同的需求。

MySQL 系统变量可以具有全局（global）或会话（session）作用域。全局作用域是指对所有连接和所有数据库都适用；会话作用域是指只对当前连接和当前数据库适用。

查看系统变量

```sql
show [global|session] variables;

show [global|session] variables like '';

select @@[global|session.]系统变量名;
```

注意：没有指定session或global时，默认是session。

设置系统变量

```sql
set [global | session] 系统变量名 = 值;

set @@[global | session.]系统变量名 = 值;
```

注意：无论是全局设置还是会话设置，当mysql服务重启之后，之前配置都会失效。可以通过修改MySQL根目录下的my.ini配置文件达到永久修改的效果。（my.ini是MySQL数据库默认的系统级配置文件，默认是不存在的，需要新建，并参考一些资料进行配置。）

### 用户变量
用户自定义的变量。只在当前会话有效。所有的用户变量'@'开始。

给用户变量赋值

```sql
set @name = 'jackson';
set @age := 30;
set @gender := '男', @addr := '北京大兴区';
select @email := 'jackson@123.com';
select sal into @sal from emp where ename ='SMITH';
```

读取用户变量的值

```sql
select @name, @age, @gender, @addr, @email, @sal;
```

注意：mysql中变量不需要声明。直接赋值就行。如果没有声明变量，直接读取该变量，返回null

### 局部变量
在存储过程中可以使用局部变量。使用declare声明。在begin和end之间有效。

变量的声明

```sql
declare 变量名 数据类型 [default ...];
```

变量的数据类型就是表字段的数据类型，例如：int、bigint、char、varchar、date、time、datetime等。

**<font style="color:#DF2A3F;">注意：declare通常出现在begin end之间的开始部分。</font>**

变量的赋值

```sql
set 变量名 = 值;
set 变量名 := 值;
select 字段名 into 变量名 from 表名 ...;
```

例如：以下程序演示局部变量的声明、赋值、读取：

```sql
create procedure p2()
begin
	declare emp_count varchar default 0;
	select count(*) into emp_count from emp;
	select emp_count;
end;
```

```sql
call p2();
```

## 5. if语句
语法格式：

```sql
if 条件 then
......
elseif 条件 then
......
elseif 条件 then
......
else
......
end if
```

案例：员工月薪sal，超过10000的属于“高收入”，6000到10000的属于“中收入”，少于6000的属于“低收入”。

```sql
create procedure p3()
begin
	declare sal int default 5000;
	declare grade varchar(20);
	if sal > 10000 then
  	set grade := '高收入';
	elseif sal >= 6000 then
  	set grade := '中收入';
	else
  	set grade := '低收入';
	end if;
	select grade;
end;
```

```sql
call p3();
```

## 6. 参数
存储过程的参数包括三种形式：

- in：入参（未指定时，默认是in）
- out：出参
- inout：既是入参，又是出参

案例：员工月薪sal，超过10000的属于“高收入”，6000到10000的属于“中收入”，少于6000的属于“低收入”。

```sql
create procedure p4(in sal int, out grade varchar(20))
begin
	if sal > 10000 then
  	set grade := '高收入';
	elseif sal >= 6000 then
  	set grade := '中收入';
	else
  	set grade := '低收入';
	end if;
end;
```

```sql
call p4(5000, @grade);
select @grade;
```

案例：将传入的工资sal上调10%

```sql
create procedure p5(inout sal int)
begin
	set sal := sal * 1.1;
end;
```

```sql
set @sal := 10000;
call p5(@sal);
select @sal;
```

## 7. case语句
语法格式：

```sql
case 值
	when 值1 then
	......
	when 值2 then
	......
	when 值3 then
	......
	else
	......
end case;
```

```sql
case
	when 条件1 then
	......
	when 条件2 then
	......
	when 条件3 then
	......
	else
	......
end case;
```

案例：根据不同月份，输出不同的季节。3 4 5月份春季。6 7 8月份夏季。9 10 11月份秋季。12 1 2 冬季。其他非法。

```sql
create procedure mypro(in month int, out result varchar(100))
begin 
	case month
		when 3 then set result := '春季';
		when 4 then set result := '春季';
		when 5 then set result := '春季';
		when 6 then set result := '夏季';
		when 7 then set result := '夏季';
		when 8 then set result := '夏季';
		when 9 then set result := '秋季';
		when 10 then set result := '秋季';
		when 11 then set result := '秋季';
		when 12 then set result := '冬季';
		when 1 then set result := '冬季';
		when 2 then set result := '冬季';
		else set result := '非法月份';
	end case;
end;
```

```sql
create procedure mypro(in month int, out result varchar(100))
begin 
	case 
		when month = 3 or month = 4 or month = 5 then 
			set result := '春季';
		when  month = 6 or month = 7 or month = 8  then 
			set result := '夏季';
		when  month = 9 or month = 10 or month = 11  then 
			set result := '秋季';
		when  month = 12 or month = 1 or month = 2  then 
			set result := '冬季';
		else 
			set result := '非法月份';
	end case;
end;
```

```sql
call mypro(9, @season);
select @season;
```

## 8. while循环
语法格式：

```sql
while 条件 do
	循环体;
end while;
```

案例：传入一个数字n，计算1~n中所有偶数的和。

```sql
create procedure mypro(in n int)
begin
	declare sum int default 0;
	while n > 0 do
  	if n % 2 = 0 then
    	set sum := sum + n;
  	end if;
  	set n := n - 1;
	end while;
	select sum;
end;
```

```sql
call mypro(10);
```

## 9. repeat循环
语法格式：

```sql
repeat
	循环体;
	until 条件
end repeat;
```

注意：条件成立时结束循环。

案例：传入一个数字n，计算1~n中所有偶数的和。

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

```sql
call mypro(10, @sum);
select @sum;
```

## 10. loop循环
语法格式：

```sql
create procedure mypro()
begin 
	declare i int default 0;
  mylp:loop 
		set i := i + 1;
		if i = 5 then 
			leave mylp;
		end if;
		select i;
	end loop;
end;
```

```sql
create procedure mypro()
begin 
	declare i int default 0;
  mylp:loop 
		set i := i + 1;
		if i = 5 then 
			iterate mylp;
		end if;
		if i = 10 then 
		  leave mylp;
		end if;
		select i;
	end loop;
end;
```

## 11. 游标cursor
游标（cursor）可以理解为一个指向结果集中某条记录的指针，允许程序逐一访问结果集中的每条记录，并对其进行逐行操作和处理。

使用游标时，需要在存储过程或函数中定义一个游标变量，并通过 `DECLARE` 语句进行声明和初始化。然后，使用 `OPEN` 语句打开游标，使用 `FETCH` 语句逐行获取游标指向的记录，并进行处理。最后，使用 `CLOSE` 语句关闭游标，释放相关资源。游标可以大大地提高数据库查询的灵活性和效率。

声明游标的语法：

```sql
declare 游标名称 cursor for 查询语句;
```

打开游标的语法：

```sql
open 游标名称;
```

通过游标取数据的语法：

```sql
fetch 游标名称 into 变量[,变量,变量......]
```

关闭游标的语法：

```sql
close 游标名称;
```

案例：从dept表查询部门编号和部门名，创建一张新表dept2，将查询结果插入到新表中。

```plsql
drop procedure if exists mypro;

create procedure mypro()
begin 

	declare no int;
	declare name varchar(100);
	declare dept_cursor cursor for select deptno,dname from dept;

	drop table if exists dept2;
	create table dept2(
		no int primary key,
		name varchar(100)
	);
	
	open dept_cursor;
	
	while true do
		fetch dept_cursor into no, name;
		insert into dept2(no,name) values(no,name);
	end while;
	
	close dept_cursor;
end;

call mypro();
```

执行结果：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1687222276547-6381cff6-311f-40a0-984c-0a79f6954a50.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_11%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

出现了异常：异常信息中显示没有数据了。这是因为while true循环导致的。

不过虽然出现了异常，但是表创建成功了，数据也插入成功了：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1687222354577-99ea5bb0-40c8-4bca-9a9a-605894b195bb.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_10%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

**<font style="color:#DF2A3F;">注意：声明局部变量和声明游标有顺序要求，局部变量的声明需要在游标声明之前完成。</font>**

## 12. 捕捉异常并处理
语法格式：

```plsql
DECLARE handler_name HANDLER FOR condition_value action_statement
```

1. handler_name 表示异常处理程序的名称，重要取值包括：
    1. CONTINUE：发生异常后，程序不会终止，会正常执行后续的过程。(捕捉)
    2. EXIT：发生异常后，终止存储过程的执行。（上抛）
2. condition_value 是指捕获的异常，重要取值包括：
    1. SQLSTATE sqlstate_value，例如：SQLSTATE '02000'
    2. SQLWARNING，代表所有01开头的SQLSTATE
    3. NOT FOUND，代表所有02开头的SQLSTATE
    4. SQLEXCEPTION，代表除了01和02开头的所有SQLSTATE
3. action_statement 是指异常发生时执行的语句，例如：CLOSE cursor_name

给之前的游标添加异常处理机制：

```plsql
drop procedure if exists mypro;

create procedure mypro()
begin 

	declare no int;
	declare name varchar(100);
	declare dept_cursor cursor for select deptno,dname from dept;

	declare exit handler for not found close dept_cursor;

	drop table if exists dept2;
	create table dept2(
		no int primary key,
		name varchar(100)
	);
	
	open dept_cursor;
	
	while true do
		fetch dept_cursor into no, name;
		insert into dept2(no,name) values(no,name);
	end while;
	
	close dept_cursor;
end;

call mypro();
```

## 13. 存储函数
存储函数：带返回值的存储过程。参数只允许是in。没有out，也没有inout。不写默认就是in参数。

语法格式：

```plsql
CREATE FUNCTION 存储函数名称(参数列表)
RETURNS 数据类型 [特征]
BEGIN
	--函数体
	RETURN ...;
END;
```

“特征”的可取重要值如下：

- deterministic：用该特征标记该函数为确定性函数（什么是确定性函数？每次调用函数时传同一个参数的时候，返回值都是固定的）。这是一种优化策略，这种情况下整个函数体的执行就会省略了，直接返回之前缓存的结果，来提高函数的执行效率。
- no sql：用该特征标记该函数执行过程中不会查询数据库，如果确实没有查询语句建议使用。告诉 MySQL 优化器不需要考虑使用查询缓存和优化器缓存来优化这个函数，这样就可以避免不必要的查询消耗产生，从而提高性能。
- reads sql data：用该特征标记该函数会进行查询操作，告诉 MySQL 优化器这个函数需要查询数据库的数据，可以使用查询缓存来缓存结果，从而提高查询性能；同时 MySQL 还会针对该函数的查询进行优化器缓存处理。

案例：计算1~n的所有偶数之和

```plsql
-- 删除函数
drop function if exists sum_fun;

-- 创建函数
create function sum_fun(n int)
returns int deterministic 
begin 
	declare result int default 0;
	while n > 0 do 
		if n % 2 = 0 then 
			set result := result + n;
		end if;
		set n := n - 1;
	end while;
	return result;
end;

-- 调用函数
set @result = sum_fun(100);
select @result;
```

## 14. 触发器
MySQL 触发器是一种数据库对象，它是与表相关联的特殊程序。它可以在特定的数据操作（例如插入（INSERT）、更新（UPDATE）或删除（DELETE））触发时自动执行。MySQL 触发器使数据库开发人员能够在数据的不同状态之间维护一致性和完整性，并且可以为特定的数据库表自动执行操作。

触发器的作用主要有以下几个方面：

1.  强制实施业务规则：触发器可以帮助确保数据表中的业务规则得到强制执行，例如检查插入或更新的数据是否符合某些规则。 
2.  数据审计：触发器可以声明在执行数据修改时自动记日志或审计数据变化的操作，使数据对数据库管理员和 SQL 审计人员更易于追踪和审计。 
3.  执行特定业务操作：触发器可以自动执行特定的业务操作，例如计算数据行的总数、计算平均值或总和等。 

MySQL 触发器分为两种类型: BEFORE 和 AFTER。BEFORE 触发器在执行 INSERT、UPDATE、DELETE 语句之前执行，而 AFTER 触发器在执行 INSERT、UPDATE、DELETE 语句之后执行。

创建触发器的语法如下：

```plsql
CREATE TRIGGER trigger_name
BEFORE/AFTER INSERT/UPDATE/DELETE ON table_name FOR EACH ROW
BEGIN
-- 触发器执行的 SQL 语句
END;
```

其中：

- trigger_name：触发器的名称
- BEFORE/AFTER：触发器的类型，可以是 BEFORE 或者 AFTER
- INSERT/UPDATE/DELETE：触发器所监控的 DML 调用类型
- table_name：触发器所绑定的表名
- FOR EACH ROW：表示触发器在每行受到 DML 的影响之后都会执行
- 触发器执行的 SQL 语句：该语句会在触发器被触发时执行

需要注意的是，触发器是一种高级的数据库功能，只有在必要的情况下才应该使用，例如在需要实施强制性业务规则时。过多的触发器和复杂的触发器逻辑可能会影响查询性能和扩展性。

**<font style="color:#DF2A3F;">关于触发器的NEW和OLD关键字：</font>**

在 MySQL 触发器中，NEW 和 OLD 是两个特殊的关键字，用于引用在触发器中受到修改的行的新值和旧值。具体而言：

- NEW：在触发 INSERT 或 UPDATE 操作期间，NEW 用于引用将要插入或更新到表中的新行的值。
- OLD：在触发 UPDATE 或 DELETE 操作期间，OLD 用于引用更新或删除之前在表中的旧行的值。

通俗的讲，NEW 是指触发器执行的操作所要插入或更新到当前行中的新数据；而 OLD 则是指当前行在触发器执行前原本的数据。

在MySQL 触发器中，NEW 和 OLD 使用方法是相似的。在触发器中，可以像引用表的其他列一样引用 NEW 和 OLD。例如，可以使用 OLD.column_name 从旧行中引用列值，也可以使用 NEW.column_name 从新行中引用列值。

示例：

假设有一个名为 my_table 的表，其中包含一个名为 quantity 的列。当在该表上执行 UPDATE 操作时，以下触发器会将旧值 OLD.quantity 累加到新值 NEW.quantity 中：

```plsql
CREATE TRIGGER my_trigger
BEFORE UPDATE ON my_table
FOR EACH ROW
BEGIN
SET NEW.quantity = NEW.quantity + OLD.quantity;
END;
```

在此触发器中，OLD.quantity 引用原始行的 quantity 值（旧值），而 NEW.quantity 引用更新行的 quantity 值（新值）。在触发器执行期间，数据行的 quantity 值将设置为旧值加上新值。

需要注意的是，在使用 NEW 和 OLD 时，需要根据 DML 操作的类型进行判断，以确定哪个关键字表示新值，哪个关键字则表示旧值。

案例：当我们对dept表中的数据进行insert delete update的时候，请将这些操作记录到日志表当中，日志表如下：

```sql
drop table if exists oper_log;

create table oper_log(
  id bigint primary key auto_increment,
  table_name varchar(100) not null comment '操作的哪张表',
  oper_type varchar(100) not null comment '操作类型包括insert delete update',
  oper_time datetime not null comment '操作时间',
  oper_id bigint not null comment '操作的那行记录的id',
  oper_desc text comment '操作描述'
);
```

触发器1：向dept表中插入数据时，记录日志

```plsql
create trigger dept_trigger_insert 
after insert on dept
for each row
begin
	insert into oper_log(id,table_name,oper_type,oper_time,oper_id,oper_desc) values
(null,'dept','insert',now(),new.deptno,concat('插入数据：deptno=', new.deptno, ',dname=', new.dname,',loc=', new.loc));
end;
```

查看触发器：

```plsql
show triggers;
```

删除触发器：

```sql
drop trigger if exists dept_trigger_insert;
```

向dept表中插入一条记录：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1687250537958-36fdd3ce-6aa3-48e9-aa34-39dac470c82f.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

日志表中多了一条记录：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1687250572044-f7216711-ee12-49bf-b687-b21b7b5856cd.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_29%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

触发器2：修改dept表中数据时，记录日志

```plsql
create trigger dept_trigger_update
after update on dept
for each row
begin
	insert into oper_log(id,table_name,oper_type,oper_time,oper_id,oper_desc) values
(null,'dept','update',now(),new.deptno,concat('更新前：deptno=', old.deptno, ',dname=', old.dname,',loc=', old.loc, 
                                              ',更新后：deptno=', new.deptno, ',dname=', new.dname,',loc=', new.loc));
end;
```

更新一条记录：

```sql
update dept set loc = '北京' where deptno = 60;
```

日志表中多了一条记录：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1687250964502-f6af7d92-c4a5-4910-9efa-d08090647643.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_35%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

**<font style="color:#DF2A3F;">注意：更新一条记录则对应一条日志。如果一次更新3条记录，那么日志表中插入3条记录。</font>**

触发器3：删除dept表中数据时，记录日志

```plsql
create trigger dept_trigger_delete
after delete on dept
for each row
begin
	insert into oper_log(id,table_name,oper_type,oper_time,oper_id,oper_desc) values
(null,'dept','delete',now(),old.deptno,concat('删除了数据：deptno=', old.deptno, ',dname=', old.dname,',loc=', old.loc));
end;
```

删除一条记录：

```sql
delete from dept where deptno = 60;
```

日志表中多了一条记录：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1687251196650-5527bf1a-370d-47c8-bf45-2b7babc5e1a5.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_37%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

# 存储引擎初步
## 存储引擎概述
MySQL存储引擎决定了数据在磁盘上的存储方式和访问方式。不同的存储引擎实现了不同的存储和检索算法，因此它们在处理和管理数据的方式上存在差异。

MySQL常见的存储引擎包括InnoDB、MyISAM、Memory、Archive等。每个存储引擎都有自己的特点和适用场景。

例如，InnoDB引擎支持事务和行级锁定，适用于需要高并发读写的应用；MyISAM引擎不支持事务，但适用于读操作较多的应用；Memory引擎数据全部存储在内存中，适用于对读写速度要求很高的应用等等。

选择适合的存储引擎可以提高MySQL的性能和效率，并且根据应用需求来合理选择存储引擎可以提供更好的数据管理和查询功能。

## MySQL支持哪些存储引擎
使用`show engines \G;`命令可以查看所有的存储引擎：

```java
*************************** 1. row ***************************
      Engine: MEMORY
     Support: YES
     Comment: Hash based, stored in memory, useful for temporary tables
Transactions: NO
          XA: NO
  Savepoints: NO
*************************** 2. row ***************************
      Engine: MRG_MYISAM
     Support: YES
     Comment: Collection of identical MyISAM tables
Transactions: NO
          XA: NO
  Savepoints: NO
*************************** 3. row ***************************
      Engine: CSV
     Support: YES
     Comment: CSV storage engine
Transactions: NO
          XA: NO
  Savepoints: NO
*************************** 4. row ***************************
      Engine: FEDERATED
     Support: NO
     Comment: Federated MySQL storage engine
Transactions: NULL
          XA: NULL
  Savepoints: NULL
*************************** 5. row ***************************
      Engine: PERFORMANCE_SCHEMA
     Support: YES
     Comment: Performance Schema
Transactions: NO
          XA: NO
  Savepoints: NO
*************************** 6. row ***************************
      Engine: MyISAM
     Support: YES
     Comment: MyISAM storage engine
Transactions: NO
          XA: NO
  Savepoints: NO
*************************** 7. row ***************************
      Engine: InnoDB
     Support: DEFAULT
     Comment: Supports transactions, row-level locking, and foreign keys
Transactions: YES
          XA: YES
  Savepoints: YES
*************************** 8. row ***************************
      Engine: ndbinfo
     Support: NO
     Comment: MySQL Cluster system information storage engine
Transactions: NULL
          XA: NULL
  Savepoints: NULL
*************************** 9. row ***************************
      Engine: BLACKHOLE
     Support: YES
     Comment: /dev/null storage engine (anything you write to it disappears)
Transactions: NO
          XA: NO
  Savepoints: NO
*************************** 10. row ***************************
      Engine: ARCHIVE
     Support: YES
     Comment: Archive storage engine
Transactions: NO
          XA: NO
  Savepoints: NO
*************************** 11. row ***************************
      Engine: ndbcluster
     Support: NO
     Comment: Clustered, fault-tolerant tables
Transactions: NULL
          XA: NULL
  Savepoints: NULL
```

`Support`是`Yes`的表示支持该存储引擎。当前MySQL的版本是`8.0.33`

MySQL默认的存储引擎是：`InnoDB`

## 指定和修改存储引擎
### 指定存储引擎
在MySQL中，你可以在创建表时指定使用的存储引擎。通过在CREATE TABLE语句中使用ENGINE关键字，你可以指定要使用的存储引擎。

以下是指定存储引擎的示例：

```sql
CREATE TABLE my_table (column1 INT, column2 VARCHAR(50)) ENGINE = InnoDB;
```

在这个例子中，我们创建了一个名为my_table的表，并指定了使用InnoDB存储引擎。

如果你不显式指定存储引擎，MySQL将使用默认的存储引擎。默认情况下，MySQL 8的默认存储引擎是InnoDB。

### 修改存储引擎
在MySQL中，你可以通过ALTER TABLE语句修改表的存储引擎。下面是修改存储引擎的示例：

```sql
ALTER TABLE my_table ENGINE = MyISAM;
```

在这个例子中，我们使用ALTER TABLE语句将my_table表的存储引擎修改为MyISAM。

请注意，在修改存储引擎之前，你需要考虑以下几点：

1.  修改存储引擎可能需要执行复制表的操作，因此可能会造成数据的丢失或不可用。确保在执行修改之前备份你的数据。 
2.  不是所有的存储引擎都支持相同的功能。要确保你选择的新存储引擎支持你应用程序所需的功能。 
3.  修改表的存储引擎可能会影响到现有的应用程序和查询。确保在修改之前评估和测试所有的影响。 
4.  ALTER TABLE语句可能需要适当的权限才能执行。确保你拥有足够的权限来执行修改存储引擎的操作。 

总而言之，修改存储引擎需要谨慎进行，且需要考虑到可能的影响和风险。建议在进行修改之前进行适当的测试和备份。

## 常用的存储引擎及适用场景
在实际开发中，以下存储引擎是比较常用的：

1.  InnoDB：
    1. MySQL默认的事务型存储引擎
    2. 支持ACID事务
    3. 具有较好的并发性能和数据完整性
    4. 支持行级锁定。
    5. 适用于大多数应用场景，尤其是需要事务支持的应用。 
2.  MyISAM：
    1. 是MySQL早期版本中常用的存储引擎
    2. 支持全文索引和表级锁定
    3. 不支持事务
    4. 由于其简单性和高性能，在某些特定的应用场景中会得到广泛应用，如**<font style="color:#DF2A3F;">读密集</font>**的应用。 
3.  MEMORY：
    1. 称为HEAP，是将表存储在内存中的存储引擎
    2. 具有非常高的读写性能，但数据会在服务器重启时丢失。
    3. 适用于需要快速读写的临时数据集、缓存和临时表等场景。 
4.  CSV：
    1. 将数据以纯文本格式存储的存储引擎
    2. 适用于需要处理和导入/导出CSV格式数据的场景。 
5.  ARCHIVE：
    1. 将数据高效地进行压缩和存储的存储引擎
    2. 适用于需要长期存储大量历史数据且不经常查询的场景。 

# 索引
## 什么是索引
索引是一种能够提高检索（查询）效率的提前排好序的数据结构。例如：书的目录就是一种索引机制。索引是解决SQL慢查询的一种方式。

## 索引的创建和删除
### 主键会自动添加索引
主键字段会自动添加索引，不需要程序员干涉，主键字段上的索引被称为`主键索引`

### unique约束的字段自动添加索引
unique约束的字段也会自动添加索引，不需要程序员干涉，这种字段上添加的索引称为`唯一索引`

### 给指定的字段添加索引
建表时添加索引：

```sql
CREATE TABLE emp (
    ...
    name varchar(255),
    ...
    INDEX idx_name (name)
);

```

如果表已经创建好了，后期给字段添加索引

```sql
ALTER TABLE emp ADD INDEX idx_name (name);
```

### 删除指定字段上的索引

```sql
ALTER TABLE emp DROP INDEX idx_name;
```

### 查看某张表上添加了哪些索引

```sql
show index from 表名;
```

## 索引的分类
不同的`存储引擎`有不同的索引类型和实现：

- 按照数据结构分类：
    - B+树 索引
    - Hash 索引（仅 `memory` 存储引擎支持）
    - Full-text 索引（仅 `InnoDB和MyISAM` 存储引擎支持）
- 按照物理存储分类：
    - 聚集索引
    - 非聚集索引
- 按照字段特性分类：
    - 主键索引（primary key）
    - 唯一索引（unique）
    - 普通索引（index）
    - 全文索引（fulltext）
- 按照字段个数分类：
    - 单列索引、联合索引（也叫复合索引、组合索引）

## 常见索引数据结构和区别
常见索引数据结构包括：

- 二叉树
- 红黑树
- B树
- B+树

区别：树的高度不同。树的高度越低，性能越高。这是因为每一个节点都是一次I/O

### 二叉树
有这样一张表

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1692335600473-ad5b7cde-e554-47ab-b42f-58168c989893.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

如果不给id字段添加索引，默认进行全表扫描，假设查询id=10的数据，那至少要进行10次磁盘IO。效率低。可以给id字段添加索引，假设该索引使用了二叉树这种数据结构，这个二叉树是这样的（**<font style="color:#DF2A3F;">推荐一个数据结构可视化网站Data Structure Visualizations，是旧金山大学（USFCA）的一个网站</font>**）：[https://www.cs.usfca.edu/~galles/visualization/Algorithms.html](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html)

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1692336231981-96990a24-7475-48a4-ba48-decb2ec2c187.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

如果这个时候要找id=10的数据，需要的IO次数是？4次。效率显著提升了。

但是MySQL并没有直接使用这种普通的二叉树，这种普通二叉树在`数据极端`的情况下，效率较低。比如下面的数据：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1692336431647-e5bb092a-7858-478b-add5-d4c5fa15deb0.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

如果给id字段添加索引，并且该索引底层使用了普通二叉树，这棵树会是这样的：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1692336585274-554cb4fd-3d32-4785-89c9-e23bce8739ac.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_14%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

你虽然使用了二叉树，但这更像一个链表。查找效率等同于链表查询O(n)【**<font style="color:#DF2A3F;">查找算法的时间复杂度是线性的</font>**】。查找效率极低。

因此对于MySQL来说，它并没有选择这种数据结构作为索引。

### 红黑树（自平衡二叉树）
通过自旋平衡规则进行旋转，子节点会自动分叉为2个分支，从而减少树的高度，当数据有序插入时比二叉树数据检索性能更好。

例如有以下数据

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1692336431647-e5bb092a-7858-478b-add5-d4c5fa15deb0.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

给id字段添加索引，并且该索引使用了`红黑树`数据结构，那么会是这样：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1692337568497-9cec3d01-cb4b-4b9f-85a5-763315fc1953.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_16%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

如果查找id=10的数据，磁盘IO次数为：5次。效率比普通二叉树要高一些。

但是如果数据量庞大，例如500万条数据，也会导致树的高度很高，磁盘IO次数仍然很多，查询效率也会比较低。

因此MySQL并没有使用红黑树这种数据结构作为索引。

### B Trees（B树）
B Trees首先是一个`自平衡`的。

B Trees每个节点下的子节点数量 > 2。

B Trees每个节点中也不是存储单个数据，可以存储多个数据。

B Trees又称为`平衡多路查找树`。

B Trees分支的数量不是2，是大于2，具体是多少个分支，由`阶`决定。例如：

- 3阶的B Trees，一个节点下最多有3个子节点，每个节点中最多有2个数据。
- 4阶的B Trees，一个节点下最多有4个子节点，每个节点中最多有3个数据。
- 5阶（5, 4）
- 6阶（6, 5）
- ....
- 16阶（16, 15）【MySQL采用了16阶】

采用B Trees，你会发现相同的数据量，**<font style="color:#DF2A3F;">B Tree 树的高度更低</font>**。磁盘IO次数更少。

3阶的B Trees：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1692341860428-41d05ad9-1a6a-46ca-b3ae-0a411999152b.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_22%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

**<font style="color:#DF2A3F;">假设id字段添加了索引，并且采用了B Trees数据结构，查找id=10的数据，只需要3次磁盘IO。</font>**

4阶的B Trees：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1692341965676-a9d34529-7b4d-45e3-baf3-4714a65bd0e4.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_20%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

更加详细的存储是这样的，请看下图：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1692346278862-ee20dcee-9b4e-4678-a777-9e782601958a.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1692344122602-a45b07fe-c85a-42c2-9a20-008b2ad5002c.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_28%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

在B Trees中，每个节点不仅存储了`索引值`，还存储该索引值对应的`数据行`。

并且每个节点中的p1 p2 p3是指向下一个节点的指针。

B Trees数据结构存在的缺点是：不适合做区间查找，对于区间查找效率较低。假设要查id在[3~7]之间的，需要查找的是3,4,5,6,7。那么查这每个索引值都需要从头节点开始。

因此MySQL使用了B+ Trees解决了这个问题。

### B+ Trees（B+ 树）
B+ Trees 相较于 B Trees改进了哪些？

- B+树将数据都存储在叶子节点中。并且叶子节点之间使用链表连接，这样很适合范围查询。
- B+树的非叶子节点上只有索引值，没有数据，所以非叶子节点可以存储更多的索引值，这样让B+树更矮更胖，提高检索效率。

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1692347138609-6544b852-3198-4920-ab3c-95a41e80802a.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_20%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

假设有这样一张表：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1692346967611-4a60f469-aa1d-4244-90e3-129d7ea36fb4.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

B+ Trees方式存储的话如下图所示：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1692349477753-ce686f45-052c-4935-9212-5edf0f73149f.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_34%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

**<font style="color:#DF2A3F;">经典面试题：</font>**mysql为什么选择B+树作为索引的数据结构，而不是B树？

1. 非叶子节点上可以存储更多的键值，阶数可以更大，更矮更胖，磁盘IO次数少，数据查询效率高。
2. 所有数据都是有序存储在叶子节点上，让范围查找，分组查找效率更高。
3. 数据页之间、数据记录之间采用链表链接，让升序降序更加方便操作。

**<font style="color:#DF2A3F;">经典面试题：</font>**如果一张表没有主键索引，那还会创建B+树吗？

<font style="color:rgb(36, 41, 47);">当一张表没有主键索引时，默认会使用一个隐藏的内置的聚集索引（clustered index）。这个聚集索引是基于表的物理存储顺序构建的，通常是使用B+树来实现的。</font>

## 其他索引及相关调优
### Hash索引
支持Hash索引的存储引擎有：

- InnoDB（不支持手动创建Hash索引，系统会自动维护一个`自适应的Hash索引`）
    - 对于InnoDB来说，即使手动指定了某字段采用Hash索引，最终`show index from 表名`的时候，还是`BTREE`。
- Memory（支持Hash索引）

Hash索引底层的数据结构就是哈希表。一个数组，数组中每个元素是链表。和java中HashMap一样。哈希表中每个元素都是key value结构。key存储`索引值`，value存储`行指针`。

原理如下：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1692401422670-6fb725df-8901-480c-9838-021bd25cc726.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

如果name字段上添加了Hash索引idx_name

Hash索引长这个样子：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1692401394351-b98f716f-7f04-4e57-823b-68fefc98b8d2.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_24%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

检索原理：假设 name='孙行者'。通过哈希算法将'孙行者'转换为数组下标，通过下标找链表，在链表上遍历找到孙行者的行指针。

注意：不同的字符串，经过哈希算法得到的数组下标可能相同，这叫做哈希碰撞/哈希冲突。【不过，好的哈希算法应该具有很低的碰撞概率。常用的哈希算法如MD5、SHA-1、SHA-256等都被设计为尽可能减少碰撞的发生。】

Hash索引优缺点：

- 优点：只能用在等值比较中，效率很高。例如：name='孙悟空'
- 缺点：不支持排序，不支持范围查找。

### 聚集索引和非聚集索引
按照数据的物理存储方式不同，可以将索引分为聚集索引（聚簇索引）和非聚集索引（非聚簇索引）。

存储引擎是InnoDB的，主键上的索引属于聚集索引。

存储引擎是MyISAM的，任意字段上的索引都是非聚集索引。

InnoDB的物理存储方式：当创建一张表t_user，并使用InnoDB存储引擎时，会在硬盘上生成这样一个文件：

- t_user.ibd （InnoDB data表索引 + 数据）
- t_user.frm （存储表结构信息）

MyISAM的物理存储方式：当创建一张表t_user，并使用MyISAM存储引擎时，会在硬盘上生成这样一个文件：

- t_user.MYD （表数据）
- t_user.MYI （表索引）
- t_user.frm （表结构）

**<font style="color:#DF2A3F;">注意：从MySQL8.0开始，不再生成frm文件了，引入了数据字典，用数据字典来统一存储表结构信息，例如：</font>**

- **<font style="color:#DF2A3F;">information_schema.TABLES （表包含了数据库中所有表的信息，例如表名、数据库名、引擎类型等）</font>**
- **<font style="color:#DF2A3F;">information_schema.COLUMNS（表包含了数据库中所有表的列信息，例如列名、数据类型、默认值等）</font>**

聚集索引的原理图：（B+树，叶子节点上存储了索引值 + 数据）

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1692349477753-ce686f45-052c-4935-9212-5edf0f73149f.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_34%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

非聚集索引的原理图：（B+树，叶子节点上存储了索引值 + 行指针）

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1692414826853-a7b1c060-26c2-43c0-ba55-6ac983e67fdb.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_55%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

聚集索引的优点和缺点：

1. 优点：聚集索引将数据存储在索引树的叶子节点上。可以减少一次查询，因为查询索引树的同时可以获取数据。
2. 缺点：对数据进行修改或删除时需要更新索引树，会增加系统的开销。

### 二级索引
二级索引也属于非聚集索引。也有人把二级索引称为辅助索引。

有表t_user，id是主键。age是非主键。在age字段上添加的索引称为二级索引。（所有非主键索引都是二级索引）

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1692416482381-7ff192ad-a4ce-4292-b5c6-045f57768b72.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_15%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

二级索引的数据结构：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1692417008406-ebae09f8-dea7-4b6a-ab56-100e31611421.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_17%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

二级索引的查询原理：

假设查询语句为：

```sql
select * from t_user where age = 30;
```

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1692417425624-818e9980-dbe6-4470-a4b2-9c91b33ca2b6.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_30%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

为什么会“回表”？因为使用了`select *`

避免“回表【回到原数据表】”是提高SQL执行效率的手段。例如：select id from t_user where age = 30; 这样的SQL语句是不需要回表的。

### 覆盖索引
覆盖索引是指一个该索引包含了查询所需的所有列，不需要再去回表查询数据。当使用覆盖索引时，MySQL可以直接通过索引，也就是索引上的数据来获取所需的结果，而不必再去查找表中的数据。这样可以显著提高查询性能。

假设有一个用户表（user）包含以下列：id, username, email, age。

常见的查询是根据用户名查询用户的邮箱。如果为了提高这个查询的性能，可以创建一个覆盖索引，包含（username, email）这两列。

创建覆盖索引的SQL语句可以如下：

```sql
CREATE INDEX idx_user_username_email ON user (username, email);
```

当执行以下查询时：

```sql
SELECT email FROM user WHERE username = 'lucy';
```

MySQL可以直接使用覆盖索引（idx_user_username_email）来获取查询结果，而不必再去查找用户表中的数据。这样可以减少磁盘I/O并提高查询效率。而如果没有覆盖索引，MySQL会先使用索引（username）来找到匹配的行，然后再回表查询获取邮箱，这个过程会增加更多的磁盘I/O和查询时间。

值得注意的是，覆盖索引的创建需要考虑查询的字段选择。如果查询需要的字段较多，可能需要创建包含更多列的覆盖索引，以满足完全覆盖查询的需要。

使用覆盖索引有以下几个优点：

1. 提高查询性能：减少IO操作，加快查询速度。
2. 减少存储空间：覆盖索引只包含需要的列，可以减小索引的大小。
3. 减少锁的竞争：由于不需要回表操作，减少了对表的访问，减少了锁的竞争。

但是覆盖索引也有一些限制：

1. 创建覆盖索引会增加索引的大小，可能会占用更多的存储空间。
2. 更新数据时，需要同时更新索引，可能会增加写操作的成本。

因此，在设计数据库索引时，需要权衡覆盖索引所带来的性能提升和存储成本，并根据具体的查询需求进行选择。

### 索引下推
索引下推是MySQL查询优化器的一种优化技术，它的目标是减少不必要的IO操作和减少查询的数据量，提高查询性能。

在MySQL中，当使用多列索引时，如果查询条件只涉及到了索引的一部分列，传统的查询优化器会将所有符合索引的记录都读入内存，然后再进行筛选。而索引下推则可以在索引的扫描过程中，对查询条件进行判断，只将符合条件的记录加载到内存中，减少不必要的IO和数据传输。

索引下推的过程分为两个阶段：

1. 索引范围扫描：首先，根据查询条件的前缀，定位到索引上的一个起始位置，然后按照索引的顺序逐个查找符合条件的记录，直到找到一个不满足条件的记录为止。
2. 回表操作：在索引扫描的过程中，对于满足条件的记录，需要回到原数据表中找到完整的行数据，以返回给查询结果。

索引下推的好处是可以减少不必要的IO和数据传输，提高查询性能。但它并不是适用于所有情况，对于某些查询条件较为复杂的情况，使用索引下推可能会导致性能下降。因此，在实际使用中，需要根据具体情况进行评估和测试，选择合适的优化方式。

假设有以下表结构：

表名：users

| id | name | age | city |
| --- | --- | --- | --- |
| 1 | John | 25 | New York |
| 2 | Alice | 30 | London |
| 3 | Bob | 40 | Paris |
| 4 | Olivia | 35 | Berlin |
| 5 | Michael | 28 | Sydney |

现在我们创建了一个多列索引：

```plain
ALTER TABLE users ADD INDEX idx_name_city_age (name, city, age);
```

假设我们要查询年龄大于30岁，并且所在城市是"London"的用户，传统的查询优化器会将所有满足年龄大于30岁的记录读入内存，然后再根据城市进行筛选。

使用索引下推优化后，在索引范围扫描的过程中，优化器会判断只有在城市列为"London"的情况下，才会将满足年龄大于30岁的记录加载到内存中。这样就可以避免不必要的IO和数据传输，提高查询性能。

具体的查询语句可以是：

```plain
SELECT * FROM users WHERE age > 30 AND city = 'London';
```

在执行这个查询时，优化器会使用索引下推技术，先根据索引范围扫描找到所有满足条件的记录，然后再回到原数据表中获取完整的行数据，最终返回结果。

通过使用索引下推优化技术，可以减少不必要的数据加载和IO操作，提高查询性能。

在一般情况下，索引下推是MySQL优化器自动处理的，并不需要程序员进行干预。

MySQL优化器会根据查询条件和索引的定义，自动决定是否使用索引下推优化技术。当条件满足索引下推的使用场景时，优化器会自动选择使用索引下推。这个决策是根据优化器的统计信息和查询的成本估算来进行的。

然而，对于某些特殊情况，MySQL优化器可能无法正确判断是否使用索引下推，或者错误地选择了不适合的优化策略。在这种情况下，程序员可以通过使用查询提示语句（Query Hints）来干预优化器的决策，强制使用或者禁用索引下推。

例如，使用查询提示语句来强制使用索引下推：

```plain
SELECT /*+ INDEX_MERGE(users idx_name_city_age) */ * FROM users WHERE age > 30 AND city = 'London';
```

或者使用查询提示语句来禁用索引下推：

```plain
SELECT /*+ NO_INDEX_MERGE(users) */ * FROM users WHERE age > 30 AND city = 'London';
```

这样，程序员可以在特定情况下，根据实际需求对索引下推的使用进行干预。但需要注意的是，不正确的干预可能会导致性能下降，因此在使用查询提示语句时，需要进行充分的测试和评估。

### 单列索引（单一索引）
单列索引是指对数据库表中的某一列或属性进行索引创建，对该列进行快速查找和排序操作。单列索引可以加快查询速度，提高数据库的性能。

举个例子，假设我们有一个学生表（student），其中有以下几个列：学生编号（student_id）、姓名（name）、年龄（age）和性别（gender）。

如果我们针对学生表的学生编号（student_id）列创建了单列索引，那么可以快速地根据学生编号进行查询或排序操作。例如，我们可以使用以下SQL语句查询学生编号为123456的学生信息：

```sql
SELECT * FROM student WHERE student_id = 123456;
```

由于我们对学生编号列建立了单列索引，所以数据库可以直接通过索引快速定位到具有学生编号123456的那一行记录，从而加快查询速度。

### 复合索引（组合索引）
复合索引（Compound Index）也称为多列索引（Multi-Column Index），是指对数据库表中多个列进行索引创建。

与单列索引不同，复合索引可以包含多个列。这样可以将多个列的值组合起来作为索引的键，以提高多列条件查询的效率。

举个例子，假设我们有一个订单表（Order），其中包含以下几个列：订单编号（OrderID）、客户编号（CustomerID）、订单日期（OrderDate）和订单金额（OrderAmount）。

如果我们为订单表的客户编号和订单日期这两列创建复合索引（CustomerID, OrderDate），那么可以在查询时同时根据客户编号和订单日期来快速定位到匹配的记录。

例如，我们可以使用以下SQL语句查询客户编号为123456且订单日期为2021-01-01的订单信息：

```sql
SELECT * FROM Order WHERE CustomerID = 123456 AND OrderDate = '2021-01-01';
```

由于我们为客户编号和订单日期创建了复合索引，数据库可以使用这个索引来快速定位到符合条件的记录，从而加快查询速度。复合索引的使用能够提高多列条件查询的效率，但需要注意的是，复合索引的创建和维护可能会增加索引的存储空间和对于写操作的影响。

**<font style="color:#DF2A3F;">重点：最左前缀原则</font>**

最左前缀原则（Leftmost Prefix Rule）是指在复合索引中，索引的最左边的列会被优先使用。

在一个复合索引中，每一个索引键都包含了多个列的值。当查询中使用了复合索引的一部分列作为条件时，最左前缀原则会发挥作用。

简单来说，如果复合索引是按照列A、列B和列C的顺序创建的，那么当查询中使用了列A和列B作为条件时，这个复合索引会被使用。但是如果只使用了列B和列C作为条件，而没有使用列A，那么这个复合索引将无法被使用。

举个例子，假设我们有一个商品表（Product），其中包含以下几个列：商品名称（ProductName）、商品分类（Category）、商品价格（Price）和库存量（Stock）。

如果我们为商品表的商品分类和商品价格这两列创建复合索引（Category, Price），那么可以在查询时同时根据商品分类和商品价格来快速定位到匹配的记录。

例如，我们可以使用以下SQL语句查询商品分类为"电子产品"且价格大于1000的商品信息：

```sql
SELECT * FROM Product WHERE Category = '电子产品' AND Price > 1000;
```

由于我们为商品分类和商品价格创建了复合索引，数据库可以使用这个索引来快速定位到符合条件的记录。

然而，如果我们只是使用了商品价格作为条件，而没有使用商品分类，例如：

```sql
SELECT * FROM Product WHERE Price > 1000;
```

虽然我们创建了（Category, Price）的复合索引，但由于没有使用最左边的列（Category），这个复合索引不能被使用，查询的效率可能会降低。

因此，在设计复合索引时，需要根据查询的实际情况和需求考虑最左前缀原则，确保复合索引能够被查询所使用，从而提高查询性能。

**<font style="color:#DF2A3F;">注意：</font>**

最左边列在编写 SQL 查询语句时的位置是有要求的。

根据最左前缀原则，在 SQL 查询语句的 WHERE 子句中，最左边的条件列必须按顺序出现在其他条件列之前。

举个例子，假设我们有一个复合索引（Column1, Column2, Column3），其中 Column1 是最左边的列。

当我们编写查询语句时，如果要使用复合索引，必须在 WHERE 子句中将使用到的条件列按照索引的顺序写出来，并且最左边的条件列必须写在其他条件列之前。

例如，以下是一个符合最左前缀原则的查询语句：

```sql
SELECT * FROM TableName WHERE Column1 = 'Value1' AND Column2 = 'Value2' AND Column3 = 'Value3';
```

在这个查询语句中，我们按照复合索引的顺序，首先使用了最左边的条件列 Column1，然后是 Column2，最后是 Column3。这样，数据库系统可以根据复合索引快速定位到符合条件的记录。

然而，如果我们改变了条件列的顺序，使最左边的条件列不在最前面，例如：

```sql
SELECT * FROM TableName WHERE Column3 = 'Value3' AND Column2 = 'Value2' AND Column1 = 'Value1';
```

在这个查询语句中，虽然我们还是使用了复合索引的所有条件列，但最左边的条件列 Column1 现在在其他条件列之后。根据最左前缀原则，这个复合索引将无法被使用，查询的性能可能会受到影响。

因此，在编写 SQL 查询语句时，需要注意保持最左边的条件列按照复合索引的顺序，并且放在其他条件列之前，以利用最左前缀原则提高查询性能。

**<font style="color:#DF2A3F;">相对于单列索引，复合索引有以下几个优势：</font>**

1. 减少索引的数量：复合索引可以包含多个列，因此可以减少索引的数量，减少索引的存储空间和维护成本。
2. 提高查询性能：当查询条件中涉及到复合索引的多个列时，数据库可以使用复合索引进行快速定位和过滤，从而提高查询性能。
3. 覆盖查询：如果复合索引包含了所有查询需要的列，那么数据库可以直接使用索引中的数据，而不需要再进行表的读取，从而提高查询性能。
4. 排序和分组：由于复合索引包含多个列，因此可以用于排序和分组操作，从而提高排序和分组的性能。

## 索引的优缺点
索引是数据库中一种重要的数据结构，用于加速数据的检索和查询操作。它的优点和缺点如下：

优点：

1. 提高查询性能：通过创建索引，可以大大减少数据库查询的数据量，从而提升查询的速度。
2. 加速排序：当查询需要按照某个字段进行排序时，索引可以加速排序的过程，提高排序的效率。
3. 减少磁盘IO：索引可以减少磁盘IO的次数，这对于磁盘读写速度较低的场景，尤其重要。

缺点：

1. 占据额外的存储空间：索引需要占据额外的存储空间，特别是在大型数据库系统中，索引可能占据较大的空间。
2. 增删改操作的性能损耗：每次对数据表进行插入、更新、删除等操作时，需要更新索引，会导致操作的性能降低。
3. 资源消耗较大：索引需要占用内存和CPU资源，特别是在大规模并发访问的情况下，可能对系统的性能产生影响。
4. 索引可能会过期：当表中的数据发生变化时，索引可能会过期，需要额外的处理来保持索引的一致性。

## 何时用索引
在以下情况下建议使用索引：

1.  频繁执行查询操作的字段：如果这些字段经常被查询，使用索引可以提高查询的性能，减少查询的时间。 
2.  大表：当表的数据量较大时，使用索引可以快速定位到所需的数据，提高查询效率。 
3.  需要排序或者分组的字段：在对字段进行排序或者分组操作时，索引可以减少排序或者分组的时间。 
4.  外键关联的字段：在进行表之间的关联查询时，使用索引可以加快关联查询的速度。 

在以下情况下不建议使用索引：

1.  频繁执行更新操作的表：如果表经常被更新数据，使用索引可能会降低更新操作的性能，因为每次更新都需要维护索引。 
2.  小表：对于数据量较小的表，使用索引可能并不会带来明显的性能提升，反而会占用额外的存储空间。 
3.  对于唯一性很差的字段，一般不建议添加索引。当一个字段的唯一性很差时，查询操作基本上需要扫描整个表的大部分数据。如果为这样的字段创建索引，索引的大小可能会比数据本身还大，导致索引的存储空间占用过高，同时也会导致查询操作的性能下降。 

总之，索引需要根据具体情况进行使用和权衡，需要考虑到表的大小、查询频率、更新频率以及业务需求等因素。

# MySQL优化
## MySQL优化手段
MySQL数据库的优化手段通常包括但不限于：

- SQL查询优化：这是最低成本的优化手段，通过优化查询语句、适当添加索引等方式进行。并且效果显著。
- 库表结构优化：通过规范化设计、优化索引和数据类型等方式进行库表结构优化，需要对数据库结构进行调整和改进
- 系统配置优化：<font style="color:rgb(36, 41, 47);">根据硬件和操作系统的特点，调整最大连接数、内存管理、IO调度等参数</font>
- 硬件优化：升级硬盘、增加内存容量、升级处理器等硬件方面的投入，需要购买和替换硬件设备，成本较高

我们主要掌握：SQL查询优化

## Explain（执行计划）
### 什么是Explain
在MySQL中，EXPLAIN语句用于分析和优化查询语句的执行计划。它提供了关于查询如何执行的详细信息，包括使用的索引、连接方式、表扫描顺序等。通过使用EXPLAIN语句，您可以了解查询语句的执行情况，找出性能瓶颈，进而对查询进行调优。

使用EXPLAIN可以帮助您识别潜在的性能问题，例如：

1. 索引是否被正确使用，是否需要创建新的索引来加快查询速度。
2. 是否使用了不必要的连接操作或表扫描，导致查询变慢。
3. 查询语句是否存在优化的机会，例如使用合适的查询条件或引入查询优化器的提示。

通过分析EXPLAIN的结果，您可以更好地了解查询语句的执行过程和性能瓶颈，并根据这些信息对查询进行优化。

### Explain用法
要使用EXPLAIN命令，只需在查询语句前加上EXPLAIN关键字，例如：

```plain
EXPLAIN SELECT * FROM customers WHERE customer_id = 1;
```

执行这个查询后，MySQL会返回一张描述查询执行计划的表。下面是一些常见的列含义：

```sql
-- 创建学生表
CREATE TABLE student (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  age INT
) engine=InnoDB default charset=utf8;

-- 创建课程表
CREATE TABLE course (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  teacher VARCHAR(50)
) engine=InnoDB default charset=utf8;

-- 创建成绩表
CREATE TABLE grade (
  student_id INT,
  course_id INT,
  grade FLOAT,
  PRIMARY KEY (student_id, course_id),
  FOREIGN KEY (student_id) REFERENCES student (id),
  FOREIGN KEY (course_id) REFERENCES course (id)
) engine=InnoDB default charset=utf8;

-- 给学生表的name age添加联合索引
alter table student add index idx_name_age (name, age);

-- 插入学生数据
INSERT INTO student (id, name, age)
VALUES
  (1, '张三', 18),
  (2, '李四', 17),
  (3, '王五', 19),
  (4, '赵六', 16),
  (5, '钱七', 18);

-- 插入课程数据
INSERT INTO course (id, name, teacher)
VALUES
  (1, '数学', '王老师'),
  (2, '英语', '李老师'),
  (3, '物理', '张老师'),
  (4, '化学', '赵老师'),
  (5, '历史', '杨老师');

-- 插入成绩数据
INSERT INTO grade (student_id, course_id, grade)
VALUES
  (1, 1, 85.5),
  (1, 2, 78.0),
  (1, 3, 92.3),
  (2, 1, 90.2),
  (2, 2, 81.7),
  (2, 3, 87.9),
  (3, 1, 88.6),
  (3, 2, 93.4),
  (3, 3, 79.8),
  (4, 1, 77.5),
  (4, 2, 85.1),
  (4, 3, 91.2),
  (5, 1, 92.0),
  (5, 2, 84.9),
  (5, 3, 86.7);

```

### Explain的id列和table列
在MySQL的EXPLAIN返回结果集中，id值代表查询的执行顺序。

- id相同时，自上而下的顺序执行。
- id不同时，大的先执行。
- id有相同的，有不同的，先执行大的，剩下相同的自上而下的顺序执行。
- id为NULL表示

**<font style="color:#DF2A3F;">id序号相同</font>**

```sql
explain
SELECT
	student.name,
	course.name,
	grade.grade 
FROM
	grade
	JOIN student ON grade.student_id = student.id
	JOIN course ON grade.course_id = course.id;
```

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1692437260098-c4498fa1-99b0-41e3-85c1-2ef4fe4f65d7.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_31%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

先扫描student表，再扫描grade表，最后扫描course表。

**<font style="color:#DF2A3F;">id序号不同</font>**

```sql
explain
SELECT
	* 
FROM
	grade 
WHERE
	grade.student_id = ( SELECT id FROM student WHERE NAME = '张三' );
```

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1692437354877-f1ab4307-6565-43d8-9ec9-5954379fbf23.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_31%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

先扫描student表，做子查询，再扫描grade表。

**<font style="color:#DF2A3F;">id序号有相同，有不同</font>**

```sql
# 以下语句作用：把 派生合并 机制关闭
# 派生合并 机制默认是开启的。这是优化器的一种优化机制。
# 我们只是为了演示这个例子，所以要把这个 派生合并 机制关闭一下。
# 派生合并机制开启的时候：表示将子查询生成的派生表合并到外部查询。
# 派生合并机制关闭的时候：表示子查询生成的派生表是一张独立的表。不合并到外部查询。
set session optimizer_switch='derived_merge=off';

explain
select grade.* from (select id from student) temp join grade on temp.id = grade.student_id;

# 以下语句作用：把 派生合并 机制打开
set session optimizer_switch='derived_merge=on';
```

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1692589931246-7027b294-1121-41c0-84ae-13b21aea707d.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_33%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

**<font style="color:#DF2A3F;">注意：table列中的</font>**`**<font style="color:#DF2A3F;"><derived2></font>**`**<font style="color:#DF2A3F;">表示查询</font>**`**<font style="color:#DF2A3F;">派生表</font>**`**<font style="color:#DF2A3F;">，其中的</font>**`**<font style="color:#DF2A3F;">2</font>**`**<font style="color:#DF2A3F;">表示id为2的派生表。</font>**

执行计划是：先生成派生表student，然后先扫描派生表student，再扫描grade表。

**<font style="color:#DF2A3F;">id为NULL</font>**

```sql
explain
select id from student
union 
select id from course;
```

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1692590567960-16d47f04-d497-4d0f-8eee-22774d83cf06.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_35%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

先扫描course表，再扫描student表。最后合并。合并动作严格来说不是一个查询操作。

**<font style="color:#DF2A3F;">注意：id为NULL表示最后执行，或者这个动作不是一个查询操作时。table为</font>**`**<font style="color:#DF2A3F;"><union 1,2></font>**`**<font style="color:#DF2A3F;">表示这是一个合并的结果集。</font>**

****

****

**<font style="color:#DF2A3F;">MySQL优化器的自动优化</font>**

```sql
explain
select name from student where id in(select student_id from grade where course_id=1);
```

我们猜测以上SQL语句的执行计划，id应该是1和2，但实际结果是：

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1692596150889-ab24fb6c-374b-4870-9632-dbff247218f6.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_34%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

我们可以使用`show warnings`来看看具体情况：

```sql
explain
select name from student where id in(select student_id from grade where course_id=1);

show warnings;
```

我们发现MySQL会对这样的子查询进行自动优化，实际上它会把子查询变成连接查询：

```sql
SELECT
	`test`.`student`.`name` AS `name` 
FROM
	`test`.`grade`
	JOIN `test`.`student` 
WHERE
	((
			`test`.`grade`.`student_id` = `test`.`student`.`id` 
		) 
	AND ( `test`.`grade`.`course_id` = 1 ))
```

为什么将子查询优化为连接查询了？如果是子查询的话，where条件在进行判断的时候，每判断一次都要执行一次子查询，效率较低。变成表连接效率高。

### Explain的select_type列
select_type列指的是：这个SQL语句的查询类型。

查询类型指示了MySQL优化器对查询的处理方式和操作顺序。

通过查询类型可以识别查询性能问题，某些查询类型可能导致性能问题，如DEPENDENT SUBQUERY和UNCACHEABLE SUBQUERY等。通过检查查询类型，可以确定是否出现了潜在的性能问题，进而对查询进行优化。

常见的查询类型有：

1. SIMPLE
2. PRIMARY
3. SUBQUERY
4. DEPENDENT SUBQUERY
5. DERIVED
6. UNION
7. DEPENDENT UNION
8. UNION RESULT

**SIMPLE：当select_type的取值是SIMPLE时，表示这是一个简单的SELECT查询，不包含任何子查询或UNION操作。这通常意味着查询不会涉及大量的数据操作和计算。**

```sql
explain
select * from student;
```

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1692599642820-9fc4b90f-3b01-4a57-bdfb-3cd199e644f1.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_34%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

```sql
explain 
select student.name,grade.grade from student join grade on student.id = grade.student_id;
```

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1692599672014-4e8d17cf-e8cc-4387-8aaf-e1cb88fcfb74.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_34%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

**PRIMARY：表示查询是在最外层执行的主查询（复杂查询中的最外层查询）。**

```sql
explain select * from grade where student_id=(select id from student where name='张三');
```

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1692667947734-1dffed87-6b45-4e6c-848a-f31c97fe08ab.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_35%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

**SUBQUERY：通常出现在select或where后面的子查询（不在from后面出现）。并且这种子查询可以独立的执行并产生结果，不需要依赖外部查询。**

```sql
explain select * from grade where student_id=(select id from student where name='张三');
```

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1692667947734-1dffed87-6b45-4e6c-848a-f31c97fe08ab.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_35%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

**DEPENDENT SUBQUERY：代表了一个依赖于外部查询的子查询。它会在外部查询的每一行记录上执行，并使用外部查询的结果进行处理或过滤。优化查询时，应尝试将子查询重写为更高效的方式，以提高查询性能。**

```sql
EXPLAIN SELECT
	student.NAME,
	( SELECT grade FROM grade WHERE student.id = grade.student_id ORDER BY grade DESC LIMIT 1 ) AS grade 
FROM
	student;
```

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1692670305188-9ee64789-746d-4422-af1e-e548749f938d.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_36%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

**DERIVED：出现在from后面的子查询。select_type是DERIVED表示该子查询的结果将作为派生表，供主查询使用。**

```sql
set session optimizer_switch='derived_merge=off'; # 如果不关闭，会导致派生表被合并优化

explain 
select * from (select student_id,grade from grade) t where student_id = 1;

set session optimizer_switch='derived_merge=on';
```

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1692672125705-382c22aa-7fc9-449d-b53f-893c89381553.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_36%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

**UNION：select_type是UNION表示这个语句的查询结果会合并到其他。例如：a union b union c，其中b和c的select_type是UNION，不过 a 的select_type就不一定了。**

**<font style="color:#DF2A3F;">如果select语句不作为子查询出现时，使用union或union all的时候，通常id是1的记录select_type是PRIMARY</font>**

```sql
explain
select id from student
union
select id from course;
```

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1692675956520-7b57783d-85c6-4bc1-9e8e-dec75f99883c.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_36%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

****

****

**<font style="color:#DF2A3F;">如果select语句作为from的子查询出现时，使用union或union all的时候，参与union的第一条select语句的select_type通常是DERIVED</font>**

```sql
explain
SELECT
	* 
FROM
	( 
	SELECT id FROM student 
	UNION
	SELECT id FROM course 
	UNION
	SELECT student_id FROM grade 
	) t;
```

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1692675921346-e8a5c0a6-05a0-4c9a-9e0a-be207036311a.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_36%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

以上语句使用了union，如果使用union all呢？（union会去重。union all不会进行去重操作。两者相对来说，union all效率更高一些。）

```sql
explain
SELECT
	* 
FROM
	( 
	SELECT id FROM student 
	UNION ALL
	SELECT id FROM course 
	UNION ALL
	SELECT student_id FROM grade 
	) t;
```

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1692676211678-85956865-27f9-424a-82e9-d0e66356aaa3.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_37%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

可以看到执行计划也有区别：相差了`UNION RESULT`，这是因为union会对合并后的结果集进行去重操作。因此使用`UNION RESULT`作为了临时表，对临时表进行去重操作。

**DEPENDENT UNION：当union出现在子查询中，并且这个子查询中第一个select语句是DEPENDENT SUBQUERY，那么第二个、第三个...select语句都是DEPENDENT UNION**

```sql

```

# InnoDB存储引擎
## InnoDB存储引擎的逻辑结构
![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1691895580554-88535fb2-4d1b-456d-b654-c4ee8d2b9302.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_22%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

MySQL的InnoDB存储引擎的逻辑存储结构从最上层开始包括数据库、表空间、段、区、页和行。

-  数据库（Database）
    - 逻辑存储结构的最上层，对应于数据存储和管理的逻辑集合，一个MySQL服务器可以包含多个数据库。 
-  表空间（Tablespace）
    - 表空间包括`系统表空间`和`用户表空间`
    - 系统表空间包含了InnoDB存储引擎的系统表和元数据，例如数据字典、Undo日志、插入缓冲、回滚段等。系统表空间的文件名为ibdata1。
    - 用户表空间包含了用户创建的表和索引的数据。每个InnoDB表都有一个对应的用户表空间文件，文件名为表名加上“.ibd”。
    - 默认情况下，一个表会对应一个表空间，一个表对应一个ibd文件。但这不是必须的，主要取决于你的数据库设计和管理需求，一个表可以分割存储在不同的表空间中，一个表空间中也可以存储多个表。
-  段（Segment）
    - 段分为：数据段（Leaf node segment），索引段（Non-leaf node segment），回滚段（Rollback segment）。
    -  InnoDB是索引组织表，索引底层采用`B+树`的数据结构。
    - 数据段就是`B+树`的叶子节点
    - 索引段就是`B+树`的非叶子节点
-  区（Extent）
    - 每个区的大小是1MB，每个页大小16KB，所以一个区中有64个连续的页 
-  页（Page）
    - InnoDB存储引擎磁盘管理的最小单元。每个页默认大小为16KB。 
    - 为了保证页的连续性，InnoDB存储引擎每次从磁盘上申请4-5个区。
-  行（Row）
    - 存储在页中的最小单位，每个页可以包含多个数据行。
    - 行的插入、更新和删除操作是基于行的方式进行的。 

## InnoDB存储引擎的内存结构
官方手册地址：[https://dev.mysql.com/doc/refman/8.0/en/innodb-architecture.html](https://dev.mysql.com/doc/refman/8.0/en/innodb-architecture.html)

![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1691922207357-ecbb6cee-d754-4f26-aab4-0fd57042df09.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_24%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)

- Buffer Pool：
    - Buffer Pool是一个用于存储数据库表数据和索引的内存区域。它充当了内存缓存，将经常使用的数据集加载到内存中，以加快数据库查询和操作的速度。
    - 缓冲区以Page页为单位，底层采用链表管理Page，Page包括三种不同的状态：
        * free page：空闲页，未被使用。
        * clean page：已经被使用，不过数据没有被修改过。
        * dirty page：已经被使用，数据被修改，并且缓存中的数据与磁盘上的数据不一致。
    - Buffer pool的大小可以通过配置文件进行设置，它的默认大小通常为总内存的75%。在buffer pool中，数据和索引以页的形式存储，每个页的大小通常为16KB。
    - 当查询需要访问数据或索引时，InnoDB会首先查找buffer pool中是否有所需的页，如果存在，则直接从内存中读取，避免了从磁盘读取的开销。如果所需的页不在buffer pool中，InnoDB会将页从磁盘加载到buffer pool，并将其标记为“热页”。
    - 热页是指频繁访问的页，InnoDB会优先将热页加载到buffer pool中，并通过一种称为LRU（Least Recently Used）算法的机制来管理内存中的页。LRU算法会根据最近的访问时间来确定哪些页应该被保留在内存中，以及哪些页应该从内存中淘汰出去。
    - 通过将数据和索引存储在内存中的buffer pool中，InnoDB可以显著提高数据库的性能，减少磁盘IO操作的次数，从而提高数据的访问速度。但是，buffer pool的大小需要根据数据库的实际情况进行调优，以充分利用可用的内存，并确保能够容纳频繁访问的数据集。
- Change Buffer：
    - InnoDB中的buffer pool是用于缓存数据页的内存区域，它具有高速读取和写入数据的能力。change buffer是用来缓存对于非聚集索引的更新的数据结构。
    - 使用buffer pool可以将热点数据直接缓存到内存中，减少磁盘IO操作，提高读取性能。但是，在插入、更新和删除操作中，对非聚集索引的改动需要对磁盘上的数据页进行读取和写入。由于磁盘IO通常是较慢的，频繁的磁盘操作会导致性能下降。
    - 为了解决这个问题，InnoDB引入了change buffer机制。当对非聚集索引进行插入、更新或删除操作时，change buffer会在内存中进行记录，而不是直接在磁盘上进行操作。这样可以延迟对磁盘的IO操作，缓解磁盘的压力，提高写入性能。
    - 当需要读取非聚集索引的数据时，InnoDB会首先检查change buffer中是否存在对应的数据记录，并将其应用到内存中的数据页上。这样可以减少对磁盘的IO操作，加快读取速度。
    - 需要注意的是，change buffer只用于非聚集索引的更新操作，对于聚集索引的更新操作不会使用change buffer。这是因为聚集索引的数据是按照索引顺序排布在一起的，直接进行插入、更新和删除操作效率更高，不需要额外的change buffer。
    - 通过使用buffer pool和change buffer的组合，InnoDB可以实现高效的数据读取和写入操作，提高数据库的性能和吞吐量。
- Adaptive Hash Index：
    - Adaptive Hash Index（自适应哈希索引）是一个用于加速索引查找的内存结构。（**<font style="color:#DF2A3F;">主要作用是优化对Buffer Pool数据的查询。</font>**）
    - 在InnoDB中，每个索引都有一个对应的B+树来存储索引数据。通常，每次查询时，需要通过B+树的搜索路径来定位到目标数据。然而，当索引数据非常大时，B+树的搜索路径可能很长，导致IO操作增多，降低查询性能。
    - Adaptive Hash Index（简称AHI）的目的就是减少索引查找的IO开销。AHI使用了哈希表数据结构，通过将索引数据的一部分存储在内存中，加速索引的查找速度。
    - AHI的工作原理是：在查询过程中，InnoDB会根据查询模式和数据分布情况自动选择某些索引页，将其放入AHI中以进行内存加速。在下次查询中，InnoDB会先查找AHI，如果找到了目标索引页，就可以直接在内存中定位到数据，而不需要将整个搜索路径都加载到内存。
    - 值得注意的是，AHI并不是适用于所有类型的查询。对于某些查询模式，如区间查询、排序和分组等操作，它的效果有限。对于这些类型的查询，仍然需要通过B+树来定位数据。
    - AHI的大小和效果取决于系统的内存和索引的大小。在InnoDB中，AHI的默认大小是16MB。如果索引数据占用的内存超过AHI的大小，那么将无法完全存储在AHI中，仍然需要通过B+树进行查找。
    - Adaptive Hash Index 可以提高索引查找的性能，但效果会受到查询模式和数据分布的影响。对于合适的查询，它有助于减少IO开销，提高查询性能。
    - **<font style="color:#DF2A3F;">自适应哈希索引不需要程序员干涉，系统根据实际情况自动完成。</font>**
    - **<font style="color:#DF2A3F;">相关配置参数：</font>**
        * **<font style="color:#DF2A3F;">innodb_adaptive_hash_index （是否启用自适应哈希索引，默认是ON，开启的。）</font>**
- Log Buffer：
    - Log Buffer（日志缓冲区）是用于暂存事务日志信息的内存区域。它用来存储被修改的数据页和相关操作的redo日志记录。
    - 当执行事务时，InnoDB会将事务的修改操作记录到Log Buffer中，而不是立即写入到磁盘。这种方式称为Write-Ahead Logging (WAL：预写日志)，通过先将日志记录到Log Buffer，可以减少磁盘IO的频率，提高事务的性能。
    - Log Buffer的大小可以通过配置文件进行设置，其默认大小为8MB。当Log Buffer中的日志记录达到一定的阈值或者事务提交时，InnoDB会将Log Buffer中的日志写入到磁盘的事务日志文件（也称为redo log）中。
    - 事务日志文件是持久化存储引擎的一部分，它保证数据库的事务持久性和一致性。通过将事务的修改操作以日志的形式写入事务日志文件，可以在发生崩溃或故障时进行恢复。当数据库需要进行崩溃恢复时，InnoDB会使用事务日志文件中的日志记录来重做尚未持久化到磁盘的修改操作，确保数据库的一致性。
    - Log Buffer的大小对数据库的性能和可靠性都有影响。较小的Log Buffer可能导致频繁的日志刷新，增加磁盘IO的开销。而较大的Log Buffer可以减少日志刷新的频率，提高事务的性能，但也会增加崩溃恢复的时间。
    - 因此，调整Log Buffer的大小需要根据数据库的实际负载和性能需求进行调优，以平衡性能和可靠性之间的权衡。
    - **<font style="color:#DF2A3F;">相关配置参数：</font>**
        * **<font style="color:#DF2A3F;">innodb_log_buffer_size：缓冲区大小</font>**
        * **<font style="color:#DF2A3F;">innodb_flush_log_at_trx_commit：日志什么时候刷新到磁盘</font>**
            - **<font style="color:#DF2A3F;">取值1：每次事务提交后，日志刷新到磁盘</font>**
            - **<font style="color:#DF2A3F;">取值0：每秒将日志刷新到磁盘</font>**
            - **<font style="color:#DF2A3F;">取值2：每次事务提交后，并且每秒刷新到磁盘</font>**

## InnoDB存储引擎的磁盘结构
![](https://cdn.nlark.com/yuque/0/2023/png/21376908/1691922229269-dc764c07-5ae0-4445-b60a-88f0f474f9bf.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_24%2Ctext_6ICB5p2c%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10)
