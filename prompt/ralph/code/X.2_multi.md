```shell
# 阶段 1：核心数据模型
/ralph-loop:ralph-loop "Phase 1: Build core data models and database schema.
Output <promise>PHASE1_DONE</promise>" --max-iterations 20

# 阶段 2：API 层（基于阶段 1 的成果）
/ralph-loop:ralph-loop "Phase 2: Build API endpoints for existing models.
Output <promise>PHASE2_DONE</promise>" --max-iterations 25

# 阶段 3：前端 UI
/ralph-loop:ralph-loop "Phase 3: Build UI components.
Output <promise>PHASE3_DONE</promise>" --max-iterations 30
```

