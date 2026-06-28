```aura width=860 height=220
<div style={{
  width:'100%', height:'100%', background:'#0d0810',
  display:'flex', alignItems:'center', justifyContent:'center',
  fontFamily:'Inter', position:'relative', overflow:'hidden',
  borderRadius:16,
}}>
  <div style={{display:'flex',flexDirection:'column',gap:8,padding:20,zIndex:10,overflow:'hidden'}}>
    <div style={{display:'flex',fontSize:10,color:'#d99d87'}}>totalStars: {String(github?.totalStars ?? 'undefined')}</div>
    <div style={{display:'flex',fontSize:10,color:'#d99d87'}}>publicRepos: {String(github?.user?.publicRepos ?? 'undefined')}</div>
    <div style={{display:'flex',fontSize:10,color:'#d99d87'}}>followers: {String(github?.user?.followers ?? github?.user?.followers?.totalCount ?? 'undefined')}</div>
    <div style={{display:'flex',fontSize:10,color:'#d99d87'}}>repos.length: {String(github?.repos?.length ?? 'undefined')}</div>
    <div style={{display:'flex',fontSize:10,color:'#999189'}}>lang[0]: {JSON.stringify(github?.languages?.[0] ?? 'undefined')}</div>
    <div style={{display:'flex',fontSize:10,color:'#999189'}}>lang[1]: {JSON.stringify(github?.languages?.[1] ?? 'undefined')}</div>
    <div style={{display:'flex',fontSize:10,color:'#999189'}}>lang[2]: {JSON.stringify(github?.languages?.[2] ?? 'undefined')}</div>
    <div style={{display:'flex',fontSize:10,color:'#7b6261'}}>github keys: {Object.keys(github ?? {}).join(', ')}</div>
    <div style={{display:'flex',fontSize:10,color:'#7b6261'}}>user keys: {Object.keys(github?.user ?? {}).join(', ')}</div>
  </div>
</div>
```

```aura width=860 height=220
<div style={{
  width:'100%', height:'100%', background:'#0d0810',
  display:'flex', alignItems:'center', justifyContent:'center',
  fontFamily:'Inter', position:'relative', overflow:'hidden',
  borderRadius:16, 
}}>
  <style>{`
    @keyframes d1 { 0%,100%{transform:translateX(0);opacity:.85} 50%{transform:translateX(280px);opacity:1} }
    @keyframes d2 { 0%,100%{transform:translateX(0);opacity:.7} 50%{transform:translateX(-220px);opacity:.95} }
    @keyframes d3 { 0%,100%{transform:translateX(0);opacity:.75} 50%{transform:translateX(180px);opacity:.55} }
    @keyframes d4 { 0%,100%{transform:translateX(0);opacity:.8} 50%{transform:translateX(-300px);opacity:1} }
    @keyframes d5 { 0%,100%{transform:translateX(0);opacity:.6} 33%{transform:translateX(-140px);opacity:.9} 66%{transform:translateX(90px);opacity:1} }
    @keyframes pg { 0%,100%{transform:scale(1);opacity:.75} 50%{transform:scale(1.3);opacity:.4} }
    @keyframes tf { 0%,100%{opacity:.9} 50%{opacity:1} }
    #h1{animation:d1 10s ease-in-out infinite} #h2{animation:d2 13s ease-in-out infinite}
    #h3{animation:d3 8s ease-in-out infinite} #h4{animation:d4 15s ease-in-out infinite reverse}
    #h5{animation:d5 11s ease-in-out infinite} #h6{animation:pg 7s ease-in-out infinite}
    #ht{animation:tf 5s ease-in-out infinite}
  `}</style>
  <svg width="860" height="220" style={{position:'absolute',top:0,left:0}}>
    <defs>
      <radialGradient id="hg1" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(90,20,40,0.85)"/><stop offset="50%" stopColor="rgba(60,10,25,0.35)"/><stop offset="100%" stopColor="rgba(60,10,25,0)"/></radialGradient>
      <radialGradient id="hg2" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(140,60,80,0.7)"/><stop offset="50%" stopColor="rgba(100,30,55,0.28)"/><stop offset="100%" stopColor="rgba(100,30,55,0)"/></radialGradient>
      <radialGradient id="hg3" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(180,110,90,0.5)"/><stop offset="50%" stopColor="rgba(140,80,60,0.2)"/><stop offset="100%" stopColor="rgba(140,80,60,0)"/></radialGradient>
      <radialGradient id="hg4" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(60,10,50,0.65)"/><stop offset="60%" stopColor="rgba(40,5,35,0.2)"/><stop offset="100%" stopColor="rgba(40,5,35,0)"/></radialGradient>
      <radialGradient id="hg5" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(110,40,60,0.55)"/><stop offset="55%" stopColor="rgba(80,20,40,0.18)"/><stop offset="100%" stopColor="rgba(80,20,40,0)"/></radialGradient>
      <radialGradient id="hg6" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(217,157,135,0.3)"/><stop offset="60%" stopColor="rgba(217,157,135,0.08)"/><stop offset="100%" stopColor="rgba(217,157,135,0)"/></radialGradient>
    </defs>
    <ellipse id="h1" cx="150" cy="240" rx="280" ry="180" fill="url(#hg1)"/>
    <ellipse id="h2" cx="350" cy="250" rx="240" ry="160" fill="url(#hg2)"/>
    <ellipse id="h3" cx="500" cy="245" rx="200" ry="140" fill="url(#hg3)"/>
    <ellipse id="h4" cx="680" cy="255" rx="170" ry="130" fill="url(#hg4)"/>
    <ellipse id="h5" cx="420" cy="235" rx="230" ry="170" fill="url(#hg5)"/>
    <ellipse id="h6" cx="760" cy="200" rx="120" ry="100" fill="url(#hg6)"/>
  </svg>
  <div style={{display:'flex',flexDirection:'column',alignItems:'center',gap:10,zIndex:10}}>
    <div id="ht" style={{display:'flex',fontSize:38,fontWeight:800,color:'#d99d87',letterSpacing:'2px',lineHeight:1}}>Luna Alkufairy</div>
    <div style={{display:'flex',fontSize:14,color:'rgba(153,145,137,0.9)',letterSpacing:'2px'}}>Software Engineer &nbsp;|&nbsp; Flutter Developer</div>
    <div style={{display:'flex',fontSize:12,marginTop:2,color:'rgba(217,157,135,0.6)',letterSpacing:'1px'}}>Crafting cross-platform mobile apps · Open to freelance &amp; internships</div>
  </div>
</div>
```

