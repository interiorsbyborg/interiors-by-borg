#!/usr/bin/env node
/*
  Optional helper for a local checkout of the published/static site.
  It searches common published files for the Selections tile and prints matching files.
  It does not modify files automatically.
*/
const fs = require('fs');
const path = require('path');
const root = process.cwd();
const exts = new Set(['.html','.js','.mjs','.cjs','.json','.css','.jsx','.ts','.tsx']);
const skip = new Set(['.git','node_modules','dist','.next','build']);
const matches = [];
function walk(dir){
  for (const entry of fs.readdirSync(dir, {withFileTypes:true})){
    if (skip.has(entry.name)) continue;
    const p = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(p);
    else if (exts.has(path.extname(entry.name).toLowerCase())){
      const text = fs.readFileSync(p, 'utf8');
      if (/Layered material palette|SELECTIONS|selections/i.test(text) && /water|ocean|wave|portfolio|image|src/i.test(text)) {
        matches.push(path.relative(root, p));
      }
    }
  }
}
walk(root);
console.log('Files that may contain the Portfolio > Selections image reference:');
console.log(matches.length ? matches.join('\n') : 'No likely files found. This published build may be hashed/minified; update source and rebuild.');
console.log('\nSet the image path to: /images/portfolio/selections.webp');
