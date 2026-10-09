import base64, html, json, io, csv, urllib.request
from pathlib import Path
import streamlit as st
import content, engine, accounts
st.set_page_config(page_title='PAK-AI Station',page_icon='🏔️',layout='wide',initial_sidebar_state='collapsed')
S=st.session_state
for k,v in {'page':'landing','lang':'en','dark':True,'size':'Medium','uid':None}.items():S.setdefault(k,v)
T=content.TEXT[S.lang]
IMAGES=Path(__file__).with_name('images')
LABEL={
'en':{'login':'Login','register':'Register','logout':'Logout','email':'Email','password':'Password','credits':'Credits','buy':'Buy credits','back':'Back to modules','home':'Home','theme':'Appearance','language':'Language','size':'Text size','account':'Account','choose':'Explore our services','welcome':'Explore Gilgit-Baltistan with AI','try':'Explore PAK-AI Station','sample':'Information is educational unless verified by an official source.'},
'ur':{'login':'لاگ اِن','register':'رجسٹر','logout':'لاگ آؤٹ','email':'ای میل','password':'پاس ورڈ','credits':'کریڈٹس','buy':'کریڈٹس خریدیں','back':'موضوعات پر واپس','home':'ہوم','theme':'ظاہری شکل','language':'زبان','size':'حروف کا سائز','account':'اکاؤنٹ','choose':'ہماری خدمات','welcome':'گلگت بلتستان کو اے آئی کے ساتھ دریافت کریں','try':'پاک اے آئی اسٹیشن کھولیں','sample':'سرکاری تصدیق کے بغیر معلومات صرف تعلیمی مقاصد کے لیے ہیں۔'}}
L=LABEL[S.lang]
def photo(mid):
 for ext in ('jpg','jpeg','png','webp'):
  f=IMAGES/(mid+'.'+ext)
  if f.exists():
   mime='jpeg' if ext in ('jpg','jpeg') else ext
   return 'data:image/'+mime+';base64,'+base64.b64encode(f.read_bytes()).decode()
 return ''
def esc(x):return html.escape(str(x),quote=True)
def navigate(page):S.page=page
def css():
 dark=S.dark
 bg='#071a2b' if dark else '#f3f7fc';fg='#f5f8ff' if dark else '#102235';panel='#17283b' if dark else '#ffffff';muted='#bbcadb' if dark else '#52677c';line='#38516a' if dark else '#d5e0e9'
 sizes={'Small':'.88','Medium':'1','Large':'1.16'}
 st.markdown(f'''<style>
 :root{{--fontscale:{sizes[S.size]};}}
 .stApp{{background:{bg};color:{fg};}}
 .block-container{{max-width:1370px;padding-top:1rem;}}
 header[data-testid="stHeader"]{{background:transparent;}}
 [data-testid="stSidebar"]{{background:{panel};}}
 h1,h2,h3,p,label,div[data-testid="stMarkdownContainer"]{{color:{fg};}}
 .stApp p{{font-size:calc(1rem * var(--fontscale));}}
 .pak-brand{{font-weight:900;font-size:1.55rem;letter-spacing:-.035em;color:{fg};}}
 .pak-caption{{color:{muted};font-size:.88rem;}}
 .pak-card{{background:{panel};border:1px solid {line};border-radius:18px;overflow:hidden;box-shadow:0 8px 20px #0002;}}
 .pak-photo{{width:100%;aspect-ratio:16/10;object-fit:cover;display:block;}}
 .pak-fallback{{aspect-ratio:16/10;display:flex;align-items:center;justify-content:center;font-size:4.2rem;}}
 .pak-text{{padding:17px 18px;min-height:145px;}}
 .pak-title{{font-size:calc(1.08rem * var(--fontscale));font-weight:800;line-height:1.3;color:{fg};min-height:2.6em;}}
 .pak-tip{{font-size:calc(.82rem * var(--fontscale));color:{muted};line-height:1.45;margin-top:.45rem;min-height:3.2em;}}
 .pak-hero{{min-height:520px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;background-position:center;background-size:cover;border-radius:22px;padding:4rem 1.5rem;box-shadow:0 15px 50px #0005;}}
 .pak-hero h1{{font-size:clamp(2.4rem,5.5vw,4.9rem);color:white!important;text-shadow:0 3px 25px #0009;max-width:950px;}}
 .pak-hero p{{font-size:1.15rem;color:#f1f5f9!important;text-shadow:0 2px 8px #000;max-width:680px;}}
 .stButton button{{border-radius:11px;}}
 [data-testid="stHorizontalBlock"]{{align-items:stretch;}}
 </style>''',unsafe_allow_html=True)
