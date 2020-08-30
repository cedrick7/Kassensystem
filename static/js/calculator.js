// angeklickte Werte zum TR-Display hinzufügen
function addToScreen(x) {
  var box = document.getElementById("calc-display");
  box.value += x;

  // falls man "c" gedrückt hat, das TR-Display zurücksetzen
  if (x == 'c') {
    box.value = '';
  }
}

// Ergebnis errechnen
function result() {
  var box = document.getElementById("calc-display");

  var x = box.value;
  x = eval(x);
  box.value = x;
}

// letzten Wert des TR-Displays löschen
function backspace() {
  var box = document.getElementById("calc-display");

  var number = box.value;
  var len = number.length - 1;
  var newnumber = number.substring(0, len);
  box.value = newnumber;
}