```aura width=860 height=200
<div style={{
  width:'100%', height:'100%', background:'#0d0810',
  display:'flex', alignItems:'center', justifyContent:'center',
  fontFamily:'Inter', position:'relative', overflow:'hidden',
  borderRadius:16, 
}}>
  <style>{`
    @keyframes a1 { 0%,100%{transform:translateX(0);opacity:.6} 50%{transform:translateX(200px);opacity:.9} }
    @keyframes a2 { 0%,100%{transform:translateX(0);opacity:.5} 50%{transform:translateX(-180px);opacity:.8} }
    @keyframes a3 { 0%,100%{transform:translateX(0);opacity:.7} 50%{transform:translateX(150px);opacity:.45} }
    #ab1{animation:a1 12s ease-in-out infinite} #ab2{animation:a2 9s ease-in-out infinite} #ab3{animation:a3 14s ease-in-out infinite reverse}
  `}</style>
  <svg width="860" height="200" style={{position:'absolute',top:0,left:0}}>
    <defs>
      <radialGradient id="ag1" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(68,33,40,0.7)"/><stop offset="100%" stopColor="rgba(68,33,40,0)"/></radialGradient>
      <radialGradient id="ag2" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(123,48,80,0.5)"/><stop offset="100%" stopColor="rgba(123,48,80,0)"/></radialGradient>
      <radialGradient id="ag3" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(42,10,64,0.55)"/><stop offset="100%" stopColor="rgba(42,10,64,0)"/></radialGradient>
    </defs>
    <ellipse id="ab1" cx="120" cy="180" rx="260" ry="140" fill="url(#ag1)"/>
    <ellipse id="ab2" cx="600" cy="180" rx="280" ry="150" fill="url(#ag2)"/>
    <ellipse id="ab3" cx="400" cy="160" rx="200" ry="120" fill="url(#ag3)"/>
  </svg>
  <div style={{display:'flex',flexDirection:'column',alignItems:'center',gap:16,zIndex:10,padding:'0 60px',textAlign:'center'}}>
    <div style={{display:'flex',fontSize:11,color:'rgba(217,157,135,0.5)',letterSpacing:'4px',textTransform:'uppercase'}}>— Who Am I —</div>
    <div style={{display:'flex',flexDirection:'column',gap:6,alignItems:'center'}}>
      <div style={{display:'flex',fontSize:14,color:'rgba(153,145,137,0.85)',letterSpacing:'0.5px',lineHeight:1.7}}>A developer who genuinely loves what she builds.</div>
      <div style={{display:'flex',fontSize:14,color:'rgba(153,145,137,0.85)',letterSpacing:'0.5px',lineHeight:1.7}}>I get excited learning something new every single day —</div>
      <div style={{display:'flex',fontSize:14,color:'rgba(153,145,137,0.85)',letterSpacing:'0.5px',lineHeight:1.7}}>curiosity is not a phase for me, it's how I'm wired.</div>
      <div style={{display:'flex',fontSize:13,color:'rgba(217,157,135,0.5)',letterSpacing:'1.5px',marginTop:6}}>4th Year · Software Engineering · University of Damascus</div>
    </div>
  </div>
</div>
```

