


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>weibo_pic/queue_crawler.py at master · atupal/weibo_pic · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <link rel="logo" type="image/svg" href="https://github-media-downloads.s3.amazonaws.com/github-logo.svg" />
    <meta property="og:image" content="https://github.global.ssl.fastly.net/images/modules/logos_page/Octocat.png">
    <meta name="hostname" content="github-fe136-cp1-prd.iad.github.net">
    <meta name="ruby" content="ruby 1.9.3p194-tcs-github-tcmalloc (e1c0c3f392) [x86_64-linux]">
    <link rel="assets" href="https://github.global.ssl.fastly.net/">
    <link rel="conduit-xhr" href="https://ghconduit.com:25035/">
    <link rel="xhr-socket" href="/_sockets" />
    


    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="B7EE9F0E:6DAA:7F3A077:52B1487C" name="octolytics-dimension-request_id" />
    

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="u8lMJI7b0fjI60kAmcZ7BpTDDrQxoI2bMvR6n4QQnsQ=" name="csrf-token" />

    <link href="https://github.global.ssl.fastly.net/assets/github-fee18e679e1beabffa719d9420fedfa11327aedf.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://github.global.ssl.fastly.net/assets/github2-1d8789e5f8f532553b7cb7377bf3d5b4773ce4bb.css" media="all" rel="stylesheet" type="text/css" />
    

    

      <script src="https://github.global.ssl.fastly.net/assets/frameworks-2e639d0c18c26c873333076fd69f2e4dc8c73424.js" type="text/javascript"></script>
      <script src="https://github.global.ssl.fastly.net/assets/github-213cad5616ea85bf8566fc9f3613c938e305f0b8.js" type="text/javascript"></script>
      
      <meta http-equiv="x-pjax-version" content="047667af48173b310014635358a79b90">

        <link data-pjax-transient rel='permalink' href='/atupal/weibo_pic/blob/7d7f79578ae1de6c0fd7c31c45e01fa77cc804c4/queue_crawler.py'>
  <meta property="og:title" content="weibo_pic"/>
  <meta property="og:type" content="githubog:gitrepository"/>
  <meta property="og:url" content="https://github.com/atupal/weibo_pic"/>
  <meta property="og:image" content="https://github.global.ssl.fastly.net/images/gravatars/gravatar-user-420.png"/>
  <meta property="og:site_name" content="GitHub"/>
  <meta property="og:description" content="weibo_pic - 下载好友列表中的某好友的相册里所有的图片"/>

  <meta name="description" content="weibo_pic - 下载好友列表中的某好友的相册里所有的图片" />

  <meta content="1540389" name="octolytics-dimension-user_id" /><meta content="atupal" name="octolytics-dimension-user_login" /><meta content="10881098" name="octolytics-dimension-repository_id" /><meta content="atupal/weibo_pic" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="10881098" name="octolytics-dimension-repository_network_root_id" /><meta content="atupal/weibo_pic" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/atupal/weibo_pic/commits/master.atom" rel="alternate" title="Recent Commits to weibo_pic:master" type="application/atom+xml" />

  </head>


  <body class="logged_out  env-production linux vis-public page-blob">
    <div class="wrapper">
      
      
      
      


      
      <div class="header header-logged-out">
  <div class="container clearfix">

    <a class="header-logo-wordmark" href="https://github.com/">
      <span class="mega-octicon octicon-logo-github"></span>
    </a>

    <div class="header-actions">
        <a class="button primary" href="/join">Sign up</a>
      <a class="button signin" href="/login?return_to=%2Fatupal%2Fweibo_pic%2Fblob%2Fmaster%2Fqueue_crawler.py">Sign in</a>
    </div>

    <div class="command-bar js-command-bar  in-repository">

      <ul class="top-nav">
          <li class="explore"><a href="/explore">Explore</a></li>
        <li class="features"><a href="/features">Features</a></li>
          <li class="enterprise"><a href="https://enterprise.github.com/">Enterprise</a></li>
          <li class="blog"><a href="/blog">Blog</a></li>
      </ul>
        <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">

<input type="text" data-hotkey=" s" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
    
      data-repo="atupal/weibo_pic"
      data-branch="master"
      data-sha="9818b19a5db1472da142a01f1256ee6d59a7eb5b"
  >

    <input type="hidden" name="nwo" value="atupal/weibo_pic" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item js-this-repository-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item js-all-repositories-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="octicon help tooltipped downwards" title="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

</form>
    </div>

  </div>
</div>


      


          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        

