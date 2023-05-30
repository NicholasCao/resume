import requests
import json

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 发送请求
response = requests.post('https://api.github.com/markdown', data=json.dumps({
    'text': content,
    'mode': 'markdown'
}))

html = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link type="text/css" rel="stylesheet" href="./github.css" />
  <title>resume</title>
</head>
<body>
  <div class="clearfix container-xl mt-4 px-md-4 px-lg-5 px-3" style="margin-bottom: 20px;">
    <readme-toc data-catalyst="">

      <div id="readme" class="Box md js-code-block-container js-code-nav-container js-tagsearch-file Box--responsive" data-tagsearch-path="README.md" data-tagsearch-lang="Markdown">

        <div class="d-flex js-sticky js-position-sticky top-0 border-top-0 border-bottom p-2 flex-items-center flex-justify-between color-bg-default rounded-top-2">
          <div class="d-flex flex-items-center">
              <details data-target="readme-toc.trigger" data-menu-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;trigger&quot;,&quot;repository_id&quot;:647083461,&quot;originating_url&quot;:&quot;https://github.com/NicholasCao/resume&quot;,&quot;user_id&quot;:32389766}}" data-menu-hydro-click-hmac="0d585701358f763105b4892b6f78e19ea7f09c8dbb45a2091a27fee932b01945" class="dropdown details-reset details-overlay">
  <summary class="btn btn-octicon m-0 mr-2 p-2" aria-haspopup="menu" aria-label="Table of Contents" role="button">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-list-unordered">
    <path d="M5.75 2.5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5Zm0 5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5Zm0 5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5ZM2 14a1 1 0 1 1 0-2 1 1 0 0 1 0 2Zm1-6a1 1 0 1 1-2 0 1 1 0 0 1 2 0ZM2 4a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg>
  </summary>


  <details-menu class="SelectMenu" role="menu" data-focus-trap="suspended"><span class="sentinel" tabindex="0" aria-hidden="true"></span>
    <div class="SelectMenu-modal rounded-3 mt-1" style="max-height:340px;">


      <div class="SelectMenu-list SelectMenu-list--borderless p-2" style="overscroll-behavior: contain;">
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 24px; background-color: var(--color-accent-emphasis);" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:647083461,&quot;originating_url&quot;:&quot;https://github.com/NicholasCao/resume&quot;,&quot;user_id&quot;:32389766}}" data-hydro-click-hmac="74db5d3ea94469fe0ab3213375e3487f17c85c53d2a4a2bcc5ea068371386d75" href="#曹庭锋" aria-current="page">曹庭锋</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 36px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:647083461,&quot;originating_url&quot;:&quot;https://github.com/NicholasCao/resume&quot;,&quot;user_id&quot;:32389766}}" data-hydro-click-hmac="74db5d3ea94469fe0ab3213375e3487f17c85c53d2a4a2bcc5ea068371386d75" href="#教育背景">教育背景</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 36px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:647083461,&quot;originating_url&quot;:&quot;https://github.com/NicholasCao/resume&quot;,&quot;user_id&quot;:32389766}}" data-hydro-click-hmac="74db5d3ea94469fe0ab3213375e3487f17c85c53d2a4a2bcc5ea068371386d75" href="#实习经历">实习经历</a>
          <a role="menuitem" class="filter-item SelectMenu-item ws-normal wb-break-word line-clamp-2 py-1 " style="-webkit-box-orient: vertical; padding-left: 36px;" data-action="click:readme-toc#blur" data-targets="readme-toc.entries" data-hydro-click="{&quot;event_type&quot;:&quot;repository_toc_menu.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;entry&quot;,&quot;repository_id&quot;:647083461,&quot;originating_url&quot;:&quot;https://github.com/NicholasCao/resume&quot;,&quot;user_id&quot;:32389766}}" data-hydro-click-hmac="74db5d3ea94469fe0ab3213375e3487f17c85c53d2a4a2bcc5ea068371386d75" href="#竞赛项目经历">竞赛/项目经历</a>
      </div>
    </div>
  <span class="sentinel" tabindex="0" aria-hidden="true"></span></details-menu>
</details>

            <h2 class="Box-title">
              <a href="#readme" data-view-component="true" class="Link--primary">README.md</a>
            </h2>
          </div>
            <div>
              <a href="/NicholasCao/resume/edit/main/README.md" class="btn btn-octicon float-right p-2" aria-label="Edit this file"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-pencil">
    <path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.253.253 0 0 0-.064.108l-.558 1.953 1.953-.558a.253.253 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"></path>
</svg></a>
            </div>
        </div>

          <div data-target="readme-toc.content" class="Box-body px-5 pb-5">
            <article class="markdown-body entry-content container-lg" itemprop="text">
''' + response.content.decode('utf-8') + '''
            </article>
          </div>
      </div>

  </readme-toc>

  </div>
  </body>
  </html>
'''


with open('resume-new.html', 'w', encoding='utf-8') as f:
    f.write(html)