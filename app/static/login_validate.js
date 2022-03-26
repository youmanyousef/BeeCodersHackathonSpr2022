var pristine;
window.onload = function () {

   var form = document.getElementById("login");

   pristine = new Pristine(form);

   form.addEventListener('submit', function (e) {
	  var valid = pristine.validate();
     if(!valid) {
        e.preventDefault();
     }
   });


};