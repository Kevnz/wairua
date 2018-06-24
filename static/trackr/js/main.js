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


console.log('not ready')
document.addEventListener("DOMContentLoaded", function () {
  console.log('ready');
  const modal = document.querySelector('#add-mood-form');
  const openDialog = (e) => {
    console.log('open')
    e.preventDefault();
    modal.showModal();
  }
  const closeDialog = (e) => {
    console.log('close')
    e.preventDefault();
    modal.close();
  }
  $('#open-mood-dialog').on('click', openDialog);
  $('#add-mood-form button.close').on('click', closeDialog);


  dialogPolyfill.registerDialog(modal);
});