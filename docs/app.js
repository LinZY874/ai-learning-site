const menu=document.querySelector('.menu-button');
menu?.addEventListener('click',()=>{const open=document.querySelector('.sidebar').classList.toggle('open');menu.setAttribute('aria-expanded',String(open));menu.textContent=open?'收起目录':'课程目录'});
document.querySelectorAll('.module-nav a').forEach(a=>a.addEventListener('click',()=>{document.querySelector('.sidebar').classList.remove('open');menu?.setAttribute('aria-expanded','false');if(menu)menu.textContent='课程目录'}));
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&document.querySelector('.sidebar.open')){document.querySelector('.sidebar').classList.remove('open');menu.setAttribute('aria-expanded','false');menu.textContent='课程目录';menu.focus()}});
const readingBreakpoint=matchMedia('(max-width:1200px)');
function adaptContents(){const toc=document.querySelector('.toc');if(toc)toc.open=!readingBreakpoint.matches}
adaptContents();readingBreakpoint.addEventListener('change',adaptContents);
document.querySelectorAll('pre').forEach(pre=>{const button=document.createElement('button');button.className='copy-button';button.textContent='复制提示词';const code=pre.querySelector('code');button.addEventListener('click',async()=>{try{await navigator.clipboard.writeText(code.textContent);button.textContent='已复制';setTimeout(()=>button.textContent='复制提示词',1800)}catch{button.textContent='请选中文字复制'}});pre.prepend(button)});
const observer=new IntersectionObserver(entries=>{entries.forEach(e=>{if(e.isIntersecting){document.querySelectorAll('.module-nav a').forEach(a=>a.classList.toggle('active',a.hash==='#'+e.target.id))}})},{rootMargin:'-10% 0px -65% 0px'});document.querySelectorAll('.course-section').forEach(s=>observer.observe(s));