def header():
 a,b,c,d,e=st.columns([4.3,1.5,1.5,1.4,1.7],vertical_alignment='center')
 a.markdown('<div class="pak-brand">🏔️ PAK-AI Station</div>',unsafe_allow_html=True)
 b.selectbox('🌐 '+L['language'],['English','اردو'],index=0 if S.lang=='en' else 1,key='language_control',on_change=lambda:setattr(S,'lang','en' if S.language_control=='English' else 'ur'))
 c.selectbox('◐ '+L['theme'],['Dark','Light'],index=0 if S.dark else 1,key='theme_control',on_change=lambda:setattr(S,'dark',S.theme_control=='Dark'))
 d.selectbox('Aa '+L['size'],['Small','Medium','Large'],index=['Small','Medium','Large'].index(S.size),key='size_control',on_change=lambda:setattr(S,'size',S.size_control))
 if S.uid:
  e.markdown('**💳 '+L['credits']+': '+str(accounts.balance(S.uid))+'**')
  if e.button(L['account'],key='account'):navigate('account');st.rerun()
 else:
  if e.button('👤 '+L['login'],key='login_header'):navigate('account');st.rerun()
def landing():
 uri=photo('welcome');background=f'linear-gradient(90deg,#061626b8,#06162655),url({uri})' if uri else 'linear-gradient(125deg,#14334e,#41666b)'
 st.markdown(f'<div class="pak-hero" style="background-image:{background}"><h1>{esc(L["welcome"])}</h1><p>{esc(T["tag"])}</p></div>',unsafe_allow_html=True)
 a,b,c=st.columns([2,1.3,2]);
 if b.button(L['try']+' →',use_container_width=True,type='primary'):navigate('home');st.rerun()
def home():
 st.title(L['choose'])
 st.caption(L['sample'])
 mods=content.MODULES
 for offset in range(0,len(mods),3):
  cols=st.columns(3,gap='medium')
  for col,m in zip(cols,mods[offset:offset+3]):
   with col:
    uri=photo(m['id'])
    visual=f'<img class="pak-photo" src="{uri}" alt="{esc(m["en"])}" />' if uri else f'<div class="pak-fallback" style="background:linear-gradient(130deg,{m["c"][0]},{m["c"][1]})">{m["icon"]}</div>'
    title=m['ur'] if S.lang=='ur' else m['en'];tip=m['tip_ur'] if S.lang=='ur' else m['tip']
    st.markdown(f'<div class="pak-card">{visual}<div class="pak-text"><div class="pak-title">{esc(title)}</div><div class="pak-tip">{esc(tip)}</div></div></div>',unsafe_allow_html=True)
    if st.button(('کھولیں ←' if S.lang=='ur' else 'Explore →'),key='open_'+m['id'],use_container_width=True):navigate(m['id']);st.rerun()
def account():
 st.title('👤 '+L['account'])
 if S.uid:
  st.metric(L['credits'],accounts.balance(S.uid))
  st.caption('1 credit is charged only after a successful AI text response. Weather and story browsing are free.')
  st.subheader('💳 '+L['buy'])
  st.info('Payment checkout is not enabled in Colab. Production Stripe Checkout + verified webhook must be configured before paid credits can be issued.')
  if st.button(L['logout']):S.uid=None;st.rerun()
  return
 tab1,tab2=st.tabs([L['login'],L['register']])
 with tab1:
  with st.form('signin'):
   email=st.text_input(L['email']);pw=st.text_input(L['password'],type='password')
   if st.form_submit_button(L['login']):
    uid=accounts.login(email,pw)
    if uid:S.uid=uid;st.success('Signed in');st.rerun()
    else:st.error('Incorrect email or password.')
 with tab2:
  with st.form('signup'):
   email=st.text_input(L['email'],key='reg_email');pw=st.text_input(L['password'],type='password',key='reg_pw')
   if st.form_submit_button(L['register']):
    try:S.uid=accounts.register(email,pw);st.success('Account created: 20 starter credits');st.rerun()
    except ValueError as exc:st.error(str(exc))
