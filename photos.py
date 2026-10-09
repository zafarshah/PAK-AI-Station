"""Subject-specific Wikimedia Commons photos. Review license metadata before public release."""
import json, requests, re
from pathlib import Path
from PIL import Image, ImageOps
from io import BytesIO
ROOT=Path(__file__).with_name('images'); ROOT.mkdir(exist_ok=True)
# Carefully scoped search phrases, with validation by a human recommended.
SEARCH={
 'info':'Gilgit Baltistan landscape Pakistan',
 'story':'grandmother reading book child photograph',
 'kids':'children reading classroom Pakistan',
 'quran':'Quran book on wooden stand photograph',
 'util':'Karakoram Highway bridge road Pakistan',
 'env':'glacier Karakoram Pakistan',
 'forest':'Himalayan ibex Capra sibirica wildlife',
 'agri':'apricot orchard blossoms Hunza',
 'tourism':'Attabad Lake Hunza Pakistan',
 'fishery':'rainbow trout aquaculture fish farm',
 'markets':'dried apricots nuts market Pakistan',
}
API='https://commons.wikimedia.org/w/api.php'
HEADERS={'User-Agent':'PAKAIStation/0.7 (educational photo attribution; contact: pak-ai-station@example.org)'}
def download_photos():
 results={}
 for mod,term in SEARCH.items():
  dst=ROOT/(mod+'.jpg')
  if dst.exists():results[mod]='Already present';continue
  try:
   data=requests.get(API,params={'action':'query','generator':'search','gsrsearch':term+' filetype:bitmap','gsrnamespace':6,'gsrlimit':8,'prop':'imageinfo','iiprop':'url|size|extmetadata','iiurlwidth':1200,'format':'json'},headers=HEADERS,timeout=20).json()
   pages=data.get('query',{}).get('pages',{})
   saved=False
   for page in pages.values():
    ii=(page.get('imageinfo') or [{}])[0]
    if ii.get('width',0)<500 or ii.get('height',0)<300:continue
    url=ii.get('thumburl') or ii.get('url','')
    if not url.startswith('https://'):continue
    r=requests.get(url,headers=HEADERS,timeout=25);r.raise_for_status()
    im=Image.open(BytesIO(r.content)).convert('RGB')
    if im.width<500 or im.height<300:continue
    # Uniform landscape ratio 16:10; no stretch.
    im=ImageOps.fit(im,(960,600),method=Image.Resampling.LANCZOS)
    im.save(dst,quality=86,optimize=True)
    meta=ii.get('extmetadata',{})
    record={'module':mod,'search':term,'file_title':page.get('title'),'source':ii.get('descriptionurl'),'license':meta.get('LicenseShortName',{}).get('value'),'artist':re.sub('<[^>]*>','',meta.get('Artist',{}).get('value',''))[:300],'reviewed':False}
    (ROOT/(mod+'.license.json')).write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
    results[mod]=page.get('title');saved=True;break
   if not saved:results[mod]='No suitable photo found; labeled placeholder used'
  except Exception as e:results[mod]='Download failed: '+type(e).__name__
 return results
if __name__=='__main__':
 for k,v in download_photos().items():print(k,':',v)