<ul class="pagehead-actions">


  <li>
    <a href="/login?return_to=%2Fatupal%2Fweibo_pic"
    class="minibutton with-count js-toggler-target star-button tooltipped upwards"
    title="You must be signed in to use this feature" rel="nofollow">
    <span class="octicon octicon-star"></span>Star
  </a>

    <a class="social-count js-social-count" href="/atupal/weibo_pic/stargazers">
      4
    </a>

  </li>

    <li>
      <a href="/login?return_to=%2Fatupal%2Fweibo_pic"
        class="minibutton with-count js-toggler-target fork-button tooltipped upwards"
        title="You must be signed in to fork a repository" rel="nofollow">
        <span class="octicon octicon-git-branch"></span>Fork
      </a>
      <a href="/atupal/weibo_pic/network" class="social-count">
        1
      </a>
    </li>
</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="repo-label"><span>public</span></span>
          <span class="mega-octicon octicon-repo"></span>
          <span class="author">
            <a href="/atupal" class="url fn" itemprop="url" rel="author"><span itemprop="title">atupal</span></a>
          </span>
          <span class="repohead-name-divider">/</span>
          <strong><a href="/atupal/weibo_pic" class="js-current-repository js-repo-home-link">weibo_pic</a></strong>

          <span class="page-context-loader">
            <img alt="Octocat-spinner-32" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      

      <div class="repository-with-sidebar repo-container  ">

        <div class="repository-sidebar">
            

<div class="sunken-menu vertical-right repo-nav js-repo-nav js-repository-container-pjax js-octicon-loaders">
  <div class="sunken-menu-contents">
    <ul class="sunken-menu-group">
      <li class="tooltipped leftwards" title="Code">
        <a href="/atupal/weibo_pic" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-gotokey="c" data-pjax="true" data-selected-links="repo_source repo_downloads repo_commits repo_tags repo_branches /atupal/weibo_pic">
          <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

        <li class="tooltipped leftwards" title="Issues">
          <a href="/atupal/weibo_pic/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-gotokey="i" data-selected-links="repo_issues /atupal/weibo_pic/issues">
            <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
            <span class='counter'>0</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>

      <li class="tooltipped leftwards" title="Pull Requests">
        <a href="/atupal/weibo_pic/pulls" aria-label="Pull Requests" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-gotokey="p" data-selected-links="repo_pulls /atupal/weibo_pic/pulls">
            <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
            <span class='counter'>0</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


    </ul>
    <div class="sunken-menu-separator"></div>
    <ul class="sunken-menu-group">

      <li class="tooltipped leftwards" title="Pulse">
        <a href="/atupal/weibo_pic/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="pulse /atupal/weibo_pic/pulse">
          <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped leftwards" title="Graphs">
        <a href="/atupal/weibo_pic/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="repo_graphs repo_contributors /atupal/weibo_pic/graphs">
          <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped leftwards" title="Network">
        <a href="/atupal/weibo_pic/network" aria-label="Network" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-selected-links="repo_network /atupal/weibo_pic/network">
          <span class="octicon octicon-git-branch"></span> <span class="full-word">Network</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
    </ul>


  </div>
</div>

            <div class="only-with-full-nav">
              

  

<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><strong>HTTPS</strong> clone URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/atupal/weibo_pic.git" readonly="readonly">

    <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/atupal/weibo_pic.git" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><strong>Subversion</strong> checkout URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/atupal/weibo_pic" readonly="readonly">

    <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/atupal/weibo_pic" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>


<p class="clone-options">You can clone with
      <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>,
      or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <span class="octicon help tooltipped upwards" title="Get help on which URL is right for you.">
    <a href="https://help.github.com/articles/which-remote-url-should-i-use">
    <span class="octicon octicon-question"></span>
    </a>
  </span>
</p>



              <a href="/atupal/weibo_pic/archive/master.zip"
                 class="minibutton sidebar-button"
                 title="Download this repository as a zip file"
                 rel="nofollow">
                <span class="octicon octicon-cloud-download"></span>
                Download ZIP
              </a>
            </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:8ddd8fec8aef22b2784316cfcba1ea4f -->

<p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

<a href="/atupal/weibo_pic/find/master" data-pjax data-hotkey="t" class="js-show-file-finder" style="display:none">Show File Finder</a>

<div class="file-navigation">
  

