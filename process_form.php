<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Получаем и очищаем данные из формы
    $name = htmlspecialchars(trim($_POST['name']));
    $email = htmlspecialchars(trim($_POST['email']));
    $room = htmlspecialchars(trim($_POST['room']));
    $number_of_rooms = htmlspecialchars(trim($_POST['number_of_rooms']));
    $number_of_guests = htmlspecialchars(trim($_POST['number_of_guests']));
    $dates = htmlspecialchars(trim($_POST['dates']));

    if (!empty($name) && !empty($email) && !empty($room) && !empty($number_of_rooms) && !empty($number_of_guests) && !empty($dates)) {
        $data = "Name: $name, Email: $email, Room: $room, Number of Rooms: $number_of_rooms, Number of Guests: $number_of_guests, Dates: $dates\n";
        
        $file = 'form_data.txt';
        file_put_contents($file, $data, FILE_APPEND | LOCK_EX);

        // Сообщение об успешной записи
        echo "<div id='server-response'>Thank you, $name! Your booking has been saved.</div>";
    } else {
        // Сообщение об ошибке (отображаем в HTML для тестирования)
        echo "<div id='error-message'>Error: All fields are required.</div>";
    }
} else {
    echo "<div id='error-message'>Invalid request.</div>";
}
?>
