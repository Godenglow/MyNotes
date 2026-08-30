## 🌊 视频对应资料


> 视频地址：动力节点最新JavaWeb视频教程,javaweb零基础入门到精通IDEA版[https://www.bilibili.com/video/BV1Z3411C7NZ?p=1&vd_source=93ab990b9131a1b90943874a5448830a](https://www.bilibili.com/video/BV1Z3411C7NZ?p=1&vd_source=93ab990b9131a1b90943874a5448830a)  
资料链接：[https://pan.baidu.com/s/1y-Dm0dGjQQOvARFBmGiG1w?pwd=1234 ](https://pan.baidu.com/s/1y-Dm0dGjQQOvARFBmGiG1w?pwd=1234)  
提取码：1234
>



## 🌊 不使用MVC架构模式程序存在的缺陷


+ 在不使用MVC架构模式的前提下，完成银行账户转账。
+ 分析以下AccountTransferServlet他都负责了什么？ 
    - 1> 负责了数据接收
    - 2> 负责了核心的业务处理
    - 3> 负责了数据库表中数据的CRUD操作（Create【增】 Retrieve【查】 Update【改】 Delete【删】）
    - 4> 负责了页面的数据展示
+ 分析这个程序存在哪些问题？ 
    - 缺点1> 代码的复用性太差。（代码的重用性太差） 
        * 导致缺点1的原因？
        * 因为没有进行“职能分工”，没有独立组件的概念，所以没有办法进行代码复用。代码和代码之间的耦合度太高，扩展力太差。
    - 缺点2> 耦合度高，导致了代码很难扩展。
    - 缺点3> 操作数据库的代码和业务逻辑混杂在一起，很容易出错。编写代码的时候很容易出错，无法专注业务逻辑的编写。



## 🌊 MVC架构模式理论基础


![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762852044483-f7d5038b-b4fe-4cb7-a479-8dcd0bb8340f.png)



## 🌊 JavaEE设计模式-DAO模式


+ AccountDao是负责Account数据的增删改查的。
+ 什么是DAO？ 
    - Data Access Object（数据访问对象）
+ DAO实际上是一种设计模式，属于JavaEE的设计模式之一。（不是23种设计模式。）
+ DAO只负责数据库表的CRUD，没有任何业务逻辑在里面。
+ 没有任何业务逻辑，只负责表中数据增删改查的对象，有一个特殊的称谓：DAO对象。
+ 为什么叫做AccountDao呢？ 
    - 这是因为这个DAO是专门处理t_act这张表的。
    - 如果处理t_user表的话，可以叫做：UserDao
    - 如果处理t_student表的话，可以叫做：StudentDao
+ 一般情况下：一张表会对应一个DAO对象(pojo / bean / domain)。
+ DAO中的方法名很固定了，一般都是： 
    - insert
    - deleteByXxx
    - update
    - selectByXxx
    - selectAll



```java
public class AccountDao {

    /**
     * 插入账户信息
     * @param act  账户信息
     * @return 1表示插入成功
     */
    public int insert(Account act) {
        Connection conn = null;
        PreparedStatement ps = null;
        int count = 0;
        try {
            conn = DBUtil.getConnection();
            String sql = "insert into t_act(actno, balance) values(?,?)";
            ps = conn.prepareStatement(sql);
            ps.setString(1, act.getActno());
            ps.setDouble(2, act.getBalance());
            count = ps.executeUpdate();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            DBUtil.close(conn, ps, null);
        }
        return count;
    }

    /**
     * 根据主键删除账户
     * @param id 主键
     * @return
     */
    public int deleteById(Long id){
        Connection conn = null;
        PreparedStatement ps = null;
        int count = 0;
        try {
            conn = DBUtil.getConnection();
            String sql = "delete from t_act where id = ?";
            ps = conn.prepareStatement(sql);
            ps.setLong(1, id);
            count = ps.executeUpdate();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            DBUtil.close(conn, ps, null);
        }
        return count;
    }

    /**
     * 更新账户
     * @param act
     * @return
     */
    public int update(Account act) {
        Connection conn = null;
        PreparedStatement ps = null;
        int count = 0;
        try {
            conn = DBUtil.getConnection();
            String sql = "update t_act set balance = ? , actno = ? where id = ?";
            ps = conn.prepareStatement(sql);
            ps.setDouble(1, act.getBalance());
            ps.setString(2, act.getActno());
            ps.setLong(3, act.getId());
            count = ps.executeUpdate();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            DBUtil.close(conn, ps, null);
        }
        return count;
    }

    /**
     * 根据账号查询账户
     * @param actno
     * @return
     */
    public Account selectByActno(String actno){
        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        Account act = null;
        try {
            conn = DBUtil.getConnection();
            String sql = "select id,balance from t_act where actno = ?";
            ps = conn.prepareStatement(sql);
            ps.setString(1, actno);
            rs = ps.executeQuery();
            if (rs.next()) {
                Long id = rs.getLong("id");
                Double balance = rs.getDouble("balance");
                // 将结果集封装成java对象
                act = new Account();
                act.setId(id);
                act.setActno(actno);
                act.setBalance(balance);
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            DBUtil.close(conn, ps, rs);
        }
        return act;
    }

    /**
     * 获取所有的账户
     * @return
     */
    public List<Account> selectAll() {
        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        List<Account> list = new ArrayList<>();
        try {
            conn = DBUtil.getConnection();
            String sql = "select id,actno,balance from t_act";
            ps = conn.prepareStatement(sql);
            rs = ps.executeQuery();
            while (rs.next()) {
                // 取出数据
                Long id = rs.getLong("id");
                String actno = rs.getString("actno");
                Double balance = rs.getDouble("balance");
                // 封装对象
                /*Account account = new Account();
                account.setId(id);
                account.setActno(actno);
                account.setBalance(balance);*/
                Account account = new Account(id, actno, balance);
                // 加到List集合
                list.add(account);
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            DBUtil.close(conn, ps, rs);
        }
        return list;
    }

}
```



## 🌊 pojo & bean & domain


+ 账户实体类：封装账户信息的。
+ 一般是一张表对应一个。
+ 这种普通简单的对象被成为pojo对象。
+ 有的人也会把这种专门封装数据的对象，称为bean对象。(javabean：咖啡豆)
+ 有的人也会把这种专门封装数据的对象，称为领域模型对象。domain对象。
+ 不同的程序员有不同的习惯。



```java
public class Account { // 这种普通简单的对象被成为pojo对象。
    /**
     * 主键
     */
    // 一般这种属性不建议设计为基本数据类型，建议使用包装类。防止null带来的问题。
    //private long id;
    private Long id;

    /**
     * 账号
     */
    private String actno;

    /**
     * 余额
     */
    //private double balance;
    private Double balance;

    @Override
    public String toString() {
        return "Account{" +
                "id=" + id +
                ", actno='" + actno + '\'' +
                ", balance=" + balance +
                '}';
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

    public Account(Long id, String actno, Double balance) {
        this.id = id;
        this.actno = actno;
        this.balance = balance;
    }

    public Account() {
    }
}
```



## 🌊 业务层抽取以及业务类实现


+ service翻译为：业务。
+ AccountService：专门处理Account业务的一个类。
+ 在该类中应该编写纯业务代码。（只专注业务。不写别的。不和其他代码混合在一块。）
+ 只希望专注业务，能够将业务完美实现，少量bug。
+ 业务类一般起名：XxxService、XxxBiz.....



```java
public class AccountService {

    // 为什么定义到这里？因为在每一个业务方法中都可以需要连接数据库。
    private AccountDao accountDao = new AccountDao();

    // 这里的方法起名，一定要体现出，你要处理的是什么业务。
    // 我们要提供一个能够实现转账的业务方法（一个业务对应一个方法。）

    /**
     * 完成转账的业务逻辑
     * @param fromActno 转出账号
     * @param toActno 转入账号
     * @param money 转账金额
     */
    public void transfer(String fromActno, String toActno, double money) throws MoneyNotEnoughException, AppException {
        // 查询余额是否充足
        Account fromAct = accountDao.selectByActno(fromActno);
        if (fromAct.getBalance() < money) {
            throw new MoneyNotEnoughException("对不起，余额不足");
        }
        // 程序到这里说明余额充足
        Account toAct = accountDao.selectByActno(toActno);
        // 修改余额（只是修改了内存中java对象的余额）
        fromAct.setBalance(fromAct.getBalance() - money);
        toAct.setBalance(toAct.getBalance() + money);
        // 更新数据库中的余额
        int count = accountDao.update(fromAct);

        // 模拟异常
        String s = null;
        s.toString();

        count += accountDao.update(toAct);
        if (count != 2) {
            throw new AppException("账户转账异常！！！");
        }
    }

}
```



## 🌊 控制层


+ 账户小程序
+ AccountServlet是一个司令官。他负责调度其他组件来完成任务。



```java
@WebServlet("/transfer")
public class AccountServlet extends HttpServlet { // AccountServlet作为Controller

    private AccountService accountService = new AccountService();

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        // 接收数据
        String fromActno = request.getParameter("fromActno");
        String toActno = request.getParameter("toActno");
        double money = Double.parseDouble(request.getParameter("money"));
        try {
            // 调用业务方法处理业务（调度Model处理业务）
            accountService.transfer(fromActno, toActno, money);
            // 执行到这里了，说明成功了。
            // 展示处理结果（调度View做页面展示）
            response.sendRedirect(request.getContextPath() + "/success.jsp");
        } catch(MoneyNotEnoughException e) {
            // 执行到这里了，说明失败了。（余额不足）
            // 展示处理结果（调度View做页面展示）
            response.sendRedirect(request.getContextPath() + "/moneynotenough.jsp");
        } catch(Exception e){
            // 执行到这里了，说明失败了。
            response.sendRedirect(request.getContextPath() + "/error.jsp");
        }
    }
}
```



## 🌊 MVC架构模式与三层架构的关系


![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762852044437-a2bcb1f6-018c-41e8-8e6e-a06005c54713.png)  
![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762852045692-2d2d9118-3d92-4917-9ede-8ba367a1ecab.png)



## 🌊 手撕ThreadLocal源码


![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762852044673-2bb92390-6d1b-4a3f-9b9f-13e309ee287f.png)



```java
public class Connection {
}
```



```java
public class DBUtil {

    // 静态变量特点：类加载时执行，并且只执行一次。
    // 全局的大Map集合
    private static MyThreadLocal<Connection> local = new MyThreadLocal<>();

    /**
     * 每一次都调用这个方法来获取Connection对象
     * @return
     */
    public static Connection getConnection(){
        Connection connection = local.get();
        if (connection == null) {
            // 第一次调用：getConnection()方法的时候，connection一定是空的。
            // 空的就new一次。
            connection = new Connection();
            // 将new的Connection对象绑定到大Map集合中。
            local.set(connection);
        }
        return connection;
    }

}
```



```java
package com.powernode.threadlocal;

import java.util.HashMap;
import java.util.Map;

/**
 * 自定义一个ThreadLocal类
 */
public class MyThreadLocal<T> {

    /**
     * 所有需要和当前线程绑定的数据要放到这个容器当中
     */
    private Map<Thread, T> map = new HashMap<>();

    /**
     * 向ThreadLocal中绑定数据
     */
    public void set(T obj){
        map.put(Thread.currentThread(), obj);
    }

    /**
     * 从ThreadLocal中获取数据
     * @return
     */
    public T get(){
        return map.get(Thread.currentThread());
    }

    /**
     * 移除ThreadLocal当中的数据
     */
    public void remove(){
        map.remove(Thread.currentThread());
    }
}
```



```java
package com.powernode.threadlocal;
// 张三发送请求，对应一个线程t1
// 李四发送请求，对应一个线程t2
public class Test {
    public static void main(String[] args) {

        Thread thread = Thread.currentThread();
        System.out.println(thread);

        // 调用service
        UserService userService = new UserService();
        userService.save();
    }
}
```



```java
package com.powernode.threadlocal;

public class UserService {

    private UserDao userDao = new UserDao();

    public void save(){
        Thread thread = Thread.currentThread();
        System.out.println(thread);

        Connection connection = DBUtil.getConnection();
        System.out.println(connection);

        userDao.insert();
    }

}
```



```java
package com.powernode.threadlocal;

public class UserDao {

    public void insert(){
        Thread thread = Thread.currentThread();
        System.out.println(thread);

        Connection connection = DBUtil.getConnection();
        System.out.println(connection);

        System.out.println("User DAO insert");
    }
}
```



## 🌊 ThreadLocal的使用


> JDK有ThreadLocal类的实现
>



```java
public class DBUtil {

    private static ResourceBundle bundle = ResourceBundle.getBundle("resources/jdbc");
    private static String driver = bundle.getString("driver");
    private static String url = bundle.getString("url");
    private static String user = bundle.getString("user");
    private static String password = bundle.getString("password");

    // 不让创建对象，因为工具类中的方法都是静态的。不需要创建对象。
    // 为了防止创建对象，故将构造方法私有化。
    private DBUtil(){}

    // DBUtil类加载时注册驱动
    static {
        try {
            Class.forName(driver);
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
    }

    // 这个对象实际上在服务器中只有一个。
    private static ThreadLocal<Connection> local = new ThreadLocal<>();

    /**
     * 这里没有使用数据库连接池，直接创建连接对象。
     * @return 连接对象
     * @throws SQLException
     */
    public static Connection getConnection() throws SQLException {
        Connection conn = local.get();
        if (conn == null) {
            conn = DriverManager.getConnection(url, user, password);
            local.set(conn);
        }
        return conn;
    }

    /**
     * 关闭资源
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
                // 思考一下：为什么conn关闭之后，这里要从大Map中移除呢？
                // 根本原因是：Tomcat服务器是支持线程池的。也就是说一个人用过了t1线程，t1线程还有可能被其他用户使用。
                local.remove();
            } catch (SQLException e) {
                throw new RuntimeException(e);
            }
        }
    }

}
```



```java
public class AccountService {

    // 为什么定义到这里？因为在每一个业务方法中都可以需要连接数据库。
    private AccountDao accountDao = new AccountDao();

    // 这里的方法起名，一定要体现出，你要处理的是什么业务。
    // 我们要提供一个能够实现转账的业务方法（一个业务对应一个方法。）

    /**
     * 完成转账的业务逻辑
     * @param fromActno 转出账号
     * @param toActno 转入账号
     * @param money 转账金额
     */
    public void transfer(String fromActno, String toActno, double money) throws MoneyNotEnoughException, AppException {
        // service层控制事务
        try (Connection connection = DBUtil.getConnection()){
            System.out.println(connection);
            // 开启事务(需要使用Connection对象)
            connection.setAutoCommit(false);

            // 查询余额是否充足
            Account fromAct = accountDao.selectByActno(fromActno);
            if (fromAct.getBalance() < money) {
                throw new MoneyNotEnoughException("对不起，余额不足");
            }
            // 程序到这里说明余额充足
            Account toAct = accountDao.selectByActno(toActno);
            // 修改余额（只是修改了内存中java对象的余额）
            fromAct.setBalance(fromAct.getBalance() - money);
            toAct.setBalance(toAct.getBalance() + money);
            // 更新数据库中的余额
            int count = accountDao.update(fromAct);

            // 模拟异常
            String s = null;
            s.toString();

            count += accountDao.update(toAct);
            if (count != 2) {
                throw new AppException("账户转账异常！！！");
            }

            // 提交事务
            connection.commit();
        } catch (SQLException e) {
            throw new AppException("账户转账异常！！！");
        }
    }

}
```



```java
public class AccountDao {

    /**
     * 插入账户信息
     * @param act  账户信息
     * @return 1表示插入成功
     */
    public int insert(Account act) {
        PreparedStatement ps = null;
        int count = 0;
        try {
            Connection conn = DBUtil.getConnection();
            String sql = "insert into t_act(actno, balance) values(?,?)";
            ps = conn.prepareStatement(sql);
            ps.setString(1, act.getActno());
            ps.setDouble(2, act.getBalance());
            count = ps.executeUpdate();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            DBUtil.close(null, ps, null);
        }
        return count;
    }

    /**
     * 根据主键删除账户
     * @param id 主键
     * @return
     */
    public int deleteById(Long id){
        PreparedStatement ps = null;
        int count = 0;
        try {
            Connection conn = DBUtil.getConnection();
            String sql = "delete from t_act where id = ?";
            ps = conn.prepareStatement(sql);
            ps.setLong(1, id);
            count = ps.executeUpdate();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            DBUtil.close(null, ps, null);
        }
        return count;
    }

    /**
     * 更新账户
     * @param act
     * @return
     */
    public int update(Account act) {
        PreparedStatement ps = null;
        int count = 0;
        try {
            Connection conn = DBUtil.getConnection();
            System.out.println(conn);
            String sql = "update t_act set balance = ? , actno = ? where id = ?";
            ps = conn.prepareStatement(sql);
            ps.setDouble(1, act.getBalance());
            ps.setString(2, act.getActno());
            ps.setLong(3, act.getId());
            count = ps.executeUpdate();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            DBUtil.close(null, ps, null);
        }
        return count;
    }

    /**
     * 根据账号查询账户
     * @param actno
     * @return
     */
    public Account selectByActno(String actno){
        PreparedStatement ps = null;
        ResultSet rs = null;
        Account act = null;
        try {
            Connection conn = DBUtil.getConnection();
            System.out.println(conn);
            String sql = "select id,balance from t_act where actno = ?";
            ps = conn.prepareStatement(sql);
            ps.setString(1, actno);
            rs = ps.executeQuery();
            if (rs.next()) {
                Long id = rs.getLong("id");
                Double balance = rs.getDouble("balance");
                // 将结果集封装成java对象
                act = new Account();
                act.setId(id);
                act.setActno(actno);
                act.setBalance(balance);
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            DBUtil.close(null, ps, rs);
        }
        return act;
    }

    /**
     * 获取所有的账户
     * @return
     */
    public List<Account> selectAll() {
        PreparedStatement ps = null;
        ResultSet rs = null;
        List<Account> list = new ArrayList<>();
        try {
            Connection conn = DBUtil.getConnection();
            String sql = "select id,actno,balance from t_act";
            ps = conn.prepareStatement(sql);
            rs = ps.executeQuery();
            while (rs.next()) {
                // 取出数据
                Long id = rs.getLong("id");
                String actno = rs.getString("actno");
                Double balance = rs.getDouble("balance");
                // 封装对象
                /*Account account = new Account();
                account.setId(id);
                account.setActno(actno);
                account.setBalance(balance);*/
                Account account = new Account(id, actno, balance);
                // 加到List集合
                list.add(account);
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        } finally {
            DBUtil.close(null, ps, rs);
        }
        return list;
    }

}
```



## 🌊 不同功能的类放在不同的包下


![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762852044579-804b21e0-2515-4e2c-97f3-153213a3b3f5.png)



> ssm里面一般都把dao包起名为mapper，把web包起名为controller
>



## 🌊 层与层之间应该使用接口进行衔接以及当前项目存在的两大问题


![](https://cdn.nlark.com/yuque/0/2025/png/58040780/1762852045203-eba87152-10f0-4875-86ee-3d84cab872f2.png)

