# scdow-projects

约束满足问题求解器毕设：SNN求解图着色问题，基于GeNN在 https://www.frontiersin.org/articles/10.3389/fnins.2017.00714/full 的基础上工作。

整车库房运营资源模拟：使用按优先级规划方法和基于or-tools的混合整数规划方法，安排低成本高效的车辆运算、仓储计划，通过docker提交结果，团队获得BMW黑客松的工业流程优化仿真赛道第二名。
https://tianchi.aliyun.com/competition/entrance/532138/customize387

产品订单需求预测：根据国内某大型制造企业3年的出货数据，构建时间戳、时序值、商品属性特征，并使用Sequential forward selection进行特征选择。使用LightGBM（通过贝叶斯优化选择超参数）, BiLSTM, Attention和组合模型，按月、周、日颗粒度预测商品未来需求量，发现使用lightgbm算法按天时间颗粒度预测精度较高，获得第十一届泰迪杯数据挖掘挑战赛省三等奖。
https://github.com/scdow/dataming

觅食机器人自适应系统：使用进化神经网络CTRNNs_NEAT在模拟器上控制小机器人在有毒药环境下的进食 https://github.com/scdow/hungry-robot 

文本分类与关键词抽取：使用Bert模型和TF-IDF算法，做基于医学/非医学论文摘要的文本分类与关键词抽取，在讯飞挑战赛中排名前25。
https://challenge.xfyun.cn/topic/info?type=abstract-of-the-paper  

生成式聊天机器人：https://github.com/scdow/chatrobot

干豆分类系统：根据干豆多特征的表格数据，使用随机搜索优化的支持向量机对7类干豆进行多分类，F1分数为0.976，结果好于原论文（原论文连接https://doi.org/10.1016/j.compag.2020.105507）。

图像色块识别：使用控制点校准图像，膨胀腐蚀后，标记和提取连通区域坐标，再根据三通道的阈值检测坐标颜色。该系统对含有4个控制点、16个色块的30张带噪模拟图片的色彩识别准确率为100%。

脑部MRI肿瘤识别：使用VGG16和Vision transformer对脑部MRI图像做有无肿瘤的分类，其中，在ImageNet上预训练的ViT模型，在MRI数据集10轮训练后准确率为92%，待优化。
https://github.com/scdow/ViT-VGG-for-brain-mri-tumor

武侠小说事件抽取：使用Bert4keras框架，微调bert-base-Chinese模型，再使用efficient global pointer全局指针网络方法，完成对武侠小说事件触发词和论元的预测。

AI跳棋：使用minimax对抗性搜索和alpha beta剪枝算法，实现AI vs 用户的跳棋游戏，该游戏通过启发式算法和不同的搜索树深度，实现不同的难度级别，并提供GUI。
https://github.com/scdow/checker-minimax-and-pruning

带GUI的Python冒险游戏：https://github.com/scdow/Dark-recipe-adventure

Android小球弹射游戏：https://github.com/scdow/compx202-assignment8-31711034-31711036



