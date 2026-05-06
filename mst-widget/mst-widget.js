(function(){
const sites={
  "A": {
    "label": "Forehead",
    "value": 34.0,
    "x": 150.12,
    "y": 34.63
  },
  "B": {
    "label": "Cheek (l)",
    "value": 33.8,
    "x": 133.77,
    "y": 92.9
  },
  "C": {
    "label": "Neck (l)",
    "value": 33.6,
    "x": 130.78,
    "y": 126.08
  },
  "D": {
    "label": "Upper arm (r)",
    "value": 32.8,
    "x": 72.5,
    "y": 222.47
  },
  "E": {
    "label": "Elbow (l)",
    "value": 32.2,
    "x": 226.42,
    "y": 277.26
  },
  "F": {
    "label": "Forearm (l)",
    "value": 32.5,
    "x": 250.11,
    "y": 323.85
  },
  "G": {
    "label": "Palm (l)",
    "value": 31.8,
    "x": 256.77,
    "y": 392.82
  },
  "H": {
    "label": "Hand (r)",
    "value": 31.6,
    "x": 27.64,
    "y": 433.89
  },
  "I": {
    "label": "Hand (l)",
    "value": 31.5,
    "x": 271.28,
    "y": 433.89
  },
  "J": {
    "label": "Back (l)",
    "value": 33.2,
    "x": 454.66,
    "y": 199.1
  },
  "K": {
    "label": "Chest (l)",
    "value": 33.5,
    "x": 150.26,
    "y": 191.71
  },
  "L": {
    "label": "Lumbar (l)",
    "value": 33.1,
    "x": 454.66,
    "y": 300.73
  },
  "M": {
    "label": "Abdomen",
    "value": 33.0,
    "x": 150.42,
    "y": 312.05
  },
  "N": {
    "label": "Buttocks (l)",
    "value": 32.8,
    "x": 485.4,
    "y": 345.25
  },
  "O": {
    "label": "Thigh (a)",
    "value": 32.0,
    "x": 182.72,
    "y": 459.67
  },
  "P": {
    "label": "Thigh (l)(p)",
    "value": 31.9,
    "x": 483.45,
    "y": 459.67
  },
  "Q": {
    "label": "Calf (a)(r)",
    "value": 31.0,
    "x": 116.73,
    "y": 593.31
  },
  "R": {
    "label": "Calf (p)(l)",
    "value": 30.9,
    "x": 487.73,
    "y": 592.85
  },
  "S": {
    "label": "Foot (l)",
    "value": 30.5,
    "x": 172.95,
    "y": 710.17
  },
  "T": {
    "label": "Foot (r)",
    "value": 30.5,
    "x": 125.98,
    "y": 710.17
  },
  "U": {
    "label": "Sole (l)",
    "value": 30.4,
    "x": 469.34,
    "y": 716.5
  }
};
const formulas=[
  {
    "id": "burton-1935-3-a",
    "name": "Burton (1935)",
    "n": 3,
    "weights": {
      "F": 0.14,
      "K": 0.5,
      "Q": 0.36
    }
  },
  {
    "id": "olesen-1984-3-b",
    "name": "Olesen (1984)",
    "n": 3,
    "weights": {
      "F": 0.14,
      "K": 0.5,
      "R": 0.36
    }
  },
  {
    "id": "cho-et-al-1996-3-c",
    "name": "Cho et al. (1996)",
    "n": 3,
    "weights": {
      "A": 0.25,
      "F": 0.5,
      "S": 0.25
    }
  },
  {
    "id": "wu-et-al-2020-3-d",
    "name": "Wu et al. (2020)",
    "n": 3,
    "weights": {
      "F": 0.3,
      "K": 0.35,
      "Q": 0.35
    }
  },
  {
    "id": "roberts-et-al-1977-3-e",
    "name": "Roberts et al. (1977)",
    "n": 3,
    "weights": {
      "D": 0.25,
      "K": 0.43,
      "O": 0.32
    }
  },
  {
    "id": "newburgh-and-spealman-1943-4-a",
    "name": "Newburgh & Spealman (1943)",
    "n": 4,
    "weights": {
      "F": 0.15,
      "K": 0.34,
      "O": 0.33,
      "Q": 0.18
    }
  },
  {
    "id": "ramanathan-1964-4-b",
    "name": "Ramanathan (1964)",
    "n": 4,
    "weights": {
      "D": 0.3,
      "K": 0.3,
      "O": 0.2,
      "Q": 0.2
    }
  },
  {
    "id": "iso-9886-1992-4-c",
    "name": "ISO 9886 (1992)",
    "n": 4,
    "weights": {
      "C": 0.28,
      "H": 0.16,
      "J": 0.28,
      "Q": 0.28
    }
  },
  {
    "id": "wu-et-al-2020-4-d",
    "name": "Wu et al. (2020a)",
    "n": 4,
    "weights": {
      "F": 0.14,
      "K": 0.35,
      "O": 0.26,
      "Q": 0.25
    }
  },
  {
    "id": "wu-et-al-2020-4-e",
    "name": "Wu et al. (2020b)",
    "n": 4,
    "weights": {
      "D": 0.14,
      "K": 0.35,
      "O": 0.26,
      "Q": 0.25
    }
  },
  {
    "id": "ouyang-1985-5-a",
    "name": "Ouyang (1985)",
    "n": 5,
    "weights": {
      "A": 0.07,
      "H": 0.05,
      "K": 0.5,
      "O": 0.18,
      "Q": 0.2
    }
  },
  {
    "id": "houdas-1982-5-b",
    "name": "Houdas (1982)",
    "n": 5,
    "weights": {
      "B": 0.07,
      "D": 0.19,
      "L": 0.175,
      "M": 0.175,
      "P": 0.39
    }
  },
  {
    "id": "wu-et-al-2020-5-c",
    "name": "Wu et al. (2020)",
    "n": 5,
    "weights": {
      "A": 0.07,
      "H": 0.05,
      "K": 0.42,
      "O": 0.26,
      "Q": 0.2
    }
  },
  {
    "id": "wang-et-al-2013-5-d",
    "name": "Wang et al. (2013)",
    "n": 5,
    "weights": {
      "A": 0.2,
      "D": 0.18,
      "H": 0.05,
      "J": 0.5,
      "O": 0.07
    }
  },
  {
    "id": "ouyang-1985-6-a",
    "name": "Ouyang (1985)",
    "n": 6,
    "weights": {
      "B": 0.14,
      "F": 0.11,
      "G": 0.05,
      "J": 0.19,
      "K": 0.19,
      "O": 0.32
    }
  },
  {
    "id": "teichner-1958-6-b",
    "name": "Teichner (1958)",
    "n": 6,
    "weights": {
      "B": 0.149,
      "D": 0.107,
      "K": 0.186,
      "L": 0.186,
      "O": 0.186,
      "P": 0.186
    }
  },
  {
    "id": "miura-et-al-1960-6-c",
    "name": "Miura et al. (1960)",
    "n": 6,
    "weights": {
      "A": 0.1,
      "F": 0.05,
      "H": 0.05,
      "K": 0.4,
      "O": 0.2,
      "Q": 0.2
    }
  },
  {
    "id": "palmes-and-park-1947-6-e",
    "name": "Palmes & Park (1947)",
    "n": 6,
    "weights": {
      "B": 0.14,
      "F": 0.11,
      "H": 0.05,
      "K": 0.19,
      "L": 0.19,
      "O": 0.32
    }
  },
  {
    "id": "hardy-and-dubois-1938-7-a",
    "name": "Hardy & DuBois (1938)",
    "n": 7,
    "weights": {
      "A": 0.07,
      "F": 0.14,
      "G": 0.05,
      "K": 0.35,
      "O": 0.19,
      "Q": 0.13,
      "U": 0.07
    }
  },
  {
    "id": "park-1988-7-b",
    "name": "Park (1988)",
    "n": 7,
    "weights": {
      "F": 0.1428571429,
      "H": 0.1428571429,
      "J": 0.1428571429,
      "K": 0.1428571429,
      "O": 0.1428571429,
      "R": 0.1428571429,
      "S": 0.1428571429
    }
  },
  {
    "id": "nadel-7-c",
    "name": "Nadel (?)",
    "n": 7,
    "weights": {
      "A": 0.21,
      "D": 0.12,
      "F": 0.06,
      "K": 0.21,
      "M": 0.17,
      "O": 0.15,
      "Q": 0.08
    }
  },
  {
    "id": "ouyang-1985-7-d",
    "name": "Ouyang (1985)",
    "n": 7,
    "weights": {
      "C": 0.098,
      "D": 0.082,
      "F": 0.114,
      "J": 0.162,
      "K": 0.166,
      "O": 0.182,
      "Q": 0.206
    }
  },
  {
    "id": "mochida-1983-7-e",
    "name": "Mochida (1983)",
    "n": 7,
    "weights": {
      "A": 0.066,
      "D": 0.149,
      "F": 0.151,
      "K": 0.153,
      "M": 0.153,
      "O": 0.163,
      "Q": 0.183
    }
  },
  {
    "id": "mochida-1983-7-f",
    "name": "Mochida (1983)",
    "n": 7,
    "weights": {
      "A": 0.198,
      "D": 0.138,
      "F": 0.076,
      "K": 0.179,
      "M": 0.145,
      "O": 0.153,
      "Q": 0.092
    }
  },
  {
    "id": "ouyang-1985-8-a",
    "name": "Ouyang (1985)",
    "n": 8,
    "weights": {
      "D": 0.085,
      "F": 0.09,
      "J": 0.11,
      "K": 0.11,
      "L": 0.11,
      "M": 0.11,
      "O": 0.23,
      "Q": 0.16
    }
  },
  {
    "id": "gagge-and-nishi-1977-8-b",
    "name": "Gagge & Nishi (1977)",
    "n": 8,
    "weights": {
      "A": 0.07,
      "D": 0.07,
      "F": 0.07,
      "H": 0.05,
      "J": 0.175,
      "K": 0.175,
      "O": 0.19,
      "Q": 0.2
    }
  },
  {
    "id": "nadel-1973-8-c",
    "name": "Nadel (1973a)",
    "n": 8,
    "weights": {
      "A": 0.21,
      "D": 0.12,
      "F": 0.06,
      "J": 0.11,
      "K": 0.1,
      "M": 0.17,
      "O": 0.15,
      "Q": 0.08
    }
  },
  {
    "id": "nadel-1973-8-d",
    "name": "Nadel (1973b)",
    "n": 8,
    "weights": {
      "A": 0.07,
      "D": 0.13,
      "F": 0.12,
      "J": 0.09,
      "K": 0.09,
      "M": 0.18,
      "O": 0.16,
      "Q": 0.16
    }
  },
  {
    "id": "crawshaw-1975-8-e",
    "name": "Crawshaw (1975)",
    "n": 8,
    "weights": {
      "A": 0.19,
      "D": 0.13,
      "F": 0.12,
      "J": 0.09,
      "K": 0.08,
      "M": 0.12,
      "O": 0.12,
      "Q": 0.15
    }
  },
  {
    "id": "ouyang-1985-9-a",
    "name": "Ouyang (1985)",
    "n": 9,
    "weights": {
      "A": 0.07,
      "D": 0.07,
      "F": 0.07,
      "H": 0.05,
      "J": 0.18,
      "K": 0.18,
      "O": 0.19,
      "Q": 0.13,
      "T": 0.06
    }
  },
  {
    "id": "teichner-1943-10-a",
    "name": "Teichner (1943)",
    "n": 10,
    "weights": {
      "B": 0.1,
      "D": 0.07,
      "F": 0.07,
      "H": 0.06,
      "J": 0.125,
      "K": 0.13,
      "O": 0.25,
      "Q": 0.15,
      "T": 0.05
    }
  },
  {
    "id": "ouyang-1985-10-b",
    "name": "Ouyang (1985)",
    "n": 10,
    "weights": {
      "A": 0.06,
      "D": 0.09,
      "F": 0.06,
      "H": 0.045,
      "J": 0.19,
      "K": 0.095,
      "M": 0.095,
      "O": 0.19,
      "Q": 0.115,
      "U": 0.06
    }
  },
  {
    "id": "colin-and-houdas-1982-10-c",
    "name": "Colin & Houdas (1982)",
    "n": 10,
    "weights": {
      "A": 0.06,
      "D": 0.08,
      "F": 0.06,
      "H": 0.05,
      "J": 0.12,
      "K": 0.12,
      "M": 0.12,
      "O": 0.19,
      "Q": 0.13,
      "T": 0.07
    }
  },
  {
    "id": "houdas-and-ring-1982-10-d",
    "name": "Houdas & Ring (1982)",
    "n": 10,
    "weights": {
      "B": 0.2,
      "D": 0.1,
      "F": 0.05,
      "J": 0.2,
      "K": 0.05,
      "M": 0.125,
      "O": 0.125,
      "Q": 0.075,
      "R": 0.075
    }
  },
  {
    "id": "stolwijk-and-hardy-1966-10-f",
    "name": "Stolwijk & Hardy (1966)",
    "n": 10,
    "weights": {
      "A": 0.1,
      "D": 0.1,
      "H": 0.1,
      "J": 0.1,
      "K": 0.1,
      "M": 0.1,
      "O": 0.1,
      "P": 0.1,
      "R": 0.1,
      "T": 0.1
    }
  },
  {
    "id": "kurata-and-funazu-11-a",
    "name": "Kurata & Funazu (?)",
    "n": 11,
    "weights": {
      "A": 0.031,
      "C": 0.043,
      "D": 0.082,
      "F": 0.061,
      "H": 0.053,
      "J": 0.166,
      "M": 0.081,
      "N": 0.081,
      "O": 0.172,
      "R": 0.134,
      "T": 0.072
    }
  },
  {
    "id": "ouyang-1985-11-b",
    "name": "Ouyang (1985)",
    "n": 11,
    "weights": {
      "A": 0.06,
      "D": 0.07,
      "F": 0.07,
      "H": 0.05,
      "J": 0.09,
      "K": 0.09,
      "L": 0.09,
      "M": 0.09,
      "O": 0.19,
      "Q": 0.13,
      "T": 0.07
    }
  },
  {
    "id": "hardy-and-dubois-1938-12",
    "name": "Hardy & DuBois (1938)",
    "n": 12,
    "weights": {
      "A": 0.07,
      "F": 0.14,
      "H": 0.05,
      "J": 0.0875,
      "K": 0.0875,
      "L": 0.0875,
      "M": 0.0875,
      "O": 0.095,
      "P": 0.095,
      "Q": 0.065,
      "R": 0.065,
      "T": 0.07
    }
  },
  {
    "id": "olesen-1992-14",
    "name": "Olesen (1992)",
    "n": 14,
    "weights": {
      "A": 0.071,
      "C": 0.071,
      "D": 0.071,
      "E": 0.071,
      "H": 0.071,
      "J": 0.071,
      "K": 0.071,
      "L": 0.071,
      "M": 0.071,
      "O": 0.071,
      "P": 0.071,
      "Q": 0.071,
      "R": 0.071,
      "T": 0.071
    }
  },
  {
    "id": "ouyang-1985-15-a",
    "name": "Ouyang (1985)",
    "n": 15,
    "weights": {
      "A": 0.06,
      "D": 0.07,
      "F": 0.05,
      "H": 0.0225,
      "I": 0.0225,
      "J": 0.18,
      "K": 0.2,
      "O": 0.1025,
      "P": 0.1025,
      "Q": 0.0625,
      "R": 0.0625,
      "S": 0.0325,
      "T": 0.0325
    }
  },
  {
    "id": "mitchell-and-wyndham-1969-15-b",
    "name": "Mitchell & Wyndham (1969)",
    "n": 15,
    "weights": {
      "A": 0.07,
      "C": 0.07,
      "D": 0.07,
      "F": 0.07,
      "H": 0.07,
      "J": 0.07,
      "K": 0.07,
      "L": 0.07,
      "M": 0.07,
      "O": 0.07,
      "P": 0.07,
      "Q": 0.07,
      "R": 0.07,
      "T": 0.07
    }
  },
  {
    "id": "ouyang-1985-17",
    "name": "Ouyang (1985)",
    "n": 17,
    "weights": {
      "A": 0.037,
      "B": 0.037,
      "D": 0.075,
      "F": 0.075,
      "H": 0.025,
      "I": 0.025,
      "J": 0.0625,
      "K": 0.0625,
      "L": 0.0625,
      "M": 0.0625,
      "N": 0.0625,
      "O": 0.0875,
      "P": 0.0875,
      "Q": 0.0875,
      "R": 0.0875,
      "S": 0.0305,
      "T": 0.0305
    }
  }
];

function coefficient(w){
  if(w < 0.05) return Number(w).toFixed(4).replace(/0+$/,'').replace(/\.$/,'');
  if(w < 0.1) return Number(w).toFixed(3).replace(/0+$/,'').replace(/\.$/,'');
  return Number(w).toFixed(2).replace(/0+$/,'').replace(/\.$/,'');
}
function equation(f){return Object.entries(f.weights).map(([k,w])=>`${coefficient(w)}·${sites[k].label}`).join(' + ')}
function calc(f){return Object.entries(f.weights).reduce((sum,[k,w])=>sum+w*sites[k].value,0)}

function validateFormulaWeights(){
  formulas.forEach(f=>{
    const total=Object.values(f.weights).reduce((a,b)=>a+b,0);
    if(Math.abs(total-1)>0.02){
      console.warn(`MST formula weight sum differs from 1.0: ${f.name} (${f.id}) = ${total.toFixed(4)}`);
    }
  });
}
validateFormulaWeights();


function cleanLabel(label){
  return label.replace(/\([lr]\)/g,'').replace(/\(a\)/g,'').replace(/\(p\)/g,'').replace(/\s+/g,' ').trim();
}
function layoutCalloutRows(items, minGap, minY, maxY){
  const rows=items.map(item=>({ ...item, labelY:item.site.y })).sort((a,b)=>a.labelY-b.labelY);
  rows.forEach((row,i)=>{
    if(i>0 && row.labelY < rows[i-1].labelY + minGap){
      row.labelY = rows[i-1].labelY + minGap;
    }
  });
  const overflow = rows.length ? rows[rows.length-1].labelY - maxY : 0;
  if(overflow > 0){
    rows.forEach(row=>row.labelY -= overflow);
  }
  rows.forEach((row,i)=>{
    if(i===0 && row.labelY < minY) row.labelY = minY;
    if(i>0 && row.labelY < rows[i-1].labelY + minGap){
      row.labelY = rows[i-1].labelY + minGap;
    }
  });
  return rows;
}

function renderCallouts(f, container){
  const NS='http://www.w3.org/2000/svg';

  // Original silhouette SVG viewBox:
  const W=603.04, H=742.93;

  // Expanded callout canvas. The silhouette is shifted by M,
  // so labels can sit in real white space to the left/right.
  const M=110;
  const CW=W + 2*M;

  container.innerHTML='';
  container.className='mst-callout-layer';

  const svg=document.createElementNS(NS,'svg');
  svg.setAttribute('class','mst-callout-svg');
  svg.setAttribute('viewBox',`0 0 ${CW} ${H}`);
  svg.setAttribute('preserveAspectRatio','xMidYMid meet');

  const active=Object.keys(f.weights)
    .filter(k=>sites[k])
    .map(k=>({
      key:k,
      site:sites[k],
      // shifted point coordinates in the expanded callout coordinate system
      px:sites[k].x + M,
      py:sites[k].y
    }));

  const left=layoutCalloutRows(active.filter(d=>d.site.x < W/2), 24, 34, H-42);
  const right=layoutCalloutRows(active.filter(d=>d.site.x >= W/2), 24, 34, H-42);

  function draw(item, side){
    const site=item.site;
    const pointX=item.px;
    const pointY=item.py;
    const labelY=item.labelY;

    // Fixed external label columns, similar to the reference diagram.
    const labelX = side==='left' ? 24 : CW-24;
    const textAnchor = side==='left' ? 'start' : 'end';

    // leader line starts near the label and ends at the anatomical point
    const lineStartX = side==='left' ? labelX + 88 : labelX - 88;
    const elbowX = side==='left'
      ? Math.min(lineStartX + 18, pointX - 6)
      : Math.max(lineStartX - 18, pointX + 6);

    const line=document.createElementNS(NS,'polyline');
    line.setAttribute('points',`${lineStartX},${labelY} ${elbowX},${labelY} ${pointX},${pointY}`);
    line.setAttribute('class','mst-callout-line');
    line.setAttribute('fill','none');

    const dot=document.createElementNS(NS,'circle');
    dot.setAttribute('cx',pointX);
    dot.setAttribute('cy',pointY);
    dot.setAttribute('r','4.1');
    dot.setAttribute('class','mst-callout-dot');

    const group=document.createElementNS(NS,'g');

    const rect=document.createElementNS(NS,'rect');
    rect.setAttribute('class','mst-callout-label-bg');

    const text=document.createElementNS(NS,'text');
    text.setAttribute('x',labelX);
    text.setAttribute('y',labelY);
    text.setAttribute('text-anchor',textAnchor);
    text.setAttribute('class','mst-callout-label');
    text.textContent=`${cleanLabel(site.label)}: ${site.value.toFixed(1)}°C`;

    group.appendChild(rect);
    group.appendChild(text);

    svg.appendChild(line);
    svg.appendChild(dot);
    svg.appendChild(group);

    requestAnimationFrame(()=>{
      try{
        const b=text.getBBox();
        rect.setAttribute('x',b.x-5);
        rect.setAttribute('y',b.y-3);
        rect.setAttribute('width',b.width+10);
        rect.setAttribute('height',b.height+6);
      }catch(e){/* getBBox can fail if hidden during initial render */}
    });
  }

  left.forEach(item=>draw(item,'left'));
  right.forEach(item=>draw(item,'right'));
  container.appendChild(svg);
}

function init(root){
 const nSelect=root.querySelector('[data-mst-n]');
 const fSelect=root.querySelector('[data-mst-formula]');
 const sliders=root.querySelector('[data-mst-sliders]');
 const badges=root.querySelector('[data-mst-badges]');
 const result=root.querySelector('[data-mst-result]');
 const ftext=root.querySelector('[data-mst-text]');
 const compare=root.querySelector('[data-mst-compare]');
 const ns=[...new Set(formulas.map(f=>f.n))].sort((a,b)=>a-b);
 ns.forEach(n=>nSelect.add(new Option(`${n} sites`,n)));
 nSelect.value=ns.includes(3)?3:ns[0];
 Object.entries(sites).forEach(([key,s])=>{
   const row=document.createElement('div');
   row.className='mst-slider';
   row.dataset.site=key;
   row.innerHTML=`<label><span>${key}</span> ${s.label}</label><input type="number" min="20" max="45" step="0.1" value="${s.value.toFixed(1)}" aria-label="${s.label} temperature"><output>°C</output>`;
   const input=row.querySelector('input');
   input.addEventListener('input',e=>{
     const next=parseFloat(e.target.value);
     if(!Number.isNaN(next)) sites[key].value=next;
     update();
   });
   sliders.appendChild(row);
 });
 function refreshFormulaOptions(){
   const previous=fSelect.value;
   fSelect.innerHTML='';
   formulas.filter(f=>f.n==nSelect.value).forEach(f=>fSelect.add(new Option(f.name,f.id)));
   if([...fSelect.options].some(o=>o.value===previous)) fSelect.value=previous;
   update();
 }
 function renderCompare(){
   if(compare) compare.innerHTML='';
 }
 function update(){
   const f=formulas.find(x=>x.id===fSelect.value)||formulas.find(x=>x.n==nSelect.value)||formulas[0];
   const active=new Set(Object.keys(f.weights));
   result.textContent=calc(f).toFixed(2)+'°C';
   if(ftext) ftext.textContent=`${f.name}: ${equation(f)}`;
   renderCallouts(f, badges);
   root.querySelectorAll('.mst-slider').forEach(row=>{
     const k=row.dataset.site;
     const on=active.has(k);
     row.classList.toggle('active',on);
     row.classList.toggle('inactive',!on);
     row.querySelector('input').disabled=!on;
   });
   renderCompare();
 }
 nSelect.addEventListener('change',refreshFormulaOptions);
 fSelect.addEventListener('change',update);
 refreshFormulaOptions();
}
document.querySelectorAll('.mst-widget').forEach(init);
})();
