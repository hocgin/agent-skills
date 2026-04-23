```shell
/ralph-loop:ralph-loop "Fix bug: 令牌过期后，用户无法重置密码.

Steps:
1. 重现缺陷
2. 找出根本原因
3. 实施修复
4. 编写回归测试
5. 验证修复是否有效
6. 检查是否引入了新的问题

After 15 iterations if not fixed:
- 记录阻塞问题
- 列出已尝试的方法
- 提出替代方案

Output <promise>FIXED</promise> when resolved." --max-iterations 20 --completion-promise "FIXED"
```