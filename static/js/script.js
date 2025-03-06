const setTheme = (theme) => {
  document.documentElement.className = theme;
  localStorage.setItem('theme', theme);
}

const hasCodeRun = localStorage.getItem('hasCodeRun');

if (!hasCodeRun) {
  const defaultTheme = "{{ config.extra.default_theme }}";
  setTheme(defaultTheme);
  localStorage.setItem('hasCodeRun', 'true');
}

const getTheme = () => {
  const theme = localStorage.getItem('theme');
  if (theme) {
    setTheme(theme);
  }
}

getTheme();

// 检测目录并添加类
document.addEventListener('DOMContentLoaded', () => {
  const tocSidebar = document.querySelector('.toc-sidebar');
  if (tocSidebar) {
    document.body.classList.add('has-toc');
  }
});