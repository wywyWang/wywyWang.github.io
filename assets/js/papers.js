(function () {
  var list = document.getElementById('paper-list');
  if (!list) return;
  var cards = Array.prototype.slice.call(list.querySelectorAll('.paper'));
  var tabs = document.querySelectorAll('.paper-tab');

  function apply(filter) {
    cards.forEach(function (card) {
      var selected = card.hasAttribute('data-selected');
      card.hidden = filter === 'selected' && !selected;
    });
  }

  cards.forEach(function (card) {
    if (!card.querySelector('.paper-body')) {
      var summary = card.querySelector('summary');
      if (summary) {
        summary.addEventListener('click', function (e) {
          if (e.target.closest('a')) return;
          e.preventDefault();
        });
      }
    }
  });

  tabs.forEach(function (tab) {
    tab.addEventListener('click', function () {
      tabs.forEach(function (t) { t.classList.remove('is-active'); });
      tab.classList.add('is-active');
      apply(tab.getAttribute('data-filter'));
    });
  });
})();
