# coding utf-8
import unittest
from common import HTMLTestRunner_yo
# 定位用例位置
casePath = "/Users/l1099182107qq.com/PycharmProjects/fengxiao/case"
# 加载用例
discover =unittest.defaultTestLoader.discover(casePath,"test*.py")


# runner = unittest.TextTestRunner()
# runner.run(discover)
# 定位报告路径
reportPath = "/Users/l1099182107qq.com/PycharmProjects/fengxiao/report/"+"result.html"
fp = open(reportPath,"wb")

runner = HTMLTestRunner_yo.HTMLTestRunner(fp,verbosity = 2,title = "报告",description = "报告描述")
runner.run(discover)
fp.close()