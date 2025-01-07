document.addEventListener('DOMContentLoaded', function () {
    const startLevel = document.getElementById('start-level');
    if (startLevel) {
        startLevel.addEventListener('click', (e) => {
            window.location.href = 'weather.html'
        });
    } else {
        console.error('Button with id "start-level" not found!');
    }
})



// Fetch data from weather-today and display it on the front end
async function fetchWeather() {
    const cityName = document.getElementById('city-data').ariaValueMax;
    try {
        // Fetch wether data from Flask API
        const response = await fetch('http://127.0.0.1:5000/api/weather');
        
        if 
        (!response.ok) {
            throw new Error('Failed to fetch data: ' + response.statusText);
        }


        const data = await response.json();

        // Find the city from the data
        const city = data.find(item => item.city.toLowerCase() === cityName.toLowerCase());

        // Store the city in varaible
        if (city) {
            document.getElementById('weatherResult').innerHTML = `
                    <h3>Weather in: <strong>${city.city}</strong></h3>
                    <p>Temperature: <strong>${city.temperature} °C</strong></p>
                    <p>Condition: <strong>${city.condition}</strong></p>
            `;
        } else {
            document.getElementById('weatherResult').innerHTML = `
                    <p>City not found. Please try another one.</p>
                    `;
        }
    } catch (error) {
        // Catch any error that occurred during the fetch or data processsing
        console.error("Error occured:", error);
        document.getElementById('weatherResult').innerHTML = `
            <p>Sorry, something went wrong. Please try again later.</p>
            `;
    }
}