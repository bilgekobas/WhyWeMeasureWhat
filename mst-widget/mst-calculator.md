```{raw} html
<link rel="stylesheet" href="../../mst-widget/mst-widget.css?v=final">

<div class="mst-widget">
  <div class="mst-top">
    <div class="mst-control">
      <label>Number of sites</label>
      <select data-mst-n></select>
    </div>
    <div class="mst-control">
      <label>Formula</label>
      <select data-mst-formula></select>
    </div>
    <div class="mst-result-wrap">
      <label class="mst-result-label">MST</label>
      <div class="mst-result"><b data-mst-result>—</b></div>
    </div>
  </div>

  <div class="mst-main">
    <div class="mst-figure">
      <img src="../../mst-widget/man_silhouette.svg" alt="body silhouette for skin temperature measurement sites">
      <div data-mst-badges></div>
    </div>

    <aside class="mst-sites-panel">
      <h4>Body-site values</h4>
      <p class="mst-site-note">All A–U sites are listed. Sites not used by the selected formula are locked.</p>
      <div class="mst-sliders" data-mst-sliders></div>
    </aside>
  </div>

  <div class="mst-equation"><code data-mst-text></code></div>
</div>

<script src="../../mst-widget/mst-widget.js?v=final"></script>
```
