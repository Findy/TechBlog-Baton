// リサイズ処理のための変数
let isResizing = false;

const dragbar = document.getElementById('dragbar');
const sidebar = document.getElementById('sidebar');
const mainContent = document.getElementById('main-content');

// マウスダウンイベント
dragbar.addEventListener('mousedown', function(e) {
  isResizing = true;
});

// マウスムーブイベント
document.addEventListener('mousemove', function(e) {
  if (isResizing) {
    const offsetRight = document.body.clientWidth - (e.clientX);
    const minWidth = 150; // 最小幅
    const maxWidth = 500; // 最大幅
    let newWidth = e.clientX;

    if (newWidth < minWidth) {
      newWidth = minWidth;
    } else if (newWidth > maxWidth) {
      newWidth = maxWidth;
    }

    sidebar.style.width = newWidth + 'px';
  }
});

// マウスアップイベント
document.addEventListener('mouseup', function(e) {
  if (isResizing) {
    isResizing = false;
  }
});
