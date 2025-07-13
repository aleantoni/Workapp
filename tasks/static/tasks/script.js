document.addEventListener("DOMContentLoaded", () => {
    console.log("JavaScript cargado correctamente.");

    // Colorea borde de las tarjetas
    const cards = document.querySelectorAll(".task-card");
    cards.forEach((card) => {
        card.style.borderLeft = "4px solid limegreen";
    });

    // Función de cambiar estado
    document.querySelectorAll('.toggle-status').forEach(button => {
        button.addEventListener('click', async () => {
            const card = button.closest('.task-card');
            const taskId = card.getAttribute('data-task-id');

            const response = await fetch("/toggle-status/", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ task_id: taskId })
            });

            if (response.ok) {
                const data = await response.json();

                // Actualiza el texto del estado visual
                card.querySelector('.task-status').textContent = data.display_status;
                // Actualiza el texto del botón
                button.textContent = data.new_status === 'P' ? 'Marcar como Completada' : 'Marcar como Pendiente';
            } else {
                alert("Error al actualizar estado.");
            }
        });
    });
});
