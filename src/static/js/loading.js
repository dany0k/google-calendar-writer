document.addEventListener("DOMContentLoaded", function () {
     // Получаем кнопку отправки формы
     var submitBtn = document.querySelector("input[type=submit]");
     // Получаем форму
     var form = document.querySelector("form");
     var preloader = document.getElementById("preloader")

     // Добавляем обработчик события нажатия на кнопку отправки формы
     submitBtn.addEventListener("click", function () {
         preloader.style.display = "block";
         form.submit();
     });
 });
 document.addEventListener("DOMContentLoaded", function () {
     // Получаем элемент с классом "loader"
     var preloader = document.getElementById("preloader")
     // Скрываем элемент с классом "loader"
     preloader.style.display = "none";
 });