// Simple JS for beginner-friendly microsite
document.addEventListener('DOMContentLoaded', () => {
  // Auto-collapse navbar on link click (mobile)
  document.querySelectorAll('.navbar-nav .nav-link').forEach(link => {
    link.addEventListener('click', () => {
      const bsCollapse = document.querySelector('.navbar-collapse');
      if (bsCollapse && bsCollapse.classList.contains('show')) {
        new bootstrap.Collapse(bsCollapse).hide();
      }
    });
  });

  // Reservation form handling (client-side only)
  const reserveForm = document.getElementById('reserveForm');
  const reserveMsg = document.getElementById('reserveMsg');
  if (reserveForm) {
    reserveForm.addEventListener('submit', (e) => {
      e.preventDefault();
      e.stopPropagation();
      if (!reserveForm.checkValidity()) {
        reserveForm.classList.add('was-validated');
        return;
      }
      // simulate sending
      reserveMsg.classList.remove('d-none');
      reserveMsg.textContent = 'Děkujeme — rezervace byla odeslána.';
      reserveForm.reset();
      reserveForm.classList.remove('was-validated');
      reserveMsg.scrollIntoView({behavior:'smooth'});
    });
  }

  // Newsletter subscribe (client-side fake)
  const subscribeBtn = document.getElementById('subscribeBtn');
  const newsletterMsg = document.getElementById('newsletterMsg');
  if (subscribeBtn) {
    subscribeBtn.addEventListener('click', (ev) => {
      ev.preventDefault();
      const email = document.getElementById('newsletterEmail').value.trim();
      if (!email) {
        // simple feedback
        document.getElementById('newsletterEmail').classList.add('is-invalid');
        setTimeout(() => document.getElementById('newsletterEmail').classList.remove('is-invalid'), 2000);
        return;
      }
      newsletterMsg.classList.remove('d-none');
      setTimeout(() => newsletterMsg.classList.add('d-none'), 4000);
      document.getElementById('newsletterEmail').value = '';
    });
  }
});