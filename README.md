# nCoV-Map: 新型肺炎疫情地图

> 「弱小和无知不是生存的障碍，傲慢才是」——《三体》

本项目旨在为各种有利于抗击新型肺炎的应用提供简单框架。目前已实现简单的疫情演进地图(自2020年1月22日22点始)及资讯展示功能。

[示例网址](http://106.13.58.203:4000/)。页面展示：

<p align="center">
  <h5>全国疫情</h5>
  <img src="nCoV-Map.png" alt="nCoV-Map.png">
  <br />
  <h5>地级市疫情</h5>
  <img src="provinceMap.png" alt="provinceMap.png">
  <br />
</p>
TODO:
*优化全国疫情图的加载（由于一次性加载很多天的数据，导致页面加载过慢，后面考虑按需加载。）

本项目遵循MIT License，您可以任何方式在此基础上扩展您的应用。以下为一些可供参考的idea：

* 微博舆情分析
* 春运交通流量
* 各地呼吸科医院展示
* 传播模拟
* 地图下钻
* 全网口罩比:价
* 捐赠信息汇总

## 项目依赖
* python3
* flask
* pyecharts
* pypinyin
## 数据来源
感谢[Isaac Lin](https://github.com/BlankerL)提供数据接口：<https://lab.isaaclin.cn/nCoV/>
