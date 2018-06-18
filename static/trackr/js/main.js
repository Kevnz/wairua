const $ = window.$ = document.querySelectorAll.bind(document);

Node.prototype.on = window.on = function (name, fn) {
  this.addEventListener(name, fn);
}

NodeList.prototype.__proto__ = Array.prototype;

NodeList.prototype.on = NodeList.prototype.addEventListener = function (name, fn) {
  this.forEach(function (elem, i) {
    elem.on(name, fn);
  });
}

const openDialog = (e) => {
  console.log('open')
  e.preventDefault();
  $('#add-mood-form')[0].setAttribute('open', true);
}
const closeDialog = (e) => {
  console.log('close')
  e.preventDefault();
  $('#add-mood-form')[0].removeAttribute('open');
}
console.log('not ready')
document.addEventListener("DOMContentLoaded", function() {
  console.log('ready')
  $('#open-mood-dialog').on('click', openDialog);
  $('#add-mood-form button.close').on('click', closeDialog)
});