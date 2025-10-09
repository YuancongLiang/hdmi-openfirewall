
# 项目名称
[![Build Release](https://github.com/YuancongLiang/hdmi-openfirewall/actions/workflows/build.yml/badge.svg)](https://github.com/YuancongLiang/hdmi-openfirewall/actions)

这是一个 Python 应用程序，用于实验室防火墙自动放行

## 🚀 快速开始

### 下载安装

从 [Releases](https://github.com/yourusername/your-repo/releases) 页面下载适用于您操作系统的版本：

- **Windows**: 下载 `*.exe` 文件
- **macOS**: 下载可执行文件

### 配置文件

在程序目录下必须包含一个名为 `ip.json` 的配置文件，格式如下：

```json
{
    "ip": "xx.xx.xx.xx",
    "name": "dyq",
    "source_group_id": "xxxxxxxx",
    "access_key_id": "xxxxxxx",
    "access_key_secret": "xxxxx",
    "role_arn": "xxxxx"
}
```

**配置项说明：**
- `ip`: 需要放行的IP地址
- `name`: 用户姓名
- `source_group_id`: 安全组id
- `access_key_id`: 访问密钥ID
- `access_key_secret`: 访问密钥Secret
- `role_arn` : arm角色id

> ⚠️ **安全提醒**：除ip以外的配置项请通过微信群询问师兄师姐。

### 使用方法
Windows:
1. 将下载的可执行文件放在一个空目录中
2. 在同一目录下创建 `ip.json` 配置文件
3. 双击运行程序

macOS:
1. 打开终端 (Terminal)
2. 切换到程序所在目录
3. 在同一目录下创建 `ip.json` 配置文件
4. 运行命令：
   ```bash
   ./openfirewall
   ```

## 🛠️ 开发者指南

### 本地开发

```bash
# 克隆项目
git clone https://github.com/YuancongLiang/hdmi-openfirewall.git
cd hdmi-openfirewall

# 安装依赖
pip install -r requirements.txt

# 运行程序
python openfirewall.py
```

### 构建可执行文件

```bash
# 安装 PyInstaller
pip install pyinstaller

# 构建单文件可执行程序
pyinstaller --onefile openfirewall.py
```


## 📝 注意事项

- 程序运行时需要在同一目录下找到 `ip.json` 配置文件
- 确保配置文件格式正确，否则程序可能无法正常启动

## 🐛 问题反馈

如果遇到任何问题，请 [创建 Issue](https://github.com/YuancongLiang/hdmi-openfirewall) 或联系开发者。

