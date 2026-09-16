---
tags:
  - Spring
  - 面试
  - SpringMVC
source: 小林coding SpringMVC 篇
date: 2026-09-16
---

# SpringMVC 工作流程

> [!question] 疑问
> 了解 SpringMVC 的处理流程吗？

## 一图走完八步

![[SpringMVC工作流程.svg]]

| 步骤 | 谁干了什么 |
| --- | --- |
| ① | 请求到达 **DispatcherServlet**（前端控制器，一切的总调度） |
| ② | DS 问 **HandlerMapping**：这个 URL 谁来处理？ |
| ③ | 返回 **HandlerExecutionChain**（Handler + 拦截器链） |
| ④ | DS 把 Handler 交给 **HandlerAdapter** 适配执行 |
| ⑤ | Handler（Controller）执行业务，返回 **ModelAndView** |
| ⑥ | 结果经 Adapter 回到 DS |
| ⑦ | DS 请求 **ViewResolver** 解析视图，渲染时把 Model 填进去 |
| ⑧ | 响应用户 |

> [!note] 截图分了 11 步，本图合并为 8 步
> 截图的 ⑥⑦（Handler→Adapter→DS 各返回一次 ModelAndView）在图里合为一条虚线 —— 过程相同，答题按 8 步讲逻辑更清楚，说"约 8 步"即可。

## 三个必考追问

**1. 拦截器挂在哪？** 三个时机正好卡在流程上：`preHandle`（④ 执行前）→ `postHandle`（⑤ 返回后）→ `afterCompletion`（⑧ 渲染完成后，finally 语义）。

**2. 前后端分离下流程怎么变？** `@RestController` 直接跳过 ⑥⑦⑧（不找 ViewResolver、不渲染），由 **HttpMessageConverter** 把返回值序列化成 JSON 写回响应 —— 这就是为什么分离架构下流程题要"减着答"。

**3. 三大组件可插拔**：HandlerMapping / HandlerAdapter / ViewResolver 都是接口，可自定义实现 —— SpringMVC 的扩展性来源（如自定义 HandlerMapping 做灰度路由）。

> [!tip] 一句话速记
> **一切汇聚 DispatcherServlet：问映射器要人 → 交适配器执行 → 拿回 ModelAndView → 解析渲染 → 响应；分离架构砍掉后三步直接回 JSON。**

> [!note] 关联
> [[04-MVC分层与SpringMVC]]（Controller/View 在 MVC 中的位置）；拦截器的 preHandle/afterCompletion 与 [[03-Bean生命周期]] 中 BPP 思想一致 —— 都是"在别人的流程里插自己的逻辑"。
