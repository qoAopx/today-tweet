# 今日は何の日

- 毎日1Tweet今日は何の日を投稿します。
- もともとGCP AppEngineで動かしてたものを移植しました。

## 設定方法

heroku config:set --app "[APPNAME]" CONSUMER_KEY="XXX"
heroku config:set --app "[APPNAME]" CONSUMER_SECRET="XXX"
heroku config:set --app "[APPNAME]" ACCESS_TOKEN_KEY="XXX"
heroku config:set --app "[APPNAME]" ACCESS_TOKEN_SECRET="XXX"

## 参考

<https://qiita.com/RollSystems/items/408cb4267a9a9770dfc9>
