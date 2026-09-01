(function () {
  var list = document.getElementById('paper-list');
  if (!list) return;
  var cards = Array.prototype.slice.call(list.querySelectorAll('.paper'));
  var tabs = document.querySelectorAll('.paper-tab');

  function apply(filter) {
    list.setAttribute('data-filter', filter);
    cards.forEach(function (card) {
      var selected = card.getAttribute('data-selected') !== 'no';
      var kind = card.getAttribute('data-kind');
      var show = false;
      if (filter === 'selected') show = selected;
      else if (filter === 'mentor') show = card.hasAttribute('data-mentored');
      else if (filter === 'conference') show = kind === 'conference';
      else if (filter === 'workshop') show = kind === 'workshop';
      card.hidden = !show;
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

  var active = document.querySelector('.paper-tab.is-active');
  apply(active ? active.getAttribute('data-filter') : 'selected');
})();
