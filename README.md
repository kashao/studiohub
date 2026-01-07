# studiohub

簡易的 Django 專案骨架，提供最基本的設定與 app 分類，方便你自行擴充。

## 目錄結構

```
studiohub/
  manage.py
  config/
    settings/
      __init__.py
      base.py
      development.py
      production.py
    urls.py
    asgi.py
    wsgi.py
  templates/
    base.html
  apps/
    files/
      templates/
        files/
    charts/
      templates/
        charts/
    chat/
      templates/
        chat/
  media/
  static/
```

## 檔案功能總覽

### 專案入口與設定
- `studiohub/manage.py`：Django 管理指令入口（`main()` 會呼叫 `execute_from_command_line`）。
- `studiohub/config/settings/base.py`：基礎設定（資料庫、靜態檔、Media、已註冊 apps）。
- `studiohub/config/settings/development.py`：開發環境設定（DEBUG=True，可從環境變數讀取 SECRET_KEY）。
- `studiohub/config/settings/production.py`：正式環境設定（DEBUG=False，ALLOWED_HOSTS 由環境變數提供）。
- `studiohub/config/urls.py`：根路由總表（包含 files/charts/chat，開發模式提供 media 服務）。
- `studiohub/config/asgi.py`：ASGI 入口（部署用）。
- `studiohub/config/wsgi.py`：WSGI 入口（部署用）。

### Apps（功能模組）
- `studiohub/apps/files/`：上傳 txt 檔案 + 列表顯示
  - `models.py`：`UploadedFile` model（檔案路徑與上傳時間）。
  - `forms.py`：`UploadedFileForm`（限制僅允許 `.txt`）。
  - `views.py`：`index()` 處理上傳與列表渲染。
  - `urls.py`：`files/` 的路由入口。
  - `migrations/`：資料庫 schema 變更記錄。
- `studiohub/apps/chat/`：聊天頁面 + 後端文字清洗
  - `views.py`：`clean_message()` 清洗文字，`process_message()` 回傳 JSON，`index()` 渲染頁面。
  - `urls.py`：`chat/` 與 `chat/message/` 路由。
- `studiohub/apps/charts/`：Highcharts 範例頁面
  - `views.py`：`index()` 渲染圖表頁。
  - `urls.py`：`charts/` 路由。

### Templates（HTML）
- `studiohub/templates/base.html`：全站基底模板。
- `studiohub/apps/*/templates/**`：各 app 的畫面模板（files/chat/charts）。

## Python 檔案內主要函式說明

### `studiohub/manage.py`
- `main()`：設定 `DJANGO_SETTINGS_MODULE` 並交給 Django 執行管理指令。

### `studiohub/apps/files/views.py`
- `index(request)`：處理檔案上傳（POST）、驗證表單與呈現已上傳檔案清單。

### `studiohub/apps/files/forms.py`
- `UploadedFileForm.__init__()`：替檔案欄位加上 `form-control` 的樣式。
- `UploadedFileForm.clean_file()`：檢查副檔名，只允許 `.txt`。

### `studiohub/apps/files/models.py`
- `UploadedFile.__str__()`：回傳檔案名稱（便於 Django admin 或除錯顯示）。

### `studiohub/apps/chat/views.py`
- `clean_message(message)`：移除標點符號並 trim 空白。
- `index(request)`：渲染聊天頁面。
- `process_message(request)`：接收前端文字、清洗後回傳 JSON。

### `studiohub/apps/charts/views.py`
- `index(request)`：渲染圖表頁面。

## 啟動前準備與指令

```bash
cd studiohub
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Migration 相關

```bash
python manage.py makemigrations
python manage.py migrate
```

## 啟動方式

```bash
python manage.py runserver
```

如需指定環境設定：

```bash
export DJANGO_SETTINGS_MODULE=config.settings.development
python manage.py runserver
```

或是：

```bash
export DJANGO_SETTINGS_MODULE=config.settings.production
python manage.py runserver
```

## 範例頁面

- `http://127.0.0.1:8000/files/`：檔案管理模板
- `http://127.0.0.1:8000/charts/`：Highcharts 圖表模板
- `http://127.0.0.1:8000/chat/`：聊天介面模板

> 目前模板使用 CDN 載入 Bootstrap 與 Highcharts，可依需求改成本地靜態檔案。
