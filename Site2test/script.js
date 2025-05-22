document.addEventListener('DOMContentLoaded', function() {
    // Мобильное меню
    const burger = document.querySelector('.burger');
    const navLinks = document.querySelector('.nav-links');
    
    burger.addEventListener('click', function() {
        navLinks.classList.toggle('active');
    });

    // Данные номеров
    const rooms = [
        {
            title: "Стандарт",
            description: "Уютный номер с всеми удобствами",
            price: "от 3 500 руб./ночь",
            img: "https://images.unsplash.com/photo-1631049307264-da0ec9d70304?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
        },
        {
            title: "Делюкс",
            description: "Просторный номер с видом на город",
            price: "от 5 500 руб./ночь",
            img: "https://images.unsplash.com/photo-1566669437685-5f63c6a685be?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
        },
        {
            title: "Люкс",
            description: "Роскошный номер с панорамным видом",
            price: "от 8 500 руб./ночь",
            img: "https://images.unsplash.com/photo-1596178065887-1198b6148b2b?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
        }
    ];

    // Данные услуг
    const services = [
        {
            icon: "fas fa-utensils",
            title: "Ресторан",
            description: "Гастрономические изыски от нашего шеф-повара"
        },
        {
            icon: "fas fa-spa",
            title: "СПА",
            description: "Расслабляющие процедуры для тела и души"
        },
        {
            icon: "fas fa-swimming-pool",
            title: "Бассейн",
            description: "Крытый бассейн с подогревом"
        },
        {
            icon: "fas fa-concierge-bell",
            title: "Консьерж",
            description: "Персональный помощник для вашего комфорта"
        }
    ];

    // Заполнение номеров
    const roomsContainer = document.querySelector('.rooms-container');
    rooms.forEach(room => {
        const roomCard = document.createElement('div');
        roomCard.className = 'room-card';
        roomCard.innerHTML = `
            <img src="${room.img}" alt="${room.title}">
            <div class="room-info">
                <h3>${room.title}</h3>
                <p>${room.description}</p>
                <p class="price">${room.price}</p>
                <a href="#booking" class="btn">Забронировать</a>
            </div>
        `;
        roomsContainer.appendChild(roomCard);
    });

    // Заполнение услуг
    const servicesGrid = document.querySelector('.services-grid');
    services.forEach(service => {
        const serviceItem = document.createElement('div');
        serviceItem.className = 'service-item';
        serviceItem.innerHTML = `
            <i class="${service.icon}"></i>
            <h3>${service.title}</h3>
            <p>${service.description}</p>
        `;
        servicesGrid.appendChild(serviceItem);
    });

    // Обработка формы бронирования
    const bookingForm = document.getElementById('booking-form');
    bookingForm.addEventListener('submit', function(e) {
        e.preventDefault();
        alert('Ваша заявка принята! Мы свяжемся с вами в ближайшее время.');
        bookingForm.reset();
    });

    // Плавная прокрутка
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 80,
                    behavior: 'smooth'
                });
                
                // Закрываем мобильное меню после клика
                navLinks.classList.remove('active');
            }
        });
    });
});