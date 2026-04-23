```shell
# 创建独立的工作树
git worktree add ../project-auth -b feature/auth
git worktree add ../project-api -b feature/api

# 终端 1：认证功能
cd ../project-auth
/ralph-loop:ralph-loop "Implement authentication..." --max-iterations 30

# 终端 2：API 功能（同时进行）
cd ../project-api
/ralph-loop:ralph-loop "Build REST API..." --max-iterations 30
```