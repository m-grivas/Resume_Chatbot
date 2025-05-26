import { useState } from 'react'
import api from './api'


function App() {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState("");
  
  // to post question(=text) to api and get answer
  const handleSubmit = async (text) => {
    try {
      const res = await api.post("/", { question: text });
      setResponse(res.data.message);
    } catch (err) {
      console.error("API error:", err);
      setResponse("Error occurred");
    }
  };

  return (
    <></>
  )
}

export default App
