
# 开发规范指南

为保证代码质量、可维护性、安全性与可扩展性，请在开发过程中严格遵循以下规范。

## 一、项目基础信息

- **项目工作目录**：`D:\BaiduNetdiskDownload\Obsidian-Notes\AngelByte_Note\Radis\Redis入门\代码\redis-demo`
- **项目构建工具**：Maven
- **主框架**：Spring Boot 2.5.7
- **语言版本**：JDK 21.0.2 (注：虽然pom.xml声明1.8，但环境信息明确为JDK 21，请确保编译环境与实际运行环境一致，若需兼容旧版本请调整pom.xml的java.version属性)
- **核心依赖**：
  - `spring-boot-starter-data-redis`
  - `commons-pool2` (Redis连接池)
  - `jackson-databind` (序列化)
  - `lombok`
- **代码作者**：29074

## 二、目录结构规范

项目需遵循以下目录树结构，保持包名与目录层级一致：

```text
redis-demo
└── redis-demo
    └── src
        ├── main
        │   ├── java
        │   │   └── com
        │   │       └── heima
        │   │           └── redis
        │   │               ├── config      # 配置类（如RedisConfig）
        │   │               └── pojo        # 实体/数据传输对象
        │   └── resources
        │       └── application.yaml        # 应用配置文件
        └── test
            └── java
                └── com
                    └── heima
```

- **包命名规范**：统一使用 `com.heima.redis` 作为基础包。
- **配置类**：所有Redis相关的配置（如`RedisTemplate`、`LettuceConnectionFactory`配置）必须放在 `config` 包下。
- **数据对象**：实体类或DTO统一放在 `pojo` 包下。

## 三、Redis 专项规范

### 1. 连接池配置
- 必须使用 `lettuce` 连接池，并在 `application.yaml` 中显式配置连接池参数（如 `max-active`, `max-idle`, `min-idle`, `max-wait`），避免默认配置在生产环境导致性能瓶颈。
- 示例配置：
  ```yaml
  spring:
    redis:
      lettuce:
        pool:
          max-active: 8
          max-idle: 8
          min-idle: 0
          max-wait: 100ms
  ```

### 2. 序列化规范
- 使用 `Jackson2JsonRedisSerializer` 作为默认的序列化方式，确保数据可读性和兼容性。
- 禁止使用 JDK 原生序列化，除非有特殊性能需求且明确知道后果。

### 3. 异常处理
- 对 Redis 操作进行必要的异常捕获（如 `TimeoutException`, `ConnectionRefusedException`），避免单点故障影响主业务逻辑。

## 四、分层架构规范

| 层级        | 职责说明                         | 开发约束与注意事项                                               |
|-------------|----------------------------------|----------------------------------------------------------------|
| **Controller** | 处理 HTTP 请求与响应，定义 API 接口 | 不得直接访问 Redis 或数据库，必须通过 Service 层调用             |
| **Service**    | 实现业务逻辑、事务管理与数据校验   | 必须通过 Repository 或 RedisTemplate 访问数据；返回 DTO          |
| **Config**     | 配置类                           | 负责 `RedisTemplate`、`StringRedisTemplate` 等 Bean 的初始化     |
| **POJO**       | 数据传输对象                     | 实体类需实现 `Serializable` 接口（若使用 JDK 序列化）或确保 JSON 序列化兼容 |

### 接口与实现分离

- 所有接口实现类需放在接口所在包下的 `impl` 子包中（若项目复杂度增加，建议重构为标准分层）。

## 五、安全与性能规范

### 输入校验

- 使用 `@Valid` 与 JSR-303 校验注解（如 `@NotBlank`, `@Size` 等）。
- **注意**：Spring Boot 2.5.x 使用 `javax.validation.constraints.*`，若迁移至 Spring Boot 3.x 需改为 `jakarta.validation.constraints.*`。

### 事务管理

- `@Transactional` 注解仅用于 **Service 层**方法。
- Redis 操作通常不涉及数据库事务，但需注意 Redis 命令的原子性。

### 性能优化

- 避免在循环中频繁执行 Redis 命令，尽量使用管道（Pipeline）或批量操作（如 `mget`, `mset`）。
- 设置合理的 Key 过期时间，防止内存泄漏。

## 六、代码风格规范

### 命名规范

| 类型       | 命名方式             | 示例                  |
|------------|----------------------|-----------------------|
| 类名       | UpperCamelCase       | `RedisConfig`         |
| 方法/变量  | lowerCamelCase       | `getUserCache()`      |
| 常量       | UPPER_SNAKE_CASE     | `DEFAULT_CACHE_TTL`   |

### 注释规范

- 所有类、方法、字段需添加 **Javadoc** 注释。
- **语言要求**：注释必须使用**中文**（用户第一语言）。

### 类型命名规范（阿里巴巴风格）

| 后缀 | 用途说明                     | 示例         |
|------|------------------------------|--------------|
| DTO  | 数据传输对象                 | `UserDTO`    |
| BO   | 业务逻辑封装对象             | `UserBO`     |
| VO   | 视图展示对象                 | `UserVO`     |
| Query| 查询参数封装对象             | `UserQuery`  |

### 实体类简化工具

- 使用 Lombok 注解替代手动编写 getter/setter/构造方法：
  - `@Data`
  - `@NoArgsConstructor`
  - `@AllArgsConstructor`

## 七、扩展性与日志规范

### 接口优先原则

- 所有业务逻辑通过接口定义，具体实现放在 `impl` 包中。

### 日志记录

- 使用 `@Slf4j` 注解代替 `System.out.println`。
- 日志级别使用规范：
  - `ERROR`：系统错误、异常
  - `WARN`：警告信息、潜在风险
  - `INFO`：关键业务流程、配置加载
  - `DEBUG`：调试信息、详细参数

## 八、编码原则总结

| 原则       | 说明                                       |
|------------|--------------------------------------------|
| **SOLID**  | 高内聚、低耦合，增强可维护性与可扩展性     |
| **DRY**    | 避免重复代码，提高复用性                   |
| **KISS**   | 保持代码简洁易懂                           |
| **YAGNI**  | 不实现当前不需要的功能                     |
| **OWASP**  | 防范常见安全漏洞，如 SQL 注入、XSS 等      |
| **Redis Best Practices** | 合理设置 TTL，使用 Pipeline 优化批量操作，注意序列化性能 |
