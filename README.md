# scdow-projects

【OP SNN】约束满足问题求解器毕设：SNN求解图着色问题，基于GeNN在 https://www.frontiersin.org/articles/10.3389/fnins.2017.00714/full 的基础上工作。

【Game Python】带GUI的怪味美食制作游戏：https://github.com/scdow/Dark-recipe-adventure

【Game Python AI】AI跳棋：使用minimax对抗性搜索和alpha beta剪枝算法，实现AI vs 用户的跳棋游戏，该游戏通过启发式算法和不同的搜索树深度，实现不同的难度级别，并提供GUI。
https://github.com/scdow/checker-minimax-and-pruning

【Game Java Android】Android小球弹射游戏：https://github.com/scdow/compx202-assignment8-31711034-31711036

【RAG prompt】https://github.com/scdow/rag-prompt  

【OP】整车库房运营资源模拟：使用按优先级规划方法和基于or-tools的混合整数规划方法，安排低成本高效的车辆运算、仓储计划，通过docker提交结果，团队获得BMW黑客松的工业流程优化仿真赛道第二名。
https://tianchi.aliyun.com/competition/entrance/532138/customize387

【Data】产品订单需求预测：根据国内某大型制造企业3年的出货数据，构建时间戳、时序值、商品属性特征，并使用Sequential forward selection进行特征选择。使用LightGBM（通过贝叶斯优化选择超参数）, BiLSTM, Attention和组合模型，按月、周、日颗粒度预测商品未来需求量，发现使用lightgbm算法按天时间颗粒度预测精度较高，获得第十一届泰迪杯数据挖掘挑战赛省三等奖。
https://github.com/scdow/dataming

【Agent AI】觅食机器人自适应系统：使用进化神经网络CTRNNs_NEAT在模拟器上控制小机器人在有毒药环境下的进食。 
https://github.com/scdow/hungry-robot 

【Agent ABM】蚁群决策分析：使用ABM建模和蒙特卡洛法，通过阈值规则解释蚁群寻找巢穴的集体决策。
https://github.com/scdow/ants-decision-making

【NLP】文本分类与关键词抽取：使用Bert模型和TF-IDF算法，做基于医学/非医学论文摘要的文本分类与关键词抽取，在讯飞挑战赛中排名前25。
https://challenge.xfyun.cn/topic/info?type=abstract-of-the-paper  

【NLP AIGC】生成式问答机器人：基于LLama-Index, LangChain和Gradio，使用ChatYuan大语言模型实现生成式知识问答系统。支持用户使用自然语言，来询问输入的文本、PDF文件中的信息。
https://github.com/scdow/QA-chatbot

【Data】干豆分类系统：根据干豆多特征的表格数据，使用随机搜索优化的支持向量机对7类干豆进行多分类，F1分数为0.976，结果好于原论文（原论文链接 https://doi.org/10.1016/j.compag.2020.105507）。

【CV】图像色块识别：使用控制点校准图像，膨胀腐蚀后，标记和提取连通区域坐标，再根据三通道的阈值检测坐标颜色。该系统对含有4个控制点、16个色块的30张带噪模拟图片的色彩识别准确率为100%。
https://github.com/scdow/lego-image-processing

【IoT PM】物联网解决方案：通过加速度传感器和陀螺仪感知车身状态，与云服务器通信并同步给工作人员，解决共享单车翻倒后堆叠、无人使用的问题。
https://github.com/scdow/IoT-shared-bikes

【CV】脑部MRI肿瘤识别：使用Vision transformer（ViT）和VGG16对2D脑部MRI图像做有无肿瘤的分类。ViT模型在ImageNet-1k数据集上预训练后，在MRI数据集中经过10轮训练（时间原因）后准确率约为95%；VGG16在ImageNet上预训练后，在模型底部增加4个全连接层、冻结其它层，微调10轮后准确率约为92%。待优化。
https://github.com/scdow/ViT-VGG-for-brain-mri-tumor

【NLP】武侠小说事件抽取：使用Bert4keras框架，微调bert-base-Chinese模型，再使用efficient global pointer全局指针网络方法，完成对武侠小说事件触发词和论元的预测。

【SDE】天气查看器：应用允许用户登录，显示选定城镇的天气信息，并能够从预定义列表中添加或删除城镇。通过xampp在本地模拟了web服务器环境，使用phpMyAdmin用web接口管理MySQL数据库，通过AJAX将数据库中的天气数据增量更新到HTML页面。
https://github.com/scdow/weather-watcher

【SDE】任务管理：springboot + vue3
https://github.com/scdow/task-spring , 
https://github.com/scdow/task-vue





