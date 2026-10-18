#!/usr/bin/env python3
"""Update assets/metrics.svg from public GitHub REST data. Python stdlib only.

This reports ONLY repositories owned by the account (not private or org-owned).
Use: python scripts/update_stats.py --user Yashuuuu02
"""
from __future__ import annotations
import argparse, datetime, html, json, os, pathlib, urllib.error, urllib.request

def github(path: str) -> object:
    token=os.environ.get("GITHUB_TOKEN","").strip()
    headers={"Accept":"application/vnd.github+json","User-Agent":"github-profile-metrics/1.0","X-GitHub-Api-Version":"2022-11-28"}
    if token: headers["Authorization"]="Bearer "+token
    req=urllib.request.Request("https://api.github.com"+path,headers=headers)
    with urllib.request.urlopen(req,timeout=25) as r: return json.load(r)

def svg(n:int,stars:int,user:str,when:str)->str:
    def tx(x,y,s,z=18,c="#F0F7EE",w=600,mono=False):
        f="DejaVu Sans Mono,monospace" if mono else "Arial,DejaVu Sans,sans-serif"
        return f'<text x="{x}" y="{y}" fill="{c}" font-size="{z}" font-weight="{w}" font-family="{f}">{html.escape(str(s))}</text>'
    def rec(x,y,w,h):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="15" fill="#14242A" stroke="#3E5959"/>'
    out=['<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="352" viewBox="0 0 1280 352" role="img">',
         '<defs><linearGradient id="b"><stop stop-color="#152025"/><stop offset="1" stop-color="#092024"/></linearGradient></defs>',
         '<rect width="1280" height="352" rx="22" fill="url(#b)" stroke="#34504F"/>',
         tx(40,54,"GITHUB / VERIFIED PUBLIC REPOSITORY SNAPSHOT",15,"#CBFF78",750,True),tx(40,101,"SHIP LOG",43,"#F0F7EE",800),
         tx(40,133,"Public account data. No estimated commits or streaks.",18,"#A1B8B2")]
    for x,title,value,foot in [(40,"PUBLIC REPOS",n,"Owned public repositories"),(356,"STARS RECEIVED",stars,"Across these public repos")]:
        out += [rec(x,159,294,156),tx(x+19,187,title,14,"#7DE2D5",720,True),tx(x+17,251,str(value).zfill(2),57,"#CBFF78",850,True),tx(x+20,291,foot,13,"#A1B8B2")]
    out += [rec(685,159,554,156),tx(711,192,"TRANSPARENCY / SCOPE",15,"#7DE2D5",750,True),
            tx(713,224,"Excludes private and organization-owned repositories.",16),tx(713,251,"Full contribution and language cards appear below.",15,"#A1B8B2"),
            tx(714,290,"REFRESHED: "+when,13,"#CBFF78",720,True),'</svg>']
    return ''.join(out)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--user',default='Yashuuuu02'); ap.add_argument('--output',default='assets/metrics.svg'); args=ap.parse_args()
    owned=[]
    for page in range(1,21):
        chunk=github(f'/users/{args.user}/repos?per_page=100&type=owner&page={page}')
        if not isinstance(chunk,list): raise ValueError('Expected list of repositories')
        for r in chunk:
            if not isinstance(r,dict):continue
            if r.get('owner',{}).get('login','').lower()==args.user.lower() and r.get('private') is False:
                owned.append(r)
        if len(chunk)<100:break
    else: raise ValueError('Too many pages: pagination safety stop')
    if not owned: raise ValueError('Zero repositories: refusing to overwrite existing snapshot with possibly broken API data')
    stars=sum(int(r.get('stargazers_count',0)) for r in owned)
    now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d UTC')
    dst=pathlib.Path(args.output); dst.parent.mkdir(parents=True,exist_ok=True)
    dst.write_text(svg(len(owned),stars,args.user,now),encoding='utf-8')
    print(f'Updated {dst}: {len(owned)} public owned repos, {stars} stars ({now})')

if __name__=='__main__': main()
