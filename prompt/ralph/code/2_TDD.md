```shell
/ralph-loop:ralph-loop "使用TDD实现支付功能.

Process:
1. 为下一个需求编写失败的测试用例
2. 实现能通过测试的最小代码量
3. 运行测试
4. 如果失败，修复并重试
5. 必要时重构
6. 对所有需求重复上述步骤

Requirements:
- 信用卡验证
- 支付处理
- 错误处理
- 交易日志记录

Output <promise>DONE</promise> when all tests green." --max-iterations 50 --completion-promise "DONE"
```