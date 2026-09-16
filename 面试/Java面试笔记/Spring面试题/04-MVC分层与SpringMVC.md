---
tags:
  - Spring
  - 面试
  - SpringMVC
  - MVC
source: 小林coding SpringMVC 篇
date: 2026-09-16
---

# MVC 分层与 SpringMVC

> [!question] 疑问
> MVC 分层介绍一下？

## 一图看懂三层协作

![[MVC分层交互.svg]]

MVC（Model-View-Controller）是一种**分层设计典范**：把业务逻辑、数据、界面显示拆开，改界面不用动业务，改业务不用动界面。

| 分层 | 职责 | 谁来干 |
| --- | --- | --- |
| Controller 控制器 | 接收请求，转发给 Model，根据结果选响应 | `@Controller` / `@RestController` |
| Model 模型 | 承载数据 + 处理计算 | 见下方两种 Bean |
| View 视图 | 界面显示，与用户交互 | JSP / Thymeleaf / 前端页面 |

## Model 的两种 Bean（本页唯一考点）

| 类型 | 是什么 | 例子 |
| --- | --- | --- |
| **业务处理 Bean** | 处理用户请求的逻辑 | Service、Dao |
| **数据承载 Bean** | 承载业务数据的实体 | User 等实体类（POJO） |

> [!tip] 一句话速记
> **Controller 是调度中枢，Model = 干活的 Bean + 装数据的 Bean，View 只管显示。**

## 演进与现代形态

- **前后端分离后**：View 交给前端框架渲染，后端 `@RestController` 直接返回 JSON —— MVC 的思想没变，View 换了实现方式
- **SpringMVC** 就是 Spring 对 MVC 模式的实现，核心是前端控制器 **DispatcherServlet** —— 它的工作流程（九大组件、执行顺序）是下一道大题

> [!note] 关联
> [[01-IOC与AOP实现原理]]：Controller / Service / Dao 全是容器里的 Bean，MVC 分层是建立在 IOC 之上的组织方式。
