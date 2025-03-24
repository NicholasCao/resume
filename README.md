## 曹庭锋

- 手机 | 微信：133 8026 1185
- 邮箱：me@nicholasc.cn
- 研究方向：AIGC、大语言模型、文生图、多模态
- 期望岗位: AIGC算法工程师
- [GitHub](https://github.com/NicholasCao) | [Google Scholar](https://scholar.google.com/citations?user=2-scyfwAAAAJ&hl=zh-CN)

<!-- --- -->

### 教育背景
- 2021.09 ~ 2024.06: 华南理工大学 | 软件工程 | 硕士
- 2017.09 ~ 2021.06: 深圳大学 | 电子信息工程 | 学士

<!-- --- -->

### 工作经历
- 2023.12 ~ 2024.04 & 2024-07 至今 阿里国际-Lazada
  - **虚拟试衣**：基于FLUX的虚拟试衣，采用CatVTON架构，迅速追平业界SOTA水位。此后在像素级loss上优化模型出图细节，解决复杂纹理错乱、颜色偏差问题，并使用mask增强、mask-free方案缓解mask泄漏问题；在ProjectS项目中，搭配智能裁剪/回帖、图片超分、模特手部/身材保持等功能集成完整试衣链路，模型评测GSB +40%优于绘蛙。同时为站内Tab2频道、商家侧提供能力解决高质量虚拟试衣难题。
  - **商品背景图优化**：
    - Lazada外投场景下，商家主图质量良莠不齐，通过AIGC技术换商品图背景以提高外投效率。提出Product2IMG和外投效率奖励偏序优化算法，前者使用对比学习增强背景表征和多模态大模型迭代地筛选高质量数据，后者基于线上数据训练奖励模型并基于奖励模型进行偏序优化提高模型出图在线上表现。两算法在东南亚六国推全，带来收益CPO(Cost Per Order)平均减少8%。
    - [Product2IMG: Prompt-Free E-commerce Product Background Generation with Diffusion Model and Self-Improved LMM](https://dl.acm.org/doi/abs/10.1145/3664647.3680753) `ACM MM 2024`
- 2022.10 ~ 2023.10 阿里云-PAI团队 `实习`
  - **BeautifulPrompt**: 基于Stable Diffusion的prompt engineering，使用完整Pipeline自动生成数据集，并基于SFT和RLAIF微调bloom-1b1。优化后的图片质量大大优于原始prompt，效果可比肩甚至超越商用的PromptPerfect。成果在云栖大会展出，模型开源到[Huggingface](https://huggingface.co/alibaba-pai/pai-bloom-1b1-text2prompt-sd)月下载量上万，产出论文[BeautifulPrompt: Towards automatic prompt engineering for text-to-image synthesis](https://arxiv.org/abs/2311.06752) `EMNLP 2023 Industry`

  - **Attention理解&图像编辑**: 深度探索了注意力机制，设计并主导探针实验证明注意力图携带语义信息，其理论应用到无需训练的文生图编辑上取得SOTA性能。产出论文：[Towards Understanding Cross and Self-Attention in Stable Diffusion for Text-Guided Image Editing](https://openaccess.thecvf.com/content/CVPR2024/papers/Liu_Towards_Understanding_Cross_and_Self-Attention_in_Stable_Diffusion_for_Text-Guided_CVPR_2024_paper.pdf)`CVPR 2024`

  - **X-STA**: 跨语言机器阅读理解任务，基于知识共享、教导和对齐三个原则，提出了一种梯度分解的知识共享技术来传输语言表征。并使用输出校准和语义对齐来进一步利用来提高模型的跨语言转移能力。在三个跨语言MRC数据集上取得新的SOTA。产出论文：[Sharing, Teaching and Aligning: Knowledgeable Transfer Learning for Cross-Lingual Machine Reading Comprehension](https://arxiv.org/abs/2311.06758)`EMNLP 2023`

- 2021.04 ~ 2021.06 腾讯IEG-光子工作室 `实习`
- 2019.07 ~ 2019.09 腾讯PCG-腾讯文档团队 `实习`

<!-- - 2021-04 ~ 2021-06 腾讯IEG-光子工作室

  光子设备管理平台前后端开发、基于React Native的APP端搭建，游戏组件版本识别算法实现等。
- 2019-07 ~ 2019-09 腾讯PCG-腾讯文档团队

  腾讯文档测试平台的前端重构，后端优化、更新以及逐步迁移到golang
接入tps、tapd等腾讯内部系统；部门实习生表现排名第二。 -->

### 竞赛&获奖经历
- 第一届粤港澳大湾区国际算法算例大赛-预训练语言模型应用调优算法（奖金池100W）- 第一名:
  <!-- - 第一名团队（获60W奖金，主要贡献）； -->
  - 在Language Model as Service场景，即以API的形式，无法访问模型权重的情况下优化模型。提出以模型校准、梯度和进化算法联合调优的算法，在不同数据效果大幅超越baselines，在初赛A榜、B榜和决赛上均取得第一名。
  - [Gradient-free tuning for large language models competition: approaches, results, current challenges and future directions](https://academic.oup.com/nsr/advance-article/doi/10.1093/nsr/nwad124/7152626) `NSR IF≈23`
- 第二届粤港澳大湾区国际算法算例大赛-大语言模型综合能力强化 - 前八
- 五粮液优秀学生奖学金（2023）: 专业内成果排名TOP3。
<!-- - [ChatBLOOM](https://github.com/NicholasCao/ChatBLOOM)

  基于BLOOM（17亿参数）微调的中英双语对话模型，可以表现出不俗的能力，模型上传到[Hugging Face](https://huggingface.co/nicholascao/chatbloom-1b7-sft)。
- [Goa](https://github.com/goa-go/goa):
  基于中间件的轻量级golang web框架，benchmark测试可比肩golang主流框架，详情可查阅[文档](https://goa-go.github.io).
- [MVVM前端框架](https://github.com/nicholascao/mvvm):
  类Vue的前端框架实现了数据监听、视图模块解析、表达式解析等以及vue中的常用指令。 -->