def weather():
 st.subheader('🌦️ '+T['weather'])
 town=st.selectbox(T['choose_town'],list(content.TOWNS))
 lat,lon=content.TOWNS[town]
 try:
  url=f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m&timezone=auto'
  with urllib.request.urlopen(url,timeout=10) as r:cur=json.load(r)['current']
  a,b=st.columns(2);a.metric('Temperature °C',cur['temperature_2m']);b.metric('Wind km/h',cur['wind_speed_10m']);st.caption('Source: Open-Meteo • '+cur.get('time',''))
 except Exception:st.warning('Live weather is currently unavailable.')
 st.subheader(T['places'])
 for place in content.PLACES:
  with st.expander(place['name']+' — '+place['area']):st.write(place['type']);st.caption('Routes, prices and opening times are not verified.')
def story():
 st.title('📖 '+('دادی کی کہانیاں' if S.lang=='ur' else 'Grandma Stories'))
 s=st.selectbox('Story',[x['title'] for x in content.STORIES]);obj=next(x for x in content.STORIES if x['title']==s)
 n=st.slider(T['scene'],1,len(obj['scenes']),1)
 title,narration,prompt=obj['scenes'][n-1]
 st.subheader(title);st.write(narration)
 with st.expander('Video prompt'):st.code(prompt,language=None)
 if n==len(obj['scenes']):st.success(obj['moral'])
 buff=io.StringIO();w=csv.writer(buff);w.writerow(['scene','title','narration','video_prompt'])
 for i,(t,txt,v) in enumerate(obj['scenes'],1):w.writerow([i,t,txt,v])
 st.download_button('Download story CSV',buff.getvalue().encode('utf-8-sig'),'story.csv')
def quran():
 st.title('🕌 '+('قرآنِ پاک' if S.lang=='ur' else 'Holy Quran / Noorani Qaida'))
 base=Path(__file__).with_name('content')/'quran'/'qaida'
 lessons=[]
 for f in base.glob('*/lesson.json'):
  try:lessons.append((f.parent,json.loads(f.read_text(encoding='utf-8'))))
  except Exception:pass
 if not lessons:st.info('No scholar-approved lessons have been installed. Add verified lesson.json files, recitation audio and attribution.');return
 names=[x[1].get('title_ur' if S.lang=='ur' else 'title_en',x[0].name) for x in lessons]
 d,l=lessons[names.index(st.selectbox('Lesson',names))]
 st.write(l.get('intro_ur' if S.lang=='ur' else 'intro_en',''))
 for item in l.get('items',[]):
  with st.expander(item.get('name',item.get('text','Lesson item'))):
   st.markdown('### '+esc(item.get('text','')))
   for field,fn in [('audio',st.audio),('video',st.video),('image',st.image)]:
    f=d/item.get(field,'')
    if item.get(field) and f.is_file():fn(str(f))
def module_page(mid):
 m=next(x for x in content.MODULES if x['id']==mid)
 st.title(m['ur'] if S.lang=='ur' else m['en'])
 if mid=='info':weather();return
 if mid=='story':story();return
 if mid=='quran':quran();return
 if S.uid is None:
  st.info('Sign in to use AI providers. You can browse modules without signing in.')
 engine.render_module(mid,S.lang,user_id=S.uid)
css();header()
if S.page!='landing':
 if st.button('← '+L['back'],key='backhome'):navigate('home');st.rerun()
if S.page=='landing':landing()
elif S.page=='home':home()
elif S.page=='account':account()
else:module_page(S.page)
