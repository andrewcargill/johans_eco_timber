
  document.addEventListener('DOMContentLoaded', function() {
    console.log('------------andy Line 7 yes', yes);
    
    var elems = document.querySelectorAll('.datepicker');
    var instances = M.Datepicker.init(elems, options);
  });

  document.addEventListener('DOMContentLoaded', function() {
    console.log('------------andy Line 10 yes', yes);
    
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems, options);
  });
