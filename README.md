# NCTU-MCP-SummerCamp

## 課程目的

一個針對沒有任何資訊背景的 Gemini CLI + MCP 教學課程。 本課程講授於 2025 臺中教育大學的高中生暑期營隊

## 簡報連結

[課程簡報](https://docs.google.com/presentation/d/1kSk76oPDqJ85kIR1wgpE-4qRHHKkrOVKJFqDKCh9I04/edit?usp=sharing)

## 課程簡介

在本課程中，你會學到
- LLM 的基本介紹以及 Gemini CLI 的使用方法
  - LLM 的原理
  - 使用 Gemini CLI 寫程式
- MCP Server, AI agent, Prompt 的初步認識
  - user prompt, system prompt
  - 透過 system prompt 進行角色扮演
  - 了解 MCP Server 與 AI agent 和 LLM 的關係
- MCP Server 的搭建與安裝
  - 使用 python 建置一個 MCP Server (Fastmcp)
  - 使用 mcp inspector 測試 MCP Server
  - 新增設定讓 Gemini CLI 可以使用 MCP Server 
- 加入其他人寫的 MCP 到 Gemini CLI
  - 如何查看官方說明
  - 根據官方指示進行安裝
 
## 事前安裝環境
> [!NOTE] 
> 課程簡報包含安裝教學以及所需指令

- nodejs
- gemini cli (透過 nodejs 安裝)
- mcp inspector (透過 nodejs 安裝)
- uv
- git
- python (建議 3.11 以上)

## 專案檔案說明

> [!NOTE] 
> .bat 檔案只需滑鼠點擊兩下即可執行

``` 
NTCU-MCP-SummerCamp:.
|   install-pokemon-mcp.bat : 安裝 pokemon mcp server 的自動化腳本
|   setup-env.bat : 初始化環境及安裝所需套件自動化腳本
|   test-pokemon-mcp.bat : 測試 pokemon mcp server 自動化腳本
|
+---.gemini
|       GEMINI.md : gemini 的 system prompt 設定檔案 (本地設定檔)
|       settings.json : gemini cli 的 mcp server 設定檔案 (本地設定檔)
|
+---gemini_setting_example : 範例設定檔，可以直接複製內容到以上檔案
|       patrick.md : 派大星的 system prompt 範例
|       settings.json : gemini cli 的設定檔案範例
|       shiroko.md : 砂狼白子的 system prompt 範例
|
\---snake-game : 使用 Gemini cli 撰寫網頁貪吃蛇遊戲範例
        index.html
        script.js
        style.css
```


## 本次課程使用到的 MCP Server:

- pokemon example MCP server is from [@Sachin-crypto/Pokemon-MCP-Server](https://github.com/Sachin-crypto/Pokemon-MCP-Server) github repo
- OP.GG example MCP server is from [opgginc@OP.GG MCP Server](https://github.com/opgginc/opgg-mcp) github repo
- Anilist example MCP server is from [yuna0x0@anilist-mcp](https://github.com/yuna0x0/anilist-mcp) github repo
- Minecraft example MCP server is from [yuniko@minecraft-mcp-server](https://github.com/yuniko-software/minecraft-mcp-server) github repo