```aura width=860 height=280
<div style={{
  width:'100%', height:'100%', background:'#0d0810',
  display:'flex', alignItems:'center', justifyContent:'center',
  fontFamily:'Inter', position:'relative', overflow:'hidden',
  borderRadius:16, 
}}>
  <style>{`
    @keyframes t1 { 0%,100%{transform:translateX(0);opacity:.65} 50%{transform:translateX(240px);opacity:.9} }
    @keyframes t2 { 0%,100%{transform:translateX(0);opacity:.55} 50%{transform:translateX(-200px);opacity:.85} }
    @keyframes t3 { 0%,100%{transform:translateX(0);opacity:.7} 50%{transform:translateX(160px);opacity:.5} }
    #tb1{animation:t1 11s ease-in-out infinite} #tb2{animation:t2 14s ease-in-out infinite} #tb3{animation:t3 9s ease-in-out infinite reverse}
  `}</style>
  <svg width="860" height="280" style={{position:'absolute',top:0,left:0}}>
    <defs>
      <radialGradient id="tg1" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(90,20,40,0.7)"/><stop offset="100%" stopColor="rgba(90,20,40,0)"/></radialGradient>
      <radialGradient id="tg2" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(150,70,90,0.5)"/><stop offset="100%" stopColor="rgba(150,70,90,0)"/></radialGradient>
      <radialGradient id="tg3" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(50,15,60,0.6)"/><stop offset="100%" stopColor="rgba(50,15,60,0)"/></radialGradient>
    </defs>
    <ellipse id="tb1" cx="100" cy="260" rx="280" ry="160" fill="url(#tg1)"/>
    <ellipse id="tb2" cx="700" cy="260" rx="260" ry="150" fill="url(#tg2)"/>
    <ellipse id="tb3" cx="430" cy="240" rx="220" ry="130" fill="url(#tg3)"/>
  </svg>
  <div style={{display:'flex',flexDirection:'column',alignItems:'center',gap:18,zIndex:10,width:'100%',padding:'0 50px'}}>
    <div style={{display:'flex',fontSize:11,color:'rgba(217,157,135,0.5)',letterSpacing:'4px'}}>— TECH STACK —</div>
    {[
      {label:'Languages', items:['Dart','Java','C++']},
      {label:'Frameworks', items:['Flutter','GetX','BLoC','Dio']},
      {label:'Databases', items:['Firebase','SQLite']},
      {label:'Design & Tools', items:['GitHub','Git','VS Code','Visual Studio','Figma','Postman']},
      {label:'Workspace', items:['Windows']},
    ].map(function(row, i) {
      return (
        <div key={i} style={{display:'flex',alignItems:'center',gap:16,width:'100%'}}>
          <div style={{display:'flex',fontSize:10,color:'rgba(123,98,97,0.7)',letterSpacing:'2px',minWidth:130,textAlign:'right'}}>{row.label}</div>
          <div style={{width:1,height:20,background:'rgba(68,33,40,0.8)'}}/>
          <div style={{display:'flex',gap:8,flexWrap:'wrap'}}>
            {row.items.map(function(item, j) {
              return (
                <div key={j} style={{
                  display:'flex',padding:'4px 14px',borderRadius:20,
                  background:'rgba(68,33,40,0.45)',
                  border:'1px solid rgba(217,157,135,0.2)',
                  color:'rgba(217,157,135,0.8)',fontSize:12,fontWeight:500,letterSpacing:'0.5px'
                }}>{item}</div>
              );
            })}
          </div>
        </div>
      );
    })}
  </div>
</div>
```

