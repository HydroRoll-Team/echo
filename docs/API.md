---
title: API Reference
---

## ES 1.0

### API

#### 1. `get_version`

| Method | field | type | notes |
| :-: | :-: | :--: | :----: |
| GET | 无 | | |

| Output | field | type | notes |
| :-: | :-: | :--: | :----: |
|     | ESV  | list | 符合语义化版本2.0.0规范的数组[^1] |
[^1]: https://github.com/HydroRoll-Team/echo/blob/main/docs/index.md#版本

示例:

```json
{
  "ESV": [1, 0, 0]
}
```
