const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const source = fs.readFileSync(require('node:path').join(__dirname, '../examples/minimal-scorm-quiz/scormdriver.js'), 'utf8');

function load(window) {
  vm.runInNewContext(source, { window, console: { warn() {} } });
  return window.scorm12;
}
function api() {
  return { LMSInitialize: () => 'true', LMSGetValue: () => 'lesson-2' };
}
function inaccessibleWindow() {
  return Object.defineProperty({}, 'API', {
    get() { throw new DOMException('Cross-origin frame access', 'SecurityError'); },
  });
}
test('standalone preview remains usable without an LMS', () => {
  const win = { opener: null }; win.parent = win;
  const driver = load(win);
  assert.equal(driver.init(), false);
  assert.equal(driver.get('cmi.core.lesson_location'), '');
});
test('discovers a same-origin parent LMS', () => {
  const driver = load({ parent: { API: api() }, opener: null });
  assert.equal(driver.init(), true);
  assert.equal(driver.get('cmi.core.lesson_location'), 'lesson-2');
});
test('cross-origin parent degrades to browser preview', () => {
  assert.equal(load({ parent: inaccessibleWindow(), opener: null }).init(), false);
});
test('tries the popup opener after an inaccessible parent', () => {
  assert.equal(load({ parent: inaccessibleWindow(), opener: { API: api() } }).init(), true);
});
test('an inaccessible opener also degrades to browser preview', () => {
  const win = { opener: inaccessibleWindow() }; win.parent = win;
  assert.equal(load(win).init(), false);
});
