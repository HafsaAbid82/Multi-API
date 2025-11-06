import { useState, useEffect } from 'react'
import axios from "axios";
import './App.css'

function App() {
  const [weather_data, setWeather_data] = useState([]);
  const [quotes_data, setQuotes_data] = useState([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8002/weather/data")
      .then((response) => setWeather_data(response.data))
      .catch((error) => console.error("Error fetching weather data:", error));
  }, []);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8001/quotes/data")
      .then((response) => setQuotes_data(response.data.slice(0, 3)))
      .catch((error) => console.error("Error fetching quotes data:", error));
  }, []);

  return (
    <div className="app-container">
      <div className="weather-section">
        <h2>🌤️ Weather Data</h2>
        <pre className="data-box">{JSON.stringify(weather_data, null, 2)}</pre>
      </div>

      <div className="quotes-section">
        <h2>💬 Quotes</h2>
        <pre className="data-box">{JSON.stringify(quotes_data, null, 2)}</pre>
      </div>
    </div>
  );
}

export default App;
