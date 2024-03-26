document.addEventListener('DOMContentLoaded', function() {
    const startButton = document.getElementById('startButton');
    const ball = document.getElementById('ball');
    const rope = document.getElementById('rope');
    const court = document.getElementById('court');

    startButton.addEventListener('click', function() {
        pole.style.animation = 'rotatePole 3s linear infinite';
        rope.style.animation = 'moveRope 3s linear infinite';
        ball.style.animation = 'rotateBall 3s linear infinite';

        const results = document.getElementById('results');
        const ropeSpeed = calculateRopeSpeed();

        const calculatedSpeed = calculateSpeed(ropeSpeed);
        results.innerText = "Velocidad calculada: " + calculatedSpeed.toFixed(2) + " m/s";
    });

    function calculateRopeSpeed() {
        return 3.5; // Velocidad de la cuerda en m/s (valor ficticio dentro del rango típico)
    }

    function calculateSpeed(ropeSpeed) {
        const ropeAngularSpeed = 180; // Velocidad angular de la cuerda en grados por segundo
        const ballRadius = 3; // Radio de la pelota en metros (valor en el rango típico)
        const ballSpeed = (ropeSpeed / ropeAngularSpeed) * (2 * Math.PI * ballRadius); // Velocidad de la pelota en m/s
        return ballSpeed;
    }

    // Escuchar el evento de cada cuadro de la animación de la cuerda
    rope.addEventListener('animationiteration', function() {
        // Obtener la posición de la cuerda y el tamaño de la pelota
        const ropePos = rope.getBoundingClientRect();
        const ballSize = ball.getBoundingClientRect();

        // Calcular la posición de la pelota para que esté pegada a la cuerda
        const ballLeft = ropePos.left + ropePos.width / 2 - ballSize.width / 2;
        const ballTop = ropePos.top - ballSize.height;

        // Establecer la posición de la pelota
        ball.style.left = `${ballLeft}px`;
        ball.style.top = `${ballTop}px`;
    });

    // Ajustar el tamaño del campo de juego para que no haya desbordamiento de la pelota
    court.style.overflow = 'hidden';
});