```aura width=860 height=260
<div style={{
  width:'100%', height:'100%', background:'#0d0810',
  display:'flex', alignItems:'center', justifyContent:'center',
  fontFamily:'Inter', position:'relative', overflow:'hidden',
  borderRadius:16, 
}}>
  <style>{`
    @keyframes s1 { 0%,100%{transform:translateX(0);opacity:.6} 50%{transform:translateX(220px);opacity:.85} }
    @keyframes s2 { 0%,100%{transform:translateX(0);opacity:.5} 50%{transform:translateX(-190px);opacity:.8} }
    @keyframes s3 { 0%,100%{opacity:.7} 50%{opacity:.35} }
    #sb1{animation:s1 13s ease-in-out infinite} #sb2{animation:s2 10s ease-in-out infinite} #sb3{animation:s3 8s ease-in-out infinite}
  `}</style>
  <svg width="860" height="260" style={{position:'absolute',top:0,left:0}}>
    <defs>
      <radialGradient id="sg1" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(80,18,35,0.75)"/><stop offset="100%" stopColor="rgba(80,18,35,0)"/></radialGradient>
      <radialGradient id="sg2" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(130,55,75,0.55)"/><stop offset="100%" stopColor="rgba(130,55,75,0)"/></radialGradient>
      <radialGradient id="sg3" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(217,157,135,0.18)"/><stop offset="100%" stopColor="rgba(217,157,135,0)"/></radialGradient>
    </defs>
    <ellipse id="sb1" cx="150" cy="250" rx="300" ry="160" fill="url(#sg1)"/>
    <ellipse id="sb2" cx="680" cy="250" rx="270" ry="150" fill="url(#sg2)"/>
    <ellipse id="sb3" cx="430" cy="130" rx="180" ry="100" fill="url(#sg3)"/>
  </svg>
  <div style={{display:'flex',flexDirection:'column',alignItems:'center',gap:20,zIndex:10,width:'100%',padding:'0 50px'}}>
    <div style={{display:'flex',fontSize:11,color:'rgba(217,157,135,0.5)',letterSpacing:'4px'}}>— GITHUB STATS —</div>
    <div style={{display:'flex',gap:30,justifyContent:'center',width:'100%'}}>
      {[
        {label:'Repositories', value: github?.repos?.length ?? github?.user?.publicRepos ?? github?.user?.repositories?.totalCount ?? '—'},
        {label:'Followers',    value: github?.user?.followers?.totalCount ?? github?.user?.followers ?? '—'},
        {label:'Following',    value: github?.user?.following?.totalCount ?? github?.user?.following ?? '—'},
        {label:'Stars',        value: github?.totalStars ?? github?.user?.starredRepositories?.totalCount ?? '—'},
      ].map(function(stat, i) {
        return (
          <div key={i} style={{display:'flex',flexDirection:'column',alignItems:'center',gap:6}}>
            <div style={{display:'flex',fontSize:28,fontWeight:800,color:'#d99d87',letterSpacing:'1px'}}>{stat.value}</div>
            <div style={{display:'flex',fontSize:10,color:'rgba(123,98,97,0.7)',letterSpacing:'2px',textTransform:'uppercase'}}>{stat.label}</div>
          </div>
        );
      })}
    </div>
    <div style={{display:'flex',width:'80%',height:1,background:'rgba(68,33,40,0.6)'}}/>
    <div style={{display:'flex',flexDirection:'column',gap:10,width:'70%'}}>
      {(function() {
        var langs = (github?.languages ?? []).slice(0, 5);
        var total = langs.reduce(function(s, l) { return s + (parseInt(l.size) || parseInt(l.bytes) || 1); }, 0);
        return langs.map(function(lang, i) {
          var size = parseInt(lang.size) || parseInt(lang.bytes) || 0;
          var pct = total > langs.length ? Math.round(size / total * 100) : Math.round(100 / langs.length);
          return (
            <div key={i} style={{display:'flex',alignItems:'center',gap:12}}>
              <div style={{display:'flex',fontSize:11,color:'rgba(153,145,137,0.8)',minWidth:70,letterSpacing:'1px'}}>{lang.name}</div>
              <div style={{display:'flex',flex:1,height:4,background:'rgba(68,33,40,0.5)',borderRadius:2}}>
                <div style={{display:'flex',width:pct+'%',height:'100%',background:'#d99d87',borderRadius:2,opacity:0.7}}/>
              </div>
              <div style={{display:'flex',fontSize:10,color:'rgba(123,98,97,0.7)',minWidth:35,justifyContent:'flex-end'}}>{pct}%</div>
            </div>
          );
        });
      })()}
    </div>
  </div>
</div>
```

```aura width=860 height=80
<div style={{
  width:'100%', height:'100%',
  background:'linear-gradient(180deg, transparent 0%, #0d0810 60%)',
  display:'flex', alignItems:'flex-end', justifyContent:'center',
  paddingBottom:12, position:'relative', overflow:'hidden'
}}>
  <svg width="860" height="80" style={{position:'absolute',top:0,left:0}}>
    <defs>
      <radialGradient id="fg1" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(90,20,40,0.6)"/><stop offset="100%" stopColor="rgba(90,20,40,0)"/></radialGradient>
      <radialGradient id="fg2" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(140,60,80,0.5)"/><stop offset="100%" stopColor="rgba(140,60,80,0)"/></radialGradient>
    </defs>
    <ellipse cx="250" cy="40" rx="300" ry="60" fill="url(#fg1)"/>
    <ellipse cx="620" cy="50" rx="260" ry="55" fill="url(#fg2)"/>
  </svg>
  <span style={{color:'rgba(123,98,97,0.5)',fontSize:11,letterSpacing:'3px',zIndex:10}}>
    lunaalkufairy · {new Date().getFullYear()}
  </span>
</div>
```
