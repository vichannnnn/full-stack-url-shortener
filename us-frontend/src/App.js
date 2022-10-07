import logo from './logo.svg';
import './App.css';
import {useState} from "react";

function App() {

  const [url, setTinyUrl] = useState("");
  const [message, setMessage] = useState("");
  let handleSubmit = async (e) => {
    e.preventDefault();
    let request = {"url": url};
    try {
      let res = await fetch("api/create", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(request),
      });
      let resJson = await res.json();
      if (res.status === 200) {
        setTinyUrl("");
        let message = `http://localhost:8000/${resJson["short_url"]}`
        setMessage(message);
      } else {
        setMessage("The URL provided is invalid.");
      }
    } catch (err) {
      console.log(err);
    }
  };

  return (
      <div className="App">
        <form onSubmit={handleSubmit}>
          <input
              type="text"
              value={url}
              placeholder="Enter the long URL to shorten it"
              onChange={(e) => setTinyUrl(e.target.value)}
          />

          <button type="submit">Shorten the URL</button>

          <div className="message">{message ? <p>{message}</p> : null}</div>
        </form>
      </div>
  );
}

export default App;
