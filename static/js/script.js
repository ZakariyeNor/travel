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


// Post the data based on user's input
async function postWeather() {
    // get the user inputs
    const city = document.getElementById('postCity').value;
    const temp = document.getElementById('postTemp').value;
    const condition = document.getElementById('postCondition').value;

    //Data to be posted 
    const postData = {
        city: city,
        temperature: temp,
        condition: condition
    };

    try {
        // Post data 
        const response = await fetch('http://127.0.0.1:5000/api/weather', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(postData)
        });

        if (response.ok) {
            const responseData = await response.json();
            console.log('Weather data posted successfully:', responseData);

            //Post the DOM with the posted data
            document.getElementById('postResult').innerHTML = `
                <h3>Weather in: <strong>${responseData.city}</strong></h3>
                <p>Temperature: <strong>${responseData.temperature} °C</strong></p>
                <p>Condition: <strong>${responseData.condition}</strong></p>  
            `;


        } else {
            throw new Error('Failed to post weather data');
        }
    } catch (error) {
        console.log('Error posting weather data:', error)
    }
}


//Update data based on the data in memory
async function updateWeather() {
    const city = document.getElementById('updateId').value;
    const temp = document.getElementById('updateTemp').value;
    const condition = document.getElementById('updateCondition').value;
    

    //Update 
    updateData = {
        city: city,
        temperature: temp,
        condition: condition
    };

    try {
        // Update data 
        const response = await fetch('http://127.0.0.1:5000/api/weather', {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ city, temperature: temp, condition })
        });

        if (!response.ok) {
            throw new Error('Failed to update the new weader data');
        } else {
            const responsUpdatedData = await response.json();
            console.log('Weather data updates successfully:', responsUpdatedData);

            // Update the frontend data
            document.getElementById('updateResult').innerHTML = `
                    <h3>Weather in: <strong>${responsUpdatedData.city}</strong></h3>
                <p>Temperature: <strong>${responsUpdatedData.temperature} °C</strong></p>
                <p>Condition: <strong>${responsUpdatedData.condition}</strong></p> 
            `;
        }
    } catch (error) {
        console.log('Error updating weather data');
    }
}


// Delete data
async function deleteWeather() {
    try {
        //Get the city id to Delete
        const deleteCity = document.getElementById('deleteId').value;


        //Send delete request to the server 
        const response = await fetch('http://127.0.0.1:5000/api/weather/id', {
            method: 'DELETE'
        });

        //Check if response is successful
        if (response.ok) {

            //Parse the response as JSON
            const deleteData = response.json();

            //update the frontend to diplay the deleted data 
            document.getElementById('deleteResult').innerHTML = `
                    <p>Deleted: <strong>${JSON.stringify(deleteData)}</strong></p>
                    `;
        } else {
            throw new Error('Failed to delete weather data');
        }
    } catch (error) {

        //Handle any error that occurred during the fetch or in the try block
        console.error('Error deleting weather data:', error);
        document.getElementById('deleteResult').innerHTML = `
            <p>Error: <strong>${error.message}</strong></p>
            `;
        
    }  
}