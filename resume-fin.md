## 曹庭锋

- 手机 | 微信：133 8026 1185
- 邮箱：me@nicholasc.cn
- 研究方向：大语言模型、AI Agent、量化交易、多模态
- [GitHub](https://github.com/NicholasCao) | [Google Scholar](https://scholar.google.com/citations?user=2-scyfwAAAAJ&hl=zh-CN)

### 教育背景
- 2021.09 ~ 2024.06: 华南理工大学 | 软件工程 | 硕士
- 2017.09 ~ 2021.06: 深圳大学 | 电子信息工程 | 学士

### 工作经历
- 2023.12 ~ 2024.04 & 2024.07 至今 阿里国际-Lazada
  - **ABuddy - 全模态电商购物Agent - 内部创业项目**（进行中）：
    - 主导 ShoppingOmniAgent 环境&评测：基于 UCP 协议构建电商沙盒环境，整合多平台数据支持全链路模拟。设计 AgentBench 评测体系，覆盖8大意图类别，支持 Model×Harness 解耦评测与动态 Criteria 自动评分
    - 设计 Agent 训练方案：闭源大模型采集轨迹蒸馏 + 用户行为模拟长尾场景，训练流程为拒绝采样蒸馏 → OPD → 全链路 RL 强化（多层奖励函数联合优化）
    - 主导视频语音搜升级为Qwen3-Omni端到端全模态方案，全链路RT **-38.3%**，Function Calling F1 **+17.7pt**
    - 搭建 Agent Team Warriors：基于 Claude Code Agent Teams 的全自动研发系统，9个Agent协作完成全链路开发
  - **LLM导购能力全链路落地**：
    - PDP伴随导购：LLM实时生成意图文案与Query改写，一跳CTR **+81%**，二跳GMV **+98%**，东南亚六国实验
    - 大模型I2I搭配推荐：LLM生成跨类目搭配关系，凑单订单 **+4.2%**，GMV **+3.6%**
  - **虚拟试衣**：提出 BVTON 框架，从无配对数据自动构造训练对实现高保真试衣。[CVPR 2026](https://arxiv.org/abs/2411.01593)
  - **商品背景图优化**：提出Product2IMG和奖励偏序优化算法，六国推全CPO平均 **-8%**。[ACM MM 2024](https://dl.acm.org/doi/abs/10.1145/3664647.3680753)
- 2022.10 ~ 2023.10 阿里云-PAI团队 `实习`
  - **BeautifulPrompt**: SFT+RLAIF微调LLM做prompt优化，云栖大会展出，开源模型月下载上万。[EMNLP 2023 Industry](https://arxiv.org/abs/2311.06752)
  - **Attention理解&图像编辑**: 证明注意力图携带语义信息，应用到无训练图像编辑取得SOTA。[CVPR 2024](https://openaccess.thecvf.com/content/CVPR2024/papers/Liu_Towards_Understanding_Cross_and_Self-Attention_in_Stable_Diffusion_for_Text-Guided_CVPR_2024_paper.pdf)
  - **X-STA**: 梯度分解知识共享+语义对齐，跨语言MRC三数据集SOTA。[EMNLP 2023](https://arxiv.org/abs/2311.06758)
- 2019.07 ~ 2019.09 & 2021.04 ~ 2021.06 腾讯（PCG-腾讯文档、IEG-光子工作室）`实习`

### 量化交易经历
- **A股多策略实盘**（2025.01至今，实盘超半年，年化约30%）：
  - 四策略融合（价投PB+ROA / 残差因子+小市值 / ETF动量R²轮动 / 红利低波），各策略资金隔离独立运行，XGBoost/SVR因子合成
- **美股专家共振因子**：抓取多个大V专家发言，通过LLM分析，将看多同一标的形成共振信号，作为辅助因子提高交易胜率

### 竞赛&获奖
- 第一届粤港澳大湾区国际算法算例大赛-预训练语言模型应用调优算法（奖金池100W）- 第一名:
  - 在Language Model as Service场景，无法访问模型权重的情况下优化模型。提出模型校准、梯度和进化算法联合调优，初赛A/B榜和决赛均第一。
  - [Gradient-free tuning for large language models competition](https://academic.oup.com/nsr/advance-article/doi/10.1093/nsr/nwad124/7152626) `NSR IF≈23`
- 第二届粤港澳大湾区国际算法算例大赛-大语言模型综合能力强化 - 前八
- 五粮液优秀学生奖学金（2023）: 专业内成果排名TOP3。
