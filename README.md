# scdow-projects
This is the collection of my projects.

路径导航毕设（进行中）：使用用于即时定位和建图的啮齿动物海马体模型RatSLAM在stanmer park数据集上实现路径导航，正在学习路径规划、SLAM算法中。

干豆分类系统：根据干豆多特征的表格数据，使用随机搜索优化的支持向量机对7类干豆进行多分类，F1分数为0.976。

产品订单需求预测：根据国内某大型制造企业3年的出货数据，使用LightGBM, BiLSTM, Attention和组合模型，按月、周、日颗粒度预测商品未来需求量，发现使用lightgbm算法按天时间颗粒度预测精度较高，获得第十一届泰迪杯数据挖掘挑战赛省三等奖。

脑部MRI肿瘤识别：使用VGG16和Vision transformer对脑部MRI图像做有无肿瘤的分类，其中，在ImageNet上预训练的ViT模型，在MRI数据集仅10轮训练便可以达到92%的准确率。
https://github.com/scdow/ViT-VGG-for-brain-mri-tumor

图像色块识别：使用控制点校准图像，膨胀腐蚀后，标记和提取连通区域坐标，再根据三通道的阈值检测坐标颜色。该系统对含有4个控制点、16个色块的30张带噪模拟图片的色彩识别准确率为100%。

武侠小说事件抽取：使用Bert4keras框架，微调bert-base-Chinese模型，再使用efficient global pointer全局指针网络方法，完成对武侠小说事件触发词和论元的预测。

AI跳棋：使用minimax对抗性搜索和alpha beta剪枝算法，实现AI vs 用户的跳棋游戏，该游戏通过启发式算法和不同的搜索树深度，实现不同的难度级别，并提供GUI。

聊天机器人：https://github.com/scdow/chatrobot

Python冒险游戏：https://github.com/scdow/Dark-recipe-adventure

安卓小球弹射游戏：https://github.com/scdow/compx202-assignment8-31711034-31711036



