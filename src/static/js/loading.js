document.addEventListener("DOMContentLoaded", function () {
     // Получаем кнопку отправки формы
     var submitBtn = document.querySelector("input[type=submit]");
     // Получаем форму
     var form = document.querySelector("form");
     var preloader = document.getElementById("preloader")
     // Добавляем обработчик события нажатия на кнопку отправки формы
     submitBtn.addEventListener("click", function () {
        if (validateForm()) {
            preloader.style.display = "block";
            form.submit();
        }
     });
 });

 document.addEventListener("DOMContentLoaded", function () {
     // Получаем элемент с классом "loader"
     var preloader = document.getElementById("preloader")
     preloader.style.display = "none";
     // Скрываем элемент с классом "loader"
 });

 function validateForm() {
    const course = document.getElementById("course_num_id"); 
    const group = document.getElementById("group_num_id"); 
    const subgroup = document.getElementById("subgroup_num_id"); 
    const week = document.getElementById("week_num_id"); 
    
    if (course.value === '' ||
        group.value === '' ||
        subgroup.value === '' ||
        week.value === '') {
        return true;
    }
    return false;
}