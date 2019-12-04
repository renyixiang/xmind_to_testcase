##感谢大佬提供的代码，直接拿过来就可以用，很稳健！

# XMind2TestCase
直接运行/Users/***/Downloads/百度网盘/xmind2testcase-master/webtool/application.py这个脚本就好了
> **XMind2TestCase** 工具，提供了一个高效测试用例设计的解决方案！


### 一、背景

软件测试过程中，最重要、最核心就是测试用例的设计，也是测试童鞋、测试团队日常投入最多时间的工作内容之一。

然而，传统的测试用例设计过程有很多痛点：
- 1、使用Excel表格进行测试用例设计，虽然成本低，但版本管理麻烦，维护更新耗时，用例评审繁琐，过程报表统计难...
- 2、使用TestLink、TestCenter、Redmine等传统测试管理工具，虽然测试用例的执行、管理、统计比较方便，但依然存在编写用例效率不高、思路不够发散、在产品快速迭代过程中比较耗时等问题...
- 3、公司自研测试管理工具，这是个不错的选择，但对于大部分小公司、小团队来说，一方面研发维护成本高，另一方面对技术要有一定要求...
- 4、...


基于这些情况，现在越来越多公司选择使用**思维导图**这种高效的生产力工具进行用例设计，特别是敏捷开发团队。

事实上也证明，思维导图其发散性思维、图形化思维的特点，跟测试用例设计时所需的思维非常吻合，所以在实际工作中极大提升了我们测试用例设计的效率，也非常方便测试用例评审。

但是与此同时，使用思维导图进行测试用例设计的过程中也带来不少问题：
- 1、测试用例难以量化管理、执行情况难以统计；
- 2、测试用例执行结果与BUG管理系统难以打通；
- 3、团队成员用思维导图设计用例的风格各异，沟通成本巨大；
- 4、...

综合以上情况，我们可以发现不同的测试用例设计方式，各有各个的优劣。

那么问题来了，我们能不能将它们各自优点合在一起呢？这样不就可以提升我们的效率了！

于是，这时候 **XMind2TestCase** 就应运而生了，该工具基于 Python 实现，通过制定**测试用例通用模板**，
然后使用 **[XMind](https://www.xmind.cn/)** 这款广为流传且开源的思维导图工具进行用例设计。
其中制定**测试用例通用模板**是一个非常核心的步骤（具体请看[使用指南](https://github.com/zhuifengshen/xmind2testcase/blob/master/webtool/static/guide/index.md)），有了通用的测试用例模板，我们就可以在 XMind 文件上解析并提取出测试用例所需的基本信息，
然后合成常见**测试用例管理系统**所需的**用例导入文件**。这样就将 **XMind 设计测试用例的便利**与**常见测试用例系统的高效管理**结合起来了！

当前 **XMind2TestCase** 已实现从 XMind 文件到 TestLink 和 Zentao(禅道) 两大常见用例管理系统的测试用例转换，同时也提供 XMind 文件解析后的两种数据接口
（TestSuites、TestCases两种级别的JSON数据），方便快速与其他测试用例管理系统打通。


### 二、使用示例

#### 1、Web工具示例

![webtool](https://raw.githubusercontent.com/zhuifengshen/xmind2testcase/master/webtool/static/guide/webtool.png)

#### 2、转换后用例预览

![testcase_preview](https://raw.githubusercontent.com/zhuifengshen/xmind2testcase/master/webtool/static/guide/xmind_to_testcase_preview.png)

#### 3、TestLink导入结果示例

![testlink](https://raw.githubusercontent.com/zhuifengshen/xmind2testcase/master/webtool/static/guide/testlink.png)

#### 4、禅道（ZenTao）导入结果示例

![zentao](https://raw.githubusercontent.com/zhuifengshen/xmind2testcase/master/webtool/static/guide/zentao_import_result.png)


### 三、安装方式
```
pip3 install xmind2testcase
```


### 四、版本升级
```
pip3 install -U xmind2testcase
```


### 五、使用方式

#### 1、命令行调用
```
Usage:
 xmind2testcase [path_to_xmind_file] [-csv] [-xml] [-json]

Example:
 xmind2testcase /path/to/testcase.xmind        => output testcase.csv、testcase.xml、testcase.json
 xmind2testcase /path/to/testcase.xmind -csv   => output testcase.csv
 xmind2testcase /path/to/testcase.xmind -xml   => output testcase.xml
 xmind2testcase /path/to/testcase.xmind -json  => output testcase.json
```

#### 2、使用Web界面

![web_tool_cli](https://raw.githubusercontent.com/zhuifengshen/xmind2testcase/master/webtool/static/guide/webtool_cli.png)

```
Usage:
 xmind2testcase [webtool] [port_num]

Example:
 xmind2testcase webtool        => launch the web testcase convertion tool locally -> 127.0.0.1:5001
 xmind2testcase webtool 8000   => launch the web testcase convertion tool locally -> 127.0.0.1:8000
```

#### 3、API调用
```
import json
import xmind
from xmind2testcase.zentao import xmind_to_zentao_csv_file
from xmind2testcase.testlink import xmind_to_testlink_xml_file
from xmind2testcase.utils import xmind_testcase_to_json_file
from xmind2testcase.utils import xmind_testsuite_to_json_file
from xmind2testcase.utils import get_xmind_testcase_list
from xmind2testcase.utils import get_xmind_testsuite_list


def main():
    xmind_file = 'docs/xmind_testcase_template.xmind'
    print('Start to convert XMind file: %s' % xmind_file)

    zentao_csv_file = xmind_to_zentao_csv_file(xmind_file)
    print('Convert XMind file to zentao csv file successfully: %s' % zentao_csv_file)

    testlink_xml_file = xmind_to_testlink_xml_file(xmind_file)
    print('Convert XMind file to testlink xml file successfully: %s' % testlink_xml_file)

    testsuite_json_file = xmind_testsuite_to_json_file(xmind_file)
    print('Convert XMind file to testsuite json file successfully: %s' % test
