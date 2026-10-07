# 左叶 · AI 学习手册

面向入门学习者的 AI 科普与创作课程网站，包含五个模块、28 篇课程、280 张图片和 8 段视频案例。

## 网站目录

所有网站文件保存在 `docs/`。这是可直接发布的静态网站，不依赖原电脑、ChatGPT 登录、后端服务或额外构建步骤。

- `docs/index.html`：课程目录。
- `docs/lessons/`：28 篇独立课程页面。
- `docs/assets/`：课程封面、正文图片和视频。
- `docs/styles.css`、`docs/app.js`：页面样式与交互。
- `scripts/validate_site.py`：检查页面链接、资源和章节锚点。

## GitHub Pages 发布

在仓库的 **Settings → Pages** 中选择：

1. **Source**：Deploy from a branch。
2. **Branch**：`main`。
3. **Folder**：`/docs`。

保存后，GitHub 会自动发布网站。后续向 `main` 推送 `docs/` 中的修改会自动更新网站。`docs/.nojekyll` 让 GitHub 直接发布现成的网页。

页面使用相对链接，兼容 `https://用户名.github.io/仓库名/` 和自定义域名。自定义域名应先在 **Settings → Pages → Custom domain** 中配置，再按 GitHub 提供的要求修改域名 DNS。

## 本地预览与检查

在仓库目录运行：

```sh
python3 scripts/validate_site.py
python3 -m http.server 4173 --directory docs
```

然后打开 `http://localhost:4173/`。

## 更新课程

直接编辑 `docs/lessons/课号/index.html` 中的内容，目录卡片在 `docs/index.html`。新增图片或视频时放入 `docs/assets/`，使用相对路径引用。提交前运行链接检查，提交并推送后由 GitHub Pages 自动发布。

此仓库收录完整网页及网页所需媒体；蓝图 Markdown、原始高清素材和 PPT 制作文件需另行保存。网页图片与视频经过格式转换和压缩，原始素材不会从本站自动恢复。
