#TestingWork

##基础知识

>bug基本要素

* 缺陷ID，状态，类型，所属项目，所属模块，缺陷提交时间，缺陷提交人（检测者），严重程度，优先级别，缺陷描述信息，测试步骤，测试前置条件，测试数据，期望结果，实际结果

>黑盒测试和白盒测试的运用场景

* 黑盒测试适用于对程序内部结构不了解而只关心程序功能的场合；
* 白盒测试适用于更关注程序内部逻辑结构的测试

>做好测试用例设计的关键是什么

* 黑盒：以较少的用例覆盖输出和输入接口
* 白盒：以较少的用例覆盖多的内部程序结果

>javaScript的加载
* ```<script src="script.js"></script>```
  
  没有 defer 或 async，浏览器会立即加载并执行指定的脚本，
  “立即”指的是在渲染该 script 标签之下的文档元素之前，
  也就是说不等待后续载入的文档元素，读到就加载并执行。
  
* ```<script async src="script.js"></script>```
  
  有 async，加载和渲染后续文档元素的过程将和 script.js 
  的加载与执行并行进行（异步）。
  
* ```<script defer src="myscript.js"></script>```
  
  有 defer，加载后续文档元素的过程将和 script.js 
  的加载并行进行（异步），但是 script.js 的执行要在所有元素解析完成之后，
  DOMContentLoaded 
  
详细参考 [defer和async的区别](https://segmentfault.com/q/1010000000640869)