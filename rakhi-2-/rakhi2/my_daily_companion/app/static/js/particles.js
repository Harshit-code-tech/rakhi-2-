document.addEventListener("DOMContentLoaded", function () {
    const canvas = document.createElement('canvas');
    canvas.id = 'particleCanvas';
    document.body.appendChild(canvas);

    const ctx = canvas.getContext('2d');
    let particles = [];
    const numParticles = 100;

    function resizeCanvas() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }

    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);

    function createParticle() {
        return {
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            radius: Math.random() * 3 + 1,
            dx: (Math.random() - 0.5) * 2,
            dy: (Math.random() - 0.5) * 2,
            color: `rgba(255, 255, 255, ${Math.random()})`
        };
    }

    for (let i = 0; i < numParticles; i++) {
        particles.push(createParticle());
    }

    function drawParticles() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        for (const particle of particles) {
            ctx.beginPath();
            ctx.arc(particle.x, particle.y, particle.radius, 0, Math.PI * 2);
            ctx.fillStyle = particle.color;
            ctx.fill();
            ctx.closePath();
        }
    }

    function updateParticles() {
        for (const particle of particles) {
            particle.x += particle.dx;
            particle.y += particle.dy;

            if (particle.x < 0 || particle.x > canvas.width) particle.dx *= -1;
            if (particle.y < 0 || particle.y > canvas.height) particle.dy *= -1;
        }
    }

    function animate() {
        drawParticles();
        updateParticles();
        requestAnimationFrame(animate);
    }

    animate();
});
