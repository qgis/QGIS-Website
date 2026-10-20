---
HasBanner: false
Reviewed: 1 June 2024
Reviewer: Tim Sutton
draft: false
sidebar: true
title: ユーザーグループ
type: page

---
{{<content-start >}}
# ユーザーグループ
Local user groups bring QGIS users together in their own country and language. They run meetings, share know how and help shape QGIS. This page explains how a group works and how to start one.

{{<rich-box-start layoutClass="has-right rounded" >}}

{{<rich-content-start themeClass="coloring-1" >}}
## Find a group near you
Search the groups by name, country or continent. Switch between cards and a sortable table.

{{<button class="is-success" link="/community/groups/list/" text="Browse the list" >}}

{{<rich-content-end >}}

{{<rich-right-start >}}

{{<user-groups-stats "groups" "/community/groups/list/" >}}

{{<rich-right-end >}}

{{<rich-box-end >}}

{{<rich-box-start layoutClass="has-right rounded" >}}

{{<rich-content-start themeClass="coloring-1" >}}
## See the groups on a map
Every highlighted country has a local group. Select a logo to meet the group.

{{<button class="is-success" link="/community/groups/map/" text="Open the map" >}}

{{<rich-content-end >}}

{{<rich-right-start >}}

{{<user-groups-stats "countries" "/community/groups/map/" >}}

{{<rich-right-end >}}

{{<rich-box-end >}}
## ユーザグループの目的
* ユーザー会議の企画
* 地域・国レベルの標準規格や要件を重視した開発の調整・取りまとめ
* QGISの情報普及活動：ミーティングの開催、GIS専門誌への寄稿、ソーシャルメディアでの情報発信、GISフォーラムへの投稿など
* 地域におけるQGISの使い方のケーススタディの収集
* スポンサー活動地域のユーザーグループは、地域に応じた適切な年会費を徴収することが奨励されています。集まった資金は、関連機能の開発費用、バグ修正のサポート、または国際QGISプロジェクトへの寄付に充てることができます。
* 利益団体の設立、例えば測量、都市計画、サーバー/ Webクライアントなど
* アプリケーションモジュールの初期化/調整。測量、都市計画、サーバー/ Webクライアントなど
* [QGIS投票メンバー]({{< ref "/community/organisation#voting-members" >}})として活動する代表者を選出すること

## 一般的な想定および推奨事項
* 地域のユーザーグループは、特定のベンダーや企業に依存しない中立性を維持することが求められます
* 地域運営委員会の民主的な組織体制の確立、投票および重要な意思決定の実施
* 透明性の維持、特に会員費の収支と使途の明確化
* 地域の活動について、国際プロジェクトへの随時の報告

## 組織
国によっては、協会や非営利組織などの小規模な法的組織を設立することも可能です。現地の法律に応じて、少なくとも年1回の総会開催、年次報告書の公表、財務報告書の会員への開示が求められる場合があります。さらに、定款の策定が必要となる場合もあります。

一例として、スイスのQGISユーザグループの規約：
* ドイツ語（正本）: [https://www.qgis.ch/assets/pdf/StatutenderQGISAnwendergruppeSchweiz.pdf](https://www.qgis.ch/assets/pdf/StatutenderQGISAnwendergruppeSchweiz.pdf)
* フランス語（翻訳）: [https://www.qgis.ch/assets/pdf/StatutsdugroupedutilisateursQGISSuisse.pdf](https://www.qgis.ch/assets/pdf/StatutsdugroupedutilisateursQGISSuisse.pdf)

メンバー申請フォーム:
* ドイツ語: [https://www.qgis.ch/assets/pdf/QGIS%20Usergruppe%20Beitrittserklaerung.pdf](https://www.qgis.ch/assets/pdf/QGIS%20Usergruppe%20Beitrittserklaerung.pdf)
* フランス語: [https://www.qgis.ch/assets/pdf/QGIS%20groupe%20d%20utilisateurs%20Suisse%20declaration%20d%20adhesion.pdf](https://www.qgis.ch/assets/pdf/QGIS%20groupe%20d%20utilisateurs%20Suisse%20declaration%20d%20adhesion.pdf)

これらの定款と入会申込書をご参考いただき、地域の実情に合わせて適宜変更してご活用ください。
## ローカルカントリードメインqgis.xx
ユーザーグループは、qgis.ch や qgis.uk といった地域の国ドメインを登録することができます。そのドメインがすでに他の組織、企業、または個人によって使用されている場合は、所有権を地域 QGIS ユーザーグループに移管できるかどうか、交渉してください。QGIS 国際プロジェクトは [QGIS を商標として登録](../organisation/guidelines) しており、このことが交渉の際に役立つはずです。
## ウェブサイト
地域ユーザーグループのウェブサイトは、グループの情報や運営に関する資料の公開に活用してください。ユーザーミーティング、ケーススタディ、共有資料、フォーラムなどがその例として挙げられます。公開資料はログインなしでアクセスできるようにし、FacebookやGoogle+などのソーシャルメディアへの加入を条件としないでください。ソーシャルメディアの活用は推奨されますが、情報発信の唯一のチャンネルとしては使用しないでください。QGISユーザーグループのウェブサイトではRSSフィードの提供が推奨されます。

地域ユーザーグループの運営がうまくいくことを願っています！QGISコミュニティリストにご登録いただき、進捗状況をご報告いただくことで、国際QGISチームへのご連絡をお願いします。地域ユーザーグループの設立・維持に関するご質問は、どうぞお気軽にお尋ねください。
## 導入セット
### QGIS.org サブドメインホスティング
ユーザーグループは、公式の QGIS.org ブランディングを使用し、ユーザーグループのウェブサイトを QGIS.org のサブドメイン（例：`sweden.qgis.org`）でホストすることを推奨しています。[https://github.com/qgis/QGIS-User-Group-Website](https://github.com/qgis/QGIS-User-Group-Website) で提供されているテンプレートリポジトリをご利用いただけます。この方法により、QGISのメインウェブサイトとのデザインの一貫性が確保されます。リポジトリ内に記載されているセットアップ手順を注意深く読み、それに従ってください。
### QGISニュースフィードの投稿アクセス権
地域のユーザーグループは、 [QGISニュースフィードシステム](https://feed.qgis.org) へのアクセスを申請できます。このシステムでは、イベント・クラウドファンディングキャンペーン・ミートアップ・お知らせなどのニュースを投稿でき、モデレーターの承認を経てQGISニュースセクションに掲載されます。グループの活動をグローバルなQGISコミュニティと共有する絶好の手段です。
### ローカルコミュニティのドメイン qgis.xx 用のテンプレート
QGIS.org のサブドメインホスティングを利用したくない場合は、[https://github.com/qgis/qgis-template.github.io](https://github.com/qgis/qgis-template.github.io) で提供されているテンプレートを使用してウェブサイトをデザインするか、最初から独自に作成することができます。

{{<content-end >}}
