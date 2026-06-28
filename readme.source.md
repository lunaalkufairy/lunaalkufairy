```aura width=860 height=820
<div style={{
  width:'100%', height:'100%', background:'#0d0810',
  display:'flex', flexDirection:'column',
  fontFamily:'Inter', position:'relative', overflow:'hidden',
  borderRadius:16,
}}>
  <style>{`
    @keyframes d1{0%,100%{transform:translateX(0);opacity:.85}50%{transform:translateX(280px);opacity:1}}
    @keyframes d2{0%,100%{transform:translateX(0);opacity:.7}50%{transform:translateX(-220px);opacity:.95}}
    @keyframes d3{0%,100%{transform:translateX(0);opacity:.75}50%{transform:translateX(180px);opacity:.55}}
    @keyframes d4{0%,100%{transform:translateX(0);opacity:.8}50%{transform:translateX(-300px);opacity:1}}
    @keyframes d5{0%,100%{transform:translateX(0);opacity:.6}33%{transform:translateX(-140px);opacity:.9}66%{transform:translateX(90px);opacity:1}}
    @keyframes tf{0%,100%{opacity:.9}50%{opacity:1}}
    #h1{animation:d1 10s ease-in-out infinite}#h2{animation:d2 13s ease-in-out infinite}
    #h3{animation:d3 8s ease-in-out infinite}#h4{animation:d4 15s ease-in-out infinite reverse}
    #h5{animation:d5 11s ease-in-out infinite}
    #ht{animation:tf 5s ease-in-out infinite}
  `}</style>

  <svg width="860" height="820" style={{position:'absolute',top:0,left:0}}>
    <defs>
      <radialGradient id="g1" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(90,20,40,0.85)"/><stop offset="50%" stopColor="rgba(60,10,25,0.35)"/><stop offset="100%" stopColor="rgba(60,10,25,0)"/></radialGradient>
      <radialGradient id="g2" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(140,60,80,0.65)"/><stop offset="50%" stopColor="rgba(100,30,55,0.25)"/><stop offset="100%" stopColor="rgba(100,30,55,0)"/></radialGradient>
      <radialGradient id="g3" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(180,110,90,0.45)"/><stop offset="50%" stopColor="rgba(140,80,60,0.15)"/><stop offset="100%" stopColor="rgba(140,80,60,0)"/></radialGradient>
      <radialGradient id="g4" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(60,10,50,0.6)"/><stop offset="60%" stopColor="rgba(40,5,35,0.18)"/><stop offset="100%" stopColor="rgba(40,5,35,0)"/></radialGradient>
      <radialGradient id="g5" cx="50%" cy="50%" r="50%"><stop offset="0%" stopColor="rgba(110,40,60,0.5)"/><stop offset="55%" stopColor="rgba(80,20,40,0.15)"/><stop offset="100%" stopColor="rgba(80,20,40,0)"/></radialGradient>
    </defs>
    <ellipse id="h1" cx="150" cy="300" rx="320" ry="280" fill="url(#g1)"/>
    <ellipse id="h2" cx="700" cy="400" rx="280" ry="260" fill="url(#g2)"/>
    <ellipse id="h3" cx="430" cy="500" rx="260" ry="200" fill="url(#g3)"/>
    <ellipse id="h4" cx="100" cy="650" rx="240" ry="200" fill="url(#g4)"/>
    <ellipse id="h5" cx="750" cy="700" rx="260" ry="220" fill="url(#g5)"/>
  </svg>

  <div style={{display:'flex',flexDirection:'column',alignItems:'center',justifyContent:'center',height:220,zIndex:10,gap:10}}>
    <div id="ht" style={{display:'flex',fontSize:38,fontWeight:800,color:'#d99d87',letterSpacing:'2px',lineHeight:1}}>Luna Alkufairy</div>
    <div style={{display:'flex',fontSize:14,color:'rgba(153,145,137,0.9)',letterSpacing:'2px'}}>Software Engineer &nbsp;|&nbsp; Flutter Developer</div>
    <div style={{display:'flex',fontSize:12,color:'rgba(217,157,135,0.6)',letterSpacing:'1px'}}>Crafting cross-platform mobile apps · Open to freelance &amp; internships</div>
  </div>

  <div style={{display:'flex',width:'80%',height:1,background:'rgba(68,33,40,0.5)',alignSelf:'center'}}/>

  <div style={{display:'flex',flexDirection:'column',alignItems:'center',justifyContent:'center',height:200,zIndex:10,gap:12,padding:'0 60px'}}>
    <div style={{display:'flex',fontSize:11,color:'rgba(217,157,135,0.45)',letterSpacing:'4px'}}>— WHO AM I —</div>
    <div style={{display:'flex',flexDirection:'column',gap:6,alignItems:'center'}}>
      <div style={{display:'flex',fontSize:14,color:'rgba(153,145,137,0.85)',letterSpacing:'0.5px'}}>A developer who genuinely loves what she builds.</div>
      <div style={{display:'flex',fontSize:14,color:'rgba(153,145,137,0.85)',letterSpacing:'0.5px'}}>I get excited learning something new every single day —</div>
      <div style={{display:'flex',fontSize:14,color:'rgba(153,145,137,0.85)',letterSpacing:'0.5px'}}>curiosity is not a phase for me, it's how I'm wired.</div>
      <div style={{display:'flex',fontSize:13,color:'rgba(217,157,135,0.45)',letterSpacing:'1.5px',marginTop:4}}>4th Year · Software Engineering · University of Damascus</div>
    </div>
  </div>

  <div style={{display:'flex',width:'80%',height:1,background:'rgba(68,33,40,0.5)',alignSelf:'center'}}/>

  <div style={{display:'flex',flexDirection:'column',alignItems:'center',justifyContent:'center',height:310,zIndex:10,gap:14,padding:'0 50px'}}>
    <div style={{display:'flex',fontSize:11,color:'rgba(217,157,135,0.45)',letterSpacing:'4px'}}>— TECH STACK —</div>
    {[
      {label:'Languages',     items:['Dart','Java','C++']},
      {label:'Frameworks',    items:['Flutter','GetX','BLoC','Dio']},
      {label:'Databases',     items:['Firebase','SQLite']},
      {label:'Design & Tools',items:['GitHub','Git','VS Code','Visual Studio','Figma','Postman']},
      {label:'Workspace',     items:['Windows']},
    ].map(function(row,i){
      return (
        <div key={i} style={{display:'flex',alignItems:'center',gap:14,width:'100%'}}>
          <div style={{display:'flex',fontSize:10,color:'rgba(123,98,97,0.65)',letterSpacing:'1.5px',minWidth:120,justifyContent:'flex-end'}}>{row.label}</div>
          <div style={{display:'flex',width:1,height:18,background:'rgba(68,33,40,0.7)'}}/>
          <div style={{display:'flex',gap:7,flexWrap:'wrap'}}>
            {row.items.map(function(item,j){
              return (
                <div key={j} style={{display:'flex',padding:'3px 12px',borderRadius:20,background:'rgba(68,33,40,0.45)',border:'1px solid rgba(217,157,135,0.18)',color:'rgba(217,157,135,0.8)',fontSize:11,fontWeight:500}}>{item}</div>
              );
            })}
          </div>
        </div>
      );
    })}
  </div>

  <div style={{display:'flex',flex:1,alignItems:'flex-end',justifyContent:'center',paddingBottom:16,zIndex:10}}>
    <span style={{display:'flex',color:'rgba(123,98,97,0.4)',fontSize:11,letterSpacing:'3px'}}>lunaalkufairy · {new Date().getFullYear()}</span>
  </div>

</div>
```
