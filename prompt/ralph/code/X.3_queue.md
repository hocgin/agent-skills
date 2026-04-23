```shell
cat << 'EOF' > overnight-work.sh
#!/bin/bash

# 任务 1：用户服务
cd /path/to/user-service
claude -p "/ralph-wiggum:ralph-loop 'Implement OAuth...' --max-iterations 50"

# 任务 2：支付服务
cd /path/to/payment-service
claude -p "/ralph-wiggum:ralph-loop 'Fix transaction bugs...' --max-iterations 30"

# 任务 3：文档生成
cd /path/to/docs
claude -p "/ralph-wiggum:ralph-loop 'Generate API docs...' --max-iterations 20"
EOF

chmod +x overnight-work.sh
./overnight-work.sh
```