<div class="select-menu js-menu-container js-select-menu" >
  <span class="minibutton select-menu-button js-menu-target" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    role="button" aria-label="Switch branches or tags" tabindex="0">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-remove-close js-menu-close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/atupal/weibo_pic/blob/master/queue_crawler.py"
                 data-name="master"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="master">master</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/atupal/weibo_pic" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">weibo_pic</span></a></span></span><span class="separator"> / </span><strong class="final-path">queue_crawler.py</strong> <span class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="queue_crawler.py" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>



  <div class="commit file-history-tease">
    <img class="main-avatar" height="24" src="https://0.gravatar.com/avatar/bf287c6a6972d9d89d0e9c951a6524fb?d=https%3A%2F%2Fidenticons.github.com%2Fe1efb76d1e7e29f02184b764ed45b871.png&amp;r=x&amp;s=140" width="24" />
    <span class="author"><a href="/atupal" rel="author">atupal</a></span>
    <time class="js-relative-date" datetime="2013-11-16T04:49:41-08:00" title="2013-11-16 04:49:41">November 16, 2013</time>
    <div class="commit-title">
        <a href="/atupal/weibo_pic/commit/1b761c2847f1ca59f39a68feb8c730a125070c71" class="message" data-pjax="true" title="update for freshmember of alg who want to learn">update for freshmember of alg who want to learn</a>
    </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>1</strong> contributor</a></p>
      
    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
          <li class="facebox-user-list-item">
            <img height="24" src="https://0.gravatar.com/avatar/bf287c6a6972d9d89d0e9c951a6524fb?d=https%3A%2F%2Fidenticons.github.com%2Fe1efb76d1e7e29f02184b764ed45b871.png&amp;r=x&amp;s=140" width="24" />
            <a href="/atupal">atupal</a>
          </li>
      </ul>
    </div>
  </div>

<div id="files" class="bubble">
  <div class="file">
    <div class="meta">
      <div class="info">
        <span class="icon"><b class="octicon octicon-file-text"></b></span>
        <span class="mode" title="File Mode">file</span>
          <span>88 lines (69 sloc)</span>
        <span>1.933 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
              <a class="minibutton disabled tooltipped leftwards" href="#"
                 title="You must be signed in to make or propose changes">Edit</a>
          <a href="/atupal/weibo_pic/raw/master/queue_crawler.py" class="button minibutton " id="raw-url">Raw</a>
            <a href="/atupal/weibo_pic/blame/master/queue_crawler.py" class="button minibutton ">Blame</a>
          <a href="/atupal/weibo_pic/commits/master/queue_crawler.py" class="button minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->
          <a class="minibutton danger disabled empty-icon tooltipped leftwards" href="#"
             title="You must be signed in and on a branch to make or propose changes">
          Delete
        </a>
      </div><!-- /.actions -->

    </div>
        <div class="blob-wrapper data type-python js-blob-data">
        <table class="file-code file-diff">
          <tr class="file-code-line">
            <td class="blob-line-nums">
              <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>

            </td>
            <td class="blob-line-code">
                    <div class="code-body highlight"><pre><div class='line' id='LC1'><span class="c">#!/usr/bin/env pythhon2</span></div><div class='line' id='LC2'><span class="c"># -*- coding: utf-8 -*-</span></div><div class='line' id='LC3'><br/></div><div class='line' id='LC4'><span class="sd">&#39;&#39;&#39;</span></div><div class='line' id='LC5'><span class="sd">  use       : used for learn， just for freshman of unique alg</span></div><div class='line' id='LC6'><span class="sd">  author    : atupal</span></div><div class='line' id='LC7'><span class="sd">  date      : 16/11/2013</span></div><div class='line' id='LC8'><span class="sd">&#39;&#39;&#39;</span></div><div class='line' id='LC9'><br/></div><div class='line' id='LC10'><span class="kn">from</span> <span class="nn">login_weibo_rsa</span> <span class="kn">import</span> <span class="n">Weibo</span></div><div class='line' id='LC11'><span class="kn">from</span>  <span class="nn">Queue</span> <span class="kn">import</span> <span class="n">Queue</span></div><div class='line' id='LC12'><br/></div><div class='line' id='LC13'><span class="kn">import</span> <span class="nn">unittest</span></div><div class='line' id='LC14'><span class="kn">import</span> <span class="nn">threading</span></div><div class='line' id='LC15'><br/></div><div class='line' id='LC16'><br/></div><div class='line' id='LC17'><span class="c"># used for global session </span></div><div class='line' id='LC18'><span class="n">s</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC19'><span class="c"># production queue</span></div><div class='line' id='LC20'><span class="n">q</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC21'><span class="c"># all photo ids</span></div><div class='line' id='LC22'><span class="n">ids</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC23'><br/></div><div class='line' id='LC24'><span class="c"># the photo&#39;s start url of 语希范&#39;s weibo</span></div><div class='line' id='LC25'><span class="n">start_url</span> <span class="o">=</span> <span class="s">&#39;http://photo.weibo.com/2432143202/talbum/detail/photo_id/3644985982455839&#39;</span></div><div class='line' id='LC26'><br/></div><div class='line' id='LC27'><span class="n">base_url</span> <span class="o">=</span> <span class="s">&#39;http://photo.weibo.com/2432143202/talbum/detail/photo_id/&#39;</span></div><div class='line' id='LC28'><br/></div><div class='line' id='LC29'><span class="kn">import</span> <span class="nn">re</span></div><div class='line' id='LC30'><br/></div><div class='line' id='LC31'><span class="k">def</span> <span class="nf">init</span><span class="p">():</span></div><div class='line' id='LC32'>&nbsp;&nbsp;<span class="n">weibo</span> <span class="o">=</span> <span class="n">Weibo</span><span class="p">(</span><span class="n">debug</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span></div><div class='line' id='LC33'>&nbsp;&nbsp;<span class="k">global</span> <span class="n">s</span><span class="p">,</span><span class="n">q</span></div><div class='line' id='LC34'>&nbsp;&nbsp;<span class="n">s</span> <span class="o">=</span> <span class="n">weibo</span><span class="o">.</span><span class="n">session</span></div><div class='line' id='LC35'>&nbsp;&nbsp;<span class="n">q</span> <span class="o">=</span> <span class="n">Queue</span><span class="p">()</span></div><div class='line' id='LC36'>&nbsp;&nbsp;<span class="n">content</span> <span class="o">=</span> <span class="n">s</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">start_url</span><span class="p">)</span><span class="o">.</span><span class="n">content</span></div><div class='line' id='LC37'>&nbsp;&nbsp;<span class="n">t</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">findall</span><span class="p">(</span><span class="s">r&#39;album_photo_ids:.{1,9}(\[[0-9, ]+\]),&#39;</span><span class="p">,</span> <span class="n">content</span><span class="p">,</span> <span class="n">re</span><span class="o">.</span><span class="n">DOTALL</span><span class="p">)</span></div><div class='line' id='LC38'>&nbsp;&nbsp;<span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">t</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC39'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&#39;can not get the ids!&#39;</span></div><div class='line' id='LC40'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">Exception</span></div><div class='line' id='LC41'>&nbsp;&nbsp;<span class="k">exec</span><span class="p">(</span> <span class="s">&#39;_ids=</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">t</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span><span class="o">.</span><span class="n">strip</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span> <span class="p">)</span></div><div class='line' id='LC42'>&nbsp;&nbsp;<span class="k">assert</span><span class="p">(</span> <span class="nb">len</span><span class="p">(</span><span class="n">_ids</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="p">)</span></div><div class='line' id='LC43'>&nbsp;&nbsp;<span class="k">global</span> <span class="n">ids</span></div><div class='line' id='LC44'>&nbsp;&nbsp;<span class="n">ids</span> <span class="o">=</span> <span class="n">_ids</span></div><div class='line' id='LC45'>&nbsp;&nbsp;</div><div class='line' id='LC46'><br/></div><div class='line' id='LC47'><span class="k">def</span> <span class="nf">get_url</span><span class="p">(</span><span class="nb">id</span><span class="p">):</span></div><div class='line' id='LC48'>&nbsp;&nbsp;<span class="n">url</span> <span class="o">=</span> <span class="n">base_url</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="nb">id</span><span class="p">)</span></div><div class='line' id='LC49'>&nbsp;&nbsp;<span class="n">content</span> <span class="o">=</span> <span class="n">s</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">url</span><span class="p">)</span><span class="o">.</span><span class="n">content</span></div><div class='line' id='LC50'>&nbsp;&nbsp;<span class="n">t</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">findall</span><span class="p">(</span><span class="s">r&#39;photo_info:.{1,9}([{].+[}])[ }]{1,9};.{1,9}var ids&#39;</span><span class="p">,</span> <span class="n">content</span><span class="p">,</span> <span class="n">re</span><span class="o">.</span><span class="n">DOTALL</span><span class="p">)</span></div><div class='line' id='LC51'>&nbsp;&nbsp;<span class="k">assert</span><span class="p">(</span> <span class="nb">len</span><span class="p">(</span><span class="n">t</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="p">)</span></div><div class='line' id='LC52'>&nbsp;&nbsp;<span class="k">exec</span><span class="p">(</span><span class="s">&#39;photoInfo=</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">t</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span><span class="o">.</span><span class="n">strip</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39;false&#39;</span><span class="p">,</span> <span class="s">&#39;False&#39;</span><span class="p">))</span></div><div class='line' id='LC53'><br/></div><div class='line' id='LC54'>&nbsp;&nbsp;<span class="n">t</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">findall</span><span class="p">(</span><span class="s">r&#39;&#39;&#39;\(&#39;[&lt;]img id=&quot;bigImg&quot; src=&quot;&#39;\+(.+)\+&#39;&quot;[&gt;]&#39;\);&#39;&#39;&#39;</span><span class="p">,</span> <span class="n">content</span><span class="p">,</span> <span class="n">re</span><span class="o">.</span><span class="n">DOTALL</span><span class="p">)</span></div><div class='line' id='LC55'>&nbsp;&nbsp;<span class="k">assert</span><span class="p">(</span> <span class="nb">len</span><span class="p">(</span><span class="n">t</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="p">)</span></div><div class='line' id='LC56'>&nbsp;&nbsp;<span class="k">exec</span><span class="p">(</span> <span class="s">&#39;purl=</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">t</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="p">)</span></div><div class='line' id='LC57'>&nbsp;&nbsp;<span class="k">return</span> <span class="n">purl</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\\</span><span class="s">&#39;</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">)</span></div><div class='line' id='LC58'><br/></div><div class='line' id='LC59'><br/></div><div class='line' id='LC60'><span class="sd">&#39;&#39;&#39;嗯哼，没想到weibo 的图片这么容易爬，就先不用 这种暴力的方法了，下次有机会再演示吧</span></div><div class='line' id='LC61'><span class="sd">class Producer(threading.Thread):</span></div><div class='line' id='LC62'><span class="sd">  def __init__(self, url):</span></div><div class='line' id='LC63'><span class="sd">    self.s = Weibo()</span></div><div class='line' id='LC64'><br/></div><div class='line' id='LC65'><span class="sd">  def run():</span></div><div class='line' id='LC66'><span class="sd">    try:</span></div><div class='line' id='LC67'><span class="sd">      url = q.get()</span></div><div class='line' id='LC68'><span class="sd">      content = self.s.get(url)</span></div><div class='line' id='LC69'><span class="sd">    except:</span></div><div class='line' id='LC70'><span class="sd">      pass</span></div><div class='line' id='LC71'><span class="sd">&#39;&#39;&#39;</span></div><div class='line' id='LC72'><br/></div><div class='line' id='LC73'><span class="k">def</span> <span class="nf">main</span><span class="p">():</span></div><div class='line' id='LC74'>&nbsp;&nbsp;<span class="n">init</span><span class="p">()</span></div><div class='line' id='LC75'>&nbsp;&nbsp;<span class="k">for</span> <span class="nb">id</span> <span class="ow">in</span> <span class="n">ids</span><span class="p">:</span></div><div class='line' id='LC76'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC77'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="n">get_url</span><span class="p">(</span><span class="nb">id</span><span class="p">)</span></div><div class='line' id='LC78'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span><span class="p">:</span></div><div class='line' id='LC79'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC80'><br/></div><div class='line' id='LC81'><br/></div><div class='line' id='LC82'><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span></div><div class='line' id='LC83'>&nbsp;&nbsp;<span class="kn">import</span> <span class="nn">sys</span></div><div class='line' id='LC84'>&nbsp;&nbsp;<span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span> <span class="ow">and</span> <span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">==</span> <span class="s">&#39;test&#39;</span><span class="p">:</span></div><div class='line' id='LC85'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">unittest</span><span class="o">.</span><span class="n">main</span><span class="p">()</span></div><div class='line' id='LC86'>&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC87'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="n">main</span><span class="p">())</span></div></pre></div>
            </td>
          </tr>
        </table>
  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="http://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/">
      <span class="mega-octicon octicon-mark-github"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2013 <span title="0.02158s from github-fe136-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
          <div class="suggester-container">
              <div class="suggester fullscreen-suggester js-navigation-container" id="fullscreen_suggester"
                 data-url="/atupal/weibo_pic/suggestions/commit">
              </div>
          </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped leftwards" title="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped leftwards"
      title="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-remove-close close ajax-error-dismiss"></a>
      Something went wrong with that request. Please try again.
    </div>

  </body>
</html>

