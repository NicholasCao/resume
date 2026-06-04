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
    - 主导 ShoppingOmniAgent 环境&评测：基于 UCP 协议构建电商沙盒环境，整合淘宝/亚马逊/Lazada多平台商品数据，支持搜索→加购→结算→支付全链路模拟与图片/视频/直播多模态交互。设计 AgentBench 评测体系，覆盖8大购物意图类别，支持 Model×Harness 解耦评测，通过规则校验与 LLM 语义评估双模式自动打分；评估框架还支持动态 Criteria 生成，可根据 Task 类型自动组合评分维度
    - 设计 Agent 训练方案：线上部署闭源大模型全量采集 Agent 轨迹（含推理链）作为教师信号，同时基于站内用户行为轨迹构建画像&购物意图让 LLM 模拟多轮交互覆盖长尾场景。训练流程为拒绝采样轨迹蒸馏 → OPD训练 → 全链路 RL 强化（线上用户反馈对齐 + Turn/Session/CTR 多层奖励函数联合优化）
    - 主导视频语音搜升级为Qwen3-Omni端到端全模态方案，全链路RT **-38.3%**，电商Function Calling Category F1 **+17.7pt**。基于真实用户拍摄图片提取anchor商品并由VLM生成多类意图，通过双Agent角色扮演自动合成含agentic轨迹多轮对话训练数据，结合相似图检索构造视频帧序列覆盖多帧场景，人工校验后用于模型SFT。
    - 搭建 Agent Team Warriors：基于 Claude Code Agent Teams 的 AI Native 全自动研发系统，9个专职 Agent 协作完成需求→调研→设计→开发→验证→监控全链路，每阶段经质量门禁闭环验收；同时产出 abuddy-server 全栈服务
  - **LLM导购能力全链路落地**：
    - PDP伴随导购：基于用户全域实时行为，LLM实时生成意图文案与Query改写，一跳CTR **+81%**，二跳引导GMV **+98%**，菲律宾全量、东南亚六国实验
    - 大模型I2I搭配推荐：利用LLM世界知识为电商叶子类目生成搭配关系，构建跨类目I2I召回数据，凑单订单 **+4.2%**（菲律宾全量），复用至图搜联想场景，GMV **+3.6%**，订单 **+1.5%**
  - **虚拟试衣**：
    - 基于FLUX的虚拟试衣，采用CatVTON架构迅速追平业界SOTA水位。在像素级loss上优化出图细节，解决复杂纹理错乱、颜色偏差问题，并使用mask增强、mask-free方案缓解mask泄漏问题。提出 BVTON 框架，从海量无配对时尚图片中自动构造训练对，摆脱对人工标注配对数据的依赖。在ProjectS项目中搭配智能裁剪/回帖、图片超分、模特手部/身材保持等功能集成完整试衣链路，模型评测GSB +40%优于绘蛙，同时为站内Tab2频道、商家侧提供能力。
    - [High-Fidelity Virtual Try-on with Large-Scale Unpaired Learning](https://arxiv.org/abs/2411.01593) `CVPR 2026`
  - **商品背景图优化**：
    - Lazada外投场景下，商家主图质量良莠不齐，通过AIGC技术换商品图背景以提高外投效率。提出Product2IMG和外投效率奖励偏序优化算法，前者使用对比学习增强背景表征和多模态大模型迭代地筛选高质量数据，后者基于线上数据训练奖励模型并基于奖励模型进行偏序优化提高模型出图在线上表现。两算法在东南亚六国推全，带来收益CPO(Cost Per Order)平均减少8%。
    - [Product2IMG: Prompt-Free E-commerce Product Background Generation with Diffusion Model and Self-Improved LMM](https://dl.acm.org/doi/abs/10.1145/3664647.3680753) `ACM MM 2024`
- 2022.10 ~ 2023.10 阿里云-PAI团队 `实习`
  - **BeautifulPrompt**: 基于SFT和RLAIF微调bloom-1b1实现text-to-image的prompt优化，效果比肩商用PromptPerfect。云栖大会展出，开源模型月下载量上万。产出论文：[BeautifulPrompt](https://arxiv.org/abs/2311.06752) `EMNLP 2023 Industry`
  - **Attention理解&图像编辑**: 设计探针实验证明注意力图携带语义信息，应用到无需训练的文生图编辑取得SOTA。产出论文：[Towards Understanding Cross and Self-Attention in Stable Diffusion for Text-Guided Image Editing](https://openaccess.thecvf.com/content/CVPR2024/papers/Liu_Towards_Understanding_Cross_and_Self-Attention_in_Stable_Diffusion_for_Text-Guided_CVPR_2024_paper.pdf) `CVPR 2024`
  - **X-STA**: 提出梯度分解知识共享技术，结合输出校准与语义对齐提升跨语言MRC转移能力，三个数据集SOTA。产出论文：[Sharing, Teaching and Aligning](https://arxiv.org/abs/2311.06758) `EMNLP 2023`

- 2019.07 ~ 2019.09 & 2021.04 ~ 2021.06 腾讯（PCG-腾讯文档、IEG-光子工作室）`实习`

### 量化交易经历
- **A股多策略实盘**（2025.01至今，实盘超半年，年化约30%）：
  - 四策略融合（价投PB+ROA / 残差因子+小市值 / ETF动量R²轮动 / 红利低波），各策略资金隔离独立运行，XGBoost/SVR因子合成
- **美股专家共振因子**：抓取多个大V专家发言，通过LLM分析，将看多同一标的形成共振信号，作为辅助因子提高交易胜率

### 竞赛&获奖
- 第一届粤港澳大湾区国际算法算例大赛-预训练语言模型应用调优算法（奖金池100W）- 第一名:
  - 在Language Model as Service场景，即以API的形式，无法访问模型权重的情况下优化模型。提出以模型校准、梯度和进化算法联合调优的算法，在不同数据效果大幅超越baselines，在初赛A榜、B榜和决赛上均取得第一名。
  - [Gradient-free tuning for large language models competition: approaches, results, current challenges and future directions](https://academic.oup.com/nsr/advance-article/doi/10.1093/nsr/nwad124/7152626) `NSR IF≈23`
- 第二届粤港澳大湾区国际算法算例大赛-大语言模型综合能力强化 - 前八
- 五粮液优秀学生奖学金（2023）: 专业内成果排名TOP3。
