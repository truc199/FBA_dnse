/* ===========================================================================
   02a -- Google Play review collector, browser console version.

   This is the method actually used for the report. It works because the code
   runs on play.google.com itself, so the request is same-origin and needs no
   key, no proxy and no library. Paste it into the DevTools console on the
   app's Play Store page.

   How it works
     Google Play's web front end talks to a single endpoint called
     batchexecute. Each remote procedure has an id; the one that returns a page
     of reviews is UsvDTd. The response is a JSON-ish blob prefixed by a few
     junk lines, so the first well-formed line is taken and parsed. Every
     response ends with a continuation token, which is fed back in to get the
     next page. Pagination stops when the token comes back null.

   Sort codes
     1 = most helpful   2 = newest   3 = rating

   Usage
     await __collect('vn.com.encapital.arrow', 2000, 2)   // DNSE, newest first
     await __collect('vn.com.vpbs.smartone',  2000, 2)    // VPS
     await __collect('com.fpts.eztrade',      2000, 2)    // FPTS
     copy(__toCSV(window.__last))                          // CSV to clipboard
   =========================================================================== */

window.__fb = async function (appId, count, token, sort) {
  const inner = JSON.stringify([
    null,
    [[sort || 2, count || 150, null], null, token ? [token] : null],
    [appId, 7]
  ]);
  const body = "f.req=" + encodeURIComponent(JSON.stringify([[["UsvDTd", inner, null, "generic"]]]));

  const res = await fetch(
    "/_/PlayStoreUi/data/batchexecute?rpcids=UsvDTd&source-path=%2Fstore%2Fapps%2Fdetails&hl=vi&gl=VN",
    {
      method: "POST",
      credentials: "include",
      headers: { "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8" },
      body
    }
  );
  const text = await res.text();

  // The response starts with a byte-count line and other noise. Take the first
  // line that parses as JSON and contains the payload.
  let envelope = null;
  for (const line of text.split("\n")) {
    if (!line.trim().startsWith("[")) continue;
    try { envelope = JSON.parse(line); break; } catch (e) { /* keep looking */ }
  }
  if (!envelope) throw new Error("could not parse batchexecute response");

  const frame = envelope.find(x => Array.isArray(x) && x[1] === "UsvDTd");
  if (!frame || !frame[2]) return { items: [], token: null };
  const payload = JSON.parse(frame[2]);

  const raw = (payload[0] || []);
  const items = raw.map(x => ({
    id:     x[0],
    author: x[1] && x[1][0],
    rating: x[2],
    text:   x[4],
    ts:     x[5] && x[5][0],            // unix seconds
    thumbs: x[6] || 0
  })).filter(r => r.id && r.rating);

  const next = payload[1] && payload[1][1] ? payload[1][1] : null;
  return { items, token: next };
};

/* Paginate until the target count is reached or the token runs out. */
window.__collect = async function (appId, target, sort) {
  const seen = new Set();
  const out = [];
  let token = null;
  for (let page = 0; page < 200; page++) {
    const { items, token: next } = await window.__fb(appId, 150, token, sort);
    for (const it of items) {
      if (!seen.has(it.id)) { seen.add(it.id); out.push(it); }
    }
    console.log(`page ${page + 1}: +${items.length}, total ${out.length}`);
    if (!next || out.length >= target || items.length === 0) break;
    token = next;
    await new Promise(r => setTimeout(r, 400));   // be polite
  }
  window.__last = out.slice(0, target);           // a page can overshoot the target
  return window.__last;
};

/* CSV, for moving the pull out of the browser. */
window.__toCSV = function (rows) {
  const esc = s => '"' + String(s == null ? "" : s)
    .replace(/"/g, '""').replace(/[\r\n]+/g, " ").trim() + '"';
  const head = "review_id,rating,date,thumbs_up,author,text";
  const body = rows.map(r => [
    r.id,
    r.rating,
    // Vietnam time, UTC+7: toISOString() alone is UTC and moves late-night reviews
    // to the previous day, and on 1 January to the previous year.
    new Date((r.ts + 7 * 3600) * 1000).toISOString().slice(0, 10),
    r.thumbs,
    esc(r.author),
    esc(r.text)
  ].join(","));
  return [head].concat(body).join("\n");
};

console.log("ready. try:  await __collect('vn.com.encapital.arrow', 2000, 2)